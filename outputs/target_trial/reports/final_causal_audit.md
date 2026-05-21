# Auditoria final de consistencia causal

## Arquivos usados

| path | exists | size_bytes | mtime_utc_epoch | sha256 |
| --- | --- | --- | --- | --- |
| outputs\target_trial\causal\main_effects.csv | True | 811 | 1778626077.071 | e492f0ec43a942ae7fec3146a93c95e399324db58bc0b5308a69674ac18cbbfa |
| outputs\target_trial\final_groups\final_group_effects.csv | True | 15469 | 1778791507.389 | aa9bd57d941b5704e1e5c112f0fa8cdc72093dc35c42a1b7980addcfcda0a103 |
| outputs\target_trial\final_groups\final_group_profiles.csv | True | 4896 | 1778791507.412 | 3e73daa051396ec1c101e66f9dd308c44461481abc90a4f4dba134859c285478 |
| outputs\target_trial\final_groups\final_group_balance.csv | True | 1532 | 1778791507.396 | 4e4029a736f68deb2b31da36c72350c64717da6720bcaad55dfe8273f0da474e |
| outputs\target_trial\legacy_crosswalk\legacy_crosswalk_report.md | True | 9561 | 1778792745.387 | 352d6faf942c1c68b06f87c4d1514b3671283705e95f3ec839c5b71b6498ad77 |
| outputs\target_trial\legacy_rule_crosswalk\run_cal03_noreplace_w48\legacy_rule_scan_crosswalk_report.md | True | 6545 | 1778793140.407 | 8ea161ab9e27292e84f4a09b9eadc12eee18feaa0755f1c6d5b1360194f06d97 |
| outputs\target_trial\legacy_rule_crosswalk\run_cal03_replace_full_w48\legacy_rule_scan_crosswalk_report.md | True | 6545 | 1778793140.411 | 8ea161ab9e27292e84f4a09b9eadc12eee18feaa0755f1c6d5b1360194f06d97 |

## Vazamento temporal

- Numero de features usadas no target trial: `102`.
- Features com padrao pos-t0 (`post`, `after`, `future`): `[]`.
- Features que coincidem exatamente com tratamento/desfechos: `[]`.
- Conclusao: nao foi detectado uso nominal de feature pos-t0 nos metadados atuais. Variaveis `*_delta` sao interpretadas como deltas dentro da janela pre-t0.

## Tratamento versus grupos

- Tratamento causal: `transfused`.
- Grupos finais: B1, B2, M1, M2, M3.
- Os grupos foram usados como estratos de heterogeneidade, nao como tratamento.

## Direcao dos efeitos finais

| group | direction_consistent |
| --- | --- |
| B1 | True |
| B2 | True |
| M1 | True |
| M2 | True |
| M3 | True |

## Suporte comum

| support | group | n | n_treated | n_control | aipw_ate | estimable |
| --- | --- | --- | --- | --- | --- | --- |
| none | B1 | 151 | 46 | 105 | -0.309 | True |
| none | B2 | 117 | 35 | 82 | -0.347 | True |
| none | M1 | 328 | 141 | 187 | 0.240 | True |
| none | M2 | 109 | 52 | 57 | 0.449 | True |
| none | M3 | 219 | 37 | 182 | 0.305 | True |
| ps_0.05_0.95 | B1 | 151 | 46 | 105 | -0.309 | True |
| ps_0.05_0.95 | B2 | 117 | 35 | 82 | -0.347 | True |
| ps_0.05_0.95 | M1 | 328 | 141 | 187 | 0.240 | True |
| ps_0.05_0.95 | M2 | 109 | 52 | 57 | 0.449 | True |
| ps_0.05_0.95 | M3 | 219 | 37 | 182 | 0.305 | True |
| ps_0.10_0.90 | B1 | 101 | 44 | 57 | -0.326 | True |
| ps_0.10_0.90 | B2 | 79 | 34 | 45 | -0.452 | True |
| ps_0.10_0.90 | M1 | 256 | 136 | 120 | 0.253 | True |
| ps_0.10_0.90 | M2 | 97 | 50 | 47 | 0.422 | True |
| ps_0.10_0.90 | M3 | 85 | 34 | 51 | 0.431 | True |

## Concordancia de estimadores

| group | direction | aipw_ate | att | overlap_weighted_diff | iptw_diff | all_estimators_same_sign | all_estimators_match_expected_direction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B1 | benefit | -0.309 | -0.223 | -0.236 | -0.276 | True | True |
| B2 | benefit | -0.347 | -0.328 | -0.272 | -0.292 | True | True |
| M1 | harm | 0.240 | 0.203 | 0.171 | 0.199 | True | True |
| M2 | harm | 0.449 | 0.355 | 0.286 | 0.345 | True | True |
| M3 | harm | 0.305 | 0.339 | 0.275 | 0.289 | True | True |

## Linguagem causal

- A secao final usa `efeito estimado`, `observacional`, `gerador de hipotese` e evita afirmar causalidade definitiva.
- A conclusao principal mantida e: efeito global fraco/nao significativo, heterogeneidade forte, beneficio em B1/B2 e maleficio em M1/M2/M3.

## Resultado da auditoria

A auditoria nao encontrou mudanca de grupos, busca adicional de subgrupos ou uso de arquivos fora dos resultados finais especificados. Os materiais gerados devem ser usados como consolidacao final da inferencia causal.