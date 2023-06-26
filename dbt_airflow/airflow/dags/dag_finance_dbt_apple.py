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
    "dag_yfinance_dbt_apple",
    start_date=days_ago(1),
    schedule_interval=None,
    catchup=False,
) as dag:
    def load(ticker, df):
        columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        df = df[columns]
        hook = PostgresHook(postgres_conn_id="postgres")
        conn = hook.get_conn()
        cursor = conn.cursor()

        table_name = 'apple' if ticker == 'AAPL' else 'google'
        insert_query = f"""
            INSERT INTO {table_name} (date_close, open, high, low, close, volume)
            VALUES ({', '.join(['%s'] * len(columns))})
        """
        
        values = [[item[column] for column in columns] for _, item in df.iterrows()]
        cursor.executemany(insert_query, values)
        conn.commit()

        cursor.close()
        conn.close()

    def get_history(ticker):
        df = yfinance.Ticker(ticker).history(
            period="1d", 
            interval="1d",
            start=('2022-06-27'),
            end=('2023-06-26'),
            prepost=True,
        )

        df = df.reset_index()

        return df
    
    def extract(*context):
        TICKERS = [
            "AAPL",
        ]
        for t in TICKERS:
            df = get_history(ticker=t)
            load(ticker=t, df=df)
            

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    dbt_task = DbtTaskGroup(
        dbt_root_path="/opt/airflow/dbt",
        dbt_project_name="airflowdbt",
        conn_id="postgres",
        profile_args={
            "schema": "public",
        },
        select={'paths': ['models/apple']}
    )

    end_pipeline = EmptyOperator(task_id="post_dbt")

    extract_task >> dbt_task >> end_pipeline
