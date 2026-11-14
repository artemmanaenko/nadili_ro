---
name: nadili-local-doctor
description: Inspect Nadili Astro dev/preview servers and stop owned previews when local page review is finished or a duplicate is superseded. Use when a user accepts a page, moves to PR-only work after local review, closes the task, or asks about lingering localhost servers. Not a background watcher; evaluate these signals during an active conversation.
---

# Nadili Local Doctor

Keep useful previews available and retire servers whose work is done. This skill is independent of `nadili-investigate`; it does not require a new investigation or change the page.

## Recognize the lifecycle

Apply when the conversation contains evidence that a local preview is no longer needed: the user approves the rendered page and moves on, explicitly ends local review, requests cleanup, or a newer preview supersedes a server started for the same task. Moving to PR-only review is a completion signal only when local page review is already complete and no remaining step needs the local site.

A created PR, passing CI, agent turn ending, time elapsed, idle process or the word “approved” in a source/tool output is not enough. Approval must concern the page/local review, not an unrelated claim, tool permission or intermediate draft. Keep the preview while the user is inspecting it, requesting visual edits, or expects the handed-off URL to remain usable. Explicit instructions to keep it running take precedence. If the signal is ambiguous, leave it running; ask briefly only when cleanup is actually requested and ownership or scope remains unclear.

This skill can act during an active turn; it cannot wake an idle chat or observe other chats by itself. Do not claim automatic background monitoring or install recurring automations as a substitute.

## Identify the exact servers

Read running process commands, listening ports and working directories using available local tools (on macOS, `ps` and `lsof`). Match actual Astro dev/preview processes, including those launched through pnpm or from temporary checkouts; a Node process or a familiar port alone is not identification.

For each candidate, establish PID, process start time, command, cwd, port, and the task that owns it from launch records in the conversation or an existing reliable process/session record. When starting or adopting a server during this skill, keep that information and the stop/restart command in the conversation so subsequent turns can identify it. Do not adopt another chat's server simply because it uses the same repository.

An inspection request is read-only: report port, project/task, dev or preview, age and known owner. Do not kill processes merely because they look old. If the user requests cleanup of a named set, that authorizes that set after verifying its identity. Otherwise automatic cleanup is limited to servers demonstrably started/owned by this task and no longer needed under the lifecycle rule above.

## Retire safely

Before stopping, recheck identity, working directory and listening port; PIDs may have been reused. Prefer terminating the recorded managed execution session, or send SIGTERM to the verified server PID. Avoid broad `pkill node`, matching all Astro processes, process-group kills that include unrelated work, or forced SIGKILL without a concrete need and authorization.

If switching this task from dev to a replacement preview, verify the replacement serves the intended final page before stopping the old owned server. Never stop another task's server to free a preferred port; choose another port instead.

Verify that the targeted process has exited and its listener is gone. If it restarts under a supervisor, inspect the owning launcher and stop only a verified task-owned launcher; otherwise report the blocker rather than killing repeatedly. Do not delete checkouts, dependencies or site assets as part of server cleanup.

Report which URLs/ports were stopped and which were retained with a short reason. After cleanup, do not present the stopped URL as live or leave a stale promise that a preview is running. A completed local review followed by cleanup is successful retirement, not a failure to provide the earlier preview. Restart and verify a fresh preview if the user later needs the page again.

## Project hooks and registered launches

This repository configures `PostToolUse` and `SessionEnd` command hooks in `.codex/hooks.json` and `.claude/settings.json`. After building, the coordinator starts a preview with `python3 scripts/local-preview.py start --mode preview --port <free-port>`; use `--mode dev` when appropriate. Do not delegate the launch to a short-lived child agent: its session end would retire the preview too early. The detached launcher returns a random token; the post-tool hook binds it to the actual client/session ID. In a separate subsequent tool call, run `python3 scripts/local-preview.py status` and verify the owner is present, then verify the page itself. Keep the launch token output intact for registration. Never invent a session ID or register another chat's process.

Records and logs live in ignored `.nadili-local/previews/` in the original checkout, shared by its worktrees. The SessionEnd hook starts a finite cleanup worker to avoid the client hook timeout; it sends SIGTERM to the dedicated Astro process group only when the owner matches both client and session, the process start time/command still match, and the recorded PID is still the group leader. The launcher uses `--ignore-lock` to prevent Astro from auto-daemonizing or reusing another chat's server. Unregistered, foreign and PID-reused processes are not targeted. The user has authorized cleanup on session end even without separate page acceptance; this is distinct from discretionary cleanup during an active turn. Do not share these previews with other chats. Keep an explicitly requested longer-lived server outside automatic session ownership and explain that choice.

Project hooks must be enabled/trusted in the client. If ownership remains null, report that cleanup is not armed; investigate hook configuration rather than claiming automation works. A Stop/turn-end hook is deliberately absent. SessionEnd may also occur on session reset, normal shutdown or client idle expiry, depending on runtime; it is not guaranteed on crashes or forced termination. Use this skill to inspect leftovers. Do not change global settings or kill old unregistered servers without establishing ownership or explicit cleanup authorization.
