# Orchestration Integrations

* * *

  *  __less than a minute

  * 


RudderStack’s orchestration integrations let you manage [Profiles](<https://www.rudderstack.com/docs/profiles/overview/>) and [Reverse ETL](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/>) jobs in your orchestration platform.

> ![info](/docs/images/info.svg)
> 
> RudderStack supports [Apache Airflow](<https://www.rudderstack.com/docs/data-pipelines/orchestration/airflow/>) and [Dagster](<https://www.rudderstack.com/docs/data-pipelines/orchestration/dagster/>) currently.

## Use cases

You can use the orchestration integrations to orchestrate your Profiles jobs, Reverse ETL syncs, or both.

Use case| Description| Example  
---|---|---  
**Profiles jobs**|  Trigger a Profiles project run when a dependent ETL or other load job completes successfully.| When an `ORDERS` table loads, you want to run your Profiles project so that your `customer_lifetime_value` and `total_orders` features are updated in the customer 360 table.  
**Reverse ETL jobs**|  Trigger a Reverse ETL sync when a transformation job runs successfully.| When a dbt model runs successfully, you can sync the output to a business tool automatically.  
**Profiles and Reverse ETL jobs**|  Trigger a Reverse ETL sync when a Profiles job runs successfully.| You want to automatically update marketing and sales tools with the latest known user information from Profiles.