# Concordancia entre estimadores

Foram comparados AIPW ATE, ATT, IPTW e overlap weighted difference. A narrativa principal e mais forte quando todos os estimadores apontam na direcao esperada.

| group | direction | aipw_ate | att | overlap_weighted_diff | iptw_diff | all_estimators_same_sign | all_estimators_match_expected_direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | benefit | -0.309 | -0.223 | -0.236 | -0.276 | True | True |
| B2 | benefit | -0.347 | -0.328 | -0.272 | -0.292 | True | True |
| M1 | harm | 0.240 | 0.203 | 0.171 | 0.199 | True | True |
| M2 | harm | 0.449 | 0.355 | 0.286 | 0.345 | True | True |
| M3 | harm | 0.305 | 0.339 | 0.275 | 0.289 | True | True |

## Conclusao

B1/B2 mantem sinal negativo em todos os estimadores. M1/M2/M3 mantem sinal positivo em todos os estimadores. Isso fortalece a evidencia de heterogeneidade, apesar das limitacoes observacionais e de balanceamento residual.