# Article 13 — Transparency and Provision of Information to Deployers

**Instrument:** Regulation (EU) 2024/1689 (EU AI Act)
**Source:** https://eur-lex.europa.eu/eli/reg/2024/1689/oj
**Applicable from:** 2 August 2026 (Annex III high-risk systems)
**Status for Stable Diffusion v1:** **Not in force — contingent.** Applies only to high-risk systems. Included here because the escalation signals in assessment §5 would bring it into force.

> Summary for engineering and legal reference. Not a verbatim reproduction of the
> legal text — read the Official Journal before relying on any point below.

---

## What it requires

High-risk AI systems must be designed and developed so that their operation is **sufficiently transparent to enable deployers to interpret the system's output and use it appropriately**.

They must be accompanied by instructions for use, in an appropriate digital or other format, that are concise, complete, correct and clear, and that include:

**Provider details** — identity and contact details of the provider and, where applicable, its authorised representative.

**Characteristics, capabilities and limitations of performance**, including:
- the intended purpose;
- the level of accuracy (including its metrics), robustness and cybersecurity against which the system has been tested and validated, and any known and foreseeable circumstances that may affect it;
- any known or foreseeable circumstance related to use in accordance with the intended purpose, or under reasonably foreseeable misuse, which may lead to risks to health, safety or fundamental rights;
- the technical capabilities to provide information relevant to explaining the system's output;
- performance regarding specific persons or groups on which the system is intended to be used;
- specifications for input data, and any relevant information about the training, validation and testing data sets used;
- where applicable, information enabling deployers to interpret the output and use it appropriately.

**Human oversight measures** under Article 14, including the technical measures put in place to facilitate interpretation of outputs by deployers.

**Resources and lifecycle** — computational and hardware resources needed, expected lifetime, and the maintenance and care measures (including software updates) necessary to ensure continued proper functioning.

**Logging** — where relevant, a description of the mechanisms allowing deployers to properly collect, store and interpret the logs under Article 12.

## Why it is in this folder

Article 13 does not bind Stable Diffusion v1 at the Limited Risk tier. It is here because it is the single clearest measure of what escalation would cost.

The gap between what [Article 50](article-50.md) asks for today and what Article 13 would ask for is large and mostly documentary. Today the obligation is "mark the output." Under Article 13 it becomes: documented accuracy metrics, tested robustness thresholds, characterised performance across demographic groups, specified input data requirements, documented training data provenance, and maintained instructions for use — for a model trained on LAION-5B, whose own model card already acknowledges unmitigated demographic bias.

Two of the open gaps are effectively down-payments on Article 13, and are worth scoping with that in mind:

- **GAP-05** (model card not surfaced to users) — Article 13 would require this as formal instructions for use, not a repository file.
- **GAP-07** (no bias or fairness assessment) — Article 13(3)(b)(v) requires performance information for specific persons or groups. The commissioned bias audit is the artefact that answers it.

Article 13 also travels with company: Articles 9 (risk management), 10 (data governance), 11 (technical documentation), 12 (logging), 14 (human oversight) and 15 (accuracy, robustness, cybersecurity), plus conformity assessment and EU database registration. Article 13 is the readable proxy for that whole set.

## Referenced by

- Not cited directly in the assessment. Relevant to the escalation signals in §5 and, forward-looking, to GAP-05 and GAP-07.

## Related

- [article-6.md](article-6.md) — what makes a system high-risk in the first place
- [annex-iii.md](annex-iii.md) — the use cases that would trigger the regime
- [article-50.md](article-50.md) — the obligation actually in force today
