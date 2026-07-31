# Repository and deployment controls

## Purpose and user outcome

Protect the public website repository from accidental or unauthorized production changes. Every proposed change to `main` must pass an automated static-site validation check, and only `main` may deploy to the GitHub Pages environment.

## Context and constraints

- Preserve the dependency-free static site and existing GitHub Pages workflow.
- Keep workflow permissions at the minimum required for checkout and Pages deployment.
- Do not commit the untracked `adjustments-30-july/` source material.
- The repository is public and owned by Luke's personal GitHub account.

## Current state

- `.github/workflows/pages.yml` deploys only on pushes to `main` and grants `pages: write` and `id-token: write` only to its deployment job.
- The `github-pages` environment already has a custom deployment branch policy allowing only `main`.
- Only `lukedarlow` currently has repository write access.
- Active ruleset `protection` blocks deletions and non-fast-forward pushes and requires pull requests, but has no required automated status check.

## Proposed approach

Add a dependency-free Node validation script and a pull-request workflow with read-only repository permissions. Run the validation once, then add its exact check name to the existing active ruleset. Retain the current Pages job permissions and verify the environment branch restriction through the GitHub API.

## Milestones

1. Add and locally run static-site validation covering JavaScript syntax, required files, asset references, portfolio count, symlinks, and artifact size.
2. Add a read-only GitHub Actions validation workflow for pull requests and `main`.
3. Push the workflow, confirm both validation and Pages deployment succeed, then require the validation check in the existing ruleset.
4. Re-read repository access, ruleset, Actions permissions, and Pages environment settings.

## Progress

- [x] 2026-07-31: Audited repository access, the existing ruleset, deployment workflow, and Pages environment.
- [x] 2026-07-31: Added and verified dependency-free validation locally (54 files, 25 portfolio images, 12.8 MiB).
- [ ] Push and observe the new validation workflow.
- [ ] Require the check and verify final controls.

## Decisions

- 2026-07-31: Extend the existing `protection` ruleset instead of creating an overlapping second ruleset.
- 2026-07-31: Keep validation dependency-free to match the site's architecture and reduce supply-chain exposure.
- 2026-07-31: Keep deployment permissions scoped to the deployment job; validation receives only `contents: read`.

## Discoveries and risks

- A required status check must exist on GitHub before it can be safely enforced and tested.
- The active ruleset has no bypass actors, so direct pushes to targeted branches are intentionally blocked after enforcement.

## Verification and acceptance

- `node scripts/validate-site.mjs`
- `node --check site/script.js`
- GitHub validation workflow succeeds on the pushed commit.
- Ruleset requires the `validate` status check and retains deletion, non-fast-forward, and pull-request rules.
- `github-pages` environment accepts deployments only from `main`.
- Only the repository owner has write access.

## Recovery and handoff

The validation requirement can be removed from the existing ruleset if an emergency correction is needed. The workflow and script are ordinary committed files and can be reverted through a pull request. The untracked adjustment sources remain untouched.
