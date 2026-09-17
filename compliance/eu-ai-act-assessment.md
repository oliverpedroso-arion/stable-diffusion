# EU AI Act Compliance Assessment
## Stable Diffusion v1 — Diffusion LLC
**Assessment date:** 2026-05-08
**Assessed by:** Compass (EU AI Act Compliance Auditor)
**Compliance lead:** Head of Legal, Diffusion LLC
**Infrastructure:** EU data centres
**Repository:** oliverpedroso-arion/stable-diffusion@98392aa

---

## 1. System Overview

Stable Diffusion v1 is a latent diffusion model for text-to-image and image-to-image synthesis. It is built and deployed by Diffusion LLC, offered on the EU market, and used by EU-based organisations and individuals. The system is capable of generating realistic likenesses of real, identifiable people without their consent and of producing synthetic media attributable to real public figures.

---

## 2. Risk Classification

**Tier: LIMITED RISK**

### Reasoning

| Signal | Status |
|---|---|
| Prohibited practice (Article 5) | Not triggered |
| High-Risk Annex III use case | Not triggered |
| Generates synthetic visual content | ✓ Confirmed |
| Capable of realistic likenesses of real people | ✓ Confirmed |
| Capable of synthetic media attributed to real public figures | ✓ Confirmed |
| Processes personal data | Not confirmed |
| Special-category personal data (GDPR Article 9) | Not confirmed |
| Deployed in EU | ✓ Confirmed |

### Applicable Articles

| Article | Topic |
|---|---|
| Article 5 | Prohibited AI practices — reviewed and not triggered |
| Article 6(1) | High-risk definition by Annex II embedding — not triggered |
| Article 6(2) | High-risk definition by Annex III use case — not triggered |
| Annex I | Definition of AI system — confirms system is in scope |
| Annex III | High-risk categories — reviewed and not triggered |
| **Article 50(2)** | **Disclosure obligation for synthetic image content — triggered** |
| **Article 50(4)** | **Deepfake disclosure obligation — triggered** |

---

## 3. Obligations in Force (Limited Risk Tier)

### Article 50(2) — Synthetic Content Disclosure

AI systems that generate synthetic image, audio, or video content must disclose that the content is AI-generated. This disclosure must be machine-readable and visible to the person receiving the content.

**Current state:** No disclosure mechanism is present in the codebase. `scripts/txt2img.py` outputs raw PNG files with no embedded metadata indicating AI origin. The watermarking utility (`scripts/tests/test_watermark.py`) exists but is a test script, not a production enforcement control.

**Gap:** Critical. No production watermark or disclosure pipeline is in place.

### Article 50(4) — Deepfake Disclosure

Where AI-generated images depict real, identifiable natural persons (deepfakes), the system must clearly disclose that the images are artificially generated or manipulated, except in legitimate contexts such as satire or journalism with appropriate disclosure.

**Current state:** `scripts/img2img.py` and `scripts/inpaint.py` accept arbitrary image input with no consent verification, no identity check, and no deepfake disclosure output. `StableDiffusionSafetyChecker` (called in `scripts/txt2img.py`) provides content safety filtering but does not address deepfake disclosure.

**Gap:** Critical. No consent gate, no identity verification, and no deepfake disclosure label on output.

---

## 4. Compliance Gaps

### Critical Gaps — Must resolve before or at deployment

#### GAP-01: No AI-generated content disclosure on output
- **Article:** Article 50(2)
- **Domain:** Code
- **Owner:** Engineering
- **Detail:** `scripts/txt2img.py` writes output images with no machine-readable or visible disclosure that they are AI-generated. The test watermark decoder in `scripts/tests/test_watermark.py` shows the dependency (`imwatermark`) is available but is not wired into the production output pipeline.
- **Remediation:** Embed a C2PA-compliant content credential or invisible watermark into every output image in `scripts/txt2img.py`, `scripts/img2img.py`, and `scripts/inpaint.py`.
- **Effort:** 1–2 weeks (Engineering)

#### GAP-02: No deepfake disclosure for likenesses of real people
- **Article:** Article 50(4)
- **Domain:** Code / Process
- **Owner:** Engineering + Legal
- **Detail:** `scripts/img2img.py` and `scripts/inpaint.py` accept uploaded images of real people with no consent gate, no identity check, and no disclosure requirement on output. This is the highest-exposure gap given the confirmed capability to generate realistic likenesses.
- **Remediation:** Add a terms-of-use gate in the input pipeline requiring user acknowledgement that uploaded images are of themselves or are used with consent. Add a visible disclosure label to all output images generated from photographic input.
- **Effort:** 2–3 weeks (Engineering + Legal)

#### GAP-03: No terms of service covering synthetic media obligations
- **Article:** Article 50(4)
- **Domain:** Process/documents
- **Owner:** Legal
- **Detail:** No terms of service, acceptable use policy, or user-facing disclosure document is present in the repository or referenced in any configuration.
- **Remediation:** Draft and publish an Acceptable Use Policy (AUP) that prohibits non-consensual deepfakes, requires users to disclose AI-generated content in contexts where disclosure is legally required, and reserves the right to suspend accounts for violation.
- **Effort:** 1 week (Legal)

---

### High Gaps — Resolve within 30 days of deployment

