<h1 align="center">Case STONE</h1><br>
<p align="center">
<img loading="lazy" src="https://img.shields.io/badge/STATUS-FINALIZADO-badge"/>
</p>
<br>

<hr></hr>

<h4 align="justify">🔹 O case abordado diz sobre organização e visualização de dados. A parte de coleta e tratamento de dados foi feita através de python (v. 3.11.8), utilizando as bibliotecas pandas, numpy e datetime. Já a parte de visualização, foi utilizado o Looker Studio (Google). Para mais detalhes, o link estará disponível no final do arquivo.
</h4>

<hr></hr><br>

<h2>Seguindo o passo a passo:</h2>

1) Os arquivos foram baixados e utilizados como base utilizando o código abaixo:
```
dim_agents = pd.read_csv('dim_agents.csv')
```
```
dim_leaders = pd.read_csv('dim_leaders.csv')
```
```
fact_leads = pd.read_csv('fact_leads.csv')
```
```
fact_sales = pd.read_csv('fact_sales.csv')
```

2) Após a coleta dos bancos de dados, algumas colunas que não seriam usadas foram retiradas dos DataFrames
e as linhas duplicadas foram removidas.<br></br>

3) Como o índice das bases de dados vieram sem nome no arquivo, as colunas de índice foram removidas e um
novo indice foi criado automaticamente.

4) Como primeira análise, foi utilizado a função ```np.select``` para definir os pesos de acordo com cada nível do agente.

5) Após definir os pesos, a mesma função foi utilizada para calcular as metas de acordo com o tipo de canal utilizado pelo agente.

6) Na parte intermediária do código, as tabelas de vendas, leads e informações de metas foram unificadas para dar continuidade ao tratamento de dados

7) Nesse passo, a coluna de folgas (1 e 2) foram padronizadas para o modelo do Python, onde 0 representa Segunda-feira e 6 representa Domingo.
Dessa forma, seria possível reconhecer os dias da semana de acordo com o número das colunas ```folga_1``` e ```folga_2``` e a coluna ```Date```.

8) Após definir os dias da semana, nesse passo foram feitas as isenções dos dias trabalhados. Considerando a coluna meta = 0 e a coluna trabalha = False

9) Finalizando o tratamento dos dados, os dias da semana foram alterados de números [0 ~ 6] para nomes [Segunda-feira ~ Domingo]

10) Por fim, as colunas foram reordenadas e selecionadas e o arquivo foi exportado no formato ```.csv```. A partir desse ponto,
as informações foram levadas ao Looker Studio fazendo o upload do arquivo no formato csv.

🟢🟢🟢<h2 align="center">[Dashboard no Looker Studio](https://lookerstudio.google.com/u/0/reporting/b028e423-55ea-4cb3-ac9d-f23a5f9b46d5/page/0oUsD/edit)</h2>
<br></br>
