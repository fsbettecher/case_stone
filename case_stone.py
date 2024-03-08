# Importando as bibliotecas utilizadas
import pandas as pd
import numpy as np
from datetime import timedelta


# Lendo os arquivos do case
dim_agents = pd.read_csv('dim_agents.csv')
dim_leaders = pd.read_csv('dim_leaders.csv')
fact_leads = pd.read_csv('fact_leads.csv')
fact_sales = pd.read_csv('fact_sales.csv')

"""
Segundo o case, as colunas lead_id e sale_id não são obrigatórias.
Por isso, nesse caso, irei remover as colunas e linhas duplicadas,
para diminuir o volume de dados
"""

fact_leads.drop('lead_id', axis=1, inplace=True)
fact_sales.drop('sale_id', axis=1, inplace=True)

fact_leads.drop_duplicates(['Agent_ID', 'Date'], inplace=True)
fact_sales.drop_duplicates(['Agent_ID', 'Date'], inplace=True)

"""
Considerando a coluna com nome vazio como o índice da tabela,
vou retirá-la das colunas e manter somente o índice gerado
ao transformar o arquivo em DataFrame
para manter os dados mais limpos
"""

dim_agents.drop('Unnamed: 0', axis=1, inplace=True)
dim_leaders.drop('Unnamed: 0', axis=1, inplace=True)
fact_leads.drop('Unnamed: 0', axis=1, inplace=True)
fact_sales.drop('Unnamed: 0', axis=1, inplace=True)

# Atribuindo valores dos fatores de acordo com o nível de cada agente
condicao_fator = [
    dim_agents['nivel'] == 1,
    dim_agents['nivel'] == 2,
    dim_agents['nivel'] == 3,
    dim_agents['nivel'] == 4,
    dim_agents['nivel'] == 5
    ]

valor_fator = [
    1,
    1.1,
    1.2,
    1.25,
    1.3
]

dim_agents['fator'] = np.select(condicao_fator, valor_fator, default=np.nan)

# Fazendo o cálculo das metas para cada agente
condicao_meta = [
    dim_agents['canal'] == 'chat',
    dim_agents['canal'] == 'whatsapp',
    dim_agents['canal'] == 'telefone',
    ]

valor_meta = [
    dim_agents['fator'] * 3,
    dim_agents['fator'] * 4,
    dim_agents['fator'] * 3.7,
]

dim_agents['meta'] = np.select(condicao_meta, valor_meta, default=np.nan)

# Unindo as tabelas de lead e sales de acordo com Agent_ID e data da ocorrência
lead_venda = pd.merge(fact_leads, fact_sales, on=['Agent_ID', 'Date'], how='outer')

# Unindo os dados de metas ao lead_venda
df_metas = lead_venda.merge(dim_agents, on='Agent_ID', how='left')

# Removendo colunas que não serão necessárias no processo
df_metas.drop(['canal', 'funcao', 'fator'], axis=1, inplace=True)

# Transformando a coluna de data em datetime
df_metas['Date'] = pd.to_datetime(df_metas['Date'])

# Para início de informações, considero a coluna trabalha = True
df_metas['trabalha'] = True

"""
Como não havia referência dos dias da semana no case, resolvi
ajustar os dias de acordo com o modelo do python [0-6], onde
0 = Segunda-feira e 6 = Domingo
"""

df_metas['folga_1'] -=  1
df_metas['folga_2'] -= 1

# Criando as colunas dos dias da semana
df_metas['dias_semana'] = [i.weekday() if i != '' else i for i in df_metas['Date']]

# Definindo a data do primeiro domingo do mês
primeiro_domingo = pd.to_datetime('2077-01-03')

# Definindo metas zeradas e trabalha = False para os dias de folga ou 4º
df_metas['meta'] = np.where(
    (df_metas['dias_semana'] == df_metas['folga_1']) |
    (df_metas['dias_semana'] == df_metas['folga_2']) |
    (df_metas['Date'] == primeiro_domingo + timedelta(21)),
    0,
    df_metas['meta']
    )

df_metas['trabalha'] = np.where(
    (df_metas['dias_semana'] == df_metas['folga_1']) |
    (df_metas['dias_semana'] == df_metas['folga_2']) |
    (df_metas['Date'] == primeiro_domingo + timedelta(21)),
    False,
    df_metas['trabalha']
    )

# Transformando dias da semana em nomes
dias_semana = [
    df_metas['dias_semana'] == 0,
    df_metas['dias_semana'] == 1,
    df_metas['dias_semana'] == 2,
    df_metas['dias_semana'] == 3,
    df_metas['dias_semana'] == 4,
    df_metas['dias_semana'] == 5,
    df_metas['dias_semana'] == 6
]

nomes_dias = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-Feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

df_metas['dias_semana'] = np.select (dias_semana, nomes_dias)

# Ordenando e removendo colunas
df_metas = df_metas[[
    'lider', 'Agent_ID', 'nivel', 'Date', 'dias_semana',
    'meta', 'trabalha'
]]

# Salvando o arquivo em formato csv
df_metas.to_csv('metas_calculadas_janeiro_2077.csv', index=False)