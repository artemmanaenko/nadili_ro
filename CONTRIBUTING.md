# Contributing

Share corrections, raw notes, sources, or useful contacts in an issue, or give them directly to your agent. Material in any language is welcome.

## Agent-friendly workflow

Agents handle the repository work for content contributions.

1. Give your agent the material and point it to [AGENTS.md](AGENTS.md). The agent writes or updates the page, runs the checks below, and opens a pull request (PR).
2. Have another agent review the PR against the repository rules and cited sources. The authoring agent addresses its findings.
3. A human checks that the page is clear in the site preview and that its claims reflect current practice and are backed by the sources.

## Content

- Look for an existing page on the topic and update it instead of creating a duplicate. Change only what the new material affects.
- Publish in Ukrainian; keep official Romanian names with a Ukrainian explanation. Do not invent missing facts, and preserve the source's uncertainty.
- Follow [AGENTS.md](AGENTS.md) for procedural guides: steps, checklists, a print memo and sources. Reference pages and contact lists do not need steps or checklists; choose a concise format suited to the material.
- For changing facts such as costs, deadlines, addresses and requirements, add links under `## Джерела`. For contacts, include the source and collection date. Prefer the latest official source; otherwise use the latest first-hand report.
- Remove private personal data from submissions. Public contact details intended for inquiries may be included.

In the PR, describe what changed and where the material came from: link to an official source or a specific Telegram message or discussion. For a first-hand report without a public link, describe it in the PR, including the date, circumstances and uncertainty, without disclosing private data; link to the PR in the page's sources. Do not link only to the community's general page instead of a specific discussion.

## Rights in contributions

You retain copyright in your contribution. By submitting a pull request, you grant the project a non-exclusive, worldwide, royalty-free, ongoing permission to reproduce, edit, translate, publish and distribute your contribution as part of the repository and site. You confirm that you have the rights or permission needed to grant this permission. Do not submit third-party material unless its terms permit these uses; identify its source and applicable terms.

The project does not claim ownership of your contribution. See [RIGHTS.md](RIGHTS.md) for the repository's use terms and the rights retained by others.

## Listings for companies and service providers

The project's primary purpose is to share practical information with the community. The site may list companies and independent service providers whose services are relevant to readers.

The repository owner may add listings directly. Other contributors, including maintainers, propose listings through a regular PR. The owner or a maintainer other than the PR author must approve the listing before it is published.

## Checks

Node.js 24 and pnpm 11 are required. From the repository root:

```sh
pnpm install --frozen-lockfile
pnpm check:sources
pnpm build
git diff --check
```

Preview the page with `pnpm dev`. For procedures, also check the printed memo: 1–2 A4 pages, covering every option shown in tabs. Before opening a PR, review the Ukrainian text, sources and private data as described in [AGENTS.md](AGENTS.md).

CI checks the build, whitespace in the diff and the presence of a `## Джерела` section with an HTTP(S) link in changed content under `src/content/docs/guides/`. The instructional page `getting-started.mdx` is excluded. When reviewing the content, open the sources and check whether they are current, reliable and support the claims.
