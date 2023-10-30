from airflow.decorators import dag
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig, RenderConfig
# adjust for other database types
from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos.profiles.bigquery import GoogleCloudServiceAccountFileProfileMapping
from pendulum import datetime
import os

YOUR_NAME = "World"
CONNECTION_ID = "postgres"
DB_NAME = "finance"
SCHEMA_NAME = "dbt"
MODEL_TO_QUERY = "models/testes"
# The path to the dbt project
DBT_PROJECT_PATH = f"{os.environ['AIRFLOW_HOME']}/dbt"
# The path where Cosmos will find the dbt executable
# in the virtual environment created in the Dockerfile
DBT_EXECUTABLE_PATH = f"/home/airflow/.local/bin/dbt"


profile_config = ProfileConfig(
    profile_name="default",
    target_name="dev",
    profile_mapping=GoogleCloudServiceAccountFileProfileMapping(
        conn_id="bigquery",
        profile_args={"dataset": "teste"},
    ),
)

execution_config = ExecutionConfig(
    dbt_executable_path=DBT_EXECUTABLE_PATH,
)


@dag(
    start_date=datetime(2023, 8, 1),
    schedule=None,
    catchup=False,
    params={"my_name": YOUR_NAME},
)
def dag_temporary_profile_cosmos():
    transform_data = DbtTaskGroup(
        group_id="transform_data",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=profile_config,
        execution_config=execution_config,
        operator_args={
            "vars": '{"my_name": {{ params.my_name }} }',
            "install_deps": True,
        },
        render_config=RenderConfig(select=["path:models/testes"]),
        default_args={"retries": 2},
    )

    transform_data

dag_temporary_profile_cosmos()