# Initial static preview

## Purpose and user outcome

Build a polished, mobile-first one-page preview that lets Luke and Amy review the Seriously Ridiculous Tattoos brand direction, browse exactly 25 tattoo works, read Amy's supplied introduction, explore concise FAQs, and initiate a booking enquiry without claiming that unfinished legal, consent, shop, or pricing systems are live.

## Context and constraints

The source brief is normalized in `docs/PROJECT_BRIEF.md`; unresolved content and operational questions remain in `docs/DECISIONS_AND_QUESTIONS.md`. The preview must be fully static, work from `/amy-website/`, avoid third-party scripts, tracking, cookies, remote fonts, and live collection of personal or health data. The 25 images are provisional and need Amy's publication approval before public deployment. GitHub Pages is a review target only, not the production commercial host.

## Current state

The repository contains 25 optimized JPEG candidates in `assets/portfolio/`, 10 alternates in `assets/alternates/`, the brief, research, and contact sheets. No website code currently exists.

## Proposed approach

Use dependency-free semantic HTML, modern CSS, and a small JavaScript enhancement layer under `site/`. This makes the preview fast, transparent, and directly deployable to GitHub Pages. The gallery is a horizontally scrollable row with visible previous/next buttons, keyboard support, circular desaturated thumbnails, and an accessible full-colour dialog. The enquiry form opens a prefilled email in the visitor's mail client rather than transmitting or storing data. Missing prices, flash, reviews, aftercare, consent, and shop content are represented honestly as review placeholders.

## Milestones

1. Create the site shell, visual system, responsive sections, and static content in `site/`.
2. Integrate exactly 25 optimized images with accessible gallery and lightbox behavior.
3. Add a valid GitHub Pages workflow that uploads only `site/` and document preview boundaries.
4. Serve locally, verify desktop/mobile layout and interactions, and present the live browser preview.

## Progress

- [x] 2026-07-28: Requirements and privacy/deployment constraints reviewed.
- [x] 2026-07-28: Implemented the dependency-free site and Pages workflow.
- [x] 2026-07-28: Verified JavaScript syntax, 25 gallery entries, 25 public image files, zero missing local references, and a 5.2 MB artifact.
- [x] 2026-07-28: Reviewed Chromium at 1440x900 and 390x844; tested mobile navigation and the accessible image dialog.
- [x] 2026-07-28: Started the local preview at `http://127.0.0.1:4173/` for Luke.

## Decisions

- 2026-07-28: Use zero-dependency static files for this first preview. This minimizes build risk and is sufficient for the one-page review experience.
- 2026-07-28: Keep booking and regulated consent separate. The preview enquiry action creates a local email draft; it does not submit data to the site.
- 2026-07-28: Do not add a cookie banner because the preview sets no cookies and loads no tracking or third-party embeds.

## Discoveries and risks

- The selected photos are provisional and include identifiable people or sensitive placements. The local preview is suitable for review, but public deployment requires Amy's explicit approval and client-permission confirmation.
- Prices, flash designs, reviews, exact service area, aftercare wording, and consent workflow are not supplied; invented content would be misleading.
- The in-app browser connection was unavailable in this session. Visual QA used the installed Playwright Chromium workflow instead; the local preview server remains available to the user.
- First-device review exposed two rendering defects: intrinsic portrait ratios overrode the intended circular mask, and plain `sips` produced black derivatives for both HEIC and some colour-profiled JPEG sources. Fixed by assigning identical explicit responsive width/height values and regenerating all 25 public derivatives through macOS Quick Look before JPEG encoding. A Pillow pixel audit reported 25 files and zero black/flat images.
- Mobile review exposed an absolutely positioned About badge overlapping the heading. It now participates in a small-screen flex layout above the heading.

## Verification and acceptance

- Confirm exactly 25 gallery items and no missing assets.
- Validate internal links, dialog behavior, keyboard controls, enquiry draft behavior, reduced-motion CSS, and absence of third-party network dependencies.
- Review at approximately 390x844 and 1440x900 in Chromium.
- Confirm the Pages artifact is only `site/` and remains small.

## Recovery and handoff

The preview is self-contained in `site/` and can be served with `python3 -m http.server 4173 --directory site`. The next action after Amy's review is to record approvals and content corrections before any public deployment.
