# Evidence, Scope and Limitations

All 37 supplied PDF files have a structured engineering extraction. Text was extracted with PDF-page boundaries; selected diagnostic tables, figures and performance tables were checked visually. This is not a claim that every page or every equation has been independently visually verified, or that the underlying studies have been reproduced. The 235-page thesis has extensive background, appendices and overlapping material; its report concentrates on operationally relevant methods, taxonomy, cases, results and limitations.

The supplied corpus is the evidence boundary. No external literature search or author/data correspondence was performed. Missing DOI, threshold, horizon, accuracy or production benefit is marked as not reported or not established; bibliographic gaps have not been filled by guessing.

## Evidence interpretation

A source-stated diagnostic rule is not necessarily validated. Hypotheses, background mechanisms, laboratory results, selected field cases, retrospective model results and engineering proposals have different evidential weight. Confidence labels are analyst judgments about the statement and its transferability, not numerical probabilities. Some High confidence labels describe a source limitation or an evidence-handling practice, rather than diagnostic accuracy.

Sections 6 and 10 serve different purposes: Section 6 preserves author logic or explicitly identified derived logic; Section 10 is an operational conversion with checks and action links. Section 7 timing is an analyst organization where the source does not specify immediate/short/long categories. When a paper gives no condition-specific action protocol, the report labels the response as a general engineering proposal.

The parameter tables are engineering mappings, not an audited Avalon inventory. Detection/prediction cells identify candidate roles or refer to the source method; they do not certify every listed parameter as an independently validated predictor. Lists include measured inputs, derived features, static context and outcome labels. Outcome labels and post-pull findings must not become live predictors.

Channel relevance in an indicator table means the channel can contribute to the stated combination. It does not establish diagnosis from that channel alone. Liquid rate is not automatically oil rate; averaged vibration is not a waveform; surface VSD voltage/current are not automatically motor-terminal measurements.

Every report retains the requested sections even for rod-pump, laboratory, proposal or statistical-taxonomy papers. These studies are marked for limited ESP/offshore transfer rather than silently treated as direct field evidence.

## Repeated or related evidence

- P04, P06, P08, P36, P37: Related Siemens / 30-ESP pilot publications; repeated 12-day case is not independent validation.
- P05, P18: Related robust-PCA / health-KPI methodology and case material; assess shared data before pooling.
- P12, P14: Overlapping thesis / failure-classification research; do not count shared taxonomy/data twice.

## Deployment status

No rule, threshold or model in this package is approved or connected to field equipment. The JSON status do_not_deploy_as_written identifies prominent source contradictions or non-transferable formulations, not an exhaustive safety assessment. Other rules also require local validation. Operational thresholds must be reconciled with actual units, equipment ratings, measurement locations, operating envelopes and approved site procedures.

Published diagnostic thresholds, data-cleaning limits, label definitions, model score cutoffs and physical equipment limits are separate objects. Keep them separate in any database or Copilot answer.

Reported lead times must distinguish input lookback, forecast target horizon, event-matching tolerance, alert persistence, time before engineer reporting and time before physical failure. The extraction does not convert one into another.

## Source-specific issues and project fit

### P01 — A Neural Network Model for Electric Submersible Pump Surveillance

[Full report](../reports/P01.md)

**Caveats:** Changes in water cut, frequency and downhole pressure are stressors/context, not independent proven failure modes. No sensor-failure or injection diagnostic was validated.

**Model limitations:** Conceptual study; incomplete feature equations; several threshold/unit/comparator errors; model-specific inputs and extensive downhole/design data required.

**Data feasibility:** Avalon alone: not established. Combined Avalon, test and surface-pressure data: insufficient without equipment ratings, fluid properties and valid downhole/calculated features. Surface-only version would be a new model.

### P02 — AI-Based ESP Optimal Control Solution to Optimize Oil Flow Across Multiple Wells

[Full report](../reports/P02.md)

**Caveats:** Printed true-rate correction Eq. 5 multiplies by 24/on-hours; this appears inconsistent with converting on-time rate to calendar daily volume. Do not implement without resolving rate definitions. Eq. 8 also simplifies random error as twice a term; use proper differencing/noise propagation.

