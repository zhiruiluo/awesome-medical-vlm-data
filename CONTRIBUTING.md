# Contributing

This repository is a data-intelligence catalog, not an unverified link list. Add an entry only when it includes medical images and language-related supervision or evaluation.

## Add A Dataset Or Benchmark

Follow the complete [record workflow](WORKFLOW.md). Add released data to `datasets/records/` using [DATASET_SCHEMA.md](DATASET_SCHEMA.md). Add evaluation suites to `benchmarks/records/` using [BENCHMARK_SCHEMA.md](BENCHMARK_SCHEMA.md). A resource may have one linked record in each catalog.

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
- Benchmark source IDs resolve to dataset records; uncataloged constituents are retained as `external_sources`.
