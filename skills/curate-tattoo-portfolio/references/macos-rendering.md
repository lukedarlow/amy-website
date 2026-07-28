# Reliable macOS review rendering

Plain `sips` conversion rendered some HEIC and colour-profiled JPEG files black during the representative corpus review. Use macOS Quick Look thumbnails for review derivatives and spot-check them against originals.

## Render source files

Create the output directory first. `qlmanage` can report success without creating it.

```bash
mkdir -p tmp/photo-curation/ql-all
qlmanage -t -s 900 -o tmp/photo-curation/ql-all \
  resources/Tattoo\ photos/*.HEIC \
  resources/Tattoo\ photos/*.heic \
  resources/Tattoo\ photos/*.JPG \
  resources/Tattoo\ photos/*.jpg \
  resources/Tattoo\ photos/*.PNG
```

Quick Look writes each derivative as `<original filename>.png`. It may require a scoped sandbox approval.

Inspect a sample from every source format and several skin-tone/colour conditions before generating sheets. Check for black frames, orientation errors, washed colour, and truncated content.

## Corpus contact sheets

Prepare a tab-separated mapping with two columns:

```text
001<TAB>resources/Tattoo photos/example.HEIC
```

Then run:

```bash
uv run --isolated --with pillow python \
  skills/curate-tattoo-portfolio/scripts/make_contact_sheets.py \
  tmp/photo-curation/mapping.tsv \
  tmp/photo-curation/all \
  tmp/photo-curation/sheets \
  tmp/photo-curation/ql-all
```

The second image-directory argument is retained for the script's non-Quick-Look mode; when the fourth argument is present, Quick Look derivatives are used.

## Selected and alternate sheets

Prepare a three-column tab-separated manifest:

```text
1<TAB>001<TAB>resources/Tattoo photos/example.HEIC
```

Run:

```bash
uv run --isolated --with pillow python \
  skills/curate-tattoo-portfolio/scripts/make_shortlist_sheet.py \
  tmp/photo-curation/selected.tsv \
  tmp/photo-curation/ql-all \
  output/photo-curation/selected-contact-sheet.jpg \
  "Proposed selection - ranked"
```

Use a separate manifest and output path for alternates. Inspect every final tile and label before delivery.
