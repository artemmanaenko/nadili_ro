---
name: nadili-qa
description: Review and directly edit a Nadili page for clear, concise Ukrainian, actionable instructions, and the repository's content format. Use for editorial QA of a page or as the required editing pass after nadili-investigate drafting; not a new factual investigation.
---

# Nadili QA

Accept a page path and edit the page, not just report suggestions. The goal is a practical tool a newcomer can use, not an encyclopedia or the shortest possible text.

## Establish scope

Locate the Nadili root and read its current `AGENTS.md`, `VOICE.md`, and `CONTRIBUTING.md`. For procedural pages, also read their designated reference guide. These files own the rules; do not substitute remembered copies.

Read the entire target page for context and inspect the working tree before editing. A standalone request covers the whole specified page. A call from `nadili-investigate` supplies the page path, whether it is new or updated, the intended reader outcome, changed sections or task-specific diff, and the evidence/approval ledger. A new page is reviewed in full; an update permits edits only to affected sections and their dependent overview, checklists and print memo. Do not treat unrelated pre-existing working-tree changes as part of that scope. If the caller omitted update boundaries, obtain them from the caller before editing an ambiguous scope.

When running as a child, take exclusive editing ownership of the target file; the author waits until you return. Preserve other files and unrelated changes. Do not commit, open a PR or invoke `nadili-investigate` recursively.

## Edit for the reader

Read once as someone doing this for the first time, then make the smallest useful edits:

- Make the promised result, eligibility gate, first action and completion recognizable. Distinguish submitting from receiving a result.
- Make each procedure say what to do, where, with what inputs and what to receive or save. Retain service/form links, meaningful button labels and official Romanian names; briefly explain unfamiliar terms using available evidence.
- Remove introductions, generic advice, promotional wording, legalese, historical background and explanations that do not change the reader's next action or choice. Prefer natural Ukrainian, concrete verbs and short sentences.
- Keep details at their point of use, conditions before the actions they block, and choices where they arise. Preserve meaningful alternatives and the criteria for choosing them.
- Apply the current repository format for this kind of page. Reference/contact pages do not acquire procedural steps or a print memo merely to match a guide. Repair markup and links affected by heading edits.

Do not impose word counts or a shortening percentage. Keep prerequisites, required documents, exceptions, useful context, source links, uncertainty and approved community attribution. Necessary repetition in the overview, preparation checklists and standalone print memo is not padding. Do not shorten a usable instruction into an unexplained command, or rewrite correct text merely to leave a diff.

## Check instructional images

Treat the author's instructional images as useful by default, even when the text covers the same action. Do not impose an indispensability threshold. Require the source-image inventory from investigate and compare every entry with the rendered page: embedded sanitized image beside its action, an equivalent embedded replacement, or a justified omission. A bare link is not an embedded illustration. Readable screenshots of forms, fields, choices and expected results should remain.

View both the supplied source images and the resulting assets, including images proposed for omission. Accept omission for concrete reasons such as duplicates, irrelevant decoration, demonstrated misleading/outdated content, or unresolved privacy/rights problems; reject “not essential” or “live UI inaccessible” as blanket exclusion reasons. Missing inventory, unexplained omissions or unreviewed instructional images are blocking findings: return them for completion instead of passing QA with a footnote. If the current UI cannot be checked, preserve that uncertainty and send factual concerns to the research/approval workflow, rather than assuming the image is obsolete. Standalone QA with no original source available must explicitly limit its conclusion to the page's existing images and cannot claim source-image coverage.

Compare every edited screenshot side by side with its original, not only with the page text. Check that cropping or masking has not removed useful section titles, screen/navigation context, neighboring fields, selected options, instructions, warnings, buttons or result/status information. A technically readable detail is not enough if the reader can no longer recognize the screen or reproduce the action. Require a wider sanitized image, or a wider view plus an optional detail crop, whenever needed context was cut away. Unjustified loss of context is a blocking QA finding: restore it within scope or return it to the author, then compare the revised image again before passing. If the original cannot be viewed, report that this comparison remains incomplete; do not infer that the crop is safe.

Check readability and placement beside the corresponding action. The driving-licence guide is the example. Keep the print memo image-free.

