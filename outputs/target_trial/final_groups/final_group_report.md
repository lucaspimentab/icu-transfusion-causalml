# Final causal inference for scan-derived transfusion phenotypes

## Final groups

- B1 benefit primary: stable/controlled heart rate, falling hemoglobin, and non-high final SpO2.
- B2 benefit sensitivity: B1 plus low-to-moderate mean arterial pressure.
- M1 harm primary: rising heart rate plus high maximum mean arterial pressure.
- M2 harm sensitivity: M1 plus high creatinine variability.
- M3 harm secondary: hemoglobin not falling.

## Main all-sample estimates

| group_id | direction | role | n | n_treated | n_control | treated_mean | control_mean | unadjusted_diff | aipw_ate | aipw_ate_ci95_low | aipw_ate_ci95_high | aipw_att | overlap_weighted_diff | iptw_diff | model_ite_mean | prop_model_benefit | prop_model_harm |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | benefit | primary | 151 | 46 | 105 | 0.217 | 0.476 | -0.259 | -0.309 | -0.537 | -0.106 | -0.223 | -0.236 | -0.276 | -0.008 | 0.563 | 0.437 |
| B2 | benefit | sensitivity | 117 | 35 | 82 | 0.200 | 0.488 | -0.288 | -0.347 | -0.575 | -0.145 | -0.328 | -0.272 | -0.292 | -0.026 | 0.564 | 0.436 |
| M1 | harm | primary | 328 | 141 | 187 | 0.496 | 0.332 | 0.165 | 0.240 | 0.101 | 0.383 | 0.203 | 0.171 | 0.199 | 0.071 | 0.442 | 0.558 |
| M2 | harm | sensitivity | 109 | 52 | 57 | 0.712 | 0.439 | 0.273 | 0.449 | 0.140 | 0.796 | 0.355 | 0.286 | 0.345 | 0.060 | 0.440 | 0.560 |
| M3 | harm | secondary | 219 | 37 | 182 | 0.649 | 0.467 | 0.182 | 0.305 | 0.116 | 0.511 | 0.339 | 0.275 | 0.289 | 0.161 | 0.306 | 0.694 |

## Discovery/validation estimates

| group_id | split | n | n_treated | n_control | aipw_ate | aipw_ate_ci95_low | aipw_ate_ci95_high | model_ite_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | discovery | 106 | 33 | 73 | -0.274 | -0.589 | -0.007 | -0.003 |
| B1 | validation | 45 | 13 | 32 | -0.391 | -0.596 | -0.186 | -0.019 |
| B2 | discovery | 79 | 25 | 54 | -0.298 | -0.622 | -0.025 | -0.026 |
| B2 | validation | 38 | 10 | 28 | -0.448 | -0.689 | -0.218 | -0.024 |
| M1 | discovery | 235 | 99 | 136 | 0.189 | 0.012 | 0.368 | 0.063 |
| M1 | validation | 93 | 42 | 51 | 0.370 | 0.172 | 0.591 | 0.092 |
| M2 | discovery | 78 | 34 | 44 | 0.372 | -0.030 | 0.804 | 0.067 |
| M2 | validation | 31 | 18 | 13 | 0.644 | 0.248 | 1.129 | 0.041 |
| M3 | discovery | 147 | 21 | 126 | 0.354 | 0.093 | 0.635 | 0.176 |
| M3 | validation | 72 | 16 | 56 | 0.205 | 0.022 | 0.396 | 0.132 |

## Primary group membership

| label | n |
| --- | --- |
| neither_primary | 1005 |
| harm_primary | 328 |
| benefit_primary | 151 |

## Interpretation

The final benefit phenotype is most consistent with dynamic anemia in a patient who remains physiologically compensated: heart rate is controlled/stable, hemoglobin is falling, and final SpO2 is not high.

The final harm phenotype is most consistent with a stress/deterioration trajectory: heart rate is rising and maximum mean arterial pressure is high before the decision point. The cardiorenal sensitivity group strengthens this signal when creatinine variability is added.

These estimates use observational target-trial emulation and doubly robust adjustment. They support heterogeneous-effect hypotheses, not clinical decision rules without external or temporal validation.

## Output files

- `final_group_effects.csv`
- `final_group_balance.csv`
- `final_group_profiles.csv`
- `final_group_assignments.parquet`
- `final_group_patient_counterfactuals.parquet`
- `final_group_report.md`