# Contributing

Propose corrections, new guides, reference material and useful contacts through a pull request (PR). You can also propose raw notes or material in another language in an issue. For small corrections, use the “Edit page” link on the site.

## Content

- Look for an existing page on the topic and update it instead of creating a duplicate. Change only what the new material affects.
- Publish in Ukrainian; keep official Romanian names with a Ukrainian explanation. Do not invent missing facts, and preserve the source's uncertainty.
- Follow [AGENTS.md](AGENTS.md) for procedural guides: steps, checklists, a print memo and sources. Reference pages and contact lists do not need steps or checklists; choose a concise format suited to the material.
- For changing facts such as costs, deadlines, addresses and requirements, add links under `## Джерела`. For contacts, include the source and collection date. Prefer the latest official source; otherwise use the latest first-hand report.
- Remove private personal data from submissions. Public contact details intended for inquiries may be included.

In the PR, describe what changed and where the material came from: link to an official source or a specific Telegram message or discussion. For a first-hand report without a public link, describe it in the PR, including the date, circumstances and uncertainty, without disclosing private data; link to the PR in the page's sources. Do not link only to the community's general page instead of a specific discussion.

## Checks

Node.js 24 and pnpm 11 are required. From the repository root:

```sh
pnpm install --frozen-lockfile
pnpm check:sources
pnpm build
git diff --check
```

Preview the page with `pnpm dev`. For procedures, also check the printed memo: 1–2 A4 pages, covering every option shown in tabs. Before opening a PR, review the Ukrainian text, sources and private data as described in [AGENTS.md](AGENTS.md).

CI checks the build, whitespace in the diff and the presence of a `## Джерела` section with an HTTP(S) link in changed content under `src/content/docs/guides/`. The instructional page `getting-started.mdx` is excluded. The check does not open links or determine whether a source is current, reliable or supports a claim; the author and reviewer must check that.
