# Article 6 — Classification Rules for High-Risk AI Systems

**Instrument:** Regulation (EU) 2024/1689 (EU AI Act)
**Source:** https://eur-lex.europa.eu/eli/reg/2024/1689/oj
**Applicable from:** 2 August 2026 (high-risk obligations under Annex III); 2 August 2027 for Annex I embedded products
**Status for Stable Diffusion v1:** Not triggered — see [the assessment](../eu-ai-act-assessment.md#2-risk-classification)

> Summary for engineering and legal reference. Not a verbatim reproduction of the
> legal text — read the Official Journal before relying on any point below.

---

## The two routes into high risk

### Article 6(1) — embedded in a regulated product

An AI system is high-risk where **both** conditions hold:

1. It is intended to be used as a safety component of a product, **or** is itself a product, covered by the Union harmonisation legislation listed in **[Annex I](annex-i.md)**; and
2. That product is required to undergo a third-party conformity assessment under that legislation.

### Article 6(2) — listed use case

An AI system falling into one of the use cases in **[Annex III](annex-iii.md)** is high-risk.

### Article 6(3) — the derogation

An Annex III system is *not* high-risk if it does not pose a significant risk of harm to health, safety or fundamental rights, including by not materially influencing the outcome of decision-making. This is available where the system:

- performs a narrow procedural task;
- improves the result of a previously completed human activity;
- detects decision-making patterns or deviations from prior patterns without replacing or influencing human assessment; or
- performs a preparatory task to an Annex III assessment.

The derogation is **never** available where the system performs profiling of natural persons.

A provider relying on the derogation must document the assessment before placing the system on the market and register it (Article 6(4)).

## Why it matters here

Neither route is engaged. Stable Diffusion v1 is a general-purpose image generator sold as such, not a safety component of a regulated product, and image synthesis is not an Annex III use case.

What makes Article 6 worth keeping in front of the Head of Legal is that **the classification follows intended purpose, not model architecture**. The same weights become high-risk the moment they are wired into a hiring screen, an education assessment, a credit decision, or a biometric matcher. `ldm/models/diffusion/classifier.py` is the component most likely to be repurposed that way.

### Numbering note

The assessment document describes Article 6(1) as "high-risk definition by **Annex II** embedding." In the adopted Regulation (EU) 2024/1689 the harmonisation legislation list is **Annex I**; Annex II is the list of criminal offences referred to in Article 5(1)(h). The Annex II label reflects the 2021 Commission proposal's numbering, which shifted before adoption. The substance of the finding — not triggered — is unaffected.

## Referenced by

- Assessment §2 — Article 6(1) and 6(2) reviewed, neither triggered
- Assessment §5 — four of the five escalation signals resolve through Article 6(2)

## Related

- [annex-i.md](annex-i.md) — the harmonisation legislation list behind 6(1)
- [annex-iii.md](annex-iii.md) — the use-case list behind 6(2)
- [article-13.md](article-13.md) — the transparency duty that attaches once a system is high-risk
