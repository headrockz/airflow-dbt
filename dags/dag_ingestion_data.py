from airflow.decorators import dag
from airflow.datasets import Dataset
from airflow.utils.task_group import TaskGroup
from airflow.operators.empty import EmptyOperator
from cosmos.operators import DbtRunOperationOperator, DbtSeedOperator
from cosmos import ProfileConfig, ExecutionConfig
# adjust for other database types
from cosmos.profiles import PostgresUserPasswordProfileMapping
from pendulum import datetime, duration
import os


# The path to the dbt project
DBT_PROJECT_PATH = f"{os.environ['AIRFLOW_HOME']}/dbt"
# The path where Cosmos will find the dbt executable
# in the virtual environment created in the Dockerfile
DBT_EXECUTABLE_PATH = f"/home/airflow/.local/bin/dbt"


profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres",
        profile_args={"schema": "public"},
    ),
)

execution_config = ExecutionConfig(
    dbt_executable_path=DBT_EXECUTABLE_PATH,
)

default_args = {
    "owner": "Asafe",
    "depens_on_past": False,
    "retries": 2,
    "retry_delay": duration(minutes=5)
}


@dag(
    start_date=datetime(2023, 8, 1),
    schedule=None,
    catchup=False,
    default_args=default_args,
    tags=['moves', 'types']
)
def dag_ingestion_data():

    start_dag = EmptyOperator(task_id='start_dag')
    end_dag = EmptyOperator(task_id='end_dag')

    with TaskGroup(group_id="drop_seeds_if_exist") as drop_seeds:
        for seed in ["pokemons", "moves", "moves_pokemons"]:
            DbtRunOperationOperator(
                task_id=f"drop_{seed}_if_exists",
                macro_name="drop_table_by_name",
                args={"table_name": seed},
                project_dir=DBT_PROJECT_PATH,
                profile_config=profile_config,
                install_deps=True,
            )

    pokemons_seed = DbtSeedOperator(
        task_id="pokemons_seed",
        project_dir=DBT_PROJECT_PATH,
        outlets=[Dataset("SEED://POKEMONS")],
        profile_config=profile_config,
        install_deps=True,
    )

    start_dag >> drop_seeds >> pokemons_seed >> end_dag

dag_ingestion_data()