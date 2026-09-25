**FABRICIO RODRIGUEZ**
Baltimore, MD · 240-439-5354 · frodrig3@umbc.edu · github.com/rodriguezzfabricio · linkedin.com/in/fabricio-rodriguez-816676255

**EDUCATION**
University of Maryland, Baltimore County — B.S. Computer Science, GPA 3.1 · Baltimore, MD · Aug 2022 – Dec 2026

---

**EXPERIENCE**

**The Walt Disney Company** — Software Engineering Intern, Studio Technology (AI Platform) | Jun – Aug 2026 | Burbank, CA
*TypeScript · Next.js (App Router, server components) · PostgreSQL · GitLab CI — stack learned on the job*

- Owned the member-facing model catalog for an internal AI platform used by teams across the studio: browse, detail, and comparison views resolving through a single server-side loader, so three views of the same model can never disagree about it.
- Closed a data exposure where permission-scoped access fields and admin metadata reached catalog responses served to unprivileged users — stripped at the serialization boundary, enforced at three independent points, with tests asserting the serialized JSON contains none of them.
- Unblocked seven approved merge requests that could not reach production after their base branch closed: replayed ten tickets of catalog and dashboard work onto main as one branch, resolving each conflict against a category taxonomy upstream had changed twice mid-flight.
- Designed a model access-request service end to end — schema with full audit history, user and admin REST APIs, permission-gated review queue — where approval records intent and a human still performs the grant, keeping model-spend permissions outside the application's blast radius. Built on a branch that closed unadopted.
- Learned TypeScript and Next.js on the job, shipping across 15 reviewed merge requests.

**Financial Industry Regulatory Authority (FINRA)** — Software Engineer Intern | Jun – Aug 2025 | Rockville, MD
*Python · Selenium/Playwright · Power BI · LLM APIs*

- Built synthetic monitoring for a company-wide Teams chatbot that exposed no vendor health endpoint: automation drove the real user path and alerted the team channel on failure. Ran unattended for four weeks and caught a Saturday outage.
- Categorized ~500 helpdesk tickets in Python and found the top recurring issues were knowledge-availability failures — the answer already existed and users could not find it — which redirected what the chatbot ingested; shipped the analysis as a Power BI dashboard.
- Defined what "business impact" meant for an LLM contract-review agent — prior terms vs. new terms vs. downstream policy effect — and built the model-calling component; team won 1st place at an internal 48-hour hackathon.

**American University** — Software Engineer Intern | Jan – Sep 2024 | Washington, DC
*Java · Spring Boot · PostgreSQL*

- Owned the API contract between a housing-market model built by researchers and a frontend built by another team — Spring Boot and PostgreSQL exposing health, inference, and ingest endpoints — and instrumented the usage logging that measured 40–50 daily users.

---

**PROJECTS**

**Job Application Engine** | Python, Next.js, SQLite, GitHub Actions
- Built resume tailoring that can only assert facts from an approved fact base: five deterministic checks, plus an adversarial suite that plants fabricated bullets and fails the build if the checks miss even one.
- Built the ingestion pipeline over three job-board APIs (Greenhouse, Ashby, Lever): ranked 600+ postings across 49 boards, recorded the matching phrase behind every flagged requirement, and de-duped on a company/title/location/requisition hash. 76 tests, GitHub Actions CI.

**Campus Delivery Platform** | Go, Gin, PostgreSQL/Supabase, Stripe, React Native — team of 4 | Fall 2025
- Led a 4-person team and built the Go backend: 17 token-authenticated routes, a seven-state order lifecycle with per-state timestamps, and courier actions guarded on both order state and caller ownership inside the update statement, so a courier cannot complete another's order.
- Kept payment authority on the server: the backend computes the fee split and creates the Stripe PaymentIntent, the client receives only a client secret, and an order reaches confirmed only from a signature-verified webhook, never from the client.

---

**TECHNICAL SKILLS**
Languages: Python, TypeScript, Go, Java, SQL, JavaScript
Backend & Data: Spring Boot, Gin, Next.js, PostgreSQL, Supabase, REST APIs, SQL migrations, Stripe
Frontend: React, React Native (Expo), Tailwind
Testing & CI: pytest, Playwright, Selenium, Node test runner, GitHub Actions, GitLab CI, OpenAPI contract checks
Tools: Git, GitLab merge requests, Jira, Figma, Power BI, LLM API integration
