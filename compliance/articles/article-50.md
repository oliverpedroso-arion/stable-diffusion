# Article 50 — Transparency Obligations for Certain AI Systems

**Instrument:** Regulation (EU) 2024/1689 (EU AI Act)
**Source:** https://eur-lex.europa.eu/eli/reg/2024/1689/oj
**Applicable from:** 2 August 2026 — **in force as of today**
**Status for Stable Diffusion v1:** **Triggered — 50(2) and 50(4).** This is the operative obligation for the whole assessment.

> Summary for engineering and legal reference. Not a verbatim reproduction of the
> legal text — read the Official Journal before relying on any point below.

---

## The obligations

### 50(1) — interaction disclosure *(provider)*

Systems intended to interact directly with natural persons must be designed so that people are informed they are interacting with an AI system, unless that is obvious to a reasonably well-informed and observant person.

### 50(2) — synthetic content marking *(provider)* — **triggered**

Providers of AI systems — including general-purpose systems — that generate synthetic audio, image, video or text must ensure the outputs are **marked in a machine-readable format and detectable as artificially generated or manipulated**.

The technical solution must be effective, interoperable, robust and reliable as far as is technically feasible, accounting for the specificities and limitations of the content type, the cost of implementation, and the generally acknowledged state of the art.

The obligation does not apply where the AI performs an assistive function for standard editing, or does not substantially alter the input data or its semantics.

### 50(3) — emotion recognition and biometric categorisation *(deployer)*

Deployers must inform the people exposed to such systems, and process personal data in line with the GDPR.

### 50(4) — deepfake disclosure *(deployer)* — **triggered**

Deployers of an AI system that generates or manipulates image, audio or video content constituting a **deep fake** must disclose that the content has been artificially generated or manipulated.

Where the content is part of an evidently artistic, creative, satirical or fictional work, the obligation is limited to disclosing the existence of such content in an appropriate manner that does not hamper the display or enjoyment of the work.

The second subparagraph extends a parallel duty to AI-generated or manipulated **text** published to inform the public on matters of public interest — unless the content has undergone human review and a person or organisation holds editorial responsibility.

### 50(5) — timing and form

Information under 50(1), (3) and (4) must be given clearly and distinguishably at the latest at the time of the first interaction or exposure, and must meet applicable accessibility requirements.

### 50(7) — codes of practice

The AI Office is tasked with encouraging codes of practice at Union level to facilitate effective implementation of detection and labelling obligations.

## Provider vs. deployer — read this before assigning owners

**50(2) binds the provider. 50(4) binds the deployer.** These are different roles in the Act, and they attract the obligations independently.

Diffusion LLC occupies both: it builds and places the model on the EU market (provider) and runs it as a service to EU users (deployer). So both duties land on the same organisation here — but they do not land on the same *control*:

- 50(2) is satisfied in the **output pipeline**: machine-readable marking on every generated image, always, regardless of subject matter. This is GAP-01.
- 50(4) is satisfied at the **point of presentation to a person**: a disclosure that the content is artificially generated, where the content is a deepfake. This is GAP-02 and GAP-03.

A watermark alone does not discharge 50(4) — a machine-readable mark is not a disclosure to the human viewing the image. Conversely, a visible label alone does not discharge 50(2), which requires machine readability. Both controls are needed.

Note also that if Diffusion LLC distributes the model to third parties who deploy it, those deployers carry 50(4) themselves — which is what makes the Acceptable Use Policy (GAP-03) load-bearing rather than cosmetic.

## Current state

No production disclosure mechanism exists in the repository. `scripts/txt2img.py` writes raw PNGs with no embedded provenance; the `imwatermark` dependency appears only in `scripts/tests/test_watermark.py`, a test script, not an enforced path. `scripts/img2img.py` and `scripts/inpaint.py` accept arbitrary photographic input with no consent gate, identity check, or output disclosure.

`StableDiffusionSafetyChecker` addresses content safety, which is a different problem from transparency. It does not contribute to either 50(2) or 50(4).

## Penalties

Non-compliance with Article 50 falls under Article 99(4)(g): administrative fines up to €15,000,000 or 3% of total worldwide annual turnover for the preceding financial year, whichever is higher.

## Timing

Article 50 became applicable on **2 August 2026**. The assessment was written on 2026-05-08 with a six-to-eight-week remediation roadmap, which would have closed ahead of that date. As of today (2026-09-17) the obligations are live, so any gap still open is an active exposure rather than a pre-deployment task. Confirm the current status of GAP-01 through GAP-03 before treating the roadmap dates as accurate.

## Referenced by

- Assessment §2 — 50(2) and 50(4) identified as the triggered articles
- Assessment §3 — obligations in force
- Assessment §4 — GAP-01 through GAP-08 all trace back here

## Related

- [article-13.md](article-13.md) — the heavier transparency regime that applies if the system ever becomes high-risk
- [article-9-gdpr.md](article-9-gdpr.md) — disclosure does not cure the data protection question raised by photographic input