**Model limitations:** Stable wells only; blending confidence algorithm undisclosed; network interference and equivalent injection unresolved; geologist approves settings; sample-count/pressure-unit discrepancies.

**Data feasibility:** Avalon alone: no. Combined three user sources: partial; need static equipment/fluid metadata, valid downhole CIPs, insulation, energy/prices and reservoir context. Injection response not solved.

### P03 — Application of a Fuzzy Expert System to Analyze and Anticipate ESP Failure Modes

[Full report](../reports/P03.md)

**Caveats:** Case Table 1 lists possible sand, gas and gas/scale sticking; these are not confirmed teardown diagnoses. Figure 4 and Tables 1–2 were visually inspected.

**Model limitations:** Nine selected wells; actual causes not established; scale/unit-sensitive arctangent; common memberships; trip contamination; three identical rule vectors; 30/60-day gaps.

**Data feasibility:** Avalon+production+surface-pressure data could support full rules only where all eight inputs exist. Lost PIP/PDP/temperature makes published rules incomplete; do not replace missing conditions by true.

### P04 — Applying Artificial Intelligence to Optimize Oil and Gas Production

[Full report](../reports/P04.md)

**Caveats:** Likely overlaps the 30-ESP/12-day use case in the cited SPE-192610-MS paper; do not count repeated descriptions as independent evidence.

**Model limitations:** Architecture/training details undisclosed; causality unclear; manual baseline cleansing; unknown anomalies hard to interpret; repeated historical tuning risks optimism.

**Data feasibility:** Avalon plus surface pressures can supply some inputs if tags exist; published model still needs three downhole channels. Production tests alone are insufficient. Reduced-sensor model requires separate training/validation.

### P05 — Applying Big Data Analytics to Detect, Diagnose, and Prevent Impending Failures in Electric Submersible Pumps

[Full report](../reports/P05.md)

**Caveats:** Printed claims that all individual values inside bands guarantee healthy joint scores are stronger than conditional mathematics warrants. Full original feature list is unavailable.

**Model limitations:** Linear normal model; correlated data; anonymized inputs; fixed-other-variable bands are not causal control policy; no held-out performance counts.

**Data feasibility:** Full replication requires downhole/thermal/vibration/leakage data and unnamed tags. A reduced Avalon+surface-pressure model is feasible as a new validated model; sparse production tests add context, not minute-scale signals.

### P06 — Artificial Intelligence Can Reduce ESP Failures

[Full report](../reports/P06.md)

**Caveats:** The advertisement on page 2 is unrelated and excluded. ML is broader than deep learning, despite the editorial's simplified description.

**Model limitations:** Two-page guest editorial; no reproducible model specification or independent results; probable same Siemens case as P04/P36.

**Data feasibility:** Cannot determine from unnamed inputs. Do not assume lost-sensor compatibility.

### P07 — Automatic Early Fault Detection for Rod Pump Systems

[Full report](../reports/P07.md)

**Caveats:** Normal is a class, not a failure mode. No injection analysis.

**Model limitations:** Rod systems; recorded-date bias; missing-data fill; table inconsistencies; claimed proof of no overfitting contradicted by reported overfit above 180 iterations; record-level CV may leak within wells.

**Data feasibility:** No direct ESP implementation with Avalon/tests/pressures: rod card/load inputs missing. General workflow transferable.

### P08 — AI4ESP - Autonomous Well Surveillance for ESP Pumps Using Artificial Intelligence

[Full report](../reports/P08.md)

**Caveats:** Do not infer autonomous equipment control from the title; authors explicitly describe support to human operators.

**Model limitations:** Architecture-level treatment; root causes and model mechanics undisclosed; availability of unknown downhole inputs not resolved.

**Data feasibility:** User sources can support an analogous architecture, but cannot establish exact model replication or sensor-loss performance.

### P09 — Condition monitoring and fault diagnosis of electric submersible pump based on wellhead electrical parameters and production parameters

[Full report](../reports/P09.md)

