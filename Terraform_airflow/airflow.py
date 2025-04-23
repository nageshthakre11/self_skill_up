from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator
from datetime import datetime

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 22),
    'retries': 1,
}

# Define the DAG
dag = DAG(
    'databricks_jobs_scheduler',  # DAG ID
    default_args=default_args,
    schedule_interval='@daily',  # Adjust the schedule as needed
    catchup=False,
)

# Trigger Databricks jobs
job_1_run = DatabricksRunNowOperator(
    task_id='run_job_1',
    job_id='<databricks-job-id-1>',  # Replace with the actual Databricks Job ID from Terraform
    dag=dag,
)

job_2_run = DatabricksRunNowOperator(
    task_id='run_job_2',
    job_id='<databricks-job-id-2>',  # Replace with the actual Databricks Job ID from Terraform
    dag=dag,
)

job_3_run = DatabricksRunNowOperator(
    task_id='run_job_3',
    job_id='<databricks-job-id-3>',  # Replace with the actual Databricks Job ID from Terraform
    dag=dag,
)

# Set task dependencies to ensure correct order of execution
job_1_run >> job_2_run >> job_3_run
