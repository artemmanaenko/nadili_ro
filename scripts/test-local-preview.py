"""Regression checks for session isolation and fail-closed process cleanup."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('preview', Path(__file__).with_name('local-preview.py'))
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)


class OwnershipTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.root_patch = patch.object(preview, 'ROOT', self.root)
        self.state_patch = patch.object(preview, 'STATE', self.root / 'state')
        self.root_patch.start()
        self.state_patch.start()
        preview.STATE.mkdir()

    def tearDown(self):
        self.root_patch.stop()
        self.state_patch.stop()
        self.temp.cleanup()

    def record(self, token='a'*32, owner=None, pid=123):
        path = preview.STATE / (token+'.json')
        preview.save(path, {'root':str(self.root), 'pid':pid, 'identity':'stamp',
                            'port':4321, 'owner':owner})
        return path

    def event(self, token='a'*32, session='one'):
        return {'session_id':session, 'tool_name':'Bash', 'tool_input':{'command':'python3 scripts/local-preview.py start --port 4321'}, 'tool_response':{'nested':[{'stdout':preview.MARKER+token}]}}

    def test_nested_response_registers_only_existing_live_record(self):
        path = self.record()
        with patch.object(preview, 'identity', return_value='stamp'):
            preview.register(self.event(), 'codex')
        self.assertEqual(json.loads(path.read_text())['owner'], {'client':'codex','session':'one'})

    def test_owner_cannot_be_reassigned(self):
        path = self.record(owner={'client':'codex','session':'one'})
        with patch.object(preview, 'identity', return_value='stamp'):
            preview.register(self.event(session='two'), 'claude')
        self.assertEqual(json.loads(path.read_text())['owner']['session'],'one')

    def test_marker_in_input_is_not_registration(self):
        path = self.record()
        preview.register({'session_id':'one','tool_input':{'command':preview.MARKER+'a'*32}}, 'codex')
        self.assertIsNone(json.loads(path.read_text())['owner'])

    def test_only_matching_session_and_client_are_signalled(self):
        self.record(owner={'client':'codex','session':'one'})
        self.record('b'*32, {'client':'codex','session':'two'},124)
        self.record('c'*32, {'client':'claude','session':'one'},125)
        self.record('d'*32, None,126)
        with patch.object(preview,'identity',return_value='stamp'), patch.object(preview.os,'getpgid',side_effect=lambda pid:pid), patch.object(preview.os,'killpg') as kill:
            preview.end_session('one','codex')
        kill.assert_called_once_with(123,preview.signal.SIGTERM)

    def test_reused_pid_is_not_signalled(self):
        self.record(owner={'client':'codex','session':'one'})
        with patch.object(preview,'identity',return_value='new process'), patch.object(preview.os,'getpgid',side_effect=lambda pid:pid), patch.object(preview.os,'killpg') as kill:
            preview.end_session('one','codex')
        kill.assert_not_called()

    def test_missing_identity_is_not_signalled(self):
        self.record(owner={'client':'codex','session':'one'})
        with patch.object(preview,'identity',return_value=None), patch.object(preview.os,'getpgid',side_effect=lambda pid:pid), patch.object(preview.os,'killpg') as kill:
            preview.end_session('one','codex')
        kill.assert_not_called()

    def test_foreign_project_record_is_ignored(self):
        path=self.record(owner={'client':'codex','session':'one'})
        record=json.loads(path.read_text()); record['root']='/other/project'; preview.save(path,record)
        with patch.object(preview.os,'getpgid',side_effect=lambda pid:pid), patch.object(preview.os,'killpg') as kill:
            preview.end_session('one','codex')
        kill.assert_not_called()

    def test_malformed_record_is_ignored(self):
        (preview.STATE/'bad.json').write_text('{')
        with patch.object(preview.os,'getpgid',side_effect=lambda pid:pid), patch.object(preview.os,'killpg') as kill:
            preview.end_session('one','codex')
        kill.assert_not_called()


if __name__ == '__main__':
    unittest.main()
