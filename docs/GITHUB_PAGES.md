# GitHub Pages preview contract

The first site Amy reviews will be the GitHub Pages **project site** at:

`https://lukedarlow.github.io/amy-website/`

This is a temporary, public, static preview. It is not the production booking or commerce host.

## Hard implementation constraints

- Emit static HTML, CSS, JavaScript, fonts, and optimized image derivatives into one deployment directory.
- Configure the framework's base/site path as `/amy-website/`. Never assume the site lives at `/`.
- Use base-aware internal links and asset URLs. Test both local root hosting and `/amy-website/` hosting.
- Use filenames and imports with exact case; GitHub's Linux environment is case-sensitive.
- Ensure direct navigation and refreshes work for every public URL. Prefer real generated HTML routes or a one-page anchored structure over client-only routes that require a server fallback.
- Do not depend on server-side rendering at request time, API routes, server actions, runtime environment secrets, a local database, or filesystem writes.
- Booking, signed consent, transactional email, uploads, analytics, and eventual payments require external services or a later production host. No provider is selected yet.
- Do not upload source HEIC files, the full 608 MB media corpus, private form data, or unapproved client images to the Pages artifact.
- The deployed artifact must remain comfortably below GitHub's published 1 GB site limit; the intended build should be a small fraction of that.

## Deployment approach after the stack is chosen

Use GitHub Actions rather than publishing this repository's `/docs` folder. `/docs` already contains internal planning material and must not become public site content.

The eventual workflow should:

1. Run on pushes to the default branch and allow manual dispatch.
2. Check out the repository.
3. Install dependencies from a locked dependency file.
4. Run lint, type, test, and static build commands.
5. Configure GitHub Pages.
6. Upload only the static output directory with `actions/upload-pages-artifact`.
7. Deploy it with `actions/deploy-pages` using the minimum `pages: write` and `id-token: write` permissions and the `github-pages` environment.

Do not add this workflow until the package manager, build command, and output directory are real; a placeholder workflow would make the repository fail by design.

## Preview privacy and safety

GitHub Pages is publicly reachable. "For Amy to see" does not mean access-controlled.

Before the first deploy:

- use only Amy-approved tattoo images and reviews;
- exclude contact submissions and consent records;
- avoid live consent or booking processing unless the external service and privacy disclosures are ready;
- clearly mark incomplete shop/booking behavior as preview-only;
- review the deployment artifact contents before upload;
- confirm that no `.env`, tokens, metadata inventories, original resources, or internal planning documents are included.

## Verification matrix

Before each preview deploy, verify:

- the production build succeeds from a clean checkout;
- the built site works when served under the exact repository subpath;
- no link or asset starts at an incorrect root path;
- page refresh/direct navigation works;
- 404 handling is intentional;
- mobile and desktop Chromium checks pass;
- keyboard navigation, focus, gallery controls, and reduced motion work;
- the uploaded artifact contains only public static output;
- image sizes and total artifact size are recorded.

## GitHub settings handoff

When the workflow exists, a repository administrator must choose **Settings -> Pages -> Build and deployment -> Source: GitHub Actions**. Add a deployment protection rule so only the default branch can deploy to the `github-pages` environment.

## Production boundary

GitHub's published Pages limits state that Pages is not intended or allowed as free hosting for an online business or ecommerce site. Before public launch, move the commercial booking/shop experience to an appropriate production host or confirm a compliant architecture with GitHub and the selected service providers.

Sources:

- https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
