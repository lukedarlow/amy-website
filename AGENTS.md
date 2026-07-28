# Repository guidance

## Mission

Build a distinctive, fast, mobile-first website for Seriously Ridiculous Tattoos, owned by Amy Jane van den Bergh: a South African multidisciplinary artist, tattooist, and screenprinter based in the Netherlands.

The site must feel like Amy: warm, direct, playful, bold, colourful, precise, and professional. Avoid generic tattoo-shop darkness, generic startup styling, or invented brand claims.

## Current phase

This repository is in context and planning only. Do not scaffold an application, choose a framework, create production assets, edit source media, or implement the website until the user explicitly starts development.

## Required context

Before substantial work, read the relevant files:

- `docs/PROJECT_BRIEF.md` for requirements and supplied copy.
- `docs/RESEARCH.md` for source-backed legal, privacy, accessibility, and performance constraints.
- `docs/GITHUB_PAGES.md` for the initial static preview deployment contract.
- `docs/MEDIA_CURATION.md` before inspecting or selecting portfolio photos.
- `docs/DECISIONS_AND_QUESTIONS.md` before making architecture or product assumptions.
- `PLANS.md` for complex, multi-stage work.
- The matching `skills/<name>/SKILL.md` before using a repo-local skill.

If a summary conflicts with Amy's original PDF, use `resources/Tattoo website instructions.pdf` as the product source of truth and record the discrepancy.

## Source assets

- Treat `resources/` as immutable.
- Never rename, delete, overwrite, crop, retouch, desaturate, convert, or strip metadata from an original file.
- Put temporary renders under `tmp/` and generated review artifacts under `output/`.
- Do not publish a client's image until usage permission is confirmed.
- Do not select the final 25 tattoo images casually. Follow `docs/MEDIA_CURATION.md`, preserve filenames in review artifacts, group duplicates and bursts by tattoo, and require a human confirmation pass.

## Product guardrails

- Mobile-first and progressively enhanced.
- Keyboard, touch, and screen-reader usable. A swipe interaction must have visible single-pointer and keyboard controls.
- Preserve usable colour contrast even with the bright palette and off-white background.
- Respect reduced-motion preferences.
- Prioritize responsive, correctly sized images and a strict performance budget.
- Keep copy succinct, but do not silently rewrite Amy's supplied copy. Put proposed edits in a reviewable document.
- Do not infer that a cookie banner is required merely because the brief asks for one; determine it from the final cookies and embeds. If consent is required, refusal must be equally clear and non-essential cookies must wait.

## Initial deployment target

The first review deployment is the GitHub Pages project site at `https://lukedarlow.github.io/amy-website/`. All implementation choices must therefore support fully static output under the `/amy-website/` base path, direct navigation/reloads, and case-sensitive asset paths. Do not assume server routes, server actions, runtime secrets, a database, or same-origin form/email processing.

Treat Pages as a temporary client preview, not the production commercial host. Do not publish the full `resources/` directory or any unapproved client media. Once a framework and output directory exist, add and verify a GitHub Actions Pages workflow; do not create a workflow that cannot build successfully.

## Sensitive and regulated flows

Booking and consent data can include personal and health information. Use data minimization, explicit purpose and retention rules, secure transport and storage, limited access, and an EEA-aware processor review.

Do not claim that a form, policy, tattoo practice, mobile-studio model, or shop is legally compliant. Verify current official Dutch sources, record the source and check date, and flag decisions for qualified review. The official RIVM consent form is the baseline; a visual reference site's form is not a legal source.

Never place real customer submissions, credentials, tokens, email-provider keys, or production secrets in the repo. Use placeholders in tests and examples.

## Working method

- For a complex feature or material architectural change, create and maintain an ExecPlan using `PLANS.md` before implementation.
- State assumptions and keep scope narrow.
- Prefer official and primary sources for law, standards, framework behavior, and deployment constraints.
- Add dependencies only when they remove a demonstrated need. Record why each production dependency exists.
- Once a stack is chosen, update this file with exact install, dev, lint, type-check, test, build, accessibility, and visual-regression commands.
- Verification must match risk: automated checks plus real-browser mobile and desktop review for UI work; security and privacy review for forms; visual contact sheets for media curation.
- Review the final diff and report what was verified and what remains unverified.

## Definition of done for later implementation

Work is not done until its user-visible outcome matches the brief, relevant automated checks pass, browser behavior is inspected at representative mobile and desktop sizes, accessibility basics are verified, and unresolved legal/content assumptions are documented rather than hidden.
