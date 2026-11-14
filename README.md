# Nadili Romania

[Nadili Romania](https://artemmanaenko.github.io/nadili_ro/) is a community guide for Ukrainians in Romania, built with [Astro Starlight](https://starlight.astro.build).

## Contributing

You don't need a finished article to contribute. Open this repository in Codex or Claude Code, give the agent a topic or Telegram message link, and let the project skills handle the research, writing and checks.

| Skill | What it does |
| --- | --- |
| [nadili-investigate](.agents/skills/nadili-investigate/SKILL.md) | Reads the discussion and linked material, checks official sources, asks you about unconfirmed claims, then creates or updates a Ukrainian guide with a PR and a running local preview. |
| [nadili-qa](.agents/skills/nadili-qa/SKILL.md) | Edits for clear actions and concise Ukrainian, removes filler and sends missing procedural details back for research. Runs automatically during investigate; also works on an existing page. |
| [nadili-local-doctor](.agents/skills/nadili-local-doctor/SKILL.md) | Checks local preview servers and retires this task's unneeded servers after local review is complete. Keeps previews still in use and leaves other tasks' servers alone. |

In Codex, start with:

```text
$nadili-investigate <Telegram message link or topic> — make a guide for the site
```

For an editorial pass only: `$nadili-qa <page path>`. In Claude Code, use `/nadili-investigate` or `/nadili-qa` instead. Telegram research needs an authenticated browser/app and computer-control tools; the agent will flag missing access. You review community claims and the resulting page before merge.

See [CONTRIBUTING.md](CONTRIBUTING.md) for source requirements, page formats and checks.
Merges to `main` deploy automatically.

## Copyright and use

All rights reserved by the respective copyright holders. See [RIGHTS.md](RIGHTS.md) for use terms and contributor rights.

## Commands

| Command        | Action                              |
| -------------- | ----------------------------------- |
| `pnpm install` | Install dependencies                |
| `pnpm dev`     | Start the local dev server          |
| `pnpm build`   | Build the static site to `./dist/`  |
| `pnpm check:sources` | Check source sections in content files |

Decisions are recorded in `docs/adr/`.

## Local previews and chat cleanup

After `pnpm build`, agents start previews with `python3 scripts/local-preview.py start --port 4321`
(choose a free port). `python3 scripts/local-preview.py status` shows the registered owner.
Project-only Codex and Claude Code hooks register each launch and send SIGTERM to that chat's
servers on `SessionEnd`; they do not stop servers when an ordinary reply ends. No global
settings are changed. Trust/enable the project hooks in your client and use a fresh session
after configuration changes. Confirm registration before relying on cleanup.

Existing servers started outside this launcher are not adopted. Forced application termination
or a crash may skip hooks; use `nadili-local-doctor` to inspect leftovers. Claude session resets
can also emit `SessionEnd`, so start a new preview when needed. Local state and logs are ignored
under `.nadili-local/`. Regression checks: `python3 scripts/test-local-preview.py`.
Worktrees share the original checkout's registry; both clients execute the script from the
active checkout resolved through Git. Keep the chat associated with this project: if its checkout
is removed before SessionEnd or hooks cannot locate it, cleanup cannot run. Inspect leftovers
with `nadili-local-doctor`.
