# Legacy K=2 phenotype crosswalk and causal inference

## Objective

This analysis treats the MiniRocket/K-means K=2 phenotypes from the previous cluster-transfusion project as pre-specified physiologic groups. It then estimates doubly robust causal effects inside those groups and crosses them with the final scan-derived groups B1/B2/M1/M2/M3.

The goal is not to relabel the old clusters as causal groups. The goal is to test whether the new causal groups are concentrated inside the old physiologic phenotypes and whether the old phenotypes still separate treatment effect in the target-trial cohort.

## Key findings

1. The old K=2 phenotypes do not separate a clear causal benefit/harm effect in the target-trial cohort. Their AIPW estimates are close to zero or have confidence intervals crossing zero.
2. The final benefit group B1 is not enriched in the old benefit-like K=2 cluster beyond the cohort baseline. In both legacy runs, around 93-94% of B1 falls in cluster 1, but 93-94% of the whole target-trial cohort also falls in cluster 1.
3. The final harm groups are not simply the old harm cluster. M1 has only a weak tendency toward the smaller old cluster in the no-replacement run, and M3 is actually enriched in cluster 1, which is the lower-hemoglobin/higher-SOFA macrocluster.
4. The important result is inside-cluster separation: within old cluster 1, B1 remains beneficial while M1/M2/M3 remain harmful. This supports the interpretation that the scan-derived groups refine the old physiologic phenotype rather than reproduce it.

## Within old cluster 1: final groups still separate effect

| run_id | group_id | legacy_k2_cluster | n | n_treated | n_control | unadjusted_diff | aipw_ate | aipw_ate_ci95_low | aipw_ate_ci95_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| run_cal03_replace_full_w48 | B1 | 1 | 142 | 43 | 99 | -0.252 | -0.300 | -0.533 | -0.088 |
| run_cal03_replace_full_w48 | B2 | 1 | 109 | 32 | 77 | -0.288 | -0.342 | -0.580 | -0.132 |
| run_cal03_replace_full_w48 | M1 | 1 | 305 | 126 | 179 | 0.186 | 0.244 | 0.101 | 0.388 |
| run_cal03_replace_full_w48 | M2 | 1 | 101 | 47 | 54 | 0.279 | 0.415 | 0.100 | 0.750 |
| run_cal03_replace_full_w48 | M3 | 1 | 217 | 36 | 181 | 0.169 | 0.289 | 0.099 | 0.500 |
| run_cal03_noreplace_w48 | B1 | 1 | 141 | 42 | 99 | -0.247 | -0.300 | -0.537 | -0.091 |
| run_cal03_noreplace_w48 | B2 | 1 | 109 | 32 | 77 | -0.288 | -0.342 | -0.580 | -0.132 |
| run_cal03_noreplace_w48 | M1 | 1 | 299 | 124 | 175 | 0.179 | 0.242 | 0.092 | 0.391 |
| run_cal03_noreplace_w48 | M2 | 1 | 101 | 47 | 54 | 0.279 | 0.415 | 0.100 | 0.750 |
| run_cal03_noreplace_w48 | M3 | 1 | 217 | 36 | 181 | 0.169 | 0.289 | 0.099 | 0.500 |

## AIPW estimates inside old K=2 phenotypes

| run_id | split | legacy_k2_cluster | legacy_article_sign | article_mortality_diff | n | n_treated | n_control | unadjusted_diff | aipw_ate | aipw_ate_ci95_low | aipw_ate_ci95_high | aipw_att | overlap_weighted_diff |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| run_cal03_replace_full_w48 | all | 0 | article_benefit | -0.066 | 85 | 43 | 42 | -0.128 | -0.021 | -0.639 | 0.629 | -0.068 | -0.163 |
| run_cal03_replace_full_w48 | all | 1 | article_benefit | -0.050 | 1399 | 463 | 936 | -0.002 | 0.043 | -0.021 | 0.107 | 0.076 | 0.026 |
| run_cal03_noreplace_w48 | all | 0 | article_harm | 0.012 | 99 | 50 | 49 | -0.089 | 0.001 | -0.557 | 0.572 | -0.057 | -0.152 |
| run_cal03_noreplace_w48 | all | 1 | article_benefit | -0.027 | 1385 | 456 | 929 | -0.003 | 0.042 | -0.023 | 0.107 | 0.077 | 0.029 |

