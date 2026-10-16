# ESP surveillance knowledge base

Engineering knowledge extracted from **37 research papers**, organized for Excel review and AI-agent knowledge preparation.

## Start here

1. **[Download the Excel workbook](https://github.com/bishal110/json-to-excel-of-papers/raw/refs/heads/main/excel/ESP_Knowledge_Base.xlsx)** — filter the tables and add your review notes or Avalon tag mappings.
2. **[Browse the CSV tables](data/csv)** — flat, versionable records for databases and data pipelines.
3. **[Use the agent knowledge files](knowledge)** — one source-qualified text file per paper. Read the [Copilot Studio setup guide](docs/COPILOT_STUDIO.md).

| Table | Records | Contents |
|---|---:|---|
| Failures | 315 | Symptoms, causes, consequences, indicators and confidence |
| Rules | 177 | IF / AND / THEN, alternatives, checks, actions and restrictions |
| Indicators | 78 | Signals, trends and qualified warning windows |
| Actions | 68 | Immediate, short-term, long-term and preventive measures |
| Parameters | 631 | Source parameter mentions and editable local tag mapping |
| AI Models | 37 | Inputs, outputs, performance, limits and future opportunities |
| Q and A | 740 | Engineer and operator questions with source-specific answers |
| Papers | 37 | Bibliography, source references, study groups and caveats |

Counts include overlapping sources; they are not counts of unique validated failure modes. **26 rules are marked `do_not_deploy_as_written`.** Other rules also require local validation.

## Use and maintain

- Start with the workbook's **Start** tab. Every data tab has an Excel Table, filters and frozen headers/identifiers.
- Join tables using **Paper ID**. Keep **Entry ID** unchanged when sorting or reviewing.
- Amber fields are editable review notes and local tag mappings. **Reviewed** means content review; it does not approve a field action.
- After editing and saving the workbook, run `python scripts/export_workbook.py` to refresh CSV and knowledge files. Install the script's dependency with `python -m pip install -r scripts/requirements.txt` if needed.
- Commit the workbook and regenerated files together. Original extraction JSON in [data/source-json](data/source-json) remains an audit snapshot.

The [37 detailed reports](reports) retain all 12 requested sections and final outputs A–F. [Project recommendations](docs/PROJECT_SYNTHESIS.md) and [evidence limitations](docs/EVIDENCE_AND_LIMITATIONS.md) explain applicability to offshore wells and missing downhole sensors.

The repository contains derived knowledge and citations. Original PDFs, local filesystem paths, well telemetry and credentials are not included. Avalon tag availability is unverified until mapped against actual field data. No Copilot connection or live model has been deployed.
