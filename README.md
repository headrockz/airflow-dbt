# Começando com o DBT (Data Build Tool)

O [DBT](https://www.getdbt.com/) é uma ferramenta de transformação de dados open-source. Caso queria conhecer um

## Estrutura do projeto

```bash
├── dbt_airflow # executando o dbt junto com o airflow
│   └── airflow
│   └── dbt
│   └── postgres
│   └── .env
│   └── docker-compose.yaml
│   └── poetry.lock
│   └── pyproject.toml
├── dbt_api     # api simples para rodar modelos no dbt
│   └── analyses
│   └── files
│   └── macros
│   └── models
│   └── seeds
│   └── snapshots
│   └── tests
│   └── app.py
│   └── dbt_project.yaml
│   └── docker-compose.yaml
│   └── Dockerfile
│   └── profiles.yml
│   └── script.sh
├── images
├── .gitignore
├── .python-version
└── README.md
```

## Executando os Projetos

### Executando um modelo no DBT via API

Para executar o esse projeto, entre na pasta ***dbt_api*** depois rode o comando `docker-compose up -d`. Ele irá subir dois containers um do Postgres e outro da imagem gerada pelo Dockerfile, essa imagem irá executar a API feita com o Flask, para acompanhar seus logs execute `docker logs dbt --follow`, e para executar um modelo, execute o comando `curl -X POST "http://<endereço>:8080/model?model=<nome modelo>"`.

### Orquestrando o DBT com o Airflow

Para executar o DBT no mesmo ambiente que o Airflow, estou utilizando o provider da Astronomer chamado [Cosmos](https://docs.astronomer.io/learn/airflow-dbt). Para executar esse projeto, entre na pasta ***dbt_airflow***, digite `docker-compose up -d`, depois entre na interface web do Airflow [http://localhost:8080](http://localhost:8080), o usuário e senha são **airflowdbt**

É necessário configurar a connection do Postgres dentro do Airflow

![image](/images/connection_postgres.png)

Criei quatro dags, uma que extrai os dados para ações da Apple e Google, executa um modelo para cada ação e depois um modelo que usa esses outros dois modelos. As outras três dags fazem a mesma coisa, só que separando cada uma das etapas.
