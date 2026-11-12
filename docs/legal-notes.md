# Legal notices for ro.nadili.eu

Research and implementation notes, 2026-11-12. This records the basis and limits of the site notices, not a legal opinion or a certification of compliance.

## Scope and evidence

- Static, editorial community reference site; GitHub Pages deployment in `.github/workflows/deploy.yml`.
- Owner confirmed no analytics or data-collection service and authorised reuse of Nadili's existing email contacts. The source has no accounts, submission backend, advertising scripts or third-party embeds.
- `PageTitle.astro` now stores checklist ticks in sessionStorage after interaction, scoped to the current tab session. Previous persistent localStorage entries are neither read nor updated; the notice explains manual removal. Pagefind searches locally. Hosting still handles connection data; email correspondence contains personal data.
- The existing footer identifies Artem Manaienko. Nadili's public privacy content identifies the same person in Romania; its corrections page uses `contacts@nadili.eu`, privacy uses `privacy@nadili.eu`, and its processor register identifies Zoho Mail for those mailboxes.
- Read-only comparison with `../nadili/apps/web-relocation/src/components/locale-shell.tsx`, `src/content/privacy/uk.ts` and `src/components/corrections-form.tsx`: reuse the informational-purpose warning and correction channel. Do not import AI, subscriptions, tracking or application-database claims.

## Legal basis and design decisions

| Issue | Source | Application here |
| --- | --- | --- |
| Liability disclaimer | [Romanian Civil Code, arts. 1355–1356](https://portal.just.ro/197/Documents/NCC.pdf) | A notice cannot remove tort liability. Intentional/grossly negligent harm and protected personal interests cannot simply be waived. Explain limitations and verification steps; preserve statutory rights. |
| Operator information | [Directive 2000/31/EC, recital 18 and art. 5](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32000L0031); [Law 365/2002, arts. 1, 5–6](https://legislatie.just.ro/Public/DetaliiDocument/37075) | These concern information-society/economic services. Free access alone is not an exemption. If the site is an economic activity, supply geographic address and applicable registration/tax information, in addition to name and effective contact. Do not invent or copy an unrelated company's details. |
| Personal data | [GDPR, arts. 5–6, 12–22, 28, 44–49, 77](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) | Describe actual hosting and correspondence, controller/contact, purposes, grounds, retention criteria and rights. No blanket claim that no personal data exists. |
| Browser storage | [Law 506/2004, art. 4(5)–(6)](https://legislatie.just.ro/Public/DetaliiDocument/288598); [WP29 Opinion 04/2012](https://ec.europa.eu/justice/article-29/documentation/opinion-recommendation/files/2012/wp194_en.pdf) | Consent rule covers device storage beyond cookies, with an exception for strictly necessary requested functionality. Replace indefinite persistence with tab-session state for the requested checklist. Treat the exception as a reasoned application, not blanket exemption for localStorage. Reassess before persistent preferences or tracking. |
| Hosting | [GitHub Pages data collection](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection); [GitHub privacy](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) | GitHub logs visitor IP addresses for security. Link its policy instead of inventing a retention period or claiming EU-only processing. |
| Email | [Zoho privacy policy](https://www.zoho.com/privacy.html) | Existing mailbox provider processes correspondence; its service data is controlled by the account owner. A public policy does not establish this account's region, DPA or transfer safeguards. |

The reviewed provisions do not prescribe a universal “not legal advice” footer phrase. A permanent footer is an accessible place for the notices, not a statutory immunity mechanism. A warning does not replace correcting known errors, dating sources or handling complaints.

## Operational follow-through

- Keep notices aligned with actual behaviour. Email retention follows Nadili's existing mailbox register: quarterly review, support after 12 months from the last message, rights correspondence after 24 months, breach evidence after 60 months. Publishing this text does not perform deletion; the mailbox review remains an operator task.
- Confirm the existing mailbox account's processing agreement, region and applicable international-transfer safeguards. Provide that information to requesters; update the notice if the account arrangements differ from Nadili's register.
- Determine economic-activity status before paid listings, affiliate income, advertising or business promotion. Article 5 may then require an operator's geographic address and other applicable particulars. Current name/email publication is not presented as proof of satisfying that obligation.
- Recheck privacy before adding forms, analytics, embeds, a proxy/CDN or other providers. Domain/account settings are not fully observable from this repository.
- The Civil Code citation is the official 2011 republication. The Portal Legislativ consolidated endpoint failed during research; a Romanian lawyer should confirm current applicability and wording for a formal legal sign-off.

Existing `RIGHTS.md` remains the source for copyright permissions. No contractual acceptance checkbox, governing-law restriction or blanket waiver is introduced.
