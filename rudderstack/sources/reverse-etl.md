# Reverse ETL Sources

Enrich your data stack with data from your Reverse ETL sources.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


RudderStack’s **Reverse ETL** feature lets you use the customer data residing in your data warehouse and route it to your entire data stack, including analytics, sales, and marketing tools.

With this feature, you can set up your data warehouse as a source in the [RudderStack dashboard](<https://app.rudderstack.com/>), specify the data to import, then sync it to your desired destination.

> ![info](/docs/images/info.svg)
> 
> You can set up to 10 connections in the RudderStack [Free and Starter](<https://www.rudderstack.com/pricing/>) plan and unlimited connections in the [Growth and Enterprise](<https://www.rudderstack.com/pricing/>) plans.

## Supported Reverse ETL Sources

[![Amazon Redshift logo](/docs/images/logos/sources/redshift.svg)Amazon Redshift](</docs/sources/reverse-etl/amazon-redshift/>)[![Amazon S3 logo](/docs/images/logos/sources/s3.svg)Amazon S3](</docs/sources/reverse-etl/amazon-s3/>)[![Databricks logo](/docs/images/logos/sources/databricks.webp)Databricks](</docs/sources/reverse-etl/databricks/>)[![Google BigQuery logo](/docs/images/logos/sources/bigquery.svg)Google BigQuery](</docs/sources/reverse-etl/google-bigquery/>)[![MySQL logo](/docs/images/logos/sources/mysql.webp)MySQL](</docs/sources/reverse-etl/mysql/>)[![PostgreSQL logo](/docs/images/logos/sources/postgresql.svg)PostgreSQL](</docs/sources/reverse-etl/postgresql/>)[![Snowflake logo](/docs/images/logos/sources/snowflake.svg)Snowflake](</docs/sources/reverse-etl/snowflake/>)[![Trino logo](/docs/images/logos/sources/trino.webp)Trino](</docs/sources/reverse-etl/trino/>)

## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage Reverse ETL sources created via warehouse tables, [SQL Models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>), and [Audiences](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/>).
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can have the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) depending on their workspace policy:

Permission| Description  
---|---  
Edit| Make changes to the configuration of Reverse ETL sources  
Connect| Connect a Reverse ETL source to a destination  
Create & Delete| Create or delete Reverse ETL sources in the workspace  
  
> ![warning](/docs/images/warning.svg)
> 
> To make a connection, that is, connect a source to a destination, the member must have both **Edit** and **Connect** permissions on both the resources.

**Click here to see how these permissions appear in the workspace policy**.  
![Permissions to manage Reverse ETL sources in RudderStack dashboard](/docs/images/access-management/reverse-etl.webp)  


#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>):

  * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) and members with the [**Connections Admin** role](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#connections>) in their workspace policy can create and delete Reverse ETL sources, and connect them to destinations
  * Members with the [**Connections Editor** role](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#connections>) in their workspace policy can only edit the Reverse ETL source configuration and connect Reverse ETL sources to destinations

[![Reverse ETL sources permissions in the legacy framework](/docs/images/access-management/data-catalog-permissions-legacy-framework.webp)](</docs/images/access-management/data-catalog-permissions-legacy-framework.webp>)

## FAQ

For answers to commonly asked questions around the Reverse ETL feature, see [FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>).