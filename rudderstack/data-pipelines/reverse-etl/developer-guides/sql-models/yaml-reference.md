# SQL Model Resources YAML Reference Alpha

Complete reference for defining your SQL model resources using YAML configuration files.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __5 minute read

  * 


This guide serves as a detailed reference for the CLI project YAML files that contain definitions of your Reverse ETL SQL model resources.

## Overview

In the context of the Rudder CLI (`rudder-cli`) tool, SQL model resources are defined using YAML files that specify the configuration for your [Reverse ETL SQL model sources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>). These YAML files enable you to manage your SQL models through a Git-based workflow with version control and collaboration features.

The location and naming of these YAML files is flexible, as you can store the YAML files anywhere within the project’s root directory or subdirectories.

> ![success](/docs/images/tick.svg)
> 
> You can also group multiple SQL model resources in the same file, allowing structures that can best serve your project’s requirements.
> 
> The Rudder CLI tool processes all valid YAML files within the project structure to recognize the defined resources.

The following sections detail the specific YAML formats and parameter definitions for SQL model resources.

## SQL model resources

You can define one or more SQL model resources in the YAML file by setting `kind` to `retl-source-sql-model`.

The `spec` parameter of the YAML file has the following structure:

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique identifier for the SQL model resource within the project. This parameter must be unique across all SQL model resources.  
`display_name`  
Required| String| Display name for the SQL model resource as shown in the RudderStack dashboard.  
`primary_key`  
Required| String| Column name to use as the primary key for the model. This column must exist in your SQL query results.  
`source_definition`  
Required| String| Warehouse type identifier.  
  
See Supported warehouse types for values that you can use.  
`enabled`  
Required| Boolean| Whether the SQL model resource is active. Set to `true` to enable the resource.  
`account_id`  
Required| String| The account ID for the data warehouse connection. You can obtain this using `./rudder-cli workspace accounts list`.  
`description`| String| Optional description for the SQL model resource.  
`sql`| String| Inline SQL query definition.  
  
Use the YAML literal block scalar `  
`file`| String| Path to an external SQL file containing the query. Path is relative to the YAML file location.  
  
> ![warning](/docs/images/warning.svg)
> 
> You must use exactly one of `sql` or `file` — they are mutually exclusive. Use `sql` for inline queries or `file` to reference external SQL files.

### Supported warehouse types

The `source_definition` field supports the following data warehouse types:

Warehouse| `source_definition` value  
---|---  
PostgreSQL| `postgres`  
MySQL| `mysql`  
Snowflake| `snowflake`  
Amazon Redshift| `redshift`  
Google BigQuery| `bigquery`  
Databricks| `databricks`  
Trino| `trino`  
  
### Example definitions

The following examples highlight the YAML configurations for SQL model resources defined using inline SQL and external SQL files. You can group multiple resources in the same YAML file to manage them together.
    
    
    version: "rudder/v0.1"
    kind: "retl-source-sql-model"
    metadata:
      name: "product-purchases-model"
    spec:
      id: "product-purchases-model"
      display_name: "Product Purchases SQL Model"
      primary_key: "user_id"
      description: "SQL model for tracking product purchases over the last 180 days"
      source_definition: "postgres"
      enabled: true
      account_id: "2rzPI1ARibivIvNH5DSpAKGTATy"
      sql: |
        SELECT 
          user_id, 
          event_name, 
          event_type,
          timestamp,
          properties,
          product_id
        FROM 
          user_events
        WHERE 
          timestamp >= CURRENT_DATE() - INTERVAL 180 DAY
          AND event_name = 'Product Purchased'
        ORDER BY 
          timestamp DESC    
    
    
    
    version: "rudder/v0.1"
    kind: "retl-source-sql-model"
    metadata:
      name: "user-analytics-model"
    spec:
      id: "user-analytics-model"
      display_name: "User Analytics Model"
      primary_key: "user_id"
      description: "Comprehensive user analytics model"
      source_definition: "snowflake"
      enabled: true
      account_id: "2rzPI1ARibivIvNH5DSpAKGTATy"
      file: "./queries/user-analytics.sql"
    

In this example, the SQL query would be stored in a separate file at `./queries/user-analytics.sql` relative to the YAML file location.
    
    
    version: "rudder/v0.1"
    kind: "retl-source-sql-model"
    metadata:
      name: "ecommerce-models"
    spec:
      - id: "product-views-model"
        display_name: "Product Views Model"
        primary_key: "user_id"
        description: "Model for tracking product page views"
        source_definition: "bigquery"
        enabled: true
        account_id: "2rzPI1ARibivIvNH5DSpAKGTATy"
        sql: |
          SELECT 
            user_id,
            product_id,
            view_timestamp,
            session_id
          FROM 
            product_views
          WHERE 
            view_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)      
      - id: "cart-abandonment-model"
        display_name: "Cart Abandonment Model"
        primary_key: "session_id"
        description: "Model for identifying cart abandonment events"
        source_definition: "bigquery"
        enabled: true
        account_id: "2rzPI1ARibivIvNH5DSpAKGTATy"
        file: "./queries/cart-abandonment.sql"
    

## Best practices

When defining SQL model resources in YAML files, follow these best practices:

### File organization

  * **Logical grouping** : Group related SQL models in the same YAML file when they share similar purposes or data sources.
  * **Clear naming** : Use descriptive file names that reflect the models’ purpose, such as `user-analytics-models.yaml` or `ecommerce-models.yaml`.
  * **Directory structure** : Organize SQL files in subdirectories (like `./queries/` or `./sql/`) to keep your project structure clean.


### Resource configuration

  * **Unique IDs** : Choose clear, descriptive IDs that reflect the model’s purpose and avoid conflicts.
  * **Meaningful names** : Use display names that clearly describe what the model does for dashboard users.
  * **Documentation** : Always include descriptions to help team members understand the model’s purpose.
  * **External files** : For complex queries, use the `file` option to keep SQL in separate files for better syntax highlighting and version control. When importing resources, use the `--sql-location` parameter if you prefer external SQL files.


### Environment management

  * **Variable substitution** : Consider using variable substitutions for `account_id` values when working across multiple environments (development, staging, or production).
  * **Environment-specific configurations** : Maintain separate configuration files or use templating for environment-specific settings.


### Query optimization

  * **Primary key selection** : Choose primary keys that are unique, stable, and efficiently indexed in your warehouse.
  * **Performance considerations** : Write efficient queries that minimize warehouse compute costs and execution time.
  * **Data freshness** : Include appropriate date filters to control data volume and ensure relevance.


## See also

  * [Create new SQL model resources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/create-new-resource/>)
  * [Import existing SQL model resources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/import-existing-resource/>)
  * [Validate and preview your SQL models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/validate/>)
  * [Manage SQL models using Rudder CLI](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/>)