**Caveats:** Table 1 underload/overload labels for current appear reversed relative to Sections 4.2/4.3. The undervoltage narrative says overload shutdown after underload limit; quarantine literal trip-type rule. Surface-to-downhole pressure equations need dimensional validation.

**Model limitations:** Several table/text contradictions; diagrams schematic; current waveform sampling requirement unspecified; live gas/liquid meter unlike intermittent tests; pressure formulas dimensionally ambiguous.

**Data feasibility:** Combined Avalon+tests+surface pressure supports a reduced screening version if time aligned; exact method requires real-time gas/liquid sensing and waveform fidelity. Avalon alone insufficient for differential diagnosis.

### P10 — Data Driven Approach to Failure Prediction for Electrical Submersible Pump Systems

[Full report](../reports/P10.md)

**Caveats:** Do not describe the paper as >90% accurate or as guaranteeing 90-day warning. Abstract's favorable language is weaker evidence than the numerical table.

**Model limitations:** Labels subjective; inefficiency versus failure confused; 90-day window can inflate usefulness; no fixed RUL; copying prior data can manufacture patterns.

**Data feasibility:** Avalon alone conditionally sufficient for scoring if four raw tags and history exist; event/maintenance labels still needed for training. Tests/surface pressures useful for diagnosis, not original inputs.

### P11 — Data-Driven Diagnosis for Artificial Lift Pump's Failures

[Full report](../reports/P11.md)

**Caveats:** Reported ESP shares ~49% cable, 30% pump, 12% other and 7% motor are approximate and do not sum exactly to 100%. Do not force normalization or treat percentages as universal.

**Model limitations:** Post-pull HUD risks target leakage; censoring treatment and held-out validation unclear; correlated feature weights are not causes; only failure cases may bias life model.

**Data feasibility:** Three sources alone insufficient: need installations/pulls/failure labels, completion geometry, equipment and contemporaneous solids data. Downhole sensors not essential to original static model.

### P12 — Detecting Electrical Submersible Pump (ESP) Failures and Estimating Run Life Using Artificial Neural Networks

[Full report](../reports/P12.md)

**Caveats:** COBRA-02 date span 10-Oct-2019 to 05-Nov-2020 is 392 days, not 312; failure-to-restart 05–19 Nov is 14 days, not 10. KAR-SE04 printed table supports 3/5 exact class matches, not claimed 4/5. High headline scores must not be ingested without experiment/split provenance. P14 overlaps this taxonomy/case history.

**Model limitations:** Conflicting cohort/metric tables, ambiguous split nomenclature, backward filling and full-well imputation risk lookahead, supervised failure clustering may require unavailable future mode, censoring handling unclear, post-event labels mixed with causal categories and WO. Claimed R² '4.0' is invalid as a conventional positive upper-bound score and likely missing a sign; retain as source error.

**Data feasibility:** Avalon+tests+surface pressures insufficient alone: installation/failure/DIFA/configuration/chemistry needed. Models include downhole channels; missing-sensor imputation is not independently validated as a virtual sensor.

### P13 — Detecting Failures and Optimizing Performance in Artificial Lift Using Machine Learning Models

[Full report](../reports/P13.md)

**Caveats:** No evidence for autonomous ESP control. ROC AUC is ranking discrimination, not accuracy; false-positive rate is 1−specificity, despite source wording.

**Model limitations:** Rod-specific features; imbalance (~1% failure time) inflates accuracy; retrospective labels use later evidence; cannot use those future observations live; small suboptimal-event cohorts.

**Data feasibility:** No direct ESP reproduction from Avalon/test/pressure sources; methodology transfers after new ESP features/labels. Gas-lift extension is not water-injection evidence.

### P14 — Dual-Level Electric Submersible Pump (ESP) Failure Classification: A Novel Comprehensive Classification Bridging Failure Modes and Root Cause Analysis

[Full report](../reports/P14.md)

**Caveats:** Closely overlaps P12, including Cobra-08. Do not double-count cases. LPUM/LOAM/HIAM mappings in Appendix C are not unique physical diagnoses. Chemical injection is not equivalent to reservoir water-injection surveillance.

