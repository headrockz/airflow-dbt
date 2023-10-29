import pandas as pd
import yfinance
from airflow import DAG
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.utils.dates import days_ago
from cosmos.providers.dbt.task_group import DbtTaskGroup


with DAG(
    "dag_dbt_join",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:
    dbt_task = DbtTaskGroup(
        dbt_root_path="/opt/airflow/dbt",
        dbt_project_name="airflowdbt",
        conn_id="postgres",
        profile_args={
            "schema": "dbt_sep",
        },
        operator_args={
            "vars": '{"my_name": {{ params.my_name }} }',
        },
        select={'paths': ['models/testes']}
    )

    end_pipeline = EmptyOperator(task_id="post_dbt")

    dbt_task >> end_pipeline
