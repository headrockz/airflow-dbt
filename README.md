# Começando com o DBT (Data Build Tool)

O [DBT](https://www.getdbt.com/) é uma ferramenta de transformação de dados open-source.

## Estrutura do projeto

```bash
├── cosmos # executando o dbt junto com o airflow
│   ├── models
│   │     └── my models
│   ├── tests
│   │     └── my tests
│   ├── postgres
│   ├── dbt_project.yaml
│   └── profiles.yml
├── dags
│   └── my dags
├── images
├── .gitignore
├── docker-compose.yaml
├── Dockerfile
├── poetry.lock
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Executando o Projeto

### Orquestrando o DBT com o Airflow

Para executar o DBT no mesmo ambiente que o Airflow, estou utilizando o provider da Astronomer chamado [Cosmos](https://docs.astronomer.io/learn/airflow-dbt). Para executar esse projeto, entre na pasta ***dbt_airflow***, digite `docker-compose up -d`, depois entre na interface web do Airflow [http://localhost:8080](http://localhost:8080), o usuário e senha são **airflowdbt**

É necessário configurar a connection do Postgres dentro do Airflow

![image](/images/connection_postgres.png)
