# Annex I — Union Harmonisation Legislation

**Instrument:** Regulation (EU) 2024/1689 (EU AI Act)
**Source:** https://eur-lex.europa.eu/eli/reg/2024/1689/oj
**Status for Stable Diffusion v1:** Not triggered — see [the assessment](../eu-ai-act-assessment.md#2-risk-classification)

> Summary for engineering and legal reference. Not a verbatim reproduction of the
> legal text — read the Official Journal before relying on any point below.

---

## What it is

Annex I is the closed list of Union product-safety legislation that feeds [Article 6(1)](article-6.md). An AI system that is a safety component of — or is itself — a product covered by one of these instruments, **and** where that product needs third-party conformity assessment, is high-risk.

**Section A — New Legislative Framework instruments:** machinery; safety of toys; recreational craft and personal watercraft; lifts; equipment for potentially explosive atmospheres (ATEX); radio equipment; pressure equipment; cableway installations; personal protective equipment; appliances burning gaseous fuels; medical devices; in vitro diagnostic medical devices.

**Section B — other Union harmonisation legislation:** civil aviation security; two- and three-wheel vehicles and quadricycles; agricultural and forestry vehicles; marine equipment; rail system interoperability; motor vehicle type-approval; unmanned aircraft and civil aviation safety (EASA).

## Why it matters here

Stable Diffusion v1 is not a regulated product and is not sold as a safety component of one, so Annex I is not engaged.

The path that would engage it is indirect: using generated output as training or validation data for a component inside one of these product categories — synthetic imagery feeding a medical imaging classifier or an automotive perception stack, for instance. The assessment flags this as an escalation signal precisely because it happens through a data pipeline rather than a product decision, and so tends not to surface in a product review.

### Naming note

The assessment's risk table lists "Annex I | Definition of AI system — confirms system is in scope." In the adopted Regulation, the definition of an AI system is **Article 3(1)**; Annex I is the harmonisation legislation list described above. The 2021 Commission proposal did use Annex I for the list of AI techniques and approaches, which is almost certainly what the row meant. The conclusion — Stable Diffusion v1 is an AI system within the Act's scope — holds under Article 3(1) either way.

## Referenced by

- Assessment §2 — cited as confirming the system is in scope
- Assessment §5 — escalation signal: "Output used as training data for a regulated safety component"

## Related

- [article-6.md](article-6.md) — the classification rule this annex serves
- [annex-iii.md](annex-iii.md) — the other route into high risk
