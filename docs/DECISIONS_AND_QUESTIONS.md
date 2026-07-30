# Decisions and open questions

Update this file when Amy or Luke answers a question. Record the date and decision; do not silently infer an answer during implementation.

## Settled from the brief

- Brand name: **seriously ridiculous tattoos.**
- Tagline: **get inky with AJ**.
- Primary artist: Amy Jane van den Bergh.
- Overall feel: light, minimal, bold, colourful, warm, whimsical, and professional.
- Mobile-first, fast, succinct, easy to navigate, and easy for Amy to update.
- Portfolio resting state uses circular desaturated images; activation reveals a larger full-colour image.
- Exactly 25 tattoo works in the final tattoo portfolio.
- Shop launches later; it should not block the initial information/booking experience.
- Original files under `resources/` remain untouched.
- The first client-review host is `https://lukedarlow.github.io/amy-website/`. It is a temporary static preview, not the production commercial/shop host.

## Business and content questions

- [ ] Which city/region does Amy serve, and is Utrecht accurate for every SEO phrase?
- [ ] What does "mobile studio" mean operationally, and which work locations are licensed?
- [x] What prices and pricing rules belong in About? **30 July 2026:** publish a standard rate of €100 per hour; final quotes depend on size, placement, detail, and time.
- [ ] Does Amy accept clients aged 16-17, or is her own policy 18+?
- [ ] Is the website English-only, Dutch/English, or multilingual?
- [ ] What exact geographic/address information may be public?
- [ ] Is the WhatsApp number intended to display internationally as a `+31` number?
- [x] Are flash art, client reviews, an artist portrait, logo/wordmark, aftercare copy, and price copy available? **30 July 2026:** Amy supplied ten available flash designs, seven approved named reviews, three artist photographs, aftercare copy, and price copy. No new logo/wordmark was supplied.
- [x] May the supplied reviews, flash, and portraits be published? **30 July 2026:** Luke confirmed permission for all supplied items on the public review preview.
- [ ] Does Amy have written permission to publish every shortlisted client photo and review?
- [ ] Which 25 tattoo works does Amy ultimately approve after the structured review?

## Product and interaction questions

- [ ] Should the site be one route with anchored sections, or a one-page-feeling home plus dedicated consent/privacy/shop routes?
- [ ] Should the quote form accept image references? The brief does not request uploads, and uploads materially change privacy/security and storage.
- [ ] Should booking and regulated tattoo consent be separate workflows? This is the safer default pending Amy's process.
- [ ] Should portfolio rows show five circles only on wide screens, with fewer larger targets on mobile?
- [ ] Should reviews be text, screenshots, or structured cards with client permission?
- [ ] What content should Amy be able to edit, and from what kind of interface?

## Privacy, consent, and operations

- [x] How should the supplied consent form appear in the review site? **30 July 2026:** publish the exact supplied PDF as a clearly labelled draft download only; do not collect or submit consent data online.
- [x] How should Amy's mobile-studio and aftercare feedback be handled in this review? **30 July 2026:** use Amy's supplied wording with light proofreading. Keep the existing licensing and qualified-review gates open for production.

- [ ] What is the lawful basis and retention period for enquiries, bookings, consent forms, ink records, and declined requests?
- [ ] Who may access submissions and signed forms?
- [ ] Which email, form, file-storage, analytics, scheduling, and commerce processors are acceptable, and where do they process data?
- [ ] How should Amy and the client securely receive/access a signed consent copy?
- [ ] What deletion, correction, export, backup, and data-breach processes will Amy operate?
- [ ] Will the site use analytics, Instagram embeds, maps, video, third-party fonts, or other tracking-capable services?
- [ ] Which cookies will actually exist? Build consent behavior from the inventory, not from the word "banner."
- [ ] Who will review the final privacy notice, cookie notice, terms, consent workflow, and aftercare language?

## Shop and ownership

- [ ] Which shop platform and payment provider fit Amy's editing needs and budget?
- [ ] Where will Amy ship, and what are the tax, delivery, return, cancellation, and custom-goods rules?
- [ ] How is the 10% T-shirt tattoo discount verified and bounded?
- [ ] Who owns the domain, hosting, deployment accounts, source repository, and recurring subscriptions?
- [ ] What is the launch and monthly operating budget?

## Technical decisions intentionally deferred

- Application framework and package manager.
- CMS/content source.
- Production hosting and deployment after the GitHub Pages preview.
- Form/transactional email service.
- Secure consent service or custom workflow.
- Shop integration.
- Analytics.
- Image storage and transformation pipeline.
- Git LFS versus external storage for the 608 MB source corpus.