**Model limitations:** Incomplete RCA, selection/subjective reporting, weak association, counts and category counts not perfectly consistent; counterfactual economics and unsupported discussion percentages.

**Data feasibility:** Avalon/tests/pressures support evidence but not confirmed root causes; DIFA, workover and installation records essential. Sensor loss does not prevent taxonomy use.

### P15 — Electrical Submersible Pump Digital Twin, the Missing Link for Successful Condition Monitoring and Failure Prediction

[Full report](../reports/P15.md)

**Caveats:** Autonomous-control/RUL capabilities are requirements, not demonstrated outcomes. No water-injection model validated.

**Model limitations:** Calibration/identifiability, uncertain physics, sim-to-real gap; stochastic life assignment is not observed RUL; no deployed validation.

**Data feasibility:** Three user data sources alone insufficient without equipment, completion, fluid and reservoir model. Virtual sensing for missing downhole channels is an opportunity, not demonstrated accuracy here.

### P16 — ESP Well and Component Failure Prediction in Advance using Engineered Analytics - A Breakthrough in Minimizing Unscheduled Subsurface Deferments

[Full report](../reports/P16.md)

**Caveats:** Figure 21 matrix visually verified. Printed blind pump accuracy does not reconcile. Estimated benefits are not field-achieved savings; authors' broad claims about uncontrollable component failures are not universal engineering rules.

**Model limitations:** Small component sample, SME-corrected event dates, balanced initial test prevalence and retrospective review. Roughly 40% well failures missed. Complete 18-feature names not disclosed.

**Data feasibility:** Not directly from three stated sources alone: requires completion/equipment/failure records and validated physical models; missing downhole sensors remove important inputs. Reduced-signal model requires separate training.

### P17 — Prediction of ESPs Failure Using ML at Western Siberia Oilfields with Large Number of Wells

[Full report](../reports/P17.md)

**Caveats:** 96% post-fill completeness describes filled dataset, not sensor coverage. No direct water-injection diagnosis.

**Model limitations:** Balanced 50/50 class evaluation; interpolated/imputed values are not recovered measurements. Akima≤5 day gaps and long-gap moving-average/linear fills may use future data unless made causal. Component/manufacturer/stage metadata unavailable.

**Data feasibility:** Needs equipment, trajectory, PVT, failure records and physical model beyond three sources. Surface-only version is a new experiment, not established by results.

### P18 — ESP Health Monitoring KPI: A Real-Time Predictive Analytics Application

[Full report](../reports/P18.md)

**Caveats:** Related to P05; do not import P05's 30 hour example into this source. Contribution-based diagnosis/prescription described as future extension.

**Model limitations:** Limited illustrated cases; no validated causal diagnosis; 95% pointwise bound does not equal 5% fleet event false-alarm rate; operating regime shifts matter.

**Data feasibility:** Potential with mapped Avalon channels; full reproduction requires 22 inputs, whose complete names are not disclosed. Missing-sensor cohort must use its own baseline. Excel tests are context, not minute inputs.

### P19 — Prescriptive-Based Decision Support System for Online Real-Time Electrical Submersible Pump Operations Management

[Full report](../reports/P19.md)

**Caveats:** Matrix visually checked onpp.7–10. Plugged pump/broken shaft/worn pump share patterns. Source suggests potentially hazardous testing/fluid/casing/electrical interventions; extraction is not an execution procedure. Temperature percentage thresholds depend on Celsius/Fahrenheit baseline and need reformulation. Specific-energy notation KWD/BPD/1000 ft*lift is ambiguous; do not encode literally.

**Model limitations:** Membership thresholds not fully reproducible; overlapping pump patterns; experimental percentages not universal limits; no sensitivity/specificity.

**Data feasibility:** Full matrix cannot run on sensor-lost wells. With Avalon electrical channels and sparse Excel only, retain partial-evidence hypotheses and request missing checks; no fabricated PIP/PDP or live rate.

### P20 — Failure Prediction for Rod Pump Artificial Lift Systems

