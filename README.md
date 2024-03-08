<h1 align="center">Case STONE</h1>
<p align="center">
<img loading="lazy" src="https://img.shields.io/badge/STATUS-FINALIZADO-badge"/>
</p>

<hr></hr>

<h4 align="justify">O case abordado é a construção de etapas sobre organização e visualização de dados. A primeira parte, sobre coleta e tratamento de dados, foi feita através de python (v. 3.11.8), utilizando as bibliotecas pandas, numpy e datetime. Já a segunda parte, de visualização, foi utilizado o Looker Studio (Google) como ferramenta de BI. Para mais detalhes, as explicações de lógicas serão explicadas e o link da dashboard criada estará disponível no arquivo.
</h4>

<hr></hr><br></br>

<h1 align="center">1ª Etapa</h1><br></br>

<h3 align="center">1ª Entrega</h3>

1) Os arquivos foram baixados e utilizados como base utilizando a função `pd.read_csv()`

2) Como o índice das bases de dados vieram sem nome no arquivo, as colunas de índice foram removidas e um
novo indice foi criado automaticamente.

3) A primeira informação gerada é a criação de uma base com os dias do mês de Janeiro de 2077 em cada linha. Dessa forma, é possível atribuir cada linha do dia para cada agente na tabela `dim_agents`. Para isso, foi criada uma lista com os dias do mês e uma lista com os IDs dos agentes.

4) Para unir os dois valores em um DataFrame, foi feita o nivelamento de dimensões, ou seja, as duas listas passaram a ter o mesmo tamanho.

5) Criada a lista dos dias e IDs e niveladas as dimensões, o DataFrame foi criado e unido ao banco principal `dim_agents`.

6) Como primeira análise, foi utilizado a função `np.select()` para definir os pesos de acordo com cada nível do agente.

7) Após definir os pesos, a mesma função foi utilizada para calcular as metas de acordo com o tipo de canal utilizado pelo agente.

8) As colunas `folga_1` e `folga_2` foram padronizadas para o modelo do Python segundo sua função nativa `weekday()`, onde 0 representa Segunda-feira e 6 representa Domingo.
Dessa forma, seria possível reconhecer os dias da semana de acordo com o número das colunas `folga_1` e `folga_2` e a coluna `Date`.

9) Após definir os dias da semana, nesse passo foram feitas as isenções dos dias trabalhados. Considerando a coluna meta = 0 e a coluna trabalha = False

10) Finalizando o tratamento dos dados, os dias da semana foram alterados de números [0 ~ 6] para nomes [Segunda-feira ~ Domingo]

11) Por fim, as colunas foram reordenadas e selecionadas e o arquivo foi exportado no formato `.csv` com o nome metas_janeiro_2077.csv

<br></br>

<h3 align="center">2ª Entrega</h3>

1) Continuando as análises, inicialmente foi feita a contagem de vendas e leads feitos por agente em cada dia do mês de Janeiro de 2077.

2) Os valores foram unidos ao banco principal que veio da 1ª entrega, `dim_agents`.

3) Como nem todos os dias houve venda ou contato com os potenciais clientes pelos agentes, os valores nulos gerados com a agragação das tabelas foram definidos como zero.

4) Como último tratamento de dados, dias em que não houve trabalho ou houve folga coletiva foram definidos com venda zerada.

5) E como última análise do banco, foi feito o cálculo da porcentagem de meta alcançada, baseado na quantidade de vendas em relação à meta calculada por agente, diariamente.

6) A tabela da segunda entrega foi exportada no formato `.csv` com o nome leads_sales_janeiro_2077.csv e utilizada no Looker Studio para análise mais detalhada dos dados.

<br></br>

<h1 align="center">2ª Etapa</h1>

 <h3 align="center">[Dashboard no Looker Studio](https://lookerstudio.google.com/u/0/reporting/b028e423-55ea-4cb3-ac9d-f23a5f9b46d5/page/0oUsD)</h3>

> [!NOTE]
> Como não sabia sobre o direito autoral da logo ou do nome da Stone, resolvi deixar o dashboard sem imagens ou rferências gráficas relacionadas. Mantive apenas a identidade visual.

<br></br>

A dashboard possui o objetivo de mostrar as médias das metas de acordo com os dias da semana, destacando o dia com maior a média geral. Dessa forma, seria possível gerar uma investigação dos dias com médias mais baixas e entender a causa.

Além disso, também há um gráfico de série temporal, descrevendo as métas ao longo do mês de janeiro, sendo possível acompanhar as metas de um agente ao longo do tempo e possíveis cíclos de quedas ou aumentos de rendimento.