Private personal data must be completely covered with opaque marks, with readable Ukrainian placeholders over the covered areas (for example «ІМ’Я ТА ПРІЗВИЩЕ», «АДРЕСА», «НОМЕР ДОКУМЕНТА», «ПІДПИС»). Check chat headers, avatars, document photos, signatures and QR/barcodes as applicable, while preserving public contacts intended for publication. Thin strike-throughs, blur and translucent overlays do not qualify. Inspect the flattened export and check for retained layers, embedded text, metadata, unsanitized originals, filenames or alt text exposing private data.

Within scope, correct masking with an available image-editing tool and verify the resulting asset while preserving form fields and useful interface details. Treat referenced assets as part of the page's editing scope, but do not overwrite a shared asset used by unrelated pages: create a sanitized page-specific copy instead. If tools or source images are unavailable, report the exact asset and unresolved check; do not claim it passed. An image with exposed private data must not be published. These visual checks complement the coordinator's page/print checks, not replace them.

## Check the social cover

Require a topic-specific `socialImage` and an existing readable asset for the page; a shared fallback or missing file is a blocking finding. Inspect the cover for relevance, legible Ukrainian text, safe cropping and absence of private data. Preserve a suitable existing cover. Return missing/unsuitable artwork to the author; the coordinator must also verify the built `og:image` and `twitter:image` URLs and image availability before delivery. Do not mark those build checks passed from frontmatter alone.

## Reject research disguised as a step

Flag “call and clarify”, “ask ONRC”, “consult a specialist” and equivalent wording when it substitutes for missing procedure or selection criteria. This is a blocking editorial finding, not a finished action. Return the exact location, missing decision/instruction and what the author must establish; do not merely rephrase the referral or pass the page because the uncertainty is disclosed. Research gaps go back through investigate's researcher/approval workflow, not to the reader. Do not mark editorial QA complete while a blocking finding remains.

The main route must serve a newcomer without paid intermediaries. A contact step is acceptable only when supplied evidence establishes a required interaction or a genuine case-specific determination; check the trigger, inputs or precise question, expected result and next action. Do not make everyone consult an institution because some exceptional cases need it. For company-specific choices, an existing accountant may be useful: require clear inputs and a concrete requested result, not “ask your accountant” alone. Do not assume one exists or introduce hiring one; check that sourced independent selection criteria are available where possible. If they are missing, return the gap rather than inventing them.

Check locality against the supplied evidence: do not let one office's practice become a Romania-wide instruction. If the ledger establishes meaningful differences between counties (județe) or offices, require them beside the affected action, preferably as a compact comparison table when it improves clarity. Preserve case dates, circumstances, sources and the distinction between official rules and observed practice. Flag omitted documented differences, unsupported regional generalizations and speculative table rows; return unresolved factual questions to the researcher. Do not add an obligation for every reader to call their local office.

## Preserve facts and return gaps

Use the page and supplied evidence for editorial clarification. Do not invent clicks, eligibility, documents, prices, durations or outcomes. Do not silently strengthen a claim, change approval status, or reintroduce rejected/pending community claims. Preserve the source collection date unless new collection actually occurred.

If an action is not executable from available evidence, return the location and precise missing fact. Distinguish a blocking route gap from an optional omission; omit optional unknowns rather than expanding the investigation. In an investigate workflow, the coordinator sends factual gaps to its Terra/Sonnet researchers and applies the existing community-claim approval gate before returning changed sections for QA. QA does not independently start web/Telegram research. In standalone mode, report the unresolved gap without starting a full investigation or pretending to have verified the facts.

## Finish and hand back

Reread the edited route and inspect your diff: did any necessary action, condition, source or uncertainty disappear? Check dependent overview/checklist/memo text for consistency and verify affected anchors. Correct concrete remaining violations; stop when none remain in scope. Recheck only sections changed after factual resolution or later substantive edits. Do not cycle on interchangeable wording; if a blocker cannot be resolved from the inputs, return it rather than looping.

Return a short result: page path, changed or unchanged, substantive editorial fixes, and any remaining gaps with locations and specific questions. An unchanged valid page is a successful result. Label the outcome as editorial QA, not factual verification or full publication readiness.

In the investigate workflow, release file ownership and let the coordinator run final source/build/visual/print checks and independent PR review after your edits. QA does not replace them. For standalone edits, perform the applicable repository checks yourself and report any checks not performed or blocked; do not create a PR unless separately requested.