[Full report](../reports/P20.md)

**Caveats:** Published test size and cross-validation error arithmetic inconsistent; do not advertise high ESP accuracy from rod data.

**Model limitations:** Very small event count; random-peek uses unlabeled test distribution (transductive evaluation); high false alarms; inconsistent counts/metrics; smoothing may erase real events.

**Data feasibility:** No direct ESP reproduction from Avalon/Excel; card/load/rod variables absent. Can reuse causal feature engineering and event-based evaluation design.

### P21 — Global Model for Failure Prediction for Rod Pump Artificial Lift Systems

[Full report](../reports/P21.md)

**Caveats:** Source data are rod pumps. Do not transfer rod-cutting/card rules directly to ESP. Training ratio statement is inconsistent with stated 50 failure/350 normal well count.

**Model limitations:** 100 day matching tolerance; alerts within 15 days of downtime filtered; different fields vary markedly; prose incorrectly labels false positive as false negative; normal-cluster cutoff 70% prose versus 50% algorithm.

**Data feasibility:** Rod-card variables absent in ESP sources; methodology transferable only after new ESP training/labels.

### P22 — Innovative Approach to Prolong ESP Run Life Using Algorithmic Models

[Full report](../reports/P22.md)

**Caveats:** Source contains equipment-description inaccuracies (pump paragraph mentions motors); do not import verbatim. Voltage rerating is specialist work. Runlife comparison does not prove program causality.

**Model limitations:** Rate/head inference requires density and calibration; claimed benefits lack control cohort.

**Data feasibility:** Basic electrical surveillance feasible if tags mapped. Full hydraulic envelope needs valid downhole pressures or independently validated estimates plus curves/PVT/completion data outside three sources.

### P23 — Intelligent diagnosis of petroleum equipment faults using a deep hybrid model

[Full report](../reports/P23.md)

**Caveats:** Table 6 visually verified. Near-perfect classification is not field Pd M accuracy. Dataset counts/repeat protocol internally inconsistent.

**Model limitations:** Labwater data; random record split may share machine/test run signatures; no held-out field run validation or predictive lead; high training cost.

**Data feasibility:** No, unless Avalon contains raw 4096 Hz waveforms with correct positions. HF operating telemetry is not automatically vibration waveform data. Excel sources cannot substitute.

### P24 — Machine Learning Approach for Predictive Maintenance of the Electrical Submersible Pumps (ESPs)

[Full report](../reports/P24.md)

**Caveats:** Do not treat flood field results as water-injection well fault model. The paper's isolated dynamometer reference does not make its ESP inputs dynamometer cards.

**Model limitations:** 70/30 versus 70/15/15 split descriptions; random folds not well/run chronological validation; full-data PCA/scaling language risks leakage; tables contain impossible descriptive ordering(mean/std versus max); standardization text says variance rather than SD.

**Data feasibility:** Full model needs downhole sensors and workover labels. Three sources alone insufficient unless labels/equipment context supplied. Sensorless variant untested.

### P25 — Multiphase gas-flow model of an electrical submersible pump

[Full report](../reports/P25.md)

**Caveats:** Paper's broad claim that failures can be easily avoided by changing conditions is not demonstrated field control validation.

**Model limitations:** Narrow test domain; no offshore validation, failure outcomes or RUL; head/elevation is not simply well depth. Some estimates negative at zero gas.

**Data feasibility:** Not directly: continuous total flow and developed head at matched conditions required. Sparse surface tests and no downhole sensors do not reproduce these inputs; requires PVT/calibrated hydraulic model and gas-reference labels.

### P26 — Predicting Non-Newtonian Fluid Electric Submersible Pump failure using Deep Learning and Artificial Neural Network

[Full report](../reports/P26.md)

**Caveats:** PDF page 1 blank. Title's non-Newtonian emphasis is not backed by a rheology-specific experiment; no quantitative accuracy should be invented.

**Model limitations:** Assumes build-up failure mechanism; instantaneous failures acknowledged; no non-Newtonian rheology validation or quantified predictive evidence; table lacks units.

