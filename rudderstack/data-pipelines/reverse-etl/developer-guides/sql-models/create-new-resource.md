# Create New SQL Model Resource using Rudder CLI Alpha

Create a new SQL model resource using Rudder CLI.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


This guide walks you through the process of creating a new SQL model resource from scratch using Rudder CLI.

## Prerequisites

  * Rudder CLI tool [installed and authenticated](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/#install-rudder-cli>) with your [Service Access Token](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/#get-started>)
  * A Rudder CLI project directory for storing the SQL model YAML resources
  * **Important** : At least one [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in the RudderStack dashboard using the data warehouse you want to query — RudderStack uses the connection credentials used to set up the warehouse account this source to fetch the account ID. An example is shown below:

[![Connection credentials for PostgreSQL source](/docs/images/retl-sources/postgres-connection-credentials.webp)](</docs/images/retl-sources/postgres-connection-credentials.webp>)

## List Reverse ETL accounts

Before creating a SQL model resource, identify the account ID for the warehouse you want to connect to.

Use the following command to list all accounts linked to your workspace:
    
    
    ./rudder-cli workspace accounts list
    

This command displays all available accounts along with their IDs. Make note of the account ID that corresponds to your target warehouse — you will need this for the resource configuration.

## Create the resource file

Create a new YAML file in your project folder containing the SQL model configuration. This file should have the following structure:
    
    
    version: "rudder/v0.1"
    kind: "retl-source-sql-model"
    metadata:
      name: "product-purchases-model"
    spec:
      id: "product-purchases-mode"
      display_name: "Product Purchases SQL Model"
      primary_key: "user_id"
      description: "SQL model for product purchases"
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
          pruduct_id
        FROM 
          user_events
        WHERE 
          timestamp >= CURRENT_DATE() - INTERVAL 180 DAY
        ORDER BY 
          timestamp DESC    
    

See the [SQL Model YAML reference](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/yaml-reference/>) for more details on the parameters.

## SQL query options

RudderStack provides two options for defining your SQL query:

### Inline SQL
    
    
    sql: |
      SELECT 
        user_id, 
        event_name
      FROM 
        user_events  
    

### External file reference
    
    
    file: "./queries/my-query.sql"
    

> ![warning](/docs/images/warning.svg)
> 
> You must use exactly one of `sql` or `file` — they are mutually exclusive.

### Supported sources

The `source_definition` field in the `spec` parameter supports the below warehouses:

Warehouse| `source_definition` value  
---|---  
PostgreSQL| `postgres`  
MySQL| `mysql`  
Snowflake| `snowflake`  
Redshift| `redshift`  
BigQuery| `bigquery`  
Databricks| `databricks`  
Trino| `trino`  
  
## Apply the SQL model

Once you have created the resource file, use the following commands to validate and create the SQL model:

### Validate configuration
    
    
    ./rudder-cli validate -l path/to/project
    

### Dry run
    
    
    ./rudder-cli apply -l path/to/project --dry-run
    

The above command lists the changes that would be applied without actually making them.

### Apply changes
    
    
    ./rudder-cli apply -l path/to/project
    

After successful application, the SQL model will be created in your workspace and you can manage it through the CLI.

## Update the SQL model

You can modify any field in the YAML file of your existing SQL model — including `source_definition`.

> ![warning](/docs/images/warning.svg)
> 
> Changing the `id` field will delete the existing resource and create a new one.

To apply the updates, repeat the validation and apply commands listed above:
    
    
    ./rudder-cli validate -l path/to/project
    ./rudder-cli apply -l path/to/project --dry-run  # Optional: Preview changes
    ./rudder-cli apply -l path/to/project
    

## Best practices

  * **Use external files** : For complex queries, use the `file` option to keep your SQL in separate `.sql` files for better syntax highlighting and version control.
  * **Descriptive IDs** : Choose clear, descriptive IDs that reflect the model’s purpose.
  * **Test first** : Always run the validation and dry-run commands before applying any changes.


## Next steps

  * [Import existing SQL model resources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/import-existing-resource/>)
  * [Validate and preview your SQL models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/validate/>)
  * [YAML reference](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/yaml-reference/>)