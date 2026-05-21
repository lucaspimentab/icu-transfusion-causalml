# Crosswalk between legacy clinical scan rules and final causal groups

## Objective

This analysis applies the representative legacy scan rules B1-B4/M1-M4 from the cluster-transfusion project to the same target-trial cohort used in the current causal analysis. It then estimates doubly robust AIPW effects in each old rule group and measures overlap with the final groups B1/B2/M1/M2/M3.

## AIPW effects in legacy scan rules

| legacy_group_id | direction | n | n_treated | n_control | unadjusted_diff | aipw_ate | aipw_ate_ci95_low | aipw_ate_ci95_high | validated_direction | name |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| old_M1 | harm | 88 | 47 | 41 | 0.044 | 0.107 | -0.086 | 0.310 | no | Falencia hepatobiliar com estresse metabolico |
| old_M2 | harm | 294 | 88 | 206 | 0.057 | 0.058 | -0.143 | 0.267 | no | Doenca critica sustentada hepatobiliar-renal |
| old_M3 | harm | 219 | 60 | 159 | 0.056 | -0.030 | -0.228 | 0.144 | no | Baixo fluxo cardiorrenal com hipotensao diastolica |
| old_M4 | harm | 86 | 50 | 36 | -0.038 | 0.099 | -0.089 | 0.297 | no | Falencia progressiva renal e hipoperfusao metabolica |

## Concordant overlap

Rows below compare old benefit rules with current benefit rules and old harm rules with current harm rules.

| legacy_group_id | current_group_id | n_legacy | n_current | n_overlap | pct_legacy_captured_by_current | pct_current_in_legacy | jaccard | fisher_odds_ratio | fisher_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| old_B1 | B1 | 0 | 151 | 0 |  | 0.000 | 0.000 |  |  |
| old_B1 | B2 | 0 | 117 | 0 |  | 0.000 | 0.000 |  |  |
| old_B2 | B1 | 0 | 151 | 0 |  | 0.000 | 0.000 |  |  |
| old_B2 | B2 | 0 | 117 | 0 |  | 0.000 | 0.000 |  |  |
| old_B3 | B1 | 0 | 151 | 0 |  | 0.000 | 0.000 |  |  |
| old_B3 | B2 | 0 | 117 | 0 |  | 0.000 | 0.000 |  |  |
| old_B4 | B1 | 0 | 151 | 0 |  | 0.000 | 0.000 |  |  |
| old_B4 | B2 | 0 | 117 | 0 |  | 0.000 | 0.000 |  |  |
| old_M1 | M1 | 88 | 328 | 22 | 0.250 | 0.067 | 0.056 | 1.187 | 0.508 |
| old_M1 | M3 | 88 | 219 | 13 | 0.148 | 0.059 | 0.044 | 1.001 | 1.000 |
| old_M1 | M2 | 88 | 109 | 11 | 0.125 | 0.101 | 0.059 | 1.892 | 0.087 |
| old_M2 | M3 | 294 | 219 | 60 | 0.204 | 0.274 | 0.132 | 1.663 | 0.003 |
| old_M2 | M1 | 294 | 328 | 52 | 0.177 | 0.159 | 0.091 | 0.712 | 0.042 |
| old_M2 | M2 | 294 | 109 | 27 | 0.092 | 0.248 | 0.072 | 1.366 | 0.172 |
| old_M3 | M3 | 219 | 219 | 31 | 0.142 | 0.142 | 0.076 | 0.945 | 0.837 |
| old_M3 | M1 | 219 | 328 | 21 | 0.096 | 0.064 | 0.040 | 0.331 | 0.000 |
| old_M3 | M2 | 219 | 109 | 19 | 0.087 | 0.174 | 0.061 | 1.240 | 0.401 |
| old_M4 | M1 | 86 | 328 | 18 | 0.209 | 0.055 | 0.045 | 0.929 | 0.894 |
| old_M4 | M2 | 86 | 109 | 15 | 0.174 | 0.138 | 0.083 | 2.931 | 0.001 |
| old_M4 | M3 | 86 | 219 | 10 | 0.116 | 0.046 | 0.034 | 0.749 | 0.530 |

## Discordant overlap

Rows below show old benefit rules overlapping current harm rules, or old harm rules overlapping current benefit rules.

