# VCIP-lite: planejamento contrafactual variacional

Este modulo e uma analise experimental inspirada em VCIP. Ele nao substitui AIPW/target trial como resultado principal.

## Definicao

- Historico: features fisiologicas pre-t0.
- Intervencao: `A=1` transfundir versus `A=0` nao transfundir.
- Alvo: `Y=0`, isto e, sobrevivencia/ausencia de mortalidade.
- Quantidade estimada: `P(Y=0 | do(A=a), X)` para `a in {0,1}`.
- Modelo: encoder variacional para estado latente `z`, cabeca de tratamento, cabeca de outcome e reconstrucao de `X`.
- Heterogeneidade: o decoder de outcome inclui interacoes `A x X` e `A x z`.
- Ajuste observacional: a perda de outcome usa ponderacao por propensity score ja estimado no target trial.
- Escopo: esta e uma adaptacao binaria e exploratoria inspirada em VCIP, nao uma reproducao completa do planejamento sequencial do artigo original.

## Performance preditiva observada

| split | n | brier | auc | average_precision |
| --- | --- | --- | --- | --- |
| all | 1484 | 0.180 | 0.804 | 0.769 |
| discovery | 1023 | 0.170 | 0.829 | 0.799 |
| validation | 461 | 0.202 | 0.747 | 0.707 |

## Efeito contrafactual medio

No conjunto completo, o VCIP-lite estimou ATE medio de mortalidade de `0.023`.
Valores negativos favorecem transfusao; valores positivos favorecem nao transfusao.

## Grupos finais

| group | n | vcip_ate_mortality | vcip_ate_ci_low | vcip_ate_ci_high | mean_target_advantage_survival | fraction_recommend_transfusion |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | 151 | -0.093 | -0.109 | -0.077 | 0.093 | 0.834 |
| B2 | 117 | -0.115 | -0.130 | -0.099 | 0.115 | 0.880 |
| M1 | 328 | 0.068 | 0.056 | 0.080 | -0.068 | 0.357 |
| M2 | 109 | 0.143 | 0.126 | 0.161 | -0.143 | 0.092 |
| M3 | 219 | 0.075 | 0.064 | 0.088 | -0.075 | 0.251 |

## Interpretacao

A leitura correta e probabilistica: para pacientes com covariaveis semelhantes, o modelo estima maior ou menor chance de atingir o alvo de sobrevivencia sob cada intervencao.
Como se trata de modelo neural variacional treinado em dados observacionais, os resultados devem ser descritos como exploratorios e geradores de hipotese.

Em relacao ao AIPW principal, o VCIP-lite preserva a direcao dos grupos finais, mas apresenta magnitudes mais atenuadas. Isso e esperado: o AIPW e o estimador causal primario; o VCIP-lite e usado aqui como apoio contrafactual individual e planejamento de alvo.