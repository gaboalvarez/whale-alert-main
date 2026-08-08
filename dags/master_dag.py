import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator

with DAG(
    dag_id="master_dag",
    start_date=datetime.datetime(2022, 1, 1),
    schedule=None,
    catchup=False,
    tags=["orchestration"],
):
    start = EmptyOperator(task_id="start")
    trigger_test_run = TriggerDagRunOperator(
        task_id="trigger_test_run",
        trigger_dag_id="test_run_dag",
        wait_for_completion=True,
    )
    trigger_minio = TriggerDagRunOperator(
        task_id="trigger_minio",
        trigger_dag_id="test_minio_connection",
        wait_for_completion=True,
    )
    trigger_whale_alert = TriggerDagRunOperator(
        task_id="trigger_whale_alert",
        trigger_dag_id="whale_alert",
        wait_for_completion=True,
    )
    end = EmptyOperator(task_id="end")
    start >> trigger_test_run >> trigger_minio >> trigger_whale_alert >> end