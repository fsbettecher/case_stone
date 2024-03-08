# Importando as bibliotecas utilizadas
import pandas as pd


# Lendo os arquivos do case
dim_agents = pd.read_csv('dim_agents.csv')
dim_leaders = pd.read_csv('dim_leaders.csv')
fact_leads = pd.read_csv('fact_leads.csv')
fact_sales = pd.read_csv('fact_sales.csv')