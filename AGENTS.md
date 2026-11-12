# AGENTS.md

Rules for any agent (Codex, Claude Code, others) that adds or edits content in this repository.
Read this file before you write anything. The rules grow over time; follow the current version.

## What this repository is

A public site of practical guides for Ukrainian IT professionals in Romania. It grew out of
the Telegram community https://t.me/romaniaitcommunity.

Several people contribute. They usually bring raw material, not a finished page: notes, a chat
thread, a link, a draft in any language. Your job is to turn that material into a guide that
follows these rules, then open a pull request.

## Language

- Every guide is published in Ukrainian.
- Source material in any other language (Russian, English, Romanian, anything else) is
  translated into Ukrainian.
- Keep official Romanian names as they are, and add a Ukrainian explanation the first time:
  `ANAF (податкова служба)`, `certificat de inregistrare`.
- Technical terms stay precise. Do not replace a correct term with a vague casual word.

## Voice

Short, clear, concrete. Write like an experienced person explaining it to a colleague, from
real experience.

- Lead with what the reader has to do. Skip introductions and background nobody asked for.
- One sentence, one point. Mix short and medium sentences.
- Ordinary words. No corporate or inspirational language ("unique opportunity", "seamless",
  "game changer", and their Ukrainian equivalents).
- No AI-style templates: no "it's not X, it's Y", no "three key takeaways", no moral or
  summary paragraph at the end.
- Assume the reader is on a phone and skimming.

## Facts

- Never invent certainty. If the source says "it took about two weeks", do not write
  "it takes 14 days".
- Keep the uncertainty that is really there: "у нашому випадку", "станом на 2026".
- Facts that change (fees, deadlines, addresses, required documents, laws) need a source
  link and the date they were checked.
- Remove personal data from source material: names, phone numbers, emails, document numbers.

## Guide format

- One guide is one file in `src/content/docs/guides/`, named in lowercase Latin with hyphens:
  `register-pfa.mdx`.
- Frontmatter has `title` (what the guide helps do) and `description` (one sentence for search
  results).
- The main procedure uses the Starlight `<Steps>` component. Use a bullet list only when the
  material really is a list.
- Asides (`:::tip`, `:::caution`) hold a single point.
- End with a `## Джерела` section: links plus `Перевірено: YYYY-MM-DD`.

## Before opening a pull request

1. `pnpm build` passes.
2. The text is in Ukrainian and reads naturally, not as a literal translation.
3. Every changing fact has a source and a check date.
4. No personal data from the source material is left.

## Development

- `pnpm dev` runs a local server; search works only after `pnpm build && pnpm preview`.
- Site configuration: `astro.config.mjs`. Theme: `src/styles/theme.css`.
- Decisions are recorded in `docs/adr/`.
