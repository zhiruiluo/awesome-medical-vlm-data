# Contributing

This repository is a data-intelligence catalog, not an unverified link list. Add an entry only when it includes medical images and language-related supervision or evaluation.

## Add A Dataset

1. Copy a record in the relevant `datasets/<domain>/` directory and give it a lowercase, hyphenated filename.
2. Fill every required field. Records are JSON-compatible YAML so the tooling needs no third-party packages.
3. Prefer a paper, official project page, or the original release repository for each link.
4. Record uncertainty as `unknown` or `unclear`; do not infer a license, commercial-use permission, or patient-level split.
5. Run the checks below and commit the regenerated documentation.

```bash
python3 scripts/validate_records.py
python3 scripts/generate_tables.py --check
python3 scripts/check_links.py --timeout 15
```

## Acceptance Criteria

- The resource pairs medical imagery with reports, captions, questions, grounding, or another language task.
- Scale uses an explicit unit, and the annotation process is summarized.
- Access and licensing fields are filled, even when the answer is uncertain.
- The record includes at least one official source URL.
- Generated files contain no hand-maintained dataset rows.
