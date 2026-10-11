# First correction to the critical mean degree in extreme long-range percolation

Anonymous · 1.1.0-candidate · 11 October 2026

DOI: [10.5281/zenodo.23294525](https://doi.org/10.5281/zenodo.23294525)

An unrefereed analytic candidate for undirected independent bond percolation on the integers with **linear** probabilities C|x-y|^(-1-sigma). For all sufficiently small positive real sigma, the critical expected degree satisfies

`p_c = 1 + zeta(2+2 sigma)/(2 zeta(1+sigma)^2) + O(sigma^3)`.

Thus `(p_c-1)/sigma^2 -> pi^2/12`. The revised candidate also extracts a kernel criterion and applies it to nonnegative summable additions and bounded mixtures of small tail exponents; see the exact manuscript statements. It does not establish an oriented result, an exponential bond-law correction, a third-order coefficient, or a practical error bound at a prescribed finite sigma.

Start with [AI_INDEX.md](AI_INDEX.md), [paper.pdf](paper.pdf), [ASSURANCE.md](ASSURANCE.md) and [CLAIMS.json](CLAIMS.json).

## Finite diagnostics

```sh
python code/verify_math.py
python -O code/verify_math.py
```

Python standard library only. The checks corroborate algebraic identities and reject plausible corrupted constants; they do not prove the analytic theorem or replay an infinite lace expansion. Build the editable manuscript with two runs of `pdflatex -interaction=nonstopmode -halt-on-error paper.tex`. Final archive integrity and PDF inspection are separately recorded by the publisher.

The original research outcome and quality assessment remain unchanged in [historical/](historical/). Historical status fields are not current publication-status claims. Current assurance is in [STATUS.md](STATUS.md).
