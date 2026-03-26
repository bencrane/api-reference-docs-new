# RudderStack-Airflow Integration

Orchestrate your Profiles and Reverse ETL jobs programmatically with RudderStack’s Airflow provider.

* * *

  * __6 minute read

  * 


[Apache Airflow](<https://airflow.apache.org/>) is an open source platform to schedule, manage, and monitor workflows for data engineering pipelines.

RudderStack provides an [Airflow operator](<https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html>) for triggering your Profiles runs and Reverse ETL syncs programmatically via Airflow.

See the [GitHub Repository](<https://github.com/rudderlabs/rudder-airflow-provider>) for more information on the codebase with [sample DAGs](<https://github.com/rudderlabs/rudder-airflow-provider/tree/main/examples>).

## Prerequisites

  * A working Apache Airflow setup in place. See the [Airflow documentation](<https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html>) for more information.
  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in the RudderStack dashboard with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>):

Resource| Permissions  
---|---  
Tables / SQL Models / Audiences| **Edit** , **Connect**  
Destinations| **Edit** , **Connect**  
Profiles| **Edit** , **Connect**  
  
  * **For testing or development purposes only** : Generate a [Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) with **Read-Write** role


> ![warning](/docs/images/warning.svg)
> 
> **RudderStack recommends using a workspace-level Service Access Token for authentication.**
> 
> Any action authenticated by a Personal Access Token will break if the user is removed from the organization or a breaking change is made to their permissions.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Admin** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Admin permission](/docs/images/access-management/permissions/legacy/admin.webp)](</docs/images/access-management/permissions/legacy/admin.webp>)

## Run Airflow

Initialize all dependencies by running Apache Airflow via the following command:
    
    
    airflow standalone
    

> ![warning](/docs/images/warning.svg)
> 
> The Airflow standalone server is not meant for use in production. It is highly recommended using alternate methods to install and run Airflow in a production environment.

## Install Airflow operator

Install the RudderStack Airflow Provider by running the following command:
    
    
    pip install rudderstack-airflow-provider
    

## Create Airflow connection

To create a new Airflow connection, follow these steps:

  1. In your Airflow dashboard, go to **Admin** > **Connections** :

[![Airflow dashboard Connections option](/docs/images/warehouse-actions-sources/airflow-provider-1.webp)](</docs/images/warehouse-actions-sources/airflow-provider-1.webp>)

  2. Add a new connection by configuring the below settings:

[![Airflow dashboard edit connection](/docs/images/warehouse-actions-sources/airflow-provider-2.webp)](</docs/images/warehouse-actions-sources/airflow-provider-2.webp>)Setting| Description  
---|---  
**Connection ID**|  Specify a unique connection name. By default, `RudderstackRETLOperator` / `RudderstackProfilesOperator` uses the connection name `rudderstack_default`.  
  
**Note** : If you have created a connection with a different name, make sure that name is passed as a parameter to the above operators.  
**Connection Type**|  Set this to **HTTP**.  
**Host**|  Set the value depending on your region.  
  


  * **Standard (US)** : `https://api.rudderstack.com`
  * **EU** : `https://api.eu.rudderstack.com`

  
**Password**|  Enter your workspace-level Service Access Token.  
  
## RudderStack operators

Use the below operators to create DAGs and schedule them via Airflow.

> ![warning](/docs/images/warning.svg)
> 
> Make sure to set the [schedule type](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) to **Manual** in the RudderStack dashboard for both Reverse ETL syncs and Profiles jobs.
> 
> This way, the sync jobs can be triggered only via Airflow.

### RudderStackRETLOperator

Use `RudderStackRETLOperator` to schedule and trigger your Reverse ETL syncs via Airflow.

