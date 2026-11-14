# Runtime adapters

Read only the section for the current client. Discover actual tool names and capabilities; this file does not install tools or grant permissions.

## Codex

- Discoverable entrypoint: `.agents/skills/nadili-investigate/SKILL.md` in the project.
- Use the runtime's subagent tool with an available Terra model. When `collaboration.spawn_agent` exposes `gpt-6.1-terra`, select it explicitly and use `fork_turns: "none"` when required for model overrides. Supply a self-contained brief; do not rely on inherited chat context.
- Inspect the launch result and runtime-reported model where available. A model name in a prompt is not model selection. If Terra is unavailable or selection cannot be honored, request a specific one-time substitute.
- Let the researcher use the available computer tool, such as `mcp__cua_repl`, following its initialization and completion protocol. Confirm the child can actually access the tool; parent-only access is a capability gap requiring an explicit substitution decision. Prefer the user's existing Telegram session. Native Telegram and Telegram Web are both valid when accessible.
- For official-source research, the child uses available web search/open tools; the parent receives source-backed findings.

## Claude Code

- Discoverable entrypoint: `.claude/skills/nadili-investigate`, a relative symlink to `../../.agents/skills/nadili-investigate`. Do not duplicate the skill body or modify global settings.
- Use the installed runtime's Agent/subagent facility with explicit `model: "sonnet"` when supported. A prompt saying “act as Sonnet” is insufficient. Check available launch metadata for overrides or failures; request a one-time substitute if the runtime cannot honor the selection. Do not pin a speculative version identifier.
- Use a child agent with the computer/browser tools needed for Telegram. Do not assume that a built-in research agent inherits Chrome or MCP tools. Verify child access first; if unavailable, ask for a specific alternative instead of moving research silently to the parent.
- Use available browser/computer integration (for example an already configured Chrome integration or computer MCP). Follow that tool's instructions, request user login when needed, and keep navigation read-only. Do not install extensions or change account settings as an implicit part of the skill.
- Delegate official-source verification to Sonnet using its available search/fetch/browser tools.

## Shared handoff and fallback

The coordinator assigns computer ownership by agent name, then waits for release before another agent uses that surface. Web-only researchers must not navigate the shared browser while it is owned by someone else. If verification needs that browser, serialize it with Telegram work.

If blocked, state the actual missing capability and propose a concrete substitution: for example, another available research model, parent-operated Telegram on the user's explicit authorization, or user-supplied message text with links and dates. Approval applies only to that run and substitution. Mark substituted or missing source coverage in the evidence ledger and final report. Never claim that supplied text was independently inspected in Telegram.

Test discovery from the repository root in a fresh client session: verify `nadili-investigate` appears in the client's skill list or available-skill context, and its reference resolves through both paths. File existence alone proves packaging, not client discovery. Do not run a live investigation merely to test discovery.
