# ESP Surveillance Copilot — Engineering Knowledge and Implementation Priorities

This cross-paper synthesis accompanies **37 individual reports**, each containing the requested Sections 1–12 and final outputs A–F. It addresses the specified offshore ESP environment, lost downhole sensors, Avalon telemetry, Excel production tests and surface pressures, and water-injection wells. Source IDs below link to those reports, which contain PDF page references.

## A. Executive Summary

**Overall practical value: 8/10, as an analyst judgment for this project.** The collection is strongest as a basis for explainable surveillance, troubleshooting and reliability learning. It does not establish a transferable, fully sensorless ESP failure predictor or a universal remaining-life model.

Start with the explicit trend patterns and action alternatives in [P19](../reports/P19.md), the evidence-preservation and root-cause workflow in [P29](../reports/P29.md), the failure taxonomy in [P14](../reports/P14.md), and the uncertainty/missing-input treatment in [P30](../reports/P30.md). Use [P09](../reports/P09.md), [P10](../reports/P10.md), [P31](../reports/P31.md) and [P33](../reports/P33.md) to scope a separate surface-data pathway. Their data requirements and validation limitations still apply.

The extraction contains **315 source-specific failure/condition entries, 177 diagnostic-rule entries and 740 engineer/operator Q&A entries**. These are audit records, not counts of unique physical faults or approved rules. Some entries are symptoms, stress states, component labels or background hypotheses. Repeated publications and overlapping mechanisms must not be treated as independent confirmation.

Three distinctions must remain visible in every Copilot answer:

1. **Observation versus cause:** falling current or unstable pressure can support several diagnoses. Plugged pump, worn pump and broken shaft share patterns in the fuzzy-rule literature. A model score does not resolve that ambiguity by itself. [P03](../reports/P03.md), [P19](../reports/P19.md)
2. **Detection versus prediction:** a lookback window, a pre-workover label, or earlier recognition than an engineer's report is not necessarily warning before physical failure. Abrupt shaft failures may have no detectable precursor in the recorded data. [P24](../reports/P24.md), [P27](../reports/P27.md), [P30](../reports/P30.md), [P32](../reports/P32.md)
3. **Missing versus normal:** lost, frozen, stale and inferred measurements need separate states. For example, P30's method cannot retain its claimed diagnostic relevance when both PIP and PDP are missing. [P28](../reports/P28.md), [P30](../reports/P30.md)

The best first release is an advisory assistant that shows the evidence window, plausible causes, missing checks, source provenance and applicable approved field procedure. Statistical calculations and model scores should be produced by a governed analytics service and presented with their timestamp and validation status. This is a proposed architecture; no Copilot or Avalon connection has been configured by this extraction.

## B. Failure Modes Library Entries

The detailed library is [failure_modes_library.json](../data/source-json/failure_modes_library.json). The families below are a cross-paper engineering organization, not a newly validated classifier.