A simple DAG for triggering syncs for a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) is shown below. See this [example](<https://github.com/rudderlabs/rudder-airflow-provider/tree/main/examples>) for the complete code.
    
    
    with DAG(
        "rudderstack-retl-sample",
        default_args=default_args,
        description="A simple tutorial DAG for Reverse ETL",
        schedule_interval=timedelta(days=1),
        start_date=datetime(2021, 1, 1),
        catchup=False,
        tags=["rs-retl"],
    ) as dag:
        # retl_connection_id, sync_type are template fields
        rs_operator = RudderstackRETLOperator(
            retl_connection_id="<retl_connection_id>",
            task_id="<airflow_task_id>",
            connection_id="<connection_id>"
        )
    

The `RudderstackRETLOperator` parameters are described below:

Parameter| Description| Type| Default value  
---|---|---|---  
`retl_connection_id`  
Required| Your Reverse ETL Connection ID from the RudderStack dashboard.| String (templatable)| -  
`connection_id`  
Required| **Connection ID** used while setting up the Airflow connection.| String| `rudderstack_default`  
`task_id`  
Required| Unique, meaningful ID for the job. See the [Airflow documentation](<https://airflow.apache.org/docs/apache-airflow/1.10.9/_api/airflow/operators/index.html#package-contents>) for more information on this parameter.| String| -  
`poll_interval`| Time (in seconds) for the polling status of triggered job.| Float| `10`  
`poll_timeout`| Time (in seconds) after which the polling for a triggered job is declared timed out.| Float| None, that is, the provider keeps polling till the job completes or fails.  
`sync_type`| Sync type. Acceptable values are `full` and `incremental`.| String| `None` as RudderStack determines the sync type.  
`request_max_retries`| Maximum number of times requests to the RudderStack API should be retried before failing.| Integer| `3`  
`request_retry_delay`| Time (in seconds) to wait between each request retry.| Integer| `1`  
`request_timeout`| Time (in seconds) after which the requests to RudderStack are declared timed out.| Integer| `30`  
`wait_for_completion`| Determines if the execution run should poll and wait till sync completion.| Boolean| `True`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack recommends retaining the default values for the non-mandatory parameters.

### RudderStackProfilesOperator

Use `RudderstackProfilesOperator` to trigger a Profiles run.

A simple DAG for triggering a Profiles project run is shown:
    
    
    with DAG(
        "rudderstack-profiles-sample",
        default_args=default_args,
        description="A simple tutorial DAG for Profiles run.",
        schedule_interval=timedelta(days=1),
        start_date=datetime(2021, 1, 1),
        catchup=False,
        tags=["rs-profiles"],
    ) as dag:
        # profile_id is template field
        rs_operator = RudderstackProfilesOperator(
            profile_id="<profiles_id>",
            task_id="<airflow_task_id>",
            connection_id="<connection_id>",
        )
    

The `RudderstackRETLOperator` parameters are described below:

Parameter| Description| Type| Default value  
---|---|---|---  
`profiles_id`  
Required| Your Profiles project ID from the RudderStack dashboard.| String (templatable)| -  
`connection_id`  
Required| **Connection ID** used while setting up the Airflow connection.| String| `rudderstack_default`  
`task_id`  
Required| Unique, meaningful ID for the job. See the [Airflow documentation](<https://airflow.apache.org/docs/apache-airflow/1.10.9/_api/airflow/operators/index.html#package-contents>) for more information on this parameter.| String| -  
`parameters`| Additional parameters to pass to the Profiles run command, as supported by the API endpoint.| String| `None`  
`poll_interval`| Time (in seconds) for the polling status of triggered job.| Float| `10`  
`poll_timeout`| Time (in seconds) after which the polling for a triggered job is declared timed out.| Float| None, that is, the provider keeps polling till the job completes or fails.  
`request_max_retries`| Maximum number of times requests to the RudderStack API should be retried before failing.| Integer| `3`  
`request_retry_delay`| Time (in seconds) to wait between each request retry.| Integer| `1`  
`request_timeout`| Time (in seconds) after which the requests to RudderStack are declared timed out.| Integer| `30`  
`wait_for_completion`| Determines if the execution run should poll and wait till sync completion.| Boolean| `True`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack recommends retaining the default values for the non-mandatory parameters.

### Run a DAG

Once you have defined a DAG and configured an Airflow connection, run the following commands to allow Airflow to pick up and run the DAG:
    
    
    export AIRFLOW_HOME=</path/to/airflow_home>
    mkdir $AIRFLOW_HOME/dags
    cp rudderstack_dag.py $AIRFLOW_HOME/dags
    

**Make sure the Airflow scheduler is running in the background**. Also, you must enable the DAG in the Airflow dashboard:

[![enabling Airflow DAG in dashboard](/docs/images/warehouse-actions-sources/airflow-provider-3.webp)](</docs/images/warehouse-actions-sources/airflow-provider-3.webp>)

You can trigger a DAG by clicking on the play button on the right as seen above and selecting **Trigger DAG**.

> ![warning](/docs/images/warning.svg)
> 
> Stopping the DAG will **not** cancel the ongoing sync.

## Sample DAG

A sample DAG for a Profiles run followed by a Reverse ETL sync is shown:
    
    
    from datetime import timedelta
    
    from airflow import DAG
    
    from rudder_airflow_provider.operators.rudderstack import (
    	RudderstackRETLOperator,
    	RudderstackProfilesOperator
    )
    
    default_args = {
        'owner': 'airflow',
        'depends_on_past': False,
        'email': ['alex@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
    }
    
    with DAG('rudderstack-profiles-then-retl-sample',
        default_args=default_args,
        description='A simple tutorial DAG for Profiles run and then Reverse ETL sync.',
        catchup=False,
        tags=['rs']) as dag:
        # profile_id is a template field.
        profiles_task = RudderstackProfilesOperator(
            profile_id="{{ var.value.profile_id }}",
            task_id="<airflow_task_id>",
            connection_id="<connection_id>",
        )
        # retl_connection_id is a template field.
        retl_sync_1_task = RudderstackRETLOperator(
            retl_connection_id="{{ var.value.retl_connection_id1 }}",
            connection_id='<connection_id>',
            wait_for_completion=True,
            retry_delay=timedelta(seconds=5),
            retries=1,
        )
    	# another retl sync
        retl_sync_2_task = RudderstackRETLOperator(
            retl_connection_id="{{ var.value.retl_connection_id2 }}",
            task_id="<airflow_task_id>",
            connection_id='<connection_id>'',
            wait_for_completion=True
        )
    	
    	# run profiles_task, then retl_sync_1_task and retl_sync_2_task in parallel
    	profiles_task >> [retl_sync_1_task, retl_sync_2_task]
    	
    

## FAQ

#### Where can I find the connection ID for my Reverse ETL connection?

The connection ID is a unique identifier for any Reverse ETL connection set up in RudderStack.

To obtain the connection ID, click the destination connected to your Reverse ETL source and go to the **Settings** tab.

[![connection ID for Reverse ETL](/docs/images/retl-sources/connection-id.webp)](</docs/images/retl-sources/connection-id.webp>)

#### Where can I find my Profiles project ID?

To obtain the Profiles project ID, go to your project in the RudderStack dashboard and note it down from the URL:

[![](/docs/images/api/source-id.webp)](</docs/images/api/source-id.webp>)