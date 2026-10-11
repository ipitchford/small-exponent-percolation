# Finite diagnostic execution

Executed on 11 October 2026 in the publication working package:

- `python3 code/verify_math.py`: 26 checks passed; 10 semantic negative controls rejected.
- `python3 -O code/verify_math.py`: identical result.

The diagnostic uses exact rational arithmetic and explicit exceptions, not removable assertions. It checks finite normalization, the nonbacktracking algebraic identity, deleted-bond subtraction, a quadratic inequality, and application coefficient arithmetic. It rejects missing normalization, conflated pointwise/convolution moments, omitted remainders and conflated mixture moments.

These are finite algebraic checks, not a replay of the analytic theorem, imported lace machinery, historical unavailable tests or an infinite-parameter limit. Final frozen-manifest checks and clean CI execution are separate later operations; this receipt does not claim they have run.
