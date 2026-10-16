# Using this knowledge with Copilot Studio

## Recommended starting route

Use **Excel for content review**, GitHub for versions and sharing, and the **37 files in knowledge/** as source-qualified retrieval documents. Each text file groups one paper's failure modes, rules, indicators, actions, model details and Q&A, retaining source IDs and caveats. This route avoids asking a conversational model to infer relationships across many workbook sheets.

Copilot Studio supports uploading Excel, CSV and text documents as knowledge sources. The documented setup is **Add knowledge → upload files → add a descriptive name/description → Add to agent**. Local-file knowledge requires Dataverse search in the documented standard-harness workflow. Check the applicable configuration in your tenant. [Microsoft documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-file-upload)

1. Review priority records in Excel. Rejected records remain in CSV for audit but are omitted from regenerated knowledge text. Pending entries remain clearly marked research references.
2. Save Excel and run `python scripts/export_workbook.py`. This reads the workbook and refreshes CSV and knowledge text; it does not change Excel.
3. Upload the resulting knowledge text files to a development agent. Add a description such as “ESP engineering research reference with source-specific diagnostic hypotheses, input requirements and limitations.”
4. Use the proposed instructions and evaluation questions below. Check retrieved source content, not only the apparent fluency of the response.
5. Keep field telemetry integration and live diagnostic calculations as a separate implementation task. Static research knowledge cannot report a current well condition.

GitHub is the source repository in this design. Publishing files there does not automatically configure, synchronize or authorize a Copilot Studio knowledge source.

## When structured tables are needed

For record lookup, explicit relationships, controlled fields or more frequent updates, import the CSVs into a reviewed Dataverse schema. Use Entry ID as a stable alternate key and Paper ID as a relationship to the Papers table. The Data Dictionary sheet describes each column. Inspect field lengths, choices and multiline text search behavior in your tenant before importing; these CSVs are staging data, not a preconfigured Dataverse solution.

Microsoft documents Dataverse tables as knowledge sources, including table/column synonyms and glossary terms. The documented route requires Dataverse search, appropriate permissions and Microsoft authentication for the agent. [Microsoft documentation](https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-add-dataverse)

Uploading a workbook as a document is different from building a structured record-query tool. If an answer must return every matching rule, apply deterministic table filters or a tested query tool; do not assume semantic retrieval exhaustively scans every row. This is an implementation recommendation, not a claim that this repository has configured that tool.

## Proposed agent instructions

You are an ESP research and surveillance support assistant. State whether an answer describes published research, an engineering proposal or current field evidence. Cite Paper ID, Entry ID and the supplied PDF page reference when available. Retrieve the paper's caveats with the record. Treat source_status=do_not_deploy_as_written as a prohibition on presenting the rule as an approved operating rule. Reviewed means content review only. Do not infer missing Avalon tags, downhole readings, phase rates, equipment limits or current well status. Retain plausible alternative causes and identify the missing discriminating checks. Distinguish observation windows, forecast horizons, matching tolerances and observed warning lead. Request the relevant approved site procedure for operational actions. If evidence is insufficient, state what cannot be concluded.

## Initial evaluation questions

| Question | Expected behavior |
|---|---|
| Current fell and PIP rose. Has the shaft broken? | Retain plugging, wear and other plausible causes; request delivery/head/operating context. |
| Can I use P30 when both downhole pressures are lost? | Explain the source's crucial-input limitation rather than fill missing values. |
| Does a seven-day pre-workover label guarantee seven days of warning? | Distinguish label window from demonstrated useful lead. |
| Can I use P35's temperature rule on every ESP? | Retrieve its source contradictions and restricted status. |
| Is vibration telemetry sufficient for P23? | Ask whether suitable waveform bandwidth and sensor configuration exist. |
| What does Avalon measure for this parameter? | Answer Unknown unless the local mapping is completed. |
| Are five publications of the same pilot five validations? | Retrieve the related study group and avoid double counting. |
| Does this diagnose my water-injection well? | Explain the producer/SAGD/polymer-flood scope limit. |

Documentation checked on 2026-10-17. Product capabilities and tenant configuration can change; the repository does not include Microsoft credentials or a deployed agent.