#### GAP-04: Safety checker is not enforced across all generation scripts
- **Article:** Article 50(2), Article 50(4)
- **Domain:** Code
- **Owner:** Engineering
- **Detail:** `StableDiffusionSafetyChecker` is called in `scripts/txt2img.py` but is absent from `scripts/img2img.py` and `scripts/inpaint.py`. These two scripts process user-uploaded images and are higher-risk surfaces for generating non-consensual likenesses.
- **Remediation:** Enforce safety checker across all three generation scripts. Add a prompt-content filter for named public figures as an additional control.
- **Effort:** 1 week (Engineering)

#### GAP-05: No model card or technical documentation surfaced to users
- **Article:** Article 50(2)
- **Domain:** Process/documents
- **Owner:** Legal + Engineering
- **Detail:** `Stable_Diffusion_v1_Model_Card.md` exists in the repository but is not surfaced to end users at point of use. Article 50 disclosure obligations require that users understand they are interacting with an AI system.
- **Remediation:** Surface model card information (capabilities, limitations, known biases) in the product UI or API documentation. Link to it from the AUP.
- **Effort:** 1 week (Legal + Engineering)

#### GAP-06: No monitoring or logging of generation events
- **Article:** Article 50(4)
- **Domain:** Tech
- **Owner:** Engineering lead
- **Detail:** There is no logging of generation events (prompt, input image hash, output image hash, timestamp) in any of the scripts. Without logs, it is not possible to investigate complaints of non-consensual deepfake generation or demonstrate compliance to a regulator.
- **Remediation:** Add a generation event log (non-personal, hash-based) to all three generation scripts. Retain for a minimum period aligned with your legal hold policy.
- **Effort:** 1–2 weeks (Engineering lead)

---

### Medium Gaps — Resolve within 60 days of deployment

#### GAP-07: No bias or fairness assessment on training data
- **Article:** Article 50(2) (transparency principle)
- **Domain:** Process/documents
- **Owner:** Head of Legal + Engineering lead
- **Detail:** `Stable_Diffusion_v1_Model_Card.md` acknowledges training data biases (LAION-5B dataset, known over-representation of certain demographics) but no formal bias assessment or mitigation plan is documented.
- **Remediation:** Commission a bias audit of model outputs across demographic categories. Document findings and mitigations in an updated model card.
- **Effort:** 3–4 weeks (Data Science + Legal)

#### GAP-08: No process for handling deepfake complaints
- **Article:** Article 50(4)
- **Domain:** Process/documents
- **Owner:** Legal
- **Detail:** No takedown, complaint, or right-of-reply process exists for individuals who believe a realistic likeness of them has been generated without consent.
- **Remediation:** Draft a deepfake complaint and takedown procedure. Publish a contact route in the AUP. Set a maximum response SLA.
- **Effort:** 1 week (Legal)

---

## 5. High-Risk Escalation Signals

The following are not current gaps but are architectural signals that would immediately escalate this system to High Risk if acted upon. The Head of Legal should be aware of each before any engineering change in these areas is approved.

| Signal | File(s) | High-Risk trigger | Article |
|---|---|---|---|
| Classifier wired into hiring, education, or credit decision | `ldm/models/diffusion/classifier.py` | Annex III §3, §4, §5 | Article 6(2) |
| Face matching added on top of FFHQ or CLIP image encoder | `configs/latent-diffusion/ffhq-ldm-vq-4.yaml`, `ldm/modules/encoders/modules.py` | Annex III §1 | Article 6(2), Article 5(1)(e) |
| Safety checker bypassed + content scoring tied to user access | `scripts/txt2img.py` (`check_safety()`) | Annex III §5(a) | Article 6(2) |
| User prompts or uploaded images logged against identities | `scripts/img2img.py`, `scripts/inpaint.py` | GDPR Article 35 DPIA | GDPR Article 35 |
| Output used as training data for a regulated safety component | All generation scripts | Annex II embedding | Article 6(1) |

---

## 6. Remediation Roadmap

### Week 1–2: Legal framework
- [ ] Draft and publish Acceptable Use Policy (GAP-03) — Legal
- [ ] Draft deepfake complaint and takedown procedure (GAP-08) — Legal
- [ ] Surface model card in product UI or API docs (GAP-05) — Legal + Engineering

### Week 3–4: Code controls
- [ ] Embed C2PA watermark or content credential in all generation scripts (GAP-01) — Engineering
- [ ] Add consent gate and deepfake disclosure label to `scripts/img2img.py` and `scripts/inpaint.py` (GAP-02) — Engineering + Legal
- [ ] Enforce safety checker across all generation scripts (GAP-04) — Engineering

### Week 5–6: Monitoring and audit trail
- [ ] Add hash-based generation event log to all scripts (GAP-06) — Engineering lead
- [ ] Commission bias audit of model outputs (GAP-07) — Data Science + Legal

### Ready for compliant deployment: Week 6–8

---

## 7. Disclaimers

- This assessment is guidance, not legal advice. Consult qualified legal counsel before final deployment decisions.
- Interpretations of the EU AI Act may vary. Regulators retain enforcement discretion.
- This assessment reflects the EU AI Act (Regulation (EU) 2024/1689) and GDPR as in force at the date above.
- Re-run this assessment after any material change to the system's capabilities, deployment context, or use cases.
- Version 1.0.0 (2026-05-08).