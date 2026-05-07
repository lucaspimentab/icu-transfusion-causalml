# Inferencia Causal Temporal da Transfusao de Hemacias em UTI

> **Aviso metodologico:** as estimativas sao observacionais e dependem das hipoteses de ignorabilidade condicional, positividade e consistencia.


## 1. Introducao

Este relatorio descreve um pipeline reprodutivel para estimar efeitos causais medios, heterogeneos e contrafactuais da transfusao de concentrado de hemacias em pacientes criticos de UTI.

## 2. Motivacao Clinica

A transfusao de hemacias e uma intervencao frequente em UTI, mas seu efeito esperado pode variar conforme a trajetoria fisiologica pre-intervencao, a gravidade clinica e a reserva organica do paciente.

## 3. Problema de Pesquisa

O objetivo e estimar o efeito causal da transfusao sobre mortalidade e suporte organico, considerando covariaveis estaticas, series temporais pre-t0 e fenotipos fisiologicos latentes.

## 4. Hipoteses

A hipotese principal e que a transfusao nao possui efeito homogeneo em pacientes criticos. Fenotipos fisiologicos definidos por trajetorias temporais devem revelar subgrupos com beneficio, neutralidade ou risco associado.

## 5. Objetivos

- Estimar ATE e ATT para mortalidade.
- Estimar CATE por fenotipo temporal.
- Estimar ITE e riscos contrafactuais Y(1) e Y(0).
- Identificar variaveis pre-t0 que distinguem beneficio e risco.

## 6. Base de Dados e Coorte

Fonte dos dados: `legacy_cluster_transfusion`.
Numero de permanencias na coorte processada: 40167.
Numero de tratados/transfundidos: 10639.
Janela pre-intervencao: 48 horas.

## 7. Tratamento e Desfechos

Tratamento A=1 corresponde a primeira transfusao de hemacias. Para controles, foi definido pseudo-t0 pela distribuicao temporal dos tratados. O desfecho primario configurado e mortalidade.

## 8. DAG Causal Preliminar

```text
V -> X_t
V -> A
V -> Y
U -> X_t
U -> A
U -> Y
X_t -> A
X_t -> Y
A -> Y
X_t -> X_t+1
```

## 9. Metodologia

Esta execucao importou artefatos do pipeline anterior de fenotipagem/transfusao e executou as etapas novas de efeitos individuais, contrafactuais e avaliacao. As features foram importadas com colunas pos-t0/delta do estudo anterior; por isso esta execucao deve ser interpretada como reaproveitamento exato do artigo, nao como estimacao estritamente pre-tratamento.

## 10. Resultados Causais

| method | estimand | n_pairs | treated_mean | control_mean | effect | phenotype | source_file | ate | att | optional_library_available | n | cate_mean | cate_median | cate_sd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| legacy_nearest_neighbor_psm | ATT | 10009.0 | 0.3845539014886602 | 0.4456988710160855 | -0.0611449695274253 | nan | effect_estimates_psm.csv | nan | nan | nan | nan | nan | nan | nan |
| legacy_nearest_neighbor_psm | ATT_by_phenotype | 121.0 | 0.3553719008264462 | 0.4710743801652892 | -0.1157024793388429 | 0.0 | effect_estimates_psm.csv | nan | nan | nan | nan | nan | nan | nan |
| legacy_nearest_neighbor_psm | ATT_by_phenotype | 2936.0 | 0.4502724795640327 | 0.5006811989100818 | -0.050408719346049 | 1.0 | effect_estimates_psm.csv | nan | nan | nan | nan | nan | nan | nan |
| legacy_nearest_neighbor_psm | ATT_by_phenotype | 6952.0 | 0.357307249712313 | 0.4220368239355581 | -0.0647295742232451 | 2.0 | effect_estimates_psm.csv | nan | nan | nan | nan | nan | nan | nan |
| causal_forest_fallback_t_learner_gbdt | nan | nan | nan | nan | nan | nan | cate_estimates.csv | 0.0118924332617541 | -0.0029892725313927 | False | nan | nan | nan | nan |
| nan | nan | nan | nan | nan | nan | 0.0 | effect_by_phenotype.csv | nan | nan | nan | 137.0 | -0.0504806544564387 | -0.0230455049900191 | 0.1113560000357668 |
| nan | nan | nan | nan | nan | nan | 1.0 | effect_by_phenotype.csv | nan | nan | nan | 2991.0 | 0.0142151254426967 | 0.0100075560321486 | 0.1117619871174605 |
| nan | nan | nan | nan | nan | nan | 2.0 | effect_by_phenotype.csv | nan | nan | nan | 7511.0 | -0.0089740994541421 | 0.0034810276220263 | 0.0948570137922804 |

## 11. Efeitos por Fenotipo

| phenotype | n | cate_mean | cate_median | cate_sd |
| --- | --- | --- | --- | --- |
| 0.0 | 137.0 | -0.0504806544564387 | -0.0230455049900191 | 0.1113560000357668 |
| 1.0 | 2991.0 | 0.0142151254426967 | 0.0100075560321486 | 0.1117619871174605 |
| 2.0 | 7511.0 | -0.0089740994541421 | 0.0034810276220263 | 0.0948570137922804 |

## 12. Desempenho Preditivo

| auc | average_precision | brier_score | accuracy | precision | recall | f1 | split | n |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0.8692279987747926 | 0.7802336579755964 | 0.1347256303513503 | 0.808375034232081 | 0.7568653717347622 | 0.6053880300015307 | 0.6727048518093294 | all | 40167 |
| 0.8491704928068564 | 0.731502553866681 | 0.1453054119172189 | 0.7887870942043418 | 0.721749226006192 | 0.5708601163146617 | 0.6374978636130576 | test | 10042 |

## 13. Analise de Sensibilidade

_Nao disponivel._

## 14. Limitacoes

- PEHE real nao e observavel sem contrafactuais verdadeiros.
- Estimativas observacionais dependem de ausencia de confundimento nao medido.
- Positividade e suporte comum devem ser avaliados antes de interpretacao clinica.
- A execucao sintetica testa software, nao valida conclusoes clinicas.
- Quando colunas pos-t0/delta forem mantidas do pipeline anterior, os resultados de modelos individuais nao devem ser apresentados como inferencia causal pre-tratamento estrita.

## 15. Proximos Passos

- Corrigir ou ressincronizar os Parquets reais truncados.
- Validar definicoes finais de mortalidade em UTI versus hospitalar.
- Revisar lista clinica de covariaveis pre-tratamento.
- Adicionar analise semi-sintetica com efeito verdadeiro conhecido.
- Comparar janelas de 24h e 48h nos dados reais.

## 16. Referencias Principais

- Hernan MA, Robins JM. Causal Inference: What If.
- Athey S, Imbens G. Recursive partitioning for heterogeneous causal effects.
- Wager S, Athey S. Estimation and inference of heterogeneous treatment effects using random forests.
- Rubin DB. Estimating causal effects of treatments in randomized and nonrandomized studies.
