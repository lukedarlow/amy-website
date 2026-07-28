# Research and validation gates

Checked 28 July 2026. This is implementation context, not legal advice. Re-check time-sensitive rules before launch and have Amy obtain qualified Dutch advice where needed.

## Agentic repository setup

OpenAI's current guidance recommends concise durable repository instructions in `AGENTS.md`, plans for complex work, tight permissions by default, explicit verification, and skills only for repeatable workflows. This repository follows that shape without choosing an application stack prematurely.

Sources:

- [Codex best practices](https://learn.chatgpt.com/guides/best-practices)
- [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Using PLANS.md for multi-hour problem solving](https://developers.openai.com/cookbook/articles/codex_exec_plans)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)

## Dutch tattoo practice and consent

### Findings

- Tattooing in the Netherlands requires a hygiene licence tied to a specific location. Multiple locations require separate licences. Amy's description of a "mobile studio" therefore needs operational and legal clarification before the website advertises it broadly.
- Clients must receive risk and aftercare information and sign a consent form. Regulators may inspect retained consent forms.
- The RIVM baseline requires client and artist details, tattoo/body-location details, ink manufacturer and batch/lot registration, client declarations, signatures, and a copy for the client.
- Under the currently published Dutch rules, tattooing under 12 is prohibited. Ages 12-15 require a parent/carer present and explicit consent; head, neck, wrist, and hand tattoos are prohibited for that age group. From 16, the client may decide independently. Amy may adopt a stricter business policy, but it should not be confused with the statutory minimum.
- RIVM notes that personal-data collection and retention must comply with the AVG/GDPR. Consent answers may reveal health information, which requires additional safeguards.

Sources:

- [RIVM explanation of NEN-EN 17169 and Dutch additions](https://www.rivm.nl/hygienerichtlijnen/EU-norm-toelichting-tatoeeren)
- [Official RIVM tattoo consent form (PDF)](https://www.rivm.nl/sites/default/files/2022-08/Toestemmingsformulier-tatoeage-aug2022_0.pdf)
- [Netherlands government: licence for tattooing and piercing](https://business.gov.nl/regulations/licence-tattooing-and-piercing/)

### Implementation gates

- Confirm Amy's licence, approved work location(s), and how a mobile service operates within those approvals.
- Confirm whether Amy accepts 16- and 17-year-olds or uses an adults-only policy.
- Base consent content on the current RIVM form, not a competitor's wording.
- Define collection purpose, legal basis, retention, deletion, access, processors, delivery method, and incident response before building the form.
- Do not email sensitive consent data as an unprotected attachment by default. Select a secure workflow after processor and threat review.

## Privacy, forms, and cookies

### Findings

- A business needs a reason to collect personal data, should collect only what is necessary, must protect it, limit access and retention, and explain processing in an easy-to-find privacy statement.
- Tracking cookies require prior active consent. Accept and refuse must both be clear; boxes cannot be pre-checked; continued browsing is not consent; access cannot depend on accepting tracking; withdrawal must be as easy as consent.
- Functional cookies and low-impact analytics may not require consent, although their use still needs disclosure. Therefore the brief's "cookie banner" is a requirement to investigate, not a reason to add a banner with no purpose.
- Third-party Instagram, map, video, analytics, scheduling, shop, and font embeds can change the cookie and data-transfer analysis.

Sources:

- [Dutch Data Protection Authority: personal data on the internet](https://autoriteitpersoonsgegevens.nl/en/themes/internet-and-smart-devices/personal-data-on-the-internet)
- [Netherlands government: GDPR for businesses](https://business.gov.nl/regulations/protection-personal-data/)
- [Netherlands government: cookies on your website](https://business.gov.nl/regulations/cookies/)
- [Netherlands government: creating a business website](https://business.gov.nl/starting-your-business/first-steps/creating-a-business-website/)

## Accessibility and interaction

Target WCAG 2.2 AA whether or not Amy's business is legally in scope for every accessibility rule.

The horizontal portfolio rows need alternatives to dragging/swiping, visible keyboard focus, logical focus order, accessible names, and sufficiently large controls. The sticky header must not obscure focused content. Modal/lightbox behavior needs focus containment, Escape-to-close, and focus restoration. Desaturation and full-colour transitions cannot carry essential meaning alone.

Source: [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)

## Image performance

The source corpus contains large HEIC/JPEG images and is the likely performance risk. The eventual pipeline should preserve originals, generate modern responsive derivatives, provide explicit dimensions, lazy-load off-screen gallery images, and avoid sending desktop-sized sources to phones. Meaningful tattoo images need useful alt text; decorative imagery should use empty alt text.

Sources:

- [web.dev: serve responsive images](https://web.dev/articles/serve-responsive-images)
- [web.dev: image performance](https://web.dev/learn/performance/image-performance)
- [web.dev: responsive images and alt text](https://web.dev/learn/design/responsive-images)

## Reference-site research

The five sites in the brief were reachable on 28 July 2026. A detailed visual teardown should be done in a later design task with same-viewport screenshots, because their live designs can change. Record transferable principles only; do not reproduce proprietary layouts or assets.

Questions for that teardown:

- What creates the light, simple feeling in Amy's three liked sites?
- How do they expose booking calls to action without clutter?
- Which navigation and content-density choices explain Amy's disliked examples?
- How do their FAQ, consent, portfolio, and mobile interactions work with keyboard and touch?

## Stack and service research still pending

Do not choose these until the open questions are answered:

- content management and Amy's editing workflow;
- hosting region, budget, and deployment ownership;
- booking and transactional email provider;
- secure consent workflow and storage;
- shop platform, payments, taxes, shipping, returns, and inventory;
- analytics need and privacy posture;
- domain ownership and desired language/localisation.

## GitHub Pages preview

The initial review build will target `https://lukedarlow.github.io/amy-website/`. GitHub Pages serves static HTML, CSS, and JavaScript and places this project site under `/amy-website/`, so the build must emit static files and use subpath-safe URLs. A custom GitHub Actions workflow is the appropriate later path when a non-Jekyll build process is chosen.

GitHub warns that Pages sites are public even when some source repositories can be private, and its published limits say the service is not intended or allowed as free hosting for an online business or ecommerce site. Use it only for Amy's temporary review preview. The eventual public booking/shop site needs a suitable production host.

Sources:

- [GitHub Pages overview and project-site URLs](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages)
- [Configuring a GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [Using custom workflows with GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
- [GitHub Pages limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