**Data feasibility:** No reproduction without downhole pressure/temperature/vibration and fuller model specification. Surface-only performance not demonstrated.

### P27 — Predictive Approach to Perform Fault Detection in Electrical Submersible Pump Systems

[Full report](../reports/P27.md)

**Caveats:** Figure 5 visually verified lists 6 specific categories plus Other despite text 'six'. No 100% reliability inference from 40 normal cases.

**Model limitations:** Normal/failure sampling resolution differs; only 70% variance retained; 20 min samples miss fast dynamics; same wells contribute healthy/failure periods; small selected normal set.

**Data feasibility:** Needs 13 inputs including downhole signals and choke. Sensor-lost model requires new baseline and separate validation; daily Excel context does not recreate 20 min telemetry.

### P28 — Predictive Data Analytics for Effective Electric Submersible Pump Management

[Full report](../reports/P28.md)

**Caveats:** Figures 3 and 6 visually verified. Reported 100% recall applies NORMAL class, not failures. Cumulative failure ratio is not an annual hazard or reliability estimate.

**Model limitations:** Small cases; automatic real-time deployment future work; tree labels/sample independence unspecified; months-long retrospective drift can reflect onset/discovery ambiguity.

**Data feasibility:** Full PCA unavailable after downhole loss; build separate surface baseline. Electrical integrity/DIFA/metadata are additional required records.

### P29 — Preventive Maintenance of Electric Submersible Pumps and its Relationship to Root Cause of Failure Analysis

[Full report](../reports/P29.md)

**Caveats:** Duplicate text layers were removed for extraction.200 to 600 days is roughly 3×run life (200% increase), not a 300% increase. Waterflood description is context, not an injection-well diagnostic model.

**Model limitations:** Small field, concurrent interventions, ambiguous improvement percentages/economic units.

**Data feasibility:** Avalon+Excel support surveillance but not full RCFA; needs DIFA, materials, chemistry, settings, installation records.

### P30 — Real-Time Data and Expert System Combine to Develop Artificial Lift Predictive Diagnostics

[Full report](../reports/P30.md)

**Caveats:** Correlation loss is not proof a causal link is broken. Conclusion percentages 20/15% differ from detailed table 25/18%; retain table counts. Abstract missing-data robustness does not imply fully sensorless operation.

**Model limitations:** Reference tuning after frequency change;~5% unusual wells require tuning; incomplete sensors+unusual conditions degrade accuracy; 57 event selection does not prove universal 100% recall.

**Data feasibility:** Some partial-sensor cases supported, 17/79 events with≥1 missing parameter. Loss ofboth PIP/PDP violates source crucial-input gate; surface-only cannot claim this method's diagnostic performance.

### P31 — Real-Time Monitoring and Diagnosis of Electrical Submersible Pump

[Full report](../reports/P31.md)

**Caveats:** Figure 4 visually transcribed. Figure 5 has overlapping/corrupted content; nine named abnormal classes retained, but ambiguous intermediate branches are not invented. Table 1 reverse-rotation causal statement is questionable and should not be copied as a general mechanism.

**Model limitations:** Synthetic training and validation not fully characterized; current classes overlap; Figure 5 rendering partly corrupted; empirical 0.78/1.5/1 cutoffs not universal.

**Data feasibility:** Current features possible from Avalon; full pressure method needs dedicated time-resolved test and extra completion/PVT/curve data. Routine Excel pressures/tests alone insufficient.

### P32 — Real-Time Monitoring and Predictive Failure Identification for Electrical Submersible Pumps

[Full report](../reports/P32.md)

**Caveats:** Table 1 visually verified.180000 minutes is study-specific baseline length. Do not suppress an urgent physical alarm merely because it lasted only one day.

**Model limitations:** Six failed wells only; parameter selection retrospective; no fleet rate denominator; two-day persistence delays fast faults; real-power proxy I×V omits three-phase power factor/efficiency.

**Data feasibility:** PCA needs pressure/rate/temperature; residual method requires measured vibration at scoring, not just surface predictors. Cannot calculate residual after losing vibration sensor.

