# AI index

Read [STATUS.md](STATUS.md) and [ASSURANCE.md](ASSURANCE.md) first.

- Exact model, bounds, and excluded claims: [CLAIMS.json](CLAIMS.json).
- Full proof: [paper.tex](paper.tex), readable [paper.pdf](paper.pdf).
- First-coefficient restrictions: manuscript equation `eq:exact-positive-bound`; original attachment nonzero and terminal vertex outside the deleted-bond cluster must remain distinct.
- Broader kernel criterion and applications: manuscript extension section; sufficient Fourier conditions, not arbitrary small maximum weight alone.
- Literature scope: [SOURCES.md](SOURCES.md), [CITATION_AUDIT.md](CITATION_AUDIT.md).
- Review dispositions: [REVIEW_RESPONSE.md](REVIEW_RESPONSE.md).
- Historical assessment: [historical/outcome.json](historical/outcome.json), [historical/ref-assessment.md](historical/ref-assessment.md); not a revised rating.
- Diagnostic entry point: [code/verify_math.py](code/verify_math.py); execution and scope: [REPLAY_RECEIPT.md](REPLAY_RECEIPT.md).
- Environment: [ENVIRONMENT.txt](ENVIRONMENT.txt), [requirements.txt](requirements.txt).
- Provenance and rights: [PROVENANCE.md](PROVENANCE.md), [LICENSES.md](LICENSES.md), [COMPONENT_MAP.json](COMPONENT_MAP.json).
- Citation: [CITATION.cff](CITATION.cff). Final frozen byte inventory: [MANIFEST.json](MANIFEST.json).

Do not conflate pointwise cube sum with three-step return probability. Do not infer that the Fourier transform of D is nonnegative. Do not drop deleted-bond or terminal restrictions to obtain the claimed cubic error. Imported infrared input itself uses the lace expansion; only the additional coefficient extraction avoids a fresh full higher-order-tail calculation. Passing finite tests is not formal verification, external peer review, or a REF rating.
