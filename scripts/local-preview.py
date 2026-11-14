#!/usr/bin/env python3
"""Project-local Astro launcher and per-chat SessionEnd cleanup (stdlib only)."""
import argparse
import contextlib
import fcntl
import json
import os
from pathlib import Path
import re
import secrets
import shutil
import signal
import socket
import subprocess
import sys
import time

CHECKOUT = Path(__file__).resolve().parents[1]
# All managed worktrees of this repository share the original checkout's registry.
try:
    common = Path(subprocess.check_output(
        ['git', 'rev-parse', '--path-format=absolute', '--git-common-dir'],
        cwd=CHECKOUT, text=True, stderr=subprocess.DEVNULL, timeout=1).strip())
    ROOT = common.parent if common.name == '.git' else CHECKOUT
except (OSError, subprocess.SubprocessError):
    ROOT = CHECKOUT
STATE = ROOT / '.nadili-local' / 'previews'
MARKER = 'NADILI_PREVIEW_TOKEN='
TOKEN = re.compile(r'NADILI_PREVIEW_TOKEN=([a-f0-9]{32})(?![a-f0-9])')


def identity(pid):
    """Start time plus full command guards PID reuse; fail closed on lookup failure."""
    try:
        result = subprocess.run(
            ['ps', '-ww', '-p', str(pid), '-o', 'lstart=,command='],
            capture_output=True, text=True, timeout=0.4, check=True)
        return result.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


@contextlib.contextmanager
def locked(timeout=1.0):
    STATE.mkdir(parents=True, exist_ok=True, mode=0o700)
    with (STATE / 'lock').open('a') as lock:
        deadline = time.monotonic() + timeout
        while True:
            try:
                fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() >= deadline:
                    raise RuntimeError('Preview registry is busy; cleanup was not performed.')
                time.sleep(0.02)
        yield


def save(path, record):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(record, indent=2) + '\n')
    temp.chmod(0o600)
    temp.replace(path)


def records():
    for path in STATE.glob('*.json'):
        try:
            record = json.loads(path.read_text())
            if (record.get('root') == str(ROOT) and
                    isinstance(record.get('pid'), int) and record['pid'] > 1 and
                    isinstance(record.get('identity'), str)):
                yield path, record
        except (OSError, ValueError, TypeError):
            continue


def response_strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from response_strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from response_strings(item)


def register(payload, client):
    session = payload.get('session_id')
    if not isinstance(session, str) or not session:
        return
    command = payload.get('tool_input', {}).get('command', '')
    if (payload.get('tool_name') != 'Bash' or not isinstance(command, str) or
            not re.search(r'local-preview\.py[\"\']?\s+start(?:\s|$)', command)):
        return
    # Read only actual launcher output, not prompts, commands or transcript text.
    tokens = {m.group(1) for s in response_strings(payload.get('tool_response'))
              for m in TOKEN.finditer(s)}
    if not tokens:
        return
    with locked():
        for path, record in records():
            if (path.stem in tokens and record.get('owner') is None and
                    identity(record['pid']) == record['identity']):
                record['owner'] = {'client': client, 'session': session}
                save(path, record)
                print(f"Registered preview on {record['port']} for this {client} chat.")


def end_session(session, client):
    if not isinstance(session, str) or not session or not STATE.exists():
        return
    owner = {'client': client, 'session': session}
    with locked(timeout=15):
        for path, record in records():
            if record.get('owner') != owner:
                continue
            current = identity(record['pid'])
            if current != record['identity']:
                # Keep record on mismatch: never target a new process with an old PID.
                record['status'] = 'not-running-or-identity-mismatch'
                save(path, record)
                continue
            try:
                if os.getpgid(record['pid']) != record['pid']:
                    continue
                os.killpg(record['pid'], signal.SIGTERM)
                record['status'] = 'termination-requested'
                save(path, record)
                print(f"Sent SIGTERM to owned preview on port {record['port']}.")
            except ProcessLookupError:
                record['status'] = 'exited'
                save(path, record)
            except PermissionError:
                print(f"Cannot stop preview PID {record['pid']}: permission denied.", file=sys.stderr)


