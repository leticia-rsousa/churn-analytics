import pandas as pd
import numpy as np
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from IPython.display import display, Markdown

# Ajuste de visualização para números decimais
pd.set_option('display.float_format', lambda x: '%.4f' % x)

def gera_dados_churn(num_clientes = 2000):
    """
    Gera dados fictícios de clientes para análise de churn.
    """

    # Reprodutibilidade dos resultados
    np.random.seed(42)

    # Variáveis simuladas dos clientes
    fidelidade_meses = np.random.randint(1, 73, size = num_clientes)
    tipo_contrato_opts = ['Mensal', 'Anual', 'Dois anos']
    contrato_probs = [0.6, 0.25, 0.15]
    tipo_contrato = np.random.choice(tipo_contrato_opts, size = num_clientes, p = contrato_probs)

    servico_internet_opts = ['Fibra Óptica', 'DSL', 'Não']
    internet_probs = [0.55, 0.35, 0.10]
    servico_internet = np.random.choice(servico_internet_opts, size = num_clientes, p = internet_probs)

    # Definição de valores médios de fatura para cada tipo de contrato
    fatura_base = {
        'Mensal': np.random.normal(60, 20),
        'Anual': np.random.normal(70, 25),
        'Dois anos': np.random.normal(80, 25)
    }

   # Cálculo da fatura mensal simulada
    fatura_mensal = [fatura_base[c] + fidelidade_meses[i] * 0.2 + np.random.normal(0, 5)
                     for i, c in enumerate(tipo_contrato)]
    fatura_mensal = np.clip(fatura_mensal, 20, 120)

    # Construção dos log-odds para definir a probabilidade de churn
    prob_churn_log = -2.5
    prob_churn_log += -0.05 * fidelidade_meses
    prob_churn_log += [3.0 if c == 'Mensal' else -1.5 if c == 'Anual' else -2.5 for c in tipo_contrato]
    prob_churn_log += [0.8 if s == 'Fibra Óptica' else -0.5 for s in servico_internet]
    prob_churn_log += 0.03 * fatura_mensal

    # Conversão dos log-odds em probabilidade via função sigmoide
    prob_churn = 1 / (1 + np.exp(-prob_churn_log))

    # Geração da variável binária de churn
    churn = np.random.binomial(1, prob_churn)

    # DataFrame final
    df = pd.DataFrame({
        'ID_Cliente': range(1, num_clientes + 1),
        'Fidelidade_Meses': fidelidade_meses,
        'Tipo_Contrato': tipo_contrato,
        'Servico_Internet': servico_internet,
        'Fatura_Mensal': fatura_mensal,
        'Churn': churn
    })

    return df

# Geração dos dados
df_churn = gera_dados_churn()
print("--- Amostra de Dados Gerada ---")
print(df_churn.head())

print("\n--- Informações Gerais do DataFrame ---")
print(df_churn.info())

print("\n--- Resumo Estatístico das Variáveis Numéricas ---")
print(df_churn.describe())

print("\n--- Resumo Estatístico das Variáveis Categóricas ---")
print(df_churn.describe(include='object'))

# Gráfico interativo de proporção de churn
churn_counts = df_churn['Churn'].value_counts()

fig_pie = px.pie(
    values = churn_counts.values,
    names = churn_counts.index.map({1: 'Sim', 0: 'Não'}),
    title = 'Taxa de Churn Geral',
    color = churn_counts.index.map({1: 'Sim', 0:'Não'}),
    color_discrete_map = {'Sim': '#EF553B', 'Não': '#636EFA'}
)
fig_pie.show()

# Cálculo da taxa de churn total
churn_counts = df_churn['Churn'].value_counts()
numerador = churn_counts.get(1, churn_counts.get('Sim', churn_counts.get(True, 0)))
taxa = 100 * numerador / len(df_churn)

# Gráficos exploratórios por categoria e variáveis numéricas
fig_bar_contrato = px.histogram(
    df_churn,
    x = 'Tipo_Contrato',
    color = 'Churn',
    barmode = 'group',
    title = 'Taxa de Churn por Tipo de Contrato',
    labels = {'Tipo_Contrato': 'Tipo de Contrato', 'Churn': 'Churn (0 = Não, 1 = Sim)'}
)
fig_bar_contrato.show()

fig_hist_fidelidade = px.histogram(
    df_churn,
    x = 'Fidelidade_Meses',
    color = 'Churn',
    marginal = 'box',
    title = 'Distribuição de Fidelidade (em Meses) por Churn',
    labels = {'Fidelidade_Meses': 'Fidelidade_Meses'}
)
fig_hist_fidelidade.show()

fig_hist_fatura = px.histogram(
    df_churn,
    x = 'Fatura_Mensal',
    color = 'Churn',
    marginal = 'box',
    title = 'Distribuição de Fatura Mensal por Churn',
    labels = {'Fatura_Mensal': 'Valor da Fatura Mensal'}
)
fig_hist_fatura.show()

print(df_churn.head())
print(df_churn.Tipo_Contrato.value_counts())
print(df_churn.Servico_Internet.value_counts())

# Preparação do dataset para o modelo (one-hot encoding)
df_model = pd.get_dummies(df_churn,
                          columns = ['Tipo_Contrato', 'Servico_Internet'],
                          drop_first = True,
                          dtype = int)

print(df_churn.head())
print(df_model.head())
print(df_model.info())

# Separação das variáveis para o modelo
y = df_model['Churn']
X = df_model.drop(['ID_Cliente', 'Churn'], axis = 1)

# Inclusão do termo constante da regressão
X = sm.add_constant(X)

print("\n--- Amostra dos Dados (X) Preparados para o Modelo ---")
print(X.head())
print("\n--- Amostra dos Dados (y) Preparados para o Modelo ---")
print(y.head())

# Criação e treino do modelo de regressão logística
modelo = sm.Logit(y, X)
modelo_treinado = modelo.fit()

print("\n--- Resultados do Modelo de Regressão Logística ---")
print(modelo_treinado.summary())

# Cálculo das razões de chance (odds ratios)
params = modelo_treinado.params
conf = modelo_treinado.conf_int()
conf['Odds Ratio'] = params
conf.columns = ['2.5%', '97.5%', 'Odds Ratio']
conf = np.exp(conf)

print("\n--- Tabela de Razão de Chances (Odds Ratio) ---")
print(conf)
