# Auditoria do Repositorio

Data da auditoria: 2026-05-04

## Objetivo

Esta auditoria registra o estado inicial do projeto antes da reorganizacao para um pipeline de inferencia causal temporal aplicado a transfusao de hemacias em UTI.

## Estrutura Observada

```text
configs/
  lab_itemids.yaml

dataset/
  README.md
  outputs_outcomes/
    outcomes_by_stay_full.csv
  timegrid_features/
    0/ ... 49/
      part-*.parquet
  _archive/
    legacy_pipeline/
      configs/
      scripts/
      src/

outputs/
  runs/
    run_cal03_replace_full_w48/
    run_cal03_noreplace_w48/

scripts/
  run_all.py
  run_overnight_w48.sh
  step0_build_outcomes_cohort.py
  step1_build_baseline_features.py
  step2_match_controls.py
  step3_embed_minirocket_temporal.py
  step4_embed_ts2vec_temporal.py
  step5_reports.py
  lib/
    duckdb_utils.py
    embedding.py
    embedding_features.py
    features.py
    logging_utils.py
    matching.py
    reporting.py
    schema_utils.py
    ts2vec.py
    utils.py
    validation.py

.gitignore
README.md
README_legacy_pipeline.md
```

Observacao: o diretorio atual nao possui metadados Git. O comando `git status --short` falhou com `fatal: not a git repository`.

## Arquivos Existentes

### Configuracao

- `configs/lab_itemids.yaml`: mapeamento de exames laboratoriais para itemids e expressoes de rotulo. E util para extracao em MIMIC-IV, mas nao configura o pipeline causal.
- Ausentes no estado inicial: `configs/config.yaml`, `configs/paths.yaml`, `configs/model_config.yaml`, `configs/causal_config.yaml`.

### Dados

- `dataset/outputs_outcomes/outcomes_by_stay_full.csv`: tabela de desfechos por permanencia em UTI. Possui 40.167 linhas e 8 colunas:
  - `stay_id`
  - `mortality_anytime`
  - `vm_time_hours`
  - `rrt_on`
  - `any_vasopressor`
  - `nee_mcgkgmin_max`
  - `icu_los_hours`
  - `ventilation_hours`
- `dataset/outputs_outcomes/outcomes_by_stay.csv`: referenciado pelo README e por scripts, mas ausente.
- `dataset/timegrid_features/`: dataset temporal particionado. Foram encontrados 56 arquivos `*.parquet` em 50 subpastas.
- `dataset/_archive/legacy_pipeline/`: pipeline antigo preservado como referencia.

### Scripts Ativos

- `scripts/run_all.py`: orquestra o pipeline antigo em etapas 0 a 5 para janelas 24/48/72h.
- `scripts/step0_build_outcomes_cohort.py`: cria coorte de desfechos e flag de transfusao usando DuckDB.
- `scripts/step1_build_baseline_features.py`: cria tabela `t0` e features agregadas pre/post `t0`.
- `scripts/step2_match_controls.py`: aplica propensity score matching 1:N e calcula balanceamento.
- `scripts/step3_embed_minirocket_temporal.py`: cria embeddings temporais MiniRocket-like para pacientes transfundidos.
- `scripts/step4_embed_ts2vec_temporal.py`: cria embeddings TS2Vec-like com PyTorch para pacientes transfundidos.
- `scripts/step5_reports.py`: clusteriza embeddings e gera comparacoes transfundido-controle por cluster.
- `scripts/run_overnight_w48.sh`: executa duas rodadas w48 com e sem reposicao de controles.

### Utilitarios

- `scripts/lib/duckdb_utils.py`: conexao DuckDB e profiling.
- `scripts/lib/schema_utils.py`: inferencia de colunas de identificador, tempo, transfusao e desfechos.
- `scripts/lib/features.py`: construcao de `t0` e agregacoes basais.
- `scripts/lib/matching.py`: selecao de covariaveis, regressao logistica de propensity score, PSM e SMD.
- `scripts/lib/embedding.py`: MiniRocketLite e matriz temporal.
- `scripts/lib/embedding_features.py`: selecao de variaveis temporais para embedding e missingness.
- `scripts/lib/ts2vec.py`: encoder convolucional contrastivo simplificado.
- `scripts/lib/logging_utils.py`: logs JSONL e formatter.
- `scripts/lib/utils.py`: caminhos de outputs e `RUN_ID`.
- `scripts/lib/validation.py`: validacoes simples de pareamento e SMD.
- `scripts/lib/reporting.py`: resumo simples de outcomes; parece subutilizado.

### Pipeline Legado

`dataset/_archive/legacy_pipeline/` contem um pipeline completo anterior para extracao/engenharia de dados, com destaque para:

- `run_pipeline.py`: ponto de entrada com conexao Postgres hardcoded.
- `src/pipeline_unified.py`: pipeline monolitico com mais de 2.400 linhas.
- `src/impute.py`: imputacao por chunks e forward fill.
- `src/features/*.py`: subqueries para demografia, comorbidades, exames, sinais vitais, terapias, transfusao e escores.
- `scripts/cluster_tabular.py`, `cluster_ts2vec.py`, `analyze_clusters.py`: fenotipagem e analises antigas.