def start(mode, port):
    node = shutil.which('node')
    astro = CHECKOUT / 'node_modules/astro/bin/astro.mjs'
    if not node or not astro.is_file():
        raise RuntimeError('Install project dependencies first; node and Astro are required.')
    # Do not reuse another chat's listener or let Astro silently choose another port.
    with socket.socket() as probe:
        probe.bind(('127.0.0.1', port))
    token = secrets.token_hex(16)
    with locked():
        log = STATE / (token + '.log')
    # Astro auto-backgrounds under agents; --ignore-lock keeps this PID in charge
    # and prevents it from reusing/stopping another chat's Astro lockfile server.
    with log.open('wb') as output:
        child = subprocess.Popen(
            [node, str(astro), mode, '--ignore-lock', '--host', '127.0.0.1', '--port', str(port)],
            cwd=CHECKOUT, stdin=subprocess.DEVNULL, stdout=output, stderr=output,
            start_new_session=True)
    stamp = None
    for _ in range(20):
        stamp = identity(child.pid)
        if stamp and str(astro) in stamp:
            break
        if child.poll() is not None:
            break
        time.sleep(0.05)
    if not stamp or str(astro) not in stamp or child.poll() is not None:
        if child.poll() is None:
            child.terminate()
        raise RuntimeError(f'Could not identify Astro process. See {log}')
    save(STATE / (token + '.json'), {
        'root': str(ROOT), 'cwd': str(CHECKOUT), 'pid': child.pid, 'identity': stamp,
        'port': port, 'mode': mode, 'owner': None, 'created': time.time(),
        'status': 'started', 'log': str(log)})
    print(f'{MARKER}{token}', flush=True)
    print(f'PID {child.pid}; requested URL http://127.0.0.1:{port}/; log {log}')
    print('PostToolUse must register ownership. Run status next and verify the actual page before handoff.')


def status():
    for _, record in records():
        current = identity(record['pid'])
        print(json.dumps({key: record.get(key) for key in
                          ('pid', 'port', 'mode', 'owner', 'cwd')} |
                         {'running': current == record['identity']}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='action', required=True)
    launch = commands.add_parser('start')
    launch.add_argument('--mode', choices=['dev', 'preview'], default='preview')
    launch.add_argument('--port', type=int, required=True)
    commands.add_parser('status')
    cleanup = commands.add_parser('cleanup')
    cleanup.add_argument('--client', choices=['codex', 'claude'], required=True)
    cleanup.add_argument('--session', required=True)
    hook = commands.add_parser('hook')
    hook.add_argument('--client', choices=['codex', 'claude'], required=True)
    args = parser.parse_args()
    if args.action == 'start':
        if not 1024 <= args.port <= 65535:
            parser.error('Choose a port between 1024 and 65535.')
        start(args.mode, args.port)
    elif args.action == 'status':
        status()
    elif args.action == 'cleanup':
        end_session(args.session, args.client)
    else:
        try:
            payload = json.load(sys.stdin)
        except ValueError:
            return
        if not isinstance(payload, dict):
            return
        if payload.get('hook_event_name') == 'PostToolUse':
            register(payload, args.client)
        elif payload.get('hook_event_name') == 'SessionEnd':
            session = payload.get('session_id')
            if not isinstance(session, str) or not session or not STATE.exists():
                return
            # SessionEnd has a short client timeout. A finite cleanup worker can wait
            # for a concurrent registry write and finish all owned processes safely.
            with (STATE / 'cleanup.log').open('ab') as log:
                subprocess.Popen(
                    [sys.executable, str(Path(__file__).resolve()), 'cleanup',
                     '--client', args.client, '--session', session],
                    stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                    start_new_session=True)


if __name__ == '__main__':
    try:
        main()
    except (OSError, RuntimeError) as error:
        print(str(error), file=sys.stderr)
        sys.exit(1)
