# Sensibilidade por suporte comum

Os efeitos foram reestimados restringindo a amostra aos pacientes com propensity score dentro de faixas de suporte comum. As regras dos grupos nao foram alteradas.

| support | group | n | n_treated | n_control | unadjusted_diff | aipw_ate | aipw_att | overlap_weighted_diff | iptw_diff | estimable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| none | B1 | 151 | 46 | 105 | -0.259 | -0.309 | -0.223 | -0.236 | -0.276 | True |
| none | B2 | 117 | 35 | 82 | -0.288 | -0.347 | -0.328 | -0.272 | -0.292 | True |
| none | M1 | 328 | 141 | 187 | 0.165 | 0.240 | 0.203 | 0.171 | 0.199 | True |
| none | M2 | 109 | 52 | 57 | 0.273 | 0.449 | 0.355 | 0.286 | 0.345 | True |
| none | M3 | 219 | 37 | 182 | 0.182 | 0.305 | 0.339 | 0.275 | 0.289 | True |
| ps_0.05_0.95 | B1 | 151 | 46 | 105 | -0.259 | -0.309 | -0.223 | -0.236 | -0.276 | True |
| ps_0.05_0.95 | B2 | 117 | 35 | 82 | -0.288 | -0.347 | -0.328 | -0.272 | -0.292 | True |
| ps_0.05_0.95 | M1 | 328 | 141 | 187 | 0.165 | 0.240 | 0.203 | 0.171 | 0.199 | True |
| ps_0.05_0.95 | M2 | 109 | 52 | 57 | 0.273 | 0.449 | 0.355 | 0.286 | 0.345 | True |
| ps_0.05_0.95 | M3 | 219 | 37 | 182 | 0.182 | 0.305 | 0.339 | 0.275 | 0.289 | True |
| ps_0.10_0.90 | B1 | 101 | 44 | 57 | -0.211 | -0.326 | -0.219 | -0.209 | -0.196 | True |
| ps_0.10_0.90 | B2 | 79 | 34 | 45 | -0.239 | -0.452 | -0.329 | -0.252 | -0.239 | True |
| ps_0.10_0.90 | M1 | 256 | 136 | 120 | 0.168 | 0.253 | 0.244 | 0.173 | 0.196 | True |
| ps_0.10_0.90 | M2 | 97 | 50 | 47 | 0.274 | 0.422 | 0.460 | 0.269 | 0.304 | True |
| ps_0.10_0.90 | M3 | 85 | 34 | 51 | 0.176 | 0.431 | 0.362 | 0.297 | 0.307 | True |

## Interpretacao

A conclusao principal e considerada mais robusta quando o sinal do AIPW permanece o mesmo apos restricoes de suporte comum. Reducoes grandes de tamanho amostral devem ser interpretadas como possivel fragilidade de positividade.