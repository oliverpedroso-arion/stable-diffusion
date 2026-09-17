# GDPR Article 35 — Data Protection Impact Assessment

**Instrument:** Regulation (EU) 2016/679 (GDPR)
**Source:** https://eur-lex.europa.eu/eli/reg/2016/679/oj
**Applicable since:** 25 May 2018
**Status for Stable Diffusion v1:** **Contingent.** Named in assessment §5 as the trigger for logging prompts or uploaded images against identities.

> Summary for engineering and legal reference. Not a verbatim reproduction of the
> legal text — read the Official Journal before relying on any point below.

---

## When a DPIA is required

Article 35(1): where a type of processing, in particular using new technologies, is likely to result in a **high risk to the rights and freedoms of natural persons**, the controller must carry out an assessment of the impact of the envisaged processing operations — **before** the processing begins.

Article 35(3) makes it mandatory in particular for:

| Ref | Case |
|---|---|
| (a) | Systematic and extensive evaluation of personal aspects based on automated processing, including profiling, on which decisions are based that produce legal effects or similarly significantly affect the person |
| (b) | Processing on a **large scale** of special categories of data under [Article 9](article-9-gdpr.md), or of criminal conviction data under Article 10 |
| (c) | Systematic monitoring of a publicly accessible area on a large scale |

Supervisory authorities also publish their own lists of processing requiring a DPIA (Article 35(4)) and, optionally, lists where it is not required (35(5)). Check the list for each Member State where processing occurs — they are not uniform.

## What a DPIA must contain

Article 35(7):

1. A systematic description of the envisaged processing operations and their purposes, including any legitimate interest pursued by the controller;
2. An assessment of the **necessity and proportionality** of the processing in relation to those purposes;
3. An assessment of the **risks to the rights and freedoms** of data subjects;
4. The **measures envisaged to address those risks**, including safeguards, security measures and mechanisms to ensure the protection of personal data and demonstrate compliance.

The controller must seek the advice of the data protection officer where one is designated (Article 35(2)), and must where appropriate seek the views of data subjects (Article 35(9)).

## Prior consultation

Under Article 36, if the DPIA indicates the processing would result in a high risk **and** the controller cannot mitigate it, the supervisory authority must be consulted **before** processing starts. The authority has up to eight weeks, extendable by six, to respond. That timeline belongs in any launch plan that depends on it.

## Why it matters here

The assessment flags this as an escalation signal: *"User prompts or uploaded images logged against identities."*

That flag sits in direct tension with **GAP-06**, which proposes adding generation event logging so that non-consensual deepfake complaints can be investigated and compliance demonstrated to a regulator. Both are correct, and the resolution is in the design rather than in choosing one over the other.

The assessment's remediation is careful on exactly this point — it specifies a **hash-based, non-personal** log: prompt, input image hash, output image hash, timestamp. That framing is what keeps GAP-06 out of Article 35(3)(a). Two design constraints carry the weight:

- **Do not join the log to user identity.** As soon as the log keys on an account or user ID, it becomes systematic evaluation of personal aspects, and the DPIA obligation is live.
- **Treat prompt text as personal data.** Free-text prompts routinely name real people. A prompt log is not anonymous simply because it holds no user ID, and hashing the image does not sanitise the text beside it.

A DPIA is a process obligation, not a liability finding. If the product needs identity-linked logging — for abuse enforcement, chargebacks, or a takedown workflow serving GAP-08 — the answer is to run the DPIA and document the mitigations, not to abandon the capability. What is not available is doing it without the assessment, since Article 35 requires it beforehand.

## Referenced by

- Assessment §5 — escalation signal: "User prompts or uploaded images logged against identities"
- Directly constrains the design of GAP-06 (generation event logging)
- Relevant to GAP-08 (complaint and takedown process), which typically needs identity-linked records to function

## Related

- [article-9-gdpr.md](article-9-gdpr.md) — special-category processing, the 35(3)(b) trigger
- [article-50.md](article-50.md) — the AI Act obligation GAP-06 is intended to evidence
