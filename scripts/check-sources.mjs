import { execFileSync } from 'node:child_process';
import { readdirSync, readFileSync } from 'node:fs';

const directory = 'src/content/docs/guides/';
const baseIndex = process.argv.indexOf('--base');
let files;
if (baseIndex !== -1) {
  const base = process.argv[baseIndex + 1];
  if (!base) throw new Error('Expected a Git revision after --base');
  files = execFileSync('git', ['diff', '--name-only', '-z', '--diff-filter=ACMR', base, 'HEAD'], { encoding: 'utf8' }).split('\0');
} else {
  files = readdirSync(directory).map((name) => directory + name);
}

// Contact-directory provenance is recorded in the PR, not on the public page.
const exemptPages = new Set(['getting-started.mdx', 'useful-contacts.mdx']);
const candidates = files.filter((file) => file.startsWith(directory) && /\.(md|mdx)$/.test(file) && !exemptPages.has(file.slice(directory.length)));
let failed = false;
for (const file of candidates) {
  const content = readFileSync(file, 'utf8');
  const section = content.match(/^## Джерела\s*\r?\n([\s\S]*?)(?=^##\s|$(?![\s\S]))/m)?.[1] ?? '';
  if (!/\]\(https?:\/\/[^\s)]+\)/.test(section)) {
    console.error(`${file}: add an HTTP(S) link under ## Джерела`);
    failed = true;
  }
}
if (failed) process.exitCode = 1;
else console.log(`Source sections checked: ${candidates.length}`);