| Failure or condition family | Typical evidence to retain | Important ambiguity / distinguishing check | Primary source reports |
|---|---|---|---|
| Gas interference, gas ingestion and gas lock | Current/pressure instability, loss of delivery, thermal response, free-gas/submergence context | Separate gas lock from intermittent gas interference; investigate fluid conditions and inflow. No universal gas-fraction limit is established. | [P19](../reports/P19.md), [P25](../reports/P25.md), [P30](../reports/P30.md) |
| Inadequate inflow, pump-off and low flow | Rate relative to duty, PIP, frequency, thermal response | Low flow is an operating state with several causes; pressure directions depend on mechanism and location. | [P22](../reports/P22.md), [P30](../reports/P30.md) |
| Pump plugging and deposits | Reduced hydraulic performance, changed load/temperature, fluid/deposit evidence | Shares several trends with wear and shaft failure. Identify solids, scale, paraffin, bacteria or polymer exposure before selecting a response. | [P19](../reports/P19.md), [P24](../reports/P24.md), [P29](../reports/P29.md) |
| Tubing or surface restriction / deadhead | PIP/PDP, wellhead or tubing pressure, flow and valve history | Pressure measurement location is essential. Check intended and actual valve status. | [P19](../reports/P19.md), [P30](../reports/P30.md) |
| Pump wear, erosion and loss of efficiency | Normalized head/flow, current, vibration, solids exposure and run history | Separate speed, fluid and system-pressure changes from degradation. | [P22](../reports/P22.md), [P29](../reports/P29.md), [P31](../reports/P31.md) |
| Broken shaft or coupling / mechanical separation | Abrupt delivery and current change, changed developed head, post-pull findings | A failure may already have occurred when the pattern appears. Protector-shaft and pump-shaft failures need distinct component fields. | [P14](../reports/P14.md), [P27](../reports/P27.md), [P30](../reports/P30.md) |
| Thrust, bearing, imbalance, misalignment and rubbing | Operating range, vibration features and inspection findings | Laboratory waveform classification is not validated by ordinary averaged vibration telemetry. | [P22](../reports/P22.md), [P23](../reports/P23.md), [P29](../reports/P29.md) |
| Motor overheating, overload or electrical failure | Thermal history, actual motor loading, voltage/current location, cooling context, electrical test/DIFA | Temperature rise can follow flow restriction or deposits; do not assign the motor as the initiating root cause automatically. | [P14](../reports/P14.md), [P19](../reports/P19.md), [P24](../reports/P24.md) |
| Cable insulation failure, mechanical damage or ground fault | Electrical history, leakage/insulation information when available, installation evidence and qualified tests | A lost gauge alone does not prove a cable ground fault. | [P28](../reports/P28.md), [P29](../reports/P29.md) |
| Seal/protector failure and fluid ingress | Component inspection, contamination and material compatibility | The first damaged component found may be a consequence rather than the initiating failure. | [P14](../reports/P14.md), [P29](../reports/P29.md) |
| Tubing leak, recirculation or Y-tool leak | Production/electrical mismatch, pressure response and integrity evidence | Requires integrity investigation; the P31 pressure test is a deliberately acquired test, not an ordinary Excel pressure sample. | [P19](../reports/P19.md), [P31](../reports/P31.md) |
| Reverse rotation | Rotation/phase verification and poor hydraulic delivery | Trend patterns alone do not prove phase sequence or authorize an electrical change. | [P19](../reports/P19.md), [P31](../reports/P31.md) |
| Power quality, VSD/control or repeated cycling | Voltage, phase currents, frequency, trips and operating history | Distinguish a commanded change or power interruption from pump deterioration. | [P09](../reports/P09.md), [P10](../reports/P10.md), [P31](../reports/P31.md) |
| Gauge/sensor/data failure | Flatline, dropout, stale timestamp, discontinuity or inconsistency between related channels | Treat data availability as a diagnostic gate and a separate reliability issue. | [P28](../reports/P28.md), [P30](../reports/P30.md) |
| Fluid changes, emulsions, viscosity, corrosion and chemical incompatibility | Tests, fluid composition, chemical history, load and inspection evidence | Telemetry alone usually cannot identify the fluid or deposit chemistry. | [P19](../reports/P19.md), [P22](../reports/P22.md), [P29](../reports/P29.md) |

The user's category list has no separate tubing, seal or protector category. Some source-specific records therefore use the nearest allowed category, with the actual component retained in the name. Before database deployment, add separate **component**, **location**, **failure mechanism**, **initiating root cause**, **consequence** and **confirmation method** fields. Keep water-injection well records separate; polymer-flood producer evidence and SAGD steam-injection variables do not establish water-injector troubleshooting rules. [P14](../reports/P14.md), [P24](../reports/P24.md), [P34](../reports/P34.md)

## C. Engineering Rules Library Entries

The full source-rule library is [engineering_rules_library.json](../data/source-json/engineering_rules_library.json). The following are prioritized **analyst-derived operational templates**, with source support. They need local definitions of windows, noise tolerance, ratings and escalation routes before execution.

