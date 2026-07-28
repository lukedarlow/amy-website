---
name: curate-tattoo-portfolio
description: Review, group, rank, and shortlist tattoo photographs for Amy's Seriously Ridiculous Tattoos portfolio. Use when asked to choose or refresh the best tattoo images, reduce a photo corpus to a fixed count such as 25, build filename-labelled contact sheets, compare duplicate/session shots, or evaluate circular-gallery crop suitability. Keep source media immutable and make the result human-reviewable.
---

# Curate the tattoo portfolio

## Ground the review

Read `AGENTS.md`, `docs/PROJECT_BRIEF.md`, and `docs/MEDIA_CURATION.md`. Use the requested selection count; default to 25 only when the user refers to Amy's established portfolio requirement.

Treat the scorecard as decision support. Aesthetic judgment, truthful representation of the tattoo, and portfolio cohesion remain essential.

## Preserve evidence

- Treat `resources/` as read-only.
- Work from derivatives under `tmp/photo-curation/`.
- Put durable labelled review sheets under `output/photo-curation/`.
- Keep the original filename attached to every thumbnail, score, selection, alternate, and warning.
- Never publish, overwrite, retouch, rename, delete, or strip metadata from an original.

## Review the complete corpus

1. Inventory all stills by path and format. Separate videos unless the user requests video review.
2. Hash files to remove byte-identical duplicates from review without deleting them.
3. Render consistent, orientation-correct JPEG review derivatives. Verify HEIC colour and orientation against several originals before trusting the batch.
4. Build legible contact sheets with no more than about 20 images per sheet. Label every tile with a stable review index and filename.
5. Inspect every sheet. Record process shots, technical rejects, screenshots/non-tattoo media, and likely same-session groups.
6. Group multiple angles or exposures of the same tattoo. Select at most one primary frame per tattoo unless a deliberate multi-image story is requested.

Do not rank from filenames, dimensions, metadata, or automated similarity alone.

On macOS, read `references/macos-rendering.md` before rendering HEIC or profiled JPEG files. Use the bundled `scripts/make_contact_sheets.py` and `scripts/make_shortlist_sheet.py` instead of recreating sheet layout code.

## Shortlist in two passes

First pass: select roughly 1.5 times the requested count from the full sheets. Favor clear finished-work photographs and keep category breadth.

Second pass: inspect each contender at larger size and score it using `docs/MEDIA_CURATION.md`. Explicitly assess:

- tattoo craft and legibility;
- photographic quality;
- circular-thumbnail composition;
- expanded full-colour quality;
- contribution to portfolio diversity;
- fit with Amy's custom, illustrative, colourful, bird/botanical, whimsical positioning.

Keep photographic criticism separate from criticism of the tattoo itself. Flag uncertainty instead of overstating it.

## Balance the set

Before finalizing, compare the set as a whole. Avoid domination by one client, session, subject, body placement, technique, or colour treatment. Seek credible coverage of birds/botanicals, fine-line/geometric, illustrative/realism, colour/black-grey, and varied scale where the source corpus supports it.

Do not include a weaker photograph merely to fill a category. Record a coverage gap when the corpus lacks a publishable example.

## Check rights and dignity

Flag visible faces, identifying details, intimate placement, unclear authorship, unclear client permission, and source images that may expose location/device metadata. A flag does not automatically reject a strong image, but it blocks publication until resolved.

## Deliver a proposal

Create or update `docs/PHOTO_SHORTLIST.md` with:

- corpus coverage and exclusions;
- methodology and grouping notes;
- exactly the requested number of selected paths;
- concise rationale, score or tier, crop note, and permission/privacy flag per selection;
- at least 10 ranked alternates for a 25-image portfolio;
- major reject patterns and known coverage gaps;
- explicit questions for Amy/Luke.

Create filename-labelled selected and alternate contact sheets under `output/photo-curation/` when image tools are available.

## Validate

- Confirm every selected and alternate path exists.
- Confirm selected filenames are unique.
- Recheck that selections represent distinct tattoo works to the best of visual judgment.
- Count the selections programmatically and state the count.
- Inspect the final contact sheets for label legibility, correct orientation, and accidental duplicates.
- Describe the result as a proposed shortlist until Amy/Luke approves it.
