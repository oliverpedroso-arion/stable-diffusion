# GDPR Article 9 — Processing of Special Categories of Personal Data

**Instrument:** Regulation (EU) 2016/679 (GDPR)
**Source:** https://eur-lex.europa.eu/eli/reg/2016/679/oj
**Applicable since:** 25 May 2018
**Status for Stable Diffusion v1:** **Not confirmed.** The assessment records special-category processing as unconfirmed rather than ruled out — see [the assessment](../eu-ai-act-assessment.md#2-risk-classification).

> Summary for engineering and legal reference. Not a verbatim reproduction of the
> legal text — read the Official Journal before relying on any point below.

---

## What it prohibits

Article 9(1) prohibits processing of personal data revealing:

- racial or ethnic origin
- political opinions
- religious or philosophical beliefs
- trade union membership

and processing of:

- genetic data
- **biometric data for the purpose of uniquely identifying a natural person**
- data concerning health
- data concerning a natural person's sex life or sexual orientation

## When the prohibition lifts

Article 9(2) lists the exhaustive exceptions. The ones plausibly reachable in a commercial generative-media context:

| Ref | Exception |
|---|---|
| (a) | **Explicit consent** of the data subject for one or more specified purposes (subject to Union or Member State law not overriding it) |
| (e) | Data **manifestly made public** by the data subject |
| (f) | Establishment, exercise or defence of legal claims |
| (g) | Substantial public interest, on the basis of Union or Member State law, proportionate and with safeguards |
| (j) | Archiving in the public interest, scientific or historical research, or statistical purposes under Article 89(1) |

The remaining exceptions — (b) employment and social security law, (c) vital interests, (d) legitimate activities of a foundation or association, (h) preventive or occupational medicine, (i) public health — are unlikely to apply here.

Note that "manifestly made public" under (e) is a narrow gate. A photograph being publicly accessible online is not the same as the data subject having manifestly made it public, and it is not a general licence for scraped imagery.

## Why it matters here

The trigger is the word **"for the purpose of uniquely identifying."** A photograph of a person is personal data, but it is not automatically Article 9 biometric data. Recital 51 draws the line: photographs become special-category data only when processed through specific technical means allowing the unique identification or authentication of a natural person.

That gives two distinct exposures:

**Inference input.** `scripts/img2img.py` and `scripts/inpaint.py` accept uploaded photographs of real people. Generating from a photo is not, on its own, unique identification — so this is Article 6 lawful-basis territory rather than Article 9, provided no identity matching happens. The assessment's GAP-02 consent gate is what keeps it that way, and it does double duty: it serves both the [Article 50(4)](article-50.md) deepfake disclosure obligation and the GDPR lawful-basis question.

**Escalation.** Adding face matching on top of the FFHQ configuration or CLIP image encoder converts the pipeline into biometric identification. At that point Article 9 applies in full, explicit consent becomes the realistic basis, and the same change simultaneously engages [AI Act Article 5(1)(e)](article-5.md) if any part of the reference database was built by untargeted scraping, and [Annex III §1](annex-iii.md) for the system as a whole. One engineering decision, three regimes.

**Generated output.** Synthetic imagery depicting an identifiable real person is personal data about that person. Output that portrays someone as having a particular religion, sexual orientation, health condition or political affiliation is special-category data about them — generated rather than collected, but no less regulated, and with no consent behind it. This is an angle the assessment does not cover and is worth raising with counsel alongside GAP-08.

## Interaction with the AI Act

The AI Act does not displace the GDPR — Article 2(7) is explicit that Union data protection law continues to apply. Satisfying [Article 50](article-50.md) disclosure duties says nothing about whether the underlying processing is lawful. The two analyses run in parallel and must both close.

## Referenced by

- Assessment §2 — special-category data recorded as "Not confirmed"
- Relevant to GAP-02 (consent gate) and the biometric escalation signal in §5

## Related

- [article-35-gdpr.md](article-35-gdpr.md) — the DPIA that Article 9 processing at scale would make mandatory
- [article-5.md](article-5.md) — where biometric identification becomes prohibited outright
