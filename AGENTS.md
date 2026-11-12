# AGENTS.md

Rules for any agent (Codex, Claude Code, others) that adds or edits content in this repository.
Read this file before you write anything. The rules grow over time; follow the current version.

## What this repository is

A public site of practical guides, reference material and contacts for Ukrainian IT professionals in Romania. It grew out of
the Telegram community https://t.me/romaniaitcommunity.

Several people contribute. They usually bring raw material, not a finished page: notes, a chat
thread, a link, a draft in any language. Your job is to turn that material into a guide that
follows these rules, then open a pull request.

For reference pages and contact lists, use the language, voice, facts and source rules below.
Use a concise format suited to the material; steps, checklists and a print memo are only required
for procedural guides. Public contact details intended for publication may be included; do not
publish private personal data from submissions.

## Workflow

1. Search `src/content/docs/guides/` for a guide on the same topic. If one exists, update it
   instead of creating a second one.
2. When updating, change only what the new material affects. Do not restructure or rewrite a
   guide unless the contributor asks for it.
3. Write or edit the guide by the rules below.
4. Run `pnpm install` (once) and `pnpm build`; the build must pass.
5. Open a pull request: one line on what changed, plus where the material came from.

For all contributions, follow `CONTRIBUTING.md` and identify the source in the pull request.

Ask the contributor only when the material is too thin to write `Кроки` and at least one
`Чек-ліст`. Otherwise write what the material supports and leave the rest out.

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
- Minimum text. Each line says what to do, or for whom it applies. If a sentence does
  neither, delete it. Long explanations belong in the institution's section, not in the
  overview steps.
- Conditions ("only if", "who this applies to") and risks go into a Starlight aside, not into
  a sentence (see Page design).
- Do not repeat a fact in several places on the page. State it once where it is acted on.

## Facts

- Never invent certainty. If the source says "it took about two weeks", do not write
  "it takes 14 days".
- Keep the uncertainty that is really there: "у нашому випадку", "станом на 2026".
- Facts that change (fees, deadlines, addresses, required documents, laws) need a source
  link in `## Джерела`.
- Remove personal data from source material: names, phone numbers, emails, document numbers.
- A fact the format asks for but the material does not give (a price, a duration) is left out,
  not guessed.
- Facts conflict: take the newest one from an official source; without one, the newest
  first-hand report.

## Guide format

A guide is a working tool, not an article. The reader opens it to find out what to bring and
what to do next, without reading prose. Every guide uses the sections below, in this order.
Skip a section only when it has nothing in it.

1. **Summary card (no heading)** - the `<Summary>` component from
   `src/components/Summary.astro`, right after the imports:

   ```mdx
   <Summary facts={[['Термін', '2-3 місяці'], ['Вартість', '139 лей + переклад']]}>
   	<Fragment slot="highlight">The one thing the reader must know before starting.</Fragment>

   	Optional one-line footnotes.
   </Summary>
   ```

   `facts` holds 2-3 short label/value pairs (duration, cost). No "where to go": the steps
   cover that.
2. **`## Кроки`** - a short overview in the Starlight `<Steps>` component: one step per
   institution or stage, each linking to its section. Each step starts with a bold action or
   the institution name, then one or two sentences.
3. **One `##` section per institution** (`## Медкомісія`, `## DRPCIV (МРЕО)`,
   `## Посольство України`), in the order the reader visits them. Everything about that place
   lives in its section, including payment for it. Inside:
   - Put `### Чек-ліст` at the end of the section, after all explanations and procedures: everything
     to have in hand when you go there, as a Markdown task
     list (`- [ ] ...`). One item per document or thing. Item format: `**Name of the thing**`
     then ` - ` and a short clarification (when it is needed, how many copies, the Romanian
     name). No conversational phrasing: "2 копії або скан", not "і пару ксерокопій". Every
     `Чек-ліст` heading gets its own print button automatically.
   - If going there needs a visit elsewhere first (e.g. a family doctor before the medical
     check), put a short `### Як пройти` with `<Steps>` before the checklist, and keep the
     checklist item itself short.
   - Add topic subsections as needed before the checklist (`### Заява`, `### Оплата`, `### Запис і подача`), with
     `<Steps>` for procedures, `<Tabs>` for alternatives (ways to pay), tables for comparisons,
     images of forms.