## Crosswalk between final groups and old K=2 phenotypes

| run_id | group_id | legacy_k2_cluster | n_in_group_cluster | n_group | pct_group_in_cluster | pct_target_trial_in_cluster | article_mortality_diff | legacy_article_sign | fisher_or_cluster1_vs_cluster0 | fisher_p_cluster1_vs_cluster0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| run_cal03_replace_full_w48 | B1 | 0 | 9 | 151 | 0.060 | 0.057 | -0.066 | article_benefit | 0.954 | 0.854 |
| run_cal03_replace_full_w48 | B1 | 1 | 142 | 151 | 0.940 | 0.943 | -0.050 | article_benefit | 0.954 | 0.854 |
| run_cal03_replace_full_w48 | B2 | 0 | 8 | 117 | 0.068 | 0.057 | -0.066 | article_benefit | 0.813 | 0.536 |
| run_cal03_replace_full_w48 | B2 | 1 | 109 | 117 | 0.932 | 0.943 | -0.050 | article_benefit | 0.813 | 0.536 |
| run_cal03_replace_full_w48 | M1 | 0 | 23 | 328 | 0.070 | 0.057 | -0.066 | article_benefit | 0.752 | 0.281 |
| run_cal03_replace_full_w48 | M1 | 1 | 305 | 328 | 0.930 | 0.943 | -0.050 | article_benefit | 0.752 | 0.281 |
| run_cal03_replace_full_w48 | M2 | 0 | 8 | 109 | 0.073 | 0.057 | -0.066 | article_benefit | 0.749 | 0.396 |
| run_cal03_replace_full_w48 | M2 | 1 | 101 | 109 | 0.927 | 0.943 | -0.050 | article_benefit | 0.749 | 0.396 |
| run_cal03_replace_full_w48 | M3 | 0 | 2 | 219 | 0.009 | 0.057 | -0.066 | article_benefit | 7.619 | 0.000 |
| run_cal03_replace_full_w48 | M3 | 1 | 217 | 219 | 0.991 | 0.943 | -0.050 | article_benefit | 7.619 | 0.000 |
| run_cal03_noreplace_w48 | B1 | 0 | 10 | 151 | 0.066 | 0.067 | 0.012 | article_harm | 1.009 | 1.000 |
| run_cal03_noreplace_w48 | B1 | 1 | 141 | 151 | 0.934 | 0.933 | -0.027 | article_benefit | 1.009 | 1.000 |
| run_cal03_noreplace_w48 | B2 | 0 | 8 | 117 | 0.068 | 0.067 | 0.012 | article_harm | 0.972 | 0.848 |
| run_cal03_noreplace_w48 | B2 | 1 | 109 | 117 | 0.932 | 0.933 | -0.027 | article_benefit | 0.972 | 0.848 |
| run_cal03_noreplace_w48 | M1 | 0 | 29 | 328 | 0.088 | 0.067 | 0.012 | article_harm | 0.665 | 0.080 |
| run_cal03_noreplace_w48 | M1 | 1 | 299 | 328 | 0.912 | 0.933 | -0.027 | article_benefit | 0.665 | 0.080 |
| run_cal03_noreplace_w48 | M2 | 0 | 8 | 109 | 0.073 | 0.067 | 0.012 | article_harm | 0.895 | 0.692 |
| run_cal03_noreplace_w48 | M2 | 1 | 101 | 109 | 0.927 | 0.933 | -0.027 | article_benefit | 0.895 | 0.692 |
| run_cal03_noreplace_w48 | M3 | 0 | 2 | 219 | 0.009 | 0.067 | 0.012 | article_harm | 9.011 | 0.000 |
| run_cal03_noreplace_w48 | M3 | 1 | 217 | 219 | 0.991 | 0.933 | -0.027 | article_benefit | 9.011 | 0.000 |

## AIPW estimates inside intersections

