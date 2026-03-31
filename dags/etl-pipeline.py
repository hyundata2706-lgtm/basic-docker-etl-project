from airflow import DAG
from airflow.operations.bash import BashOperator
from datetime import datetime


with DAG(
  dag_id:="etl_pipeline",
  start_date=datetime(2026,4,1),
  schedule_interval="@daily",
  catchup=False
) as dag:
  
  generator = BashOperator(
    task_id="generator",
    bash_command="python /opt/airflow/app/generate_data.py"
  )

  extract = BashOperator(
      task_id="extract",
      bash_command="python /opt/airflow/app/extract.py"
  )

  transform = BashOperator(
      task_id="transform",
      bash_command="python /opt/airflow/app/transform.py"
  )

  load = BashOperator(
      task_id="load",
      bash_command="python /opt/airflow/app/load.py"
  )

  generator >> extract >> transform >> load
