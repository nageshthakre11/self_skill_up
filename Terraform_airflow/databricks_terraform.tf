# Provider for Databricks
provider "databricks" {
  host  = "https://<databricks-instance>"
  token = "<databricks-personal-access-token>"
}

# Provider for Airflow
provider "airflow" {
  host     = "<airflow-server-url>"
  username = "<airflow-username>"
  password = "<airflow-password>"
}

# Databricks Notebook Resources
resource "databricks_notebook" "example_notebook_1" {
  path     = "/Workspace/Example/Job1"
  language = "PYTHON"  # You can also use SQL, R, or Scala depending on your notebook
  content_base64 = base64encode(<<EOF
# Python notebook content here
print("This is Job 1")
EOF
  )
}

resource "databricks_notebook" "example_notebook_2" {
  path     = "/Workspace/Example/Job2"
  language = "PYTHON"
  content_base64 = base64encode(<<EOF
# Python notebook content here
print("This is Job 2")
EOF
  )
}

resource "databricks_notebook" "example_notebook_3" {
  path     = "/Workspace/Example/Job3"
  language = "PYTHON"
  content_base64 = base64encode(<<EOF
# Python notebook content here
print("This is Job 3")
EOF
  )
}

# Databricks Jobs Definition
resource "databricks_job" "example_job_1" {
  name = "example-job-1"

  new_cluster {
    spark_version = "7.3.x-scala2.12"
    node_type_id  = "r4.xlarge"
    num_workers   = 2
  }

  notebook_task {
    notebook_path = databricks_notebook.example_notebook_1.path
  }
}

resource "databricks_job" "example_job_2" {
  name = "example-job-2"

  new_cluster {
    spark_version = "7.3.x-scala2.12"
    node_type_id  = "r4.xlarge"
    num_workers   = 2
  }

  notebook_task {
    notebook_path = databricks_notebook.example_notebook_2.path
  }
}

resource "databricks_job" "example_job_3" {
  name = "example-job-3"

  new_cluster {
    spark_version = "7.3.x-scala2.12"
    node_type_id  = "r4.xlarge"
    num_workers   = 2
  }

  notebook_task {
    notebook_path = databricks_notebook.example_notebook_3.path
  }
}

# Airflow DAG Definition for scheduling Databricks Jobs
resource "airflow_dag" "databricks_jobs_dag" {
  dag_id            = "databricks_jobs_scheduler"
  schedule_interval = "0 0 * * *"  # Adjust as needed

  task {
    task_id = "run_job_1"
    operator = "DatabricksRunNowOperator"
    job_id   = databricks_job.example_job_1.id
  }

  task {
    task_id = "run_job
