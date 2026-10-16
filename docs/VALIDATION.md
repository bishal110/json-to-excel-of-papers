# Package validation

Checked 2026-10-17.

- Failures: 315 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- Rules: 177 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- Indicators: 78 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- Actions: 68 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- Parameters: 631 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- AI Models: 37 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- Q and A: 740 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- Papers: 37 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- Study Groups: 3 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- Data Dictionary: 119 records; values, table/filter, frozen headers/IDs and CSV round-trip match.
- Summary counts recalculate correctly; changing one source status raised the restricted-rule count from 26 to 27, then restoration returned it to 26.
- Saved workbook has no cached Excel formula errors. All 11 worksheets were rendered and visually reviewed.
- Knowledge export contains 1,415 source-qualified records across 37 text files.
- Publication files contain no original PDFs or absolute local filesystem references. Relative Markdown links resolve.

Validation concerns file structure, content preservation and export behavior. It does not validate the original research, field thresholds, model performance or a live Copilot integration. Native Excel was not used to execute the workbook; formulas were recalculated in the authoring engine and the saved XLSX was independently inspected.
