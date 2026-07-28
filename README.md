# Seriously Ridiculous Tattoos website

Static preview and planning repository for Amy Jane van den Bergh's artist and tattoo portfolio, booking, consent, FAQ, and future shop website.

The first dependency-free preview lives in `site/`. It deliberately uses an email-draft enquiry rather than collecting data and marks unresolved business content honestly.

## Run the preview

```sh
python3 -m http.server 4173 --directory site
```

Then open `http://127.0.0.1:4173/`. The same directory is the GitHub Pages deployment artifact.

## Start here

- [AGENTS.md](AGENTS.md): durable working rules for coding agents.
- [docs/PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md): normalized source brief and supplied copy.
- [docs/RESEARCH.md](docs/RESEARCH.md): current official research and validation gates.
- [docs/GITHUB_PAGES.md](docs/GITHUB_PAGES.md): constraints and later deployment handoff for the first review site.
- [docs/MEDIA_CURATION.md](docs/MEDIA_CURATION.md): photo inventory and the future top-25 selection method.
- [docs/DECISIONS_AND_QUESTIONS.md](docs/DECISIONS_AND_QUESTIONS.md): settled decisions and blockers that need Amy or Luke.
- [PLANS.md](PLANS.md): execution-plan format for later complex work.
- [skills/README.md](skills/README.md): repo-local agent skills and how to use them.

## Original material

`resources/` contains Amy's original brief and circular-gallery references. The local `resources/Tattoo photos/` archive is intentionally gitignored; treat it as read-only source material. Do not crop, rename, recompress, delete, or overwrite originals.

The repository tracks only 25 optimized portfolio candidates in `site/assets/portfolio/` and 10 optimized alternates in `assets/alternates/`. The full media archive is about 608 MB and must remain outside Git unless a later storage decision explicitly changes that.

## First review host

The initial client-review build will target the GitHub Pages project site at `https://lukedarlow.github.io/amy-website/`. It is a temporary static preview, not the production business/shop host. See `docs/GITHUB_PAGES.md` before choosing or configuring the framework.
