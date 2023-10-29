from pendulum import datetime


from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator
from cosmos.providers.dbt.task_group import DbtTaskGroup


@dag(
    start_date=datetime(2023, 8, 1),
    schedule=None,
    catchup=False,
    params={"my_name": "asafe"},
)
def my_simple_dbt_dag():

    e1 = EmptyOperator(task_id="pre_dbt")

    dbt_tg = DbtTaskGroup(
        group_id="transform_data",
        dbt_root_path="/opt/airflow/dbt",
        dbt_project_name="dbt",
        conn_id="postgres",
        profile_args={
            "schema": "dbt_sep",
        },
        operator_args={
            "vars": '{"my_name": {{ params.my_name }} }',
        },
        select={'paths': ['models/teste']}
    )


    e2 = EmptyOperator(task_id="post_dbt")

    e1 >> dbt_tg >> e2

my_simple_dbt_dag()
