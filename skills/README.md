# Repo-local skills

These official OpenAI skill bundles are copied into the repository so their instructions, scripts, references, and licences travel with the project.

## Included

- `pdf`: render and inspect PDF briefs; used for Amy's six-page requirements document.
- `playwright`: real-browser interaction and visual-flow checks for later implementation.
- `screenshot`: OS-level capture fallback when browser- or design-specific capture is unavailable.
- `security-best-practices`: framework-specific secure-development and review guidance for the future booking, consent, and shop surfaces.
- `curate-tattoo-portfolio`: project-specific, non-destructive visual review for selecting and refreshing Amy's filename-traceable portfolio set.

Read the matching `SKILL.md` completely before using a skill. Load only the relevant referenced files it names.

## Why these four

They cover the project's demonstrated workflows: source-document review, browser verification, visual comparison, and secure handling of forms. Image generation was not copied because Amy's authentic art and photography should lead the site; use an installed image-generation capability only for a clearly requested, justified asset task. Deployment and framework-specific skills remain deferred until those choices are made.

## Discovery note

OpenAI recommends `.agents/skills` for shared automatic skill discovery. This managed workspace exposes `.agents/` as read-only, while the user requested `skills/`. `AGENTS.md` therefore routes agents here explicitly. If `.agents/` becomes writable later, link or copy this directory to `.agents/skills` rather than maintaining divergent versions.

## Provenance

Copied from the `openai/skills` curated catalog on 28 July 2026. Preserve each bundle's `LICENSE.txt` and `NOTICE.txt` files when updating.
