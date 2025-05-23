from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def investigate():
    print("Investigating site and regulations")


def analyze():
    print("Measuring area and climate data")


def detect():
    print("Detecting rooftops and constraints")


def size_system():
    print("Sizing PV system and estimating generation")


def recommend():
    print("Generating proposal for installation")


default_args = {"start_date": datetime(2024, 1, 1)}

with DAG(
    dag_id="solar_project_workflow",
    schedule_interval=None,
    catchup=False,
    default_args=default_args,
    description="Solar workflow with investigative steps",
) as dag:

    t1 = PythonOperator(task_id="investigate", python_callable=investigate)
    t2 = PythonOperator(task_id="analyze", python_callable=analyze)
    t3 = PythonOperator(task_id="detect", python_callable=detect)
    t4 = PythonOperator(task_id="dimension", python_callable=size_system)
    t5 = PythonOperator(task_id="recommend", python_callable=recommend)

    t1 >> t2 >> t3 >> t4 >> t5
