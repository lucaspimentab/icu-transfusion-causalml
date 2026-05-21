# Diagnosticos causais finais

Este diretorio contem as tabelas pedidas para fortalecer a secao de inferencia causal.

## Arquivos principais

- `temporal_leakage_check.csv`
- `smd_balance_summary.csv`
- `positivity_overlap_summary.csv`
- `aipw_nuisance_model_diagnostics.csv`
- `refutation_tests.csv`
- `threshold_robustness_summary.csv`
- `evalue_sensitivity.csv`
- `diagnostic_tables_for_overleaf.tex`

## Nota sobre PS extremo

Os propensity scores foram previamente clipados em 0.05. Por isso, a coluna `% PS extremo` usa limite inclusivo (`<=0.05` ou `>=0.95`) para capturar observacoes encostadas no limite de positividade.