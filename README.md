<h1 align="center">Case STONE</h1><br>
<p align="center">
<img loading="lazy" src="https://img.shields.io/badge/STATUS-FINALIZADO-badge"/>
</p>
<br>

<hr></hr>

<h4 align="justify">🔹 O case abordado diz sobre organização e visualização de dados. A parte de coleta e tratamento de dados foi feita através de python (v. 3.11.8), utilizando as bibliotecas pandas, numpy e datetime. Já a parte de visualização, foi utilizado o Looker Studio (Google). Para mais detalhes, o link estará disponível no final do arquivo.
</h4>

<hr></hr><br>

<h2>Primeiramente, é necessário possuir uma conta no site Kaggle</h2>

• Acesse [www.kaggle.com](https://www.kaggle.com/)<br></br>
• Crie uma conta clicando em "Register" no canto superior direito, conforme a imagem abaixo:<br></br>
![Registro no Kaggle](https://github.com/fsbettecher/world_population/assets/62480910/72e77922-67f0-4bf3-88eb-54dedd943ddb)<br>
<br></br>

• Após criar a conta, será necessário criar um token para acessar os datasets via API<br></br>
![Baixando o Token](https://github.com/fsbettecher/world_population/assets/62480910/5e49ab5f-ce7d-49f5-ac82-95a2db4dba08)
<br></br>

• Seguindo os passos acima, será feito o download do token no formato json para o seu computador.

• Em seguida, abra o Git Bash e execute as linhas de comando abaixo:

```
cd C:/users/nome_do_usuario
```

>Altere "<strong>nome_do_usuario</strong>" para o nome que está registrado em seu computador
<br>

```
mkdir .kaggle
```
```
cd .kaggle
```
```
cp diretorio/onde/está/o/arquivo/kaggle.json .
```
>Essa última linha deve conter o final "<strong>/kaggle.json</strong>" no endereço, para que seja feita uma cópia do arquivo correto na pasta atual representada por "."
>
>Por exemplo: no meu computador o comando seria `cp D:/Downloads/kaggle.json .`
<br>

• Dessa forma, o arquivo token baixado será copiado para a pasta .kaggle criada na pasta do usuário. Essa etapa é importante para a autenticação da API no código e não deve ser pulada.

<h2>🎉 Pronto! Agora seu computador está configurado e pronto para rodar o código e utilizar a API do Kaggle! 🎉</h2>