4. **Print memo** - a `<PrintMemo>` block (`src/components/PrintMemo.astro`) right before
   `## Джерела`. Hidden on screen; "Друк пам'ятки" prints only this. It must fit 1-2 A4
   pages: one `<div class="memo-step">` per institution with its checklist (`- [ ]`) and only
   the facts needed on the spot (form fields to tick, amounts, IBAN, where to book). No
   headings inside (they would appear in the navigation), no links (paper), no images.
5. **`## Джерела`** - links, then one line: `Зібрано YYYY-MM-DD.` Nothing else: the site
   is community experience, not legal advice, so no "verified / not verified" notes.

Other rules:

- One guide is one file in `src/content/docs/guides/`, named in lowercase Latin with hyphens:
  `register-pfa.mdx`. Images go to `src/assets/<guide-name>/`.
- Frontmatter has `title` (what the guide helps do) and `description` (one sentence for search
  results).
- Use a plain bullet list only when the material really is a list.

## Page design

The theme does the layout; write plain Markdown and the components below. Do not add your own
CSS, `<hr>`, colours or spacing.

- **Headings.** `##` only for `Кроки`, one per institution, and `Джерела`. `###` for parts of
  an institution. No `####`. Spell `Кроки`, `Чек-ліст` and `Джерела` exactly so: the theme
  finds them by name (print buttons, section numbers, hiding sources in print). `## Кроки` is
  the first `##`, `## Джерела` the last, and the task list comes right after
  `### Чек-ліст` with nothing in between. The theme draws a divider and a "Крок N" label above every
  institution `##` automatically, numbered in page order, so keep institutions in the same
  order as the overview steps.
- **Navigation.** The right-hand menu is built from `##` and `###`. Keep headings short (1-3
  words) and unique within a section. There are no links between guides.
- **Asides, by meaning:** `:::note[Лише якщо]` - who needs a step; `:::caution[...]` - a known
  risk; `:::danger[...]` - something that, if missed, breaks the process (e.g. "make a copy
  before you hand over the original"). Title of 1-3 words, body of one or two lines.
- **Tables** for comparisons (groups, clinics, bank details). Always a real header row, short
  cells, the first column names the row. No more than 4 columns.
- **Tabs** (`<Tabs>`) for alternative ways to do the same thing (pay online / terminal /
  bank). Only the open tab is printed, so the memo must cover every option.
- **Forms.** Show the fields to tick as rendered fragments of the official blank (orange =
  everyone ticks, dashed = depends), not as prose. A full filled example goes to
  `public/examples/` with personal data replaced (`DOE John`, zeros) and is linked with the
  `example-link` card.
- **Reference guide:** `src/content/docs/guides/exchange-driving-licence.mdx` uses every
  pattern above; copy markup from it.
- **Romanian terms** on the page as the reader will see them on site or on paper: `Grupa 1`,
  `Preschimbare permis străin`, `Dovada`.
- **Addresses** of offices link to Google Maps
  (`https://www.google.com/maps/search/?api=1&query=...`).
- **Third parties** (clinics, translators) are examples, not recommendations: a compact table
  with name, price, how to get there. No cards or logos.

## Before opening a pull request

1. `pnpm build` passes.
2. The text is in Ukrainian and reads naturally, not as a literal translation.
3. The print memo fits 1-2 A4 pages and covers every option shown in tabs.
4. Every changing fact has a source in `## Джерела`.
5. No personal data from the source material is left.

## Development

- `pnpm dev` runs a local server; search works only after `pnpm build && pnpm preview`.
- Site configuration: `astro.config.mjs`. Theme: `src/styles/theme.css`.
- Decisions are recorded in `docs/adr/`.
