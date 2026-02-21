## Churn Analytics
**Descrição Geral** 📄<br>
Este projeto apresenta uma **análise de churn** de clientes, utilizando **Python** e bibliotecas de manipulação, modelagem estatística e visualização de dados. O sistema realiza **limpeza, tratamento de valores ausentes, análise exploratória, criação de variáveis, modelagem estatística e interpretação dos resultados.**
O projeto demonstra conceitos de **análise de dados, engenharia de atributos, estatística aplicada e interpretação de métricas de churn.**

---
**Objetivo** 🎯 <br> 
O objetivo principal do projeto é **identificar padrões e fatores associados ao churn**, aplicando técnicas de **pré-processamento, modelagem estatística e interpretação dos coeficientes.**
Com isso, o projeto permite **entender o comportamento dos clientes, avaliar variáveis relevantes e apoiar decisões baseadas em dados.**

---
**Tecnologias Utilizadas** 💻 <br>
* ***Python*** - linguagem principal.
* ***Pandas*** - manipulação de dados em DataFrames.
* ***NumPy*** - operações matemáticas.
* ***Matplotlib / Seaborn*** - criação de gráficos exploratórios.
* ***Statsmodels*** – modelagem estatística (Regressão Logística).

---
**Arquitetura e Estrutura do Código** 🧱 <br><br>
***1. Script Principal (churn_analysis.py)*** <br>
Responsável por:
* ***Carregar e inspecionar o dataset.*** 
* ***Realizar limpeza e tratamento de dados (nulos, duplicados, tipos incorretos).***
* ***Criar variáveis derivadas e normalizar colunas quando necessário.***
* ***Executar análise exploratória por meio de tabelas, gráficos e estatísticas.***
* ***Rodar o modelo de Regressão Logística para prever churn.***
* ***Interpretar coeficientes, odds ratio e significância estatística.***
* ***Gerar métricas de avaliação do modelo.***

---
**Conceitos e Funcionalidades Demonstradas** 🔍 <br><br>
✅ ***Manipulação de dados:*** <br>
Uso de **Pandas e NumPy** para corrigir inconsistências, padronizar informações e preparar o dataset para modelagem.

✅***Limpeza de dados:*** <br>
Inclui:
* ***tratamento de valores ausentes,***
* ***correção de tipos de dados,***
* ***remoção de duplicidades,***
* ***detecção básica de outliers.***

✅***Análise Exploratória (EDA)*** <br>
Geração de gráficos e estatísticas para entender:
* ***distribuição das variáveis,***
* ***relação entre características e churn,***
* ***padrões de comportamento dos clientes.***

✅***Modelagem Estatística*** <br>
Aplicação de **Regressão Logística**, com:
* ***interpretação dos coeficientes,***
* ***cálculo de odds ratio,***
* ***avaliação da significância (p-values),***
* ***análise da qualidade do ajuste.***

✅***Avaliação do Modelo*** <br>
Uso de métricas como:
* ***matriz de confusão,***
* ***acurácia, precisão, recall.***

---
**Como Executar o Projeto** ▶️ <br><br>
***1. Instale as dependências (recomendado via requirements.txt):*** <br>
```pip install -r requirements.txt```

***2. Execute o script principal:*** <br>
```python churn_analysis.py```

***3. Veja a saída com análises, coeficientes e gráficos.*** <br>

***Exemplo de saída:*** <br>
```
Dataset carregado: (5000, 15)

Resumo Estatístico:
- Taxa de churn geral: 26.4%
- Variáveis com maior correlação: Tenure, MonthlyCharges, ContractType

Modelo de Regressão Logística:
--------------------------------
coef  p-value   odds_ratio
...

AUC = 0.82
Matriz de confusão exibida.
Gráficos de distribuição e correlação gerados.
```

---
**Conclusão** 📌 <br>
Este projeto demonstra, de forma prática, como realizar **tratamento de dados, engenharia de atributos e análise estatística aplicada ao churn.**
Ele oferece uma abordagem completa — desde a preparação dos dados até a modelagem e interpretação — permitindo **identificar padrões relevantes e apoiar estratégias de retenção de clientes.**