| Rule name | IF / AND | THEN: candidate conclusion | Alternatives, checks and recommended response | Confidence / source |
|---|---|---|---|---|
| Data-quality gate | A required signal is stale, frozen, missing or inconsistent; AND the rule depends on it | Evidence is incomplete; suppress a definitive physical diagnosis | Check historian timestamps, acquisition mode and other channels; report which premises cannot be evaluated | High for the need to gate; thresholds require local definition. [P28](../reports/P28.md), [P30](../reports/P30.md) |
| Operating-state gate | A trend starts near a frequency, choke, restart or operational change; AND a steady-duty baseline is used | The change may be an operating response | Compare equivalent duty and update the reference only after reviewing the event | Medium. [P19](../reports/P19.md), [P30](../reports/P30.md) |
| Restriction candidate | Delivery falls, heating increases and the appropriate pressure combination changes; AND frequency/location/quality are known | Surface or tubing restriction may be present | Compare PIP, PDP and wellhead pressure; verify actual valve state and intervention history | Medium; patterns are non-unique. [P19](../reports/P19.md), [P30](../reports/P30.md) |
| Gas-interference candidate | PIP/current are unstable with reduced delivery; AND operating/fluid context supports gas entry | Gas interference or pump-off is plausible | Check inflow, gas and submergence evidence; retain plugging and measurement error as alternatives; request engineering assessment | Medium. [P19](../reports/P19.md), [P30](../reports/P30.md) |
| Mechanical/hydraulic loss of delivery | Current and delivery decrease and PIP/head behavior changes; AND evidence is valid | Wear, plugging or shaft failure are candidates | Use abruptness, head/efficiency, vibration, integrity checks and later DIFA to discriminate; do not label one cause from the shared pattern | Medium for the candidate set, low for a unique cause. [P03](../reports/P03.md), [P19](../reports/P19.md), [P27](../reports/P27.md) |
| Production/electrical mismatch | Tested production deteriorates while electrical behavior remains comparatively unchanged; AND test timing/duty are comparable | Integrity or hydraulic efficiency needs investigation | A tubing leak is one candidate; compare fluid changes, tests and pump performance before planning a qualified integrity test | Medium. [P31](../reports/P31.md) |
| Thermal/deposit feedback | Temperature rises and control response/load changes persist; AND polymer or deposit exposure is supported | Cooling impairment or deposition is plausible | Review fluid/chemical history, flow and operating range; obtain condition-specific engineering advice | Medium for mechanism, low for cause from telemetry alone. [P24](../reports/P24.md), [P29](../reports/P29.md) |
| Electrical/gauge coincidence | Downhole measurements disappear or freeze with electrical anomalies; AND the timing is corroborated | Electrical failure and instrumentation failure both require assessment | Preserve drive/gauge history; qualified electrical checks distinguish ground fault, sensor fault and acquisition loss | Medium. [P28](../reports/P28.md), [P29](../reports/P29.md) |
| Relative vibration deterioration | Vibration increases at comparable speed and sensor configuration; AND baseline quality is adequate | Mechanical or hydraulic stress may be increasing | Check speed, gas, bearing/stage condition and sensor changes; do not use laboratory accuracy as field confidence | Medium. [P19](../reports/P19.md), [P23](../reports/P23.md), [P32](../reports/P32.md) |
| Missing-downhole model eligibility | Both PIP and PDP are missing; AND P30's full Bayesian method is proposed | This source method is not supported for that well | Use a separately validated surface-only pathway or an incomplete-evidence advisory | High for the source limitation. [P30](../reports/P30.md) |
| Root-cause evidence preservation | An ESP trips or fails; AND investigation/restart is being considered | Preserve evidence before it is overwritten | Capture trip history, trends, recent actions, tests and run identifiers; follow site procedure and later connect DIFA to the initiating causal chain | High as a reliability practice. [P29](../reports/P29.md) |
| Ambiguous or contradictory source rule | Units, definitions, thresholds or source results conflict | Retain as reference; block deployment as written | Resolve against original data, equipment ratings and independent validation | High as an evidence-quality rule. See [Evidence and limitations](EVIDENCE_AND_LIMITATIONS.md) |

Numeric values are retained in each paper report for audit. They are not merged into universal limits. Particularly important exclusions are percentage temperature changes without a defined scale, zero discharge pressure as a general failure test, hard fault exclusions from one surface trend, and retrospective lifetime tree leaves used as live predictions. [P19](../reports/P19.md), [P26](../reports/P26.md), [P33](../reports/P33.md), [P34](../reports/P34.md)

## D. Predictive Maintenance Opportunities

