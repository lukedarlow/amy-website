# Amy feedback implementation — 30 July 2026

## Purpose and user outcome

Apply Amy's second-round feedback to the static review site. Visitors will see Amy in the hero, the available flash designs, client reviews, updated FAQs, a draft consent-form download, direct WhatsApp contact, and the revised September 2026 shop teaser.

## Context and constraints

- Preserve the dependency-free static site in `site/` and GitHub Pages compatibility under `/amy-website/`.
- Preserve all supplied files in `adjustments-30-july/`; publish only generated derivatives and an exact PDF copy.
- Keep the existing 25 tattoo photographs and their circular gallery treatment.
- Consent remains a downloadable draft. The site must not collect or transmit health or consent data.
- Amy explicitly requested her mobile-studio and aftercare wording. Record, but do not conceal, the existing operational and qualified-review gates.

## Current state

The current one-page site contains the hero sunburst without a photograph, a 25-image tattoo rail, six FAQs, a mailto enquiry form, and a generic shop teaser. There are no flash, review, portrait, consent-download, or WhatsApp assets in the public artifact.

## Proposed approach

Retain the current information architecture and visual language. Extend the selected-work section with separate flash and review rails, generalize the gallery JavaScript, and use responsive generated WebP derivatives for the new images. Use Amy's square portrait in the hero. Link the supplied PDF as a clearly labelled draft and leave it byte-identical.

## Milestones

1. Generate responsive public image derivatives and copy the draft PDF; verify dimensions, file sizes, and source immutability.
2. Update markup and styling for the hero, About portraits, three portfolio rails, FAQs, contact details, and shop teaser.
3. Generalize rail controls and lightbox behavior while preserving keyboard, touch, reduced-motion, and focus behavior.
4. Run syntax and artifact checks, then inspect representative mobile and desktop viewports in a real browser.

## Progress

- [x] 2026-07-30: Reviewed all adjustment assets, current site, and project constraints.
- [x] 2026-07-30: Generated responsive public assets; the exact draft PDF copy matches the source SHA-256.
- [x] 2026-07-30: Implemented content and interactions, including Amy's live review refinements to the hero border, working-photo scale, and open-ended flash/review labels.
- [x] 2026-07-30: Completed automated and browser verification.

## Decisions

- 2026-07-30: Publish all seven named reviews and ten flash designs; permission is confirmed and all flash is available.
- 2026-07-30: Lightly proofread supplied copy without changing meaning or voice.
- 2026-07-30: Link the exact consent PDF as a draft; do not add online consent handling.
- 2026-07-30: Use Amy's supplied mobile-studio and aftercare wording, while retaining the existing review warnings.
- 2026-07-30: Initially used all three portraits. **Superseded 30 July 2026:** keep only `IMG_4094.jpg` in the hero and remove the two working photos.
- 2026-07-30: Use `#34104f` as the dark-purple ink colour.

## Discoveries and risks

- The supplied consent PDF is three pages with a nearly empty second page and describes itself as a practical template requiring comparison with current RIVM/GGD requirements.
- Dutch tattoo licences are location-specific. The mobile-studio wording still requires operational confirmation before production launch.
- The supplied flash files total about 9 MB and need responsive derivatives to avoid doubling the current artifact size.

## Verification and acceptance

- `node --check site/script.js`
- `find site/assets/portfolio -type f | wc -l` returns 25.
- `du -sh site` is recorded and remains comfortably small.
- Inspect 390x844, 768x1024, and 1440x900 layouts; exercise all rails, lightboxes, FAQs, consent download, WhatsApp link, required phone field, mailto generation, mobile navigation, keyboard focus, and reduced-motion behavior.
- Confirm every public asset path is relative, case-correct, and safe under `/amy-website/`.

Completed 30 July 2026: JavaScript syntax passed; the portfolio count remained 25; the artifact measured 14 MB; mobile and desktop Chromium showed no page-level horizontal overflow; the browser console had no errors or warnings; loaded static requests returned 200/304; the flash lightbox restored focus to its opener; visible rail controls scrolled their own rail; and the empty phone field was both required and invalid. The supplied PDF and public copy have identical SHA-256 hashes.

## Recovery and handoff

Generated images can be recreated from the unchanged adjustment sources. The site remains plain HTML/CSS/JavaScript and can be previewed with `python3 -m http.server 4173 --directory site`. If qualified review rejects the consent or safety copy, remove the draft download and replace only the affected FAQ text without changing the rest of the implementation.
