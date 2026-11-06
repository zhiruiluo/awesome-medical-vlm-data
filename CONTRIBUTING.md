# Contributing

This repository is a data-intelligence catalog, not an unverified link list. New entries may be image-only resources annotated or evaluated for a medical visual task, image-and-language resources with language-related supervision or evaluation, or text-only medical-language resources. Physiological signals and structured annotations can accompany image-only resources, but do not count as language-related supervision.

## Add A Dataset Or Benchmark

Follow the complete [record workflow](WORKFLOW.md). Add released data to `datasets/records/` using [DATASET_SCHEMA.md](DATASET_SCHEMA.md). Add evaluation suites to `benchmarks/records/` using [BENCHMARK_SCHEMA.md](BENCHMARK_SCHEMA.md). A resource may have one linked record in each catalog.

```bash
python3 scripts/validate_records.py
python3 scripts/generate_tables.py
python3 scripts/generate_tables.py --check
python3 scripts/check_links.py --timeout 15
```

## Acceptance Criteria

- The resource provides medical images with language-related supervision or evaluation, image-only annotations/evaluation for a medical visual task, or text-only data for a medical-language task.
- `language_supervision: ["none"]` records the absence of language supervision for an image-only dataset; it does not disqualify an otherwise in-scope image-only resource.
- Scale uses an explicit unit, and the annotation process is summarized.
- Access and licensing fields are filled, even when the answer is uncertain.
- The record includes at least one official source URL.
- Generated files contain no hand-maintained dataset rows.
- Benchmark source IDs resolve to dataset records; uncataloged constituents are retained as `external_sources`.