| Opportunity | What the evidence supports | Lead-time interpretation | Feasibility for this project |
|---|---|---|---|
| Multivariate anomaly detection | PCA/residual monitoring can identify departure from reference behavior | P05 illustrates about 30 hours; other papers show different event definitions. No universal lead follows. | Good first pilot on well-conditioned runs; use separate feature sets for full-sensor and surface-only wells. [P05](../reports/P05.md), [P18](../reports/P18.md), [P27](../reports/P27.md) |
| Electrical-only risk scoring | Current, voltage, frequency and runtime can support a predictive classifier | P10's 90-day event-matching interval is not demonstrated 90-day warning; reported precision/recall are about 62% | Relevant to lost-sensor wells if those electrical tags and independent failure histories exist. [P10](../reports/P10.md) |
| Short-horizon boosted-tree risk | P17 demonstrates stronger discrimination at shorter horizons in its study | AUC falls from 0.944 at one day to 0.625 at 14 days; sampling and interpolation limit transfer | Pilot one-, three- and seven-day targets only after causal preprocessing and grouped validation. [P17](../reports/P17.md) |
| Well/component risk | Engineered features and component labels can support separate models | P16 reports long average leads in selected detections, including near-zero cases; its target windows and observed leads differ | Valuable where component-level DIFA and sufficiently complete histories exist. [P16](../reports/P16.md) |
| Pre-workover classification | P24 distinguishes samples within a seven-day label window, with pre-event precision 0.80 and recall 0.60 | A seven-day class definition does not guarantee seven-day notice | Useful benchmark after reviewing electrical-event labels and polymer-context transfer. [P24](../reports/P24.md) |
| Vibration residual warnings | P32 contrasts a lower false-alert PCA option with earlier but noisier residual alerts | Reported average leads of roughly 5 versus 40 days depend on selected cases; some apparent warning is delayed failure confirmation | Requires actual vibration and the predictor signals. Treat the small cohort as a design example. [P32](../reports/P32.md) |
| Surface symptom ranking | P33 supports a knowledge-assisted diagnosis design using surface signals and calculated rates | 60 time steps is an input window; Recall@3 is not top-one accuracy or an established future horizon | Promising, but sparse Excel tests cannot replace its continuous production estimates. [P33](../reports/P33.md) |
| Remaining useful life | Several sources explore life regression or operational exposure | Whole-run features, post-pull findings and censored survivors make prospective RUL much harder | Defer until run histories, outcomes and censoring are reliable. [P11](../reports/P11.md), [P12](../reports/P12.md), [P34](../reports/P34.md) |

The 12-day example repeated across [P04](../reports/P04.md), [P06](../reports/P06.md), [P08](../reports/P08.md), [P36](../reports/P36.md) and [P37](../reports/P37.md) belongs to a related pilot-publication family. It should contribute one case of evidence, not five independent validations.

For each pilot, use an entire ESP run/well as the grouping unit, reserve later runs for testing, and compute features from the past only. Record failure onset, first observable symptom, trip, workover and DIFA confirmation separately. Report event recall, precision, false alarms per well-month, alert duration, median/range of useful lead, and missed sudden failures. Accuracy on highly imbalanced samples is insufficient. These are analyst recommendations responding to the study limitations.

Production value should be measured from actual interventions and incremental production or avoided deferment, with intervention cost and false-alert workload. Historical comparisons and estimated savings in these papers do not establish a guaranteed project return.

## E. Recommended Copilot Knowledge Entries

Prioritize these topics for retrieval, with the paper ID and PDF pages attached to every answer:

1. **ESP component, failure mode and root-cause vocabulary:** separate mechanism from consequence and confirmed from suspected. [P14](../reports/P14.md), [P29](../reports/P29.md)
2. **Current/pressure/temperature trend interpretation:** include frequency and pressure location, with competing causes. [P19](../reports/P19.md), [P30](../reports/P30.md)
3. **What can still be assessed after losing downhole sensors:** explicit required-input lists and abstention behavior. [P09](../reports/P09.md), [P10](../reports/P10.md), [P30](../reports/P30.md), [P33](../reports/P33.md)
4. **Sensor versus equipment fault:** loss, freezing, staleness and physically inconsistent measurements. [P28](../reports/P28.md)
5. **Pump duty and operating-envelope interpretation:** equipment curves, fluid properties, thrust and loading. [P22](../reports/P22.md)
6. **Evidence to capture after a trip:** preserve recent and long-term history, test records and operating changes. [P29](../reports/P29.md)
7. **Production/electrical mismatch and integrity checks:** distinguish routine surveillance from engineered testing. [P31](../reports/P31.md)
8. **Chemical/deposit and material mechanisms:** only when the well's fluid, chemical and completion context supports them. [P24](../reports/P24.md), [P29](../reports/P29.md)
9. **How to interpret an AI alert:** input completeness, model version, risk versus cause, lead-time definition and validation cohort. [P16](../reports/P16.md), [P17](../reports/P17.md), [P32](../reports/P32.md)
10. **Source limitations and rejected thresholds:** keep caveats retrievable together with the proposed rule, rather than in a separate document that an answer may omit.