| run_id | group_id | legacy_k2_cluster | n | n_treated | n_control | unadjusted_diff | aipw_ate | aipw_ate_ci95_low | aipw_ate_ci95_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| run_cal03_replace_full_w48 | B1 | 0 | 9 | 3 | 6 | -0.333 | -0.456 | -0.973 | -0.043 |
| run_cal03_replace_full_w48 | B1 | 1 | 142 | 43 | 99 | -0.252 | -0.300 | -0.533 | -0.088 |
| run_cal03_replace_full_w48 | B2 | 0 | 8 | 3 | 5 | -0.200 | -0.410 | -0.994 | 0.036 |
| run_cal03_replace_full_w48 | B2 | 1 | 109 | 32 | 77 | -0.288 | -0.342 | -0.580 | -0.132 |
| run_cal03_replace_full_w48 | M1 | 0 | 23 | 15 | 8 | -0.042 | 0.187 | -0.308 | 0.856 |
| run_cal03_replace_full_w48 | M1 | 1 | 305 | 126 | 179 | 0.186 | 0.244 | 0.101 | 0.388 |
| run_cal03_replace_full_w48 | M2 | 0 | 8 | 5 | 3 | 0.267 | 0.879 | -0.310 | 2.453 |
| run_cal03_replace_full_w48 | M2 | 1 | 101 | 47 | 54 | 0.279 | 0.415 | 0.100 | 0.750 |
| run_cal03_replace_full_w48 | M3 | 0 | 2 | 1 | 1 | 1.000 | 2.048 | 0.996 | 3.099 |
| run_cal03_replace_full_w48 | M3 | 1 | 217 | 36 | 181 | 0.169 | 0.289 | 0.099 | 0.500 |
| run_cal03_noreplace_w48 | B1 | 0 | 10 | 4 | 6 | -0.333 | -0.434 | -0.884 | -0.057 |
| run_cal03_noreplace_w48 | B1 | 1 | 141 | 42 | 99 | -0.247 | -0.300 | -0.537 | -0.091 |
| run_cal03_noreplace_w48 | B2 | 0 | 8 | 3 | 5 | -0.200 | -0.410 | -0.994 | 0.036 |
| run_cal03_noreplace_w48 | B2 | 1 | 109 | 32 | 77 | -0.288 | -0.342 | -0.580 | -0.132 |
| run_cal03_noreplace_w48 | M1 | 0 | 29 | 17 | 12 | 0.103 | 0.222 | -0.181 | 0.757 |
| run_cal03_noreplace_w48 | M1 | 1 | 299 | 124 | 175 | 0.179 | 0.242 | 0.092 | 0.391 |
| run_cal03_noreplace_w48 | M2 | 0 | 8 | 5 | 3 | 0.267 | 0.879 | -0.310 | 2.453 |
| run_cal03_noreplace_w48 | M2 | 1 | 101 | 47 | 54 | 0.279 | 0.415 | 0.100 | 0.750 |
| run_cal03_noreplace_w48 | M3 | 0 | 2 | 1 | 1 | 1.000 | 2.048 | 0.996 | 3.099 |
| run_cal03_noreplace_w48 | M3 | 1 | 217 | 36 | 181 | 0.169 | 0.289 | 0.099 | 0.500 |

## Old phenotype profile medians

| run_id | legacy_k2_cluster | age_max | creatinine_mean | heart_rate_mean | hemoglobin_mean | lactate_mean | mbp_mean | sofa_mean |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| run_cal03_replace_full_w48 | 0 | 69.000 | 0.900 | 76.000 | 11.629 | 1.283 | 83.667 | 3.000 |
| run_cal03_replace_full_w48 | 1 | 68.000 | 1.087 | 87.946 | 8.822 | 1.420 | 73.731 | 4.807 |
| run_cal03_noreplace_w48 | 0 | 69.000 | 0.900 | 76.075 | 11.618 | 1.282 | 83.667 | 3.000 |
| run_cal03_noreplace_w48 | 1 | 68.000 | 1.098 | 87.939 | 8.817 | 1.425 | 73.649 | 4.847 |

## Interpretation

In this target-trial cohort, the old K=2 phenotypes are broad physiologic macrophenotypes. Most eligible patients fall into the same old K=2 cluster because the target trial selects a narrower hemoglobin-eligible population than the original matched cohort.

Therefore, the final scan-derived groups should be interpreted as causal refinements inside the physiologic space identified by the previous paper, not as exact reproductions of the old clusters.

A strong bridge would require B1/B2 to be enriched in an old benefit phenotype and M1/M2/M3 to be enriched in an old harm phenotype. If enrichment is weak or absent, the conclusion is that K=2 was too coarse for the causal question and the rule-based target-trial groups provide finer heterogeneity.