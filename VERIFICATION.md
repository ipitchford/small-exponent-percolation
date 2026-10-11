# Verification boundaries

The complete argument is a written analytic proof with cited imported results. Current AI-assisted scrutiny is not formal proof verification or independent human peer review. See ASSURANCE.md and REVIEW_RESPONSE.md.

The current finite exact diagnostics pass normally and under Python optimization; see REPLAY_RECEIPT.md. The publisher separately inspected all 13 pages of the revised PDF and reported no overflow. Neither fact validates every analytic step.

After freezing, run `python3 code/check_manifest.py` to verify the listed hashes and sizes. The manifest checker verifies byte integrity, not correctness or exhaustive directory coverage. The manifest excludes itself. A passing local check does not establish remote-provider bytes, DOI resolution, deployment or external CI success; those require separate evidence.