The [Q&A library](../data/source-json/copilot_qa_library.json) provides 10 engineer and 10 operator questions for each paper. These are source-specific retrieval candidates. Before production use, merge equivalent questions and preserve disagreements, scope and citations; do not rank answers by the number of duplicate publications.

### Data arrangement proposed for the user's environment

| Data group | Required treatment | Why it matters |
|---|---|---|
| Avalon telemetry | Audit actual tag names, units, location, sampling/store-on-change behavior, quality and sensor availability; retain raw timestamps | High frequency alone does not establish raw waveform bandwidth, complete coverage or valid downhole data |
| Excel production tests | Map well/run IDs; keep test start/end, measured phase rates, units, operating conditions and validity | Do not fill a month of telemetry with one test rate and present it as continuously measured production |
| Excel surface pressure | Preserve measurement location, timestamp, units and whether measured manually or continuously | PIP/PDP, tubing, casing and network pressure are not interchangeable |
| Equipment and completion | Nameplates, pump curves/stages, motor/cable/transformer details, depth and fluid context | Needed for rated-limit checks, physical models and comparable operating duty |
| Failures and maintenance | Independent onset/trip/pull dates, DIFA components and cause, interventions and censoring | Needed to validate prediction and distinguish root cause from consequence |
| Water injection | Separate injector schema and engineering knowledge | Producer, polymer-flood and SAGD evidence does not validate injector fault diagnosis |

**Availability tiers:** full downhole instrumentation; partial downhole instrumentation; surface electrical plus surface pressure and periodic tests; insufficient reliable data. Evaluate every rule/model against the tier and actual required inputs. A model trained with complete downhole data must not silently receive zeros or long forward-filled values when a gauge fails.

The proposed answer structure is: observation and time window; data quality; candidate causes; supporting and contradictory evidence; missing checks; approved response reference; confidence basis; source pages. A static research report can explain physics but cannot tell whether a well is currently abnormal without a live or dated data query.

## F. Recommended Future AI Models

| Priority | Model candidate | Required inputs / target | Initial test and release condition |
|---|---|---|---|
| 1 | Quality and operating-state classifier | Timestamps, run state, electrical trends, control/operation log; missing/frozen/stale/stopped states | Verify against sampled historian/operations records; quantify false data-fault flags |
| 1 | Explainable rule and candidate-ranking engine | Valid trends, equipment/fluid context and source-linked hypotheses | Expert review of real events and alternatives; no numeric probability claim without calibration |
| 1 | PCA/robust residual or change-point detector | Comparable operating windows; separate full-sensor and surface-only feature sets | Compare with simple univariate baselines and false alarms per well-month |
| 2 | Surface-only boosted-tree failure-risk model | Current, voltage, frequency, runtime, available pressures/tests; independently confirmed future events | Later-run/well holdout, causal preprocessing, calibrated risk and useful lead distribution |
| 2 | Full-sensor and component-specific risk models | Pressure, temperature, vibration, electrical/context variables and DIFA component outcomes | Prove value beyond the surface-only and simple-rule baselines; report missing-sensor performance separately |
| 2 | Physics-assisted virtual measurement / residual model | Equipment curves, fluid/completion data, valid boundary measurements | Validate inferred pressure/rate against held-out measurements and publish uncertainty; mark every estimate |
| 2 | Production-change and integrity screening | Aligned production tests, electrical duty and surface pressure | Test against fluid, network, sensor and tubing-leak events; accept that test sparsity limits detection speed |
| 3 | Constraint-aware frequency recommendation | Validated rate model, operating envelope, temperatures/pressures/electrical limits and economics | Offline replay followed by engineer-reviewed advisory trials; evaluate production and stress together. [P02](../reports/P02.md) |
| 3 | Survival / competing-risk model | Install/pull history, active exposure, censored survivors, component events and pre-outcome covariates | Time-dependent calibration and prospective validation; exclude whole-run or post-pull leakage |
| 3, conditional | Waveform mechanical classifier | Actual suitable-bandwidth vibration waveforms, sensor positions and labeled field faults | Separate rigs/runs/wells in testing; laboratory near-perfect accuracy is not a field claim. [P23](../reports/P23.md) |

The rule engine, surface-only model and full-sensor model should be evaluated separately. More complex architectures are justified only after they improve useful lead, diagnostic ranking or production decisions on independent local events. None of these papers supplies a complete validated water-injection surveillance model.
