# Roteiro de slides

## Slide 1: Problema clinico
- Transfusao de hemacias e frequente na UTI.
- A decisao costuma depender de hemoglobina, gravidade e contexto clinico.
- O efeito pode variar entre pacientes.

## Slide 2: Por que associacao nao basta
- Pacientes transfundidos tendem a ser mais graves.
- Ha confundimento por indicacao.
- Comparar mortalidade bruta pode induzir conclusoes erradas.

## Slide 3: Pergunta causal
- Qual e o efeito de transfundir versus nao transfundir?
- Estimando $Y(1)-Y(0)$.
- O grupo/fenotipo estratifica o efeito; nao e o tratamento.

## Slide 4: Target trial
- Definicao de t0.
- Features apenas antes de t0.
- Tratamento A: transfusao.
- Desfecho Y: mortalidade.

## Slide 5: Estimadores
- Propensity score.
- Modelo de outcome.
- AIPW/doubly robust como principal.
- ATT, IPTW e overlap como triangulacao.

## Slide 6: Resultado global
- Efeito global fraco e nao significativo.
- AIPW ATE = +0.040, IC95% [-0.027, +0.117].
- A transfusao nao parece ter efeito medio homogeneo.

## Slide 7: Heterogeneidade
- Scan causal identificou cinco grupos.
- B1/B2 com beneficio estimado.
- M1/M2/M3 com maleficio estimado.

## Slide 8: Grupos B1/B2
- B1: FC controlada, Hb em queda, SpO2 nao alta.
- B2: B1 + PAM media baixa/moderada.
- Interpretacao: anemia dinamica em paciente relativamente compensado.

## Slide 9: Grupos M1/M2/M3
- M1: FC subindo + pico de PAM elevado.
- M2: M1 + variabilidade de creatinina.
- M3: hemoglobina sem queda relevante.
- Interpretacao: deterioracao/indicacao residual/risco cardiorrenal.

## Slide 10: Contrafactual individual
- Modelo estima mu0 e mu1.
- ITE = mu1 - mu0.
- Uso exploratorio; o foco principal e efeito por grupo.

## Slide 11: Limitacoes
- Estudo observacional.
- Confundimento residual.
- Positividade e overlap limitados em subgrupos.
- Sem ground truth contrafactual individual.

## Slide 12: Conclusao
- Efeito global nao significativo.
- Heterogeneidade forte.
- Beneficio em anemia dinamica compensada.
- Maleficio em trajetorias de estresse hemodinamico/cardiorrenal.
- Resultados geradores de hipotese para validacao externa.
