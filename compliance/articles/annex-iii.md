# Annex III — High-Risk Use Cases

**Instrument:** Regulation (EU) 2024/1689 (EU AI Act)
**Source:** https://eur-lex.europa.eu/eli/reg/2024/1689/oj
**Applicable from:** 2 August 2026
**Status for Stable Diffusion v1:** Not triggered — see [the assessment](../eu-ai-act-assessment.md#2-risk-classification)

> Summary for engineering and legal reference. Not a verbatim reproduction of the
> legal text — read the Official Journal before relying on any point below.

---

## The eight categories

| § | Area | Covered uses (abbreviated) |
|---|---|---|
| 1 | **Biometrics** | Remote biometric identification; biometric categorisation by sensitive or protected attributes; emotion recognition — insofar as permitted at all under [Article 5](article-5.md) |
| 2 | **Critical infrastructure** | Safety components in the management and operation of road traffic, and in the supply of water, gas, heating and electricity |
| 3 | **Education and vocational training** | Admission or assignment to institutions; evaluating learning outcomes; assessing the appropriate level of education a person will receive; monitoring and detecting prohibited behaviour during tests |
| 4 | **Employment and workers management** | Recruitment and selection (targeted job ads, filtering applications, evaluating candidates); decisions on promotion, termination, task allocation; monitoring and evaluating performance and behaviour |
| 5 | **Essential private and public services** | (a) Eligibility for public assistance benefits and services; (b) creditworthiness and credit scoring (excluding financial fraud detection); (c) risk assessment and pricing in life and health insurance; (d) emergency call triage and dispatch of emergency services |
| 6 | **Law enforcement** | Risk assessments of offending or re-offending, polygraphs, evidence reliability evaluation, profiling in the course of investigations |
| 7 | **Migration, asylum and border control** | Risk assessments, examination of applications, detection and recognition of persons |
| 8 | **Justice and democratic processes** | Assisting judicial authorities in researching and interpreting facts and law; influencing the outcome of an election or referendum, or voting behaviour |

The Commission may amend this list under Article 7. Treat it as a moving target, not a fixed schedule.

## Why it matters here

Text-to-image and image-to-image synthesis is not an Annex III use case. Generation alone stays outside the list regardless of how capable the model is.

The distance between the current system and Annex III is short in three places, and each is a wiring decision rather than a model change:

- **§1 (biometrics)** — attaching face matching or identity retrieval to the FFHQ configuration or CLIP image encoder.
- **§3, §4, §5 (education, employment, credit)** — routing `ldm/models/diffusion/classifier.py` into any decision about a person's access to schooling, a job, or credit.
- **§5(a)** — the assessment reads content scoring tied to user access as touching eligibility for services. This is the most interpretive of the mappings: §5(a) is written for *public* assistance benefits and services, so a commercial access tier is a weaker fit than the education, employment and credit signals. It is worth a second read with counsel rather than being treated as settled.

Anything that lands in Annex III pulls in the full high-risk regime: risk management (Article 9), data governance (Article 10), technical documentation (Article 11), logging (Article 12), [transparency to deployers (Article 13)](article-13.md), human oversight (Article 14), accuracy and robustness (Article 15), conformity assessment, and registration. That is a programme of work, not a patch.

## Referenced by

- Assessment §2 — reviewed and not triggered
- Assessment §5 — escalation signals mapping to §1, §3, §4, §5 and §5(a)

## Related

- [article-6.md](article-6.md) — Article 6(2) is what makes this list binding, and 6(3) is the narrow way out
- [article-5.md](article-5.md) — where biometric uses cross from high-risk into prohibited
