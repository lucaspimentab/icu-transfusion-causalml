# Interpretacao do balanceamento dos grupos finais

## B1

- SMD medio absoluto apos overlap weighting: `0.157`.
- SMD maximo absoluto apos overlap weighting: `0.426`.
- Variaveis com SMD > 0.1: `62`.
- Avaliacao qualitativa: **fragil**.
- Impacto na confianca causal: Ha desequilibrio residual relevante; o sinal causal estimado e informativo, mas a confianca e reduzida por possivel confundimento residual.

Variaveis mais desequilibradas:

| feature | smd_overlap |
| --- | --- |
| ventilation_on_std | -0.426 |
| mbp_delta | 0.417 |
| ventilation_on_max | -0.412 |
| any_vasopressor_delta | 0.392 |
| lactate_delta | -0.385 |
| any_vasopressor_slope | 0.378 |
| spo2_last | 0.351 |
| ventilation_on_delta | 0.339 |
| lactate_slope | -0.325 |
| any_vasopressor_max | -0.316 |
| any_vasopressor_mean | -0.310 |
| ventilation_on_slope | 0.308 |
| heart_rate_max | -0.296 |
| any_vasopressor_std | -0.295 |
| spo2_first | 0.293 |

Resumo original do arquivo final_group_balance.csv: `ventilation_on_std:-0.426; mbp_delta:0.417; ventilation_on_max:-0.412; any_vasopressor_delta:0.392; lactate_delta:-0.385`.

## B2

- SMD medio absoluto apos overlap weighting: `0.173`.
- SMD maximo absoluto apos overlap weighting: `0.590`.
- Variaveis com SMD > 0.1: `62`.
- Avaliacao qualitativa: **fragil**.
- Impacto na confianca causal: Ha desequilibrio residual relevante; o sinal causal estimado e informativo, mas a confianca e reduzida por possivel confundimento residual.

Variaveis mais desequilibradas:

| feature | smd_overlap |
| --- | --- |
| lactate_slope | -0.590 |
| lactate_delta | -0.537 |
| spo2_std | 0.527 |
| spo2_min | -0.473 |
| lactate_min | 0.466 |
| any_vasopressor_delta | 0.432 |
| lactate_first | 0.387 |
| any_vasopressor_slope | 0.368 |
| mbp_delta | 0.362 |
| mbp_max | 0.357 |
| ventilation_on_std | -0.341 |
| spo2_last | 0.329 |
| resp_rate_mean | 0.323 |
| resp_rate_median | 0.307 |
| ventilation_on_slope | 0.300 |

Resumo original do arquivo final_group_balance.csv: `lactate_slope:-0.590; lactate_delta:-0.537; spo2_std:0.527; spo2_min:-0.473; lactate_min:0.466`.

## M1

- SMD medio absoluto apos overlap weighting: `0.080`.
- SMD maximo absoluto apos overlap weighting: `0.279`.
- Variaveis com SMD > 0.1: `28`.
- Avaliacao qualitativa: **moderado**.
- Impacto na confianca causal: Ha algum desequilibrio residual, mas o grupo mantem suporte interpretavel; a inferencia deve ser lida com cautela moderada.

Variaveis mais desequilibradas:

| feature | smd_overlap |
| --- | --- |
| mbp_min | -0.279 |
| resp_rate_min | -0.234 |
| lactate_delta | 0.229 |
| lactate_median | -0.218 |
| any_vasopressor_last | 0.217 |
| heart_rate_slope | -0.208 |
| lactate_last | 0.206 |
| any_vasopressor_delta | 0.204 |
| lactate_mean | -0.192 |
| mbp_delta | -0.190 |
| spo2_std | 0.164 |
| mbp_last | -0.161 |
| hemoglobin_max | 0.159 |
| hemoglobin_first | 0.157 |
| ventilation_on_min | -0.155 |

Resumo original do arquivo final_group_balance.csv: `mbp_min:-0.279; resp_rate_min:-0.234; lactate_delta:0.229; lactate_median:-0.218; any_vasopressor_last:0.217`.

## M2

- SMD medio absoluto apos overlap weighting: `0.147`.
- SMD maximo absoluto apos overlap weighting: `0.501`.
- Variaveis com SMD > 0.1: `57`.
- Avaliacao qualitativa: **fragil**.
- Impacto na confianca causal: Ha desequilibrio residual relevante; o sinal causal estimado e informativo, mas a confianca e reduzida por possivel confundimento residual.

Variaveis mais desequilibradas:

| feature | smd_overlap |
| --- | --- |
| age | -0.501 |
| hemoglobin_median | 0.428 |
| mbp_mean | 0.421 |
| mbp_median | 0.377 |
| lactate_delta | 0.366 |
| lactate_last | 0.363 |
| hemoglobin_mean | 0.363 |
| any_vasopressor_median | 0.348 |
| resp_rate_delta | -0.336 |
| mbp_first | 0.319 |
| resp_rate_min | -0.307 |
| resp_rate_std | 0.305 |
| any_vasopressor_last | 0.299 |
| any_vasopressor_delta | 0.295 |
| resp_rate_last | -0.288 |

Resumo original do arquivo final_group_balance.csv: `age:-0.501; hemoglobin_median:0.428; mbp_mean:0.421; mbp_median:0.377; lactate_delta:0.366`.

## M3

- SMD medio absoluto apos overlap weighting: `0.139`.
- SMD maximo absoluto apos overlap weighting: `0.785`.
- Variaveis com SMD > 0.1: `47`.
- Avaliacao qualitativa: **fragil**.
- Impacto na confianca causal: Ha desequilibrio residual relevante; o sinal causal estimado e informativo, mas a confianca e reduzida por possivel confundimento residual.

Variaveis mais desequilibradas:

| feature | smd_overlap |
| --- | --- |
| any_vasopressor_delta | 0.785 |
| hemoglobin_std | 0.557 |
| any_vasopressor_first | -0.509 |
| any_vasopressor_last | 0.474 |
| mbp_delta | -0.405 |
| spo2_min | -0.372 |
| lactate_max | 0.368 |
| spo2_std | 0.356 |
| mbp_min | -0.348 |
| any_vasopressor_slope | 0.338 |
| lactate_slope | -0.336 |
| lactate_std | 0.335 |
| mbp_last | -0.335 |
| sofa_std | 0.319 |
| lactate_last | 0.290 |

Resumo original do arquivo final_group_balance.csv: `any_vasopressor_delta:0.785; hemoglobin_std:0.557; any_vasopressor_first:-0.509; any_vasopressor_last:0.474; mbp_delta:-0.405`.
