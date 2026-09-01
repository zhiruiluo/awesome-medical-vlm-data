# Contributing

This repository is a data-intelligence catalog, not an unverified link list. Add an entry only when it includes medical images and language-related supervision or evaluation.

## Add A Dataset

Follow the complete [record workflow](WORKFLOW.md). In brief: create a JSON-compatible YAML record in `datasets/records/`, assign a `resource_type` and one or more controlled `domains`, validate it, then generate and commit the final report files.

```bash
python3 scripts/validate_records.py
python3 scripts/generate_tables.py
python3 scripts/generate_tables.py --check
python3 scripts/check_links.py --timeout 15
```

## Acceptance Criteria

- The resource pairs medical imagery with reports, captions, questions, grounding, or another language task.
- Scale uses an explicit unit, and the annotation process is summarized.
- Access and licensing fields are filled, even when the answer is uncertain.
- The record includes at least one official source URL.
- Generated files contain no hand-maintained dataset rows.
