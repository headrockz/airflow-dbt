from airflow.decorators import dag
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig, RenderConfig, LoadMode
# adjust for other database types
from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos.profiles.bigquery import GoogleCloudServiceAccountFileProfileMapping
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
        profile_args={"schema": "dbt"},
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
    tags=['pokemons', 'types']
)
def dag_pokemons_types():
    transform_data = DbtTaskGroup(
        group_id="pokemons_type",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=profile_config,
        execution_config=execution_config,
        operator_args={
            "vars": '{"start_date": {{ data_interval_start }} }',
            "install_deps": True,
        },
        render_config=RenderConfig(select=["path:models/pokedex/pokemons/types"]),
        default_args={"retries": 2},
    )

    transform_data

dag_pokemons_types()