import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator


def hello_world_function():
    print("Hello World From Python Operator!")


with DAG(
    dag_id="test_run_dag",
    start_date=datetime.datetime(2025, 1, 1),
    schedule=None,
    default_args={"retries": 1, "retry_delay": datetime.timedelta(minutes=5)},
):
    PythonOperator(task_id="test_run_dag", python_callable=hello_world_function)