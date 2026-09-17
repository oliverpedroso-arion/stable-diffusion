# Article 5 — Prohibited AI Practices

**Instrument:** Regulation (EU) 2024/1689 (EU AI Act)
**Source:** https://eur-lex.europa.eu/eli/reg/2024/1689/oj
**Applicable since:** 2 February 2025
**Status for Stable Diffusion v1:** Not triggered — see [the assessment](../eu-ai-act-assessment.md#2-risk-classification)

> Summary for engineering and legal reference. Not a verbatim reproduction of the
> legal text — read the Official Journal before relying on any point below.

---

## What it prohibits

Article 5(1) bans placing on the market, putting into service, or using AI systems that:

| Ref | Practice |
|---|---|
| (a) | Deploy subliminal, purposefully manipulative or deceptive techniques that materially distort behaviour and cause (or are likely to cause) significant harm |
| (b) | Exploit vulnerabilities arising from age, disability, or a specific social or economic situation, with the same harm threshold |
| (c) | Social scoring — evaluating or classifying people over time from social behaviour or personal characteristics, leading to detrimental or disproportionate treatment |
| (d) | Predictive policing — assessing the risk that a natural person will commit a criminal offence based solely on profiling or personality traits |
| (e) | **Untargeted scraping of facial images** from the internet or CCTV footage to create or expand facial recognition databases |
| (f) | Emotion inference in the workplace or in education institutions (except for medical or safety reasons) |
| (g) | Biometric categorisation that deduces race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation |
| (h) | Real-time remote biometric identification in publicly accessible spaces for law enforcement, outside narrowly drawn exceptions |

Breach carries the Act's highest penalty band: up to €35,000,000 or 7% of worldwide annual turnover, whichever is higher (Article 99(3)).

## Why it matters here

Stable Diffusion v1 as assessed is a generative image model. It does not score people, infer emotion, categorise by protected attribute, or perform biometric identification, so no limb of Article 5(1) is engaged today.

**Limb (e) is the one to watch.** The model ships with an FFHQ face configuration (`configs/latent-diffusion/ffhq-ldm-vq-4.yaml`) and a CLIP image encoder (`ldm/modules/encoders/modules.py`). Building any face-matching or identity-lookup capability on top of those, fed by scraped facial imagery, moves the system from a transparency obligation to an outright prohibition. That is not a gap to remediate — it is a line not to cross.

Note that (e) prohibits the *untargeted scraping to build the database*. Training data provenance for LAION-derived weights is therefore a live question for any future face-recognition derivative, not only for the inference path.

## Referenced by

- Assessment §2 — reviewed and not triggered
- Assessment §5 — escalation signal: "Face matching added on top of FFHQ or CLIP image encoder"

## Related

- [article-6.md](article-6.md) — what happens if the system is not prohibited but is high-risk
- [annex-iii.md](annex-iii.md) — the biometrics category that sits just below the prohibition line
