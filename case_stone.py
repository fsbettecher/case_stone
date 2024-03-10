# Importando as bibliotecas utilizadas
import pandas as pd
import numpy as np
import datetime

# Lendo os arquivos do case
dim_agents = pd.read_csv('dim_agents.csv')
dim_leaders = pd.read_csv('dim_leaders.csv')
fact_leads = pd.read_csv('fact_leads.csv')
fact_sales = pd.read_csv('fact_sales.csv')


"""
Considerando a coluna com nome vazio como o índice da tabela,
vou retirá-la das colunas e manter somente o índice gerado
ao transformar o arquivo em DataFrame para manter os dados
mais limpos
"""

dim_agents.drop('Unnamed: 0', axis=1, inplace=True)
dim_leaders.drop('Unnamed: 0', axis=1, inplace=True)
fact_leads.drop('Unnamed: 0', axis=1, inplace=True)
fact_sales.drop('Unnamed: 0', axis=1, inplace=True)

# Criando uma lista dos dias do mês de Janeiro de 2077
primeiro_dia = datetime.date(2077, 1, 1)
ultimo_dia = datetime.date(2077, 1, 31)

delta_time = ultimo_dia - primeiro_dia

dias = []
for i in range(delta_time.days + 1):
    day = primeiro_dia + datetime.timedelta(days=i)
    dias.append(day)

lista_dias_str = [datetime.datetime.strftime(dt, format="%Y-%m-%d") for dt in dias]

# Criando uma lista dos Agent_ID únicos
lista_agent_id = list(dim_agents['Agent_ID'].unique())

# Obtendo as dimensões de cada lista
len_dias = len(lista_dias_str)
len_agent_id = len(lista_agent_id)

# Multiplicando as listas para atingirem a mesma dimensão
lista_dias_str = lista_dias_str * len_agent_id
lista_agent_id = lista_agent_id * len_dias

# Criando o DataFrame com as duas listas
df_dias = pd.DataFrame({'Agent_ID': lista_agent_id, 'Date': lista_dias_str})
df_dias.sort_values(['Agent_ID', 'Date'], inplace=True)

# Unindo o DataFrame criado com o dim_agents
dim_agents = df_dias.merge(dim_agents, on='Agent_ID', how='left')

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

# Transformando a coluna de data em datetime
dim_agents['Date'] = pd.to_datetime(dim_agents['Date'])

# Para início de informações, considero a coluna trabalha = True
dim_agents['trabalha'] = True

"""
Como não havia referência dos dias da semana no case, resolvi
ajustar os dias de acordo com o modelo do python [0-6], onde
0 = Segunda-feira e 6 = Domingo
"""

dim_agents['folga_1'] -=  1
dim_agents['folga_2'] -= 1

# Criando as colunas dos dias da semana
dim_agents['dias_semana'] = [i.weekday() if i != '' else i for i in dim_agents['Date']]

# Definindo a data do primeiro domingo do mês
primeiro_domingo = pd.to_datetime('2077-01-03')

# Definindo metas zeradas e trabalha = False para os dias de folga ou 4º
dim_agents['meta'] = np.where(
    (dim_agents['dias_semana'] == dim_agents['folga_1']) |
    (dim_agents['dias_semana'] == dim_agents['folga_2']) |
    (dim_agents['Date'] == primeiro_domingo + datetime.timedelta(21)),
    0,
    dim_agents['meta']
    )

dim_agents['trabalha'] = np.where(
    (dim_agents['dias_semana'] == dim_agents['folga_1']) |
    (dim_agents['dias_semana'] == dim_agents['folga_2']) |
    (dim_agents['Date'] == primeiro_domingo + datetime.timedelta(21)),
    False,
    dim_agents['trabalha']
    )

# Transformando dias da semana em nomes
dias_semana = [
    dim_agents['dias_semana'] == 0,
    dim_agents['dias_semana'] == 1,
    dim_agents['dias_semana'] == 2,
    dim_agents['dias_semana'] == 3,
    dim_agents['dias_semana'] == 4,
    dim_agents['dias_semana'] == 5,
    dim_agents['dias_semana'] == 6
]

nomes_dias = [
    'Segunda-feira',
    'Terça-feira',
    'Quarta-feira',
    'Quinta-feira',
    'Sexta-feira',
    'Sábado',
    'Domingo'
]

dim_agents['dias_semana'] = np.select (dias_semana, nomes_dias)

# Ordenando e removendo colunas
dim_agents = dim_agents[[
    'lider', 'Agent_ID', 'nivel', 'Date', 'dias_semana',
    'meta', 'trabalha'
]]

# Conclusão do Passo 1:
# Exportando a primeira tabela
dim_agents.to_csv('metas_janeiro_2077.csv')


# Passo 2:
# contando a quantidade de leads e sales por agente, por dia
count_leads = fact_leads.groupby(['Agent_ID', 'Date'])['lead_id'].count()
count_sales = fact_sales.groupby(['Agent_ID', 'Date'])['sale_id'].count()

# Transformando os dados em DataFrames
count_leads = pd.DataFrame(count_leads).reset_index()
count_sales = pd.DataFrame(count_sales).reset_index()

# Renomeando as colunas de contagem
count_leads.rename(columns={'lead_id': 'count_leads'}, inplace=True)
count_sales.rename(columns={'sale_id': 'count_sales'}, inplace=True)

# Transformando a coluna Date para datetime
count_leads['Date'] = pd.to_datetime(count_leads['Date'])
count_sales['Date'] = pd.to_datetime(count_sales['Date'])

# Unindo as informações em um único DataFrame
leads_sales = count_leads.merge(count_sales, on=['Agent_ID', 'Date'], how='outer')
leads_sales = dim_agents.merge(leads_sales, on=['Agent_ID', 'Date'], how='left')

# Transformando valores nulos em 0 para o cálculo da % de metas alcançadas
leads_sales['count_leads'].fillna(0, inplace=True)
leads_sales['count_sales'].fillna(0, inplace=True)

# Tratando valores de vendas em que não houve trabalho
leads_sales['count_sales'] = np.where(
    leads_sales['trabalha'] == False,
    0,
    leads_sales['count_sales']
    )

leads_sales['%_meta_ancancada'] = leads_sales['count_sales'] / leads_sales['meta']

# Conclusão do Passo 2:
# Exportando a segunda tabela
leads_sales.to_csv('leads_sales_janeiro_2077.csv', index=False)