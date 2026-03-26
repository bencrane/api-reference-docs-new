# Warehouse Destinations

Send event data from RudderStack to your specified data warehouse platforms.

* * *

  * __2 minute read

  * 


RudderStack supports integration with all leading data warehouses. Now you can set up these warehouses as destinations in RudderStack and send all your event data from your preferred sources.

## Warehouse destinations

[![Amazon Redshift logo](/docs/images/logos/destinations/redshift.svg)Amazon Redshift](</docs/destinations/warehouse-destinations/redshift/>)[![Azure Synapse logo](/docs/images/logos/destinations/azure-synapse.svg)Azure Synapse](</docs/destinations/warehouse-destinations/azure-synapse/>)[![ClickHouse logo](/docs/images/logos/destinations/clickhouse.svg)ClickHouse](</docs/destinations/warehouse-destinations/clickhouse/>)[![Google BigQuery logo](/docs/images/logos/destinations/bigquery.svg)Google BigQuery](</docs/destinations/warehouse-destinations/bigquery/>)[![Materialize logo](/docs/images/logos/destinations/materialize.webp)Materialize](</docs/destinations/warehouse-destinations/materialize/>)[![Microsoft SQL Server logo](/docs/images/logos/destinations/sql-server.webp)Microsoft SQL Server](</docs/destinations/warehouse-destinations/sql-server/>)[![PostgreSQL logo](/docs/images/logos/destinations/postgresql.svg)PostgreSQL](</docs/destinations/warehouse-destinations/postgresql/>)[![Snowflake logo](/docs/images/logos/destinations/snowflake.svg)Snowflake](</docs/destinations/warehouse-destinations/snowflake/>)[![Snowflake Streaming logo](/docs/images/logos/destinations/snowflake.svg)Snowflake Streaming](</docs/destinations/warehouse-destinations/snowflake-streaming/>)

  


## Data lake destinations

[![Amazon S3 Data Lake logo](/docs/images/logos/destinations/s3-datalake.svg)Amazon S3 Data Lake](</docs/destinations/warehouse-destinations/s3-datalake/>)[![Azure Data Lake logo](/docs/images/logos/destinations/azure-datalake.svg)Azure Data Lake](</docs/destinations/warehouse-destinations/azure-datalake/>)[![Databricks Delta Lake logo](/docs/images/logos/destinations/databricks.webp)Databricks Delta Lake](</docs/destinations/warehouse-destinations/delta-lake/>)[![Google Cloud Storage Data Lake logo](/docs/images/logos/destinations/gcs.svg)Google Cloud Storage Data Lake](</docs/destinations/warehouse-destinations/gcs-datalake/>)

  


## Warehouse schema

When sending your events to a data warehouse via RudderStack, you don’t need to define a schema for your event data - RudderStack automatically does that for you by following a predefined [warehouse schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>).

## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to create and manage destinations.
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can have the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) depending on their workspace policy:

Permission| Description  
---|---  
Edit| Make changes to the configuration of destinations  
Connect| Connect a destination to a source or transformation  
Create & Delete| Create or delete destinations  
Retry Syncs| Retry syncs for a destination in case of failures  
  
> ![warning](/docs/images/warning.svg)
> 
> To make a connection, that is, connect a source to a destination, the member must have both **Edit** and **Connect** permissions on both the resources.

#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>):

  * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) and members with the [**Connections Admin** role](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#connections>) in their workspace policy can create and delete destinations, manage their configuration, and connect them to sources
  * Members with the [**Connections Editor** role](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#connections>) in their workspace policy can only edit the destination configuration and connect destinations to sources

[![Destinations permissions in the legacy framework](/docs/images/access-management/data-catalog-permissions-legacy-framework.webp)](</docs/images/access-management/data-catalog-permissions-legacy-framework.webp>)

## FAQ

Refer to the comprehensive [FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide for the solutions to some of the commonly-asked questions around the RudderStack warehouse integrations.