### P33 — A Fault Diagnosis Model of an Electric Submersible Pump Based on Mechanism Knowledge

[Full report](../reports/P33.md)

**Caveats:** Figure 3 visually inspected. Taxonomy includes translated/ambiguous labels retained as such; do not claim each is a validated distinct failure mode. BiLSTM must operate only on a fully available past window for online use.

**Model limitations:** Restricted private data/graph; hard exclusions physically overbroad; random event split not external-field validation; equation 8 accuracy omits TN and F1 derivation inconsistent; confidence scores from two models may be incomparable; exact 50-label taxonomy not cleanly enumerated.

**Data feasibility:** Potentially close to project, but requires continuous surface channels, plant rate-estimation method, verified fault labels and graph. Sparse Excel tests cannot substitute for minute production estimates. No downhole sensors required by core input set.

### P34 — Three Approaches to Predicting ESP Pump Failures During SAGD Operations

[Full report](../reports/P34.md)

**Caveats:** Appendix tree/tables visually verified. Source prose alternates mean/min producer-choke summary names; tree uses MIN_MEDIAN. Higher R² does not establish prospective RUL accuracy.

**Model limitations:** Completed-run summaries leak future information if used as prospective predictors; only 29/42 failure cases; correlated features; no reliable external validation or forecast lead.

**Data feasibility:** Surface concepts transferable, but SAGD steam/injector/geological inputs absent from stated sources. Ordinary water injection cannot substitute for SAGD steam variables.

### P35 — Time-aware predictive maintenance of electrical submersible pumps using catboost ensemble learning and trend-based labeling

[Full report](../reports/P35.md)

**Caveats:** 87390 points at 30 s span~30.34 days of samples, not 105 continuous days; coverage/gaps unclear. Cleaned motor temperature minimum 95°C conflicts with stable<85°C rule. Data availability statement says no datasets analyzed despite empirical study. Do not advertise 99.85% field failure prediction.

**Model limitations:** One well, selected anomalous window; labels depend on same signals as features; no independent event-level prospective validation; chronological versus stratified K-fold descriptions conflict; preprocessing/SMOTE placement unclear; outlier removal may discard true faults; claimed 5 PC variance 90/95/97% inconsistent.

**Data feasibility:** Requires working downhole pressure/temperature/vibration; surface voltage/current prior to transformer must not be treated as motor-terminal values. Missing-sensor version untested.

### P36 — Usage of Artificial Intelligence to Reduce Operational Disruptions of ESPs by Implementing Predictive Maintenance

[Full report](../reports/P36.md)

**Caveats:** Overlaps P04/P06/P08/P36/P37 pilot family; do not count repeated 12 day example as independent validation. Conventional alarms can also be preventive; broad vendor contrast is not engineering fact. Source typography 2000 C likely intended 200°C; not a valid equipment operating limit.

**Model limitations:** Manual training-data curation; repeated tuning on same history; missing cause specificity; limited reproducibility; related publications reuse pilot evidence.

**Data feasibility:** Potential Avalon-fed monitoring, but full published model uses downhole inputs. A sensor-lost cohort requires new baseline and validation; Excel tests supply contextual evidence rather than fast stream.

### P37 — Using Machine Learning-Based Predictive Models to Enable Preventative Maintenance and Prevent ESP Downtime

[Full report](../reports/P37.md)

**Caveats:** Overlaps P04/P06/P08/P36/P37 pilot family; do not count repeated 12 day example as independent validation. Conventional alarms can also be preventive; broad vendor contrast is not engineering fact. Pilot running since May 2018; abstract says 10 months and case discussion refers totwo-year project. Autonomous refers surveillance, not closed-loop control. Advisory separation does not eliminate all cybersecurity or bad-advice risk.

**Model limitations:** Manual training-data curation; repeated tuning on same history; missing cause specificity; limited reproducibility; related publications reuse pilot evidence.

**Data feasibility:** Potential Avalon-fed monitoring, but full published model uses downhole inputs. A sensor-lost cohort requires new baseline and validation; Excel tests supply contextual evidence rather than fast stream.
