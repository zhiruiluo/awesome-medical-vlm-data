# Record Workflow

Use this workflow for every new dataset or benchmark entry. Dataset records are the only hand-maintained source of catalog metadata; the README tables and reports are generated outputs.

## 1. Create The Record

1. Copy an existing record in `datasets/records/` and rename it with the dataset's lowercase kebab-case ID, for example `datasets/records/example-vqa.yaml`.
2. Fill the required fields documented in [DATASET_SCHEMA.md](DATASET_SCHEMA.md). Classify the released payload as `text-only`, `image-only`, or `text-image-pairs`; choose one or more controlled taxonomy values and keep unknown information explicit as `unknown` or `null`; do not guess licensing or access rights.
3. Set `catalog_status` to `included` when the resource has a verified official source and enough metadata to classify it. Image-only records use `language_supervision: ["none"]`; keep resources that do not meet the catalog's scope or verification standard as `excluded` records for provenance.
4. Use primary sources for `homepage`, `paper`, `repository`, and `download`. At least one official URL is required.

## 2. Validate The Record

Run the validator before generating any documentation:

```bash
python3 scripts/validate_records.py
```

Resolve every reported error. Validation checks required fields, IDs, URLs, access metadata, ISO dates, and duplicate dataset IDs.

Optionally verify live source URLs:

```bash
python3 scripts/check_links.py --timeout 15
```

Protected downloads and servers that reject `HEAD` requests are warnings. Use `--strict` when those should fail the command.

## 3. Emit The Final Report

Generate the catalog views from all records:

```bash
python3 scripts/generate_tables.py
```

To emit only the README after editing `datasets/records/`, run:

```bash
python3 scripts/generate_tables.py --readme-only
```

This writes the final report to three locations:

- `README.md`: catalog-status summary, specialty tables, and capability coverage.
- `reports/landscape.md`: domain and capability counts.
- `reports/gaps.md`: current coverage and license/access follow-up areas.

Confirm that no generated output is stale:

```bash
python3 scripts/generate_tables.py --check
git diff -- README.md reports/
```

## 4. Finish The Contribution

Commit the new record and regenerated report files together. GitHub Actions reruns record validation and the generated-output freshness check for every push and pull request.
