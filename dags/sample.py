from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}

with DAG(
    dag_id="sample_dag",
    default_args=default_args,
    schedule_interval="@hourly",
    catchup=False,
    description="A simple test DAG",
) as dag:

    hello = BashOperator(
        task_id="print_hello",
        bash_command="echo 'Hello from GitHub Actions deployment!'"
    )