| legacy_group_id | current_group_id | n_legacy | n_current | n_overlap | pct_legacy_captured_by_current | pct_current_in_legacy | jaccard | fisher_odds_ratio | fisher_p_value |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| old_B1 | M1 | 0 | 328 | 0 |  | 0.000 | 0.000 |  |  |
| old_B1 | M2 | 0 | 109 | 0 |  | 0.000 | 0.000 |  |  |
| old_B1 | M3 | 0 | 219 | 0 |  | 0.000 | 0.000 |  |  |
| old_B2 | M1 | 0 | 328 | 0 |  | 0.000 | 0.000 |  |  |
| old_B2 | M2 | 0 | 109 | 0 |  | 0.000 | 0.000 |  |  |
| old_B2 | M3 | 0 | 219 | 0 |  | 0.000 | 0.000 |  |  |
| old_B3 | M1 | 0 | 328 | 0 |  | 0.000 | 0.000 |  |  |
| old_B3 | M2 | 0 | 109 | 0 |  | 0.000 | 0.000 |  |  |
| old_B3 | M3 | 0 | 219 | 0 |  | 0.000 | 0.000 |  |  |
| old_B4 | M1 | 0 | 328 | 0 |  | 0.000 | 0.000 |  |  |
| old_B4 | M2 | 0 | 109 | 0 |  | 0.000 | 0.000 |  |  |
| old_B4 | M3 | 0 | 219 | 0 |  | 0.000 | 0.000 |  |  |
| old_M1 | B1 | 88 | 151 | 3 | 0.034 | 0.020 | 0.013 | 0.298 | 0.028 |
| old_M1 | B2 | 88 | 117 | 3 | 0.034 | 0.026 | 0.015 | 0.397 | 0.150 |
| old_M2 | B1 | 294 | 151 | 23 | 0.078 | 0.152 | 0.055 | 0.704 | 0.161 |
| old_M2 | B2 | 294 | 117 | 18 | 0.061 | 0.154 | 0.046 | 0.719 | 0.229 |
| old_M3 | B1 | 219 | 151 | 32 | 0.146 | 0.212 | 0.095 | 1.648 | 0.028 |
| old_M3 | B2 | 219 | 117 | 31 | 0.142 | 0.265 | 0.102 | 2.261 | 0.001 |
| old_M4 | B1 | 86 | 151 | 9 | 0.105 | 0.060 | 0.039 | 1.034 | 0.855 |
| old_M4 | B2 | 86 | 117 | 8 | 0.093 | 0.068 | 0.041 | 1.213 | 0.540 |

## AIPW effects in intersections

| legacy_group_id | current_group_id | same_direction | n | n_treated | n_control | unadjusted_diff | aipw_ate | aipw_ate_ci95_low | aipw_ate_ci95_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| old_M1 | B1 | False | 3 | 1 | 2 | -1.000 | -0.993 | -1.023 | -0.968 |
| old_M1 | B2 | False | 3 | 1 | 2 | -1.000 | -0.993 | -1.023 | -0.968 |
| old_M1 | M1 | True | 22 | 13 | 9 | 0.103 | 0.255 | -0.070 | 0.588 |
| old_M1 | M2 | True | 11 | 8 | 3 | -0.250 | 0.154 | -0.223 | 0.530 |
| old_M1 | M3 | True | 13 | 7 | 6 | 0.238 | 0.150 | -0.318 | 0.578 |
| old_M2 | B1 | False | 23 | 6 | 17 | -0.314 | -0.638 | -1.504 | -0.046 |
| old_M2 | B2 | False | 18 | 6 | 12 | -0.333 | -0.766 | -1.797 | -0.063 |
| old_M2 | M1 | True | 52 | 20 | 32 | 0.231 | 0.497 | 0.064 | 1.105 |
| old_M2 | M2 | True | 27 | 15 | 12 | 0.100 | 0.826 | 0.057 | 1.945 |
| old_M2 | M3 | True | 60 | 10 | 50 | 0.200 | 0.449 | 0.058 | 0.959 |
| old_M3 | B1 | False | 32 | 10 | 22 | -0.282 | -0.445 | -1.051 | 0.006 |
| old_M3 | B2 | False | 31 | 10 | 21 | -0.267 | -0.440 | -1.071 | 0.030 |
| old_M3 | M1 | True | 21 | 8 | 13 | 0.365 | 0.290 | -0.173 | 0.786 |
| old_M3 | M2 | True | 19 | 8 | 11 | 0.386 | 0.329 | -0.186 | 0.840 |
| old_M3 | M3 | True | 31 | 4 | 27 | 0.370 | 0.143 | -0.066 | 0.344 |
| old_M4 | B1 | False | 9 | 3 | 6 | -0.500 | -0.278 | -0.693 | 0.222 |
| old_M4 | B2 | False | 8 | 3 | 5 | -0.467 | -0.241 | -0.710 | 0.303 |
| old_M4 | M1 | True | 18 | 13 | 5 | -0.154 | 0.216 | -0.100 | 0.537 |
| old_M4 | M2 | True | 15 | 11 | 4 | -0.182 | 0.212 | -0.108 | 0.525 |
| old_M4 | M3 | True | 10 | 7 | 3 | 0.190 | 0.356 | -0.336 | 1.138 |

## Interpretation

If an old rule has the same sign under AIPW and overlaps strongly with a current same-direction group, it is reproduced by the current causal scan. If the old rule does not keep its sign or overlaps weakly, it should be treated as an earlier associative phenotype rather than a confirmed causal subgroup.