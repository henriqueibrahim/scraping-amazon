# scraping-amazon

* Meu primeiro projeto. Um scraper que raspa os resultados de uma pesquisa na amazon e salva em um banco sql
* Ainda em desenvolvimento
* Não está optimizado nem com a melhor lógica
* To aprendendo ainda :)


# Executando o script

Para executar o script é necessário alguns passos antes:

1. Instalar os requirements
2. Configuração do banco de dados
3. Inserir as informações no arquivo .env


Para instalar os requirements sugiro fazer dentro de um ambiente virtual do python para não interferir com seu sistema

```
python3 -m venv virtualenvironment
```
Depois só dar o source

```
source virtualenvironment/bin/activate
```

Agora só instalar

```
pip install -r requirements.txt
```


**Vocẽ já deve ter o banco de dados instalado e rodando na máquina**


Crie a database:

```
CREATE DATABASE nomequequiser;
```

Depois de selecionada (```USE nomequequiser; ```), é preciso criar as tables

```
CREATE TABLE Data (
   title VARCHAR(500) NOT NULL,
   price VARCHAR(10) NOT NULL,
   PRIMARY KEY (title, price)
);
```

*É meu primeiro contato com SQL, não sei se é a melhor maneira de se fazer isso*
*Coloco o PRIMARY KEY para ele evitar duplicados e não salvar 2x a mesma coisa*


Depois de criada, se deve criar um arquivo .env com as informações da database

```
USER=usuárioDoBancoSQL
PASSWORD=senhaDoBancoSQL
DATABASE=nomeDaDatabase
```

Depois disso, só entrar no arquivo "search_urls.txt" e colocar as URLs de pesquisa que deseja raspar (lembrando que somente da amazon) e rodar o main.py
segue o padrão que já vai no arquivo


# TODO:

1. Precisa passar para as outras páginas de pesquisa, só está raspando a primeira
2. Tem mais coisa pra fazer mas por enquanto só lembro disso rs