Esse conteudo deve ser tratado como referencia, nao como pipeline ativo.

## Problemas Encontrados

1. O projeto nao e um repositorio Git no diretorio atual.
2. O README inicial esta desatualizado:
   - cita `outputs/schema_report.txt`, mas o pipeline atual grava em `outputs/runs/<run_id>/shared/schema_report.txt`;
   - cita scripts inexistentes, como `step3_cluster_transfused_tabular.py` e `step4_embed_and_cluster_transfused_temporal.py`.
3. Ha ausencia de arquivos de configuracao para causal ML.
4. Ha ausencia de `requirements.txt` e `environment.yml`.
5. Ha ausencia dos modulos `dataset/load_data.py`, `dataset/preprocess.py`, `dataset/build_cohort.py`, `dataset/time_anchor.py` e `dataset/feature_engineering.py`.
6. O pipeline antigo tem risco de vazamento temporal:
   - `scripts/lib/features.py` cria `*_post_mean` e `*_delta` usando dados apos `t0`;
   - `scripts/lib/matching.py` pode selecionar essas colunas como covariaveis para pareamento.
7. `scripts/step5_reports.py` remove outputs antigos com `unlink`; a nova versao deve evitar apagar resultados sem backup.
8. `dataset/_archive/legacy_pipeline/run_pipeline.py` contem credenciais Postgres hardcoded.
9. Ha duplicacao funcional entre `scripts/` e `dataset/_archive/legacy_pipeline/`.
10. Ha arquivos `__pycache__` e `.pyc` dentro do diretorio.
11. Dados Parquet locais parecem incompletos/corrompidos:
    - 56 arquivos Parquet foram encontrados em `dataset/timegrid_features/`;
    - apenas 6 puderam ser lidos com sucesso;
    - 50 falharam com `Parquet magic bytes not found in footer`;
    - os arquivos invalidos tem tamanho identico de 14 MiB, sugerindo truncamento ou sincronizacao parcial.
12. Arquivos `baseline_features.parquet` em outputs de execucoes anteriores tambem falharam como Parquet invalido.

## Dependencias

### Instaladas no ambiente inspecionado

- pandas
- numpy
- scikit-learn
- matplotlib
- scipy
- PyYAML
- duckdb
- pyarrow
- torch
- seaborn

### Ausentes

- sktime
- econml
- causalml

O novo pipeline deve usar fallbacks com scikit-learn quando bibliotecas opcionais nao estiverem disponiveis.

## Organizacao Proposta

```text
configs/
  config.yaml
  paths.yaml
  model_config.yaml
  causal_config.yaml
  lab_itemids.yaml

dataset/
  __init__.py
  load_data.py
  build_cohort.py
  time_anchor.py
  preprocess.py
  feature_engineering.py

scripts/
  run_all.py
  run_all_legacy.py
  01_temporal_representation.py
  02_clustering.py
  03_cluster_analysis.py
  04_propensity_score.py
  05_matching_weighting.py
  06_balance_diagnostics.py
  07_cate_meta_learners.py
  08_causal_forest.py
  09_heterogeneous_effects.py
  10_counterfactual_model.py
  11_counterfactual_evaluation.py
  12_evaluation.py
  13_sensitivity_analysis.py
  14_generate_report.py
  causal_utils.py
  pipeline_common.py

outputs/
  processed/
  phenotypes/
  causal/
  counterfactual/
  evaluation/
  figures/
  logs/
```

## Principios Para a Nova Implementacao

- Manter compatibilidade com dados reais via CSV, Parquet ou Pickle.
- Usar dados sinteticos pequenos por padrao quando dados reais estiverem ausentes ou invalidos.
- Marcar explicitamente resultados sinteticos como demonstrativos.
- Nao usar informacao apos `t0` em features pre-tratamento.
- Salvar tabelas intermediarias padronizadas em `outputs/processed/`.
- Implementar metodos avancados com fallback quando dependencias opcionais nao existirem.
- Evitar caminhos absolutos.
- Usar `pathlib`.
- Preservar scripts antigos e outputs anteriores.

## Scripts a Criar ou Ajustar

- Criar:
  - `dataset/load_data.py`
  - `dataset/build_cohort.py`
  - `dataset/time_anchor.py`
  - `dataset/preprocess.py`
  - `dataset/feature_engineering.py`
  - `scripts/pipeline_common.py`
  - `scripts/causal_utils.py`
  - `scripts/01_temporal_representation.py` a `scripts/14_generate_report.py`
  - `requirements.txt`
  - `environment.yml`
- Ajustar:
  - `scripts/run_all.py`
  - `README.md`
- Preservar:
  - `scripts/run_all_legacy.py`
  - `README_legacy_pipeline.md`
  - `dataset/_archive/legacy_pipeline/`

## Status Inicial

O projeto possui material valioso do estudo anterior, especialmente a criacao de timegrid, embeddings temporais, PSM e analise por clusters. Contudo, a arquitetura atual ainda nao atende ao objetivo de inferencia causal temporal reprodutivel com CATE, ITE, contrafactuais e avaliacao formal. A nova implementacao deve iniciar por uma versao minima funcional com dados sinteticos e manter pontos de entrada estaveis para dados reais assim que os arquivos locais forem corrigidos ou substituidos.
