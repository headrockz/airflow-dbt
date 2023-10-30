from airflow.decorators import dag
from cosmos import DbtTaskGroup, ProjectConfig, ProfileConfig, ExecutionConfig, RenderConfig
# adjust for other database types
from cosmos.profiles import PostgresUserPasswordProfileMapping
from cosmos.profiles.bigquery import GoogleCloudServiceAccountFileProfileMapping
from pendulum import datetime
import os

YOUR_NAME = "profile"
DBT_PROJECT_PATH = f"{os.environ['AIRFLOW_HOME']}/dbt"
DBT_EXECUTABLE_PATH = f"/home/airflow/.local/bin/dbt"

execution_config = ExecutionConfig(
    dbt_executable_path=DBT_EXECUTABLE_PATH,
)


@dag(
    start_date=datetime(2023, 8, 1),
    schedule=None,
    catchup=False,
    params={"my_name": YOUR_NAME},
)
def dag_my_profile():
    transform_data = DbtTaskGroup(
        group_id="transform_data",
        project_config=ProjectConfig(DBT_PROJECT_PATH),
        profile_config=ProfileConfig(
        profile_name="cosmos",
        target_name="bq",
        profiles_yml_filepath=f"{DBT_PROJECT_PATH}/profiles.yml",
    ),
        execution_config=execution_config,
        operator_args={
            "vars": '{"my_name": {{ params.my_name }} }',
            "install_deps": True,
        },
        render_config=RenderConfig(select=["path:models/testes"]),
        default_args={"retries": 2},
    )

    transform_data

dag_my_profile()