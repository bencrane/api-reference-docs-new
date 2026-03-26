# Validate SQL Model Resource using Rudder CLI Alpha

Validate and preview SQL model resources using Rudder CLI.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


This guide covers how to validate configurations and preview query results using Rudder CLI.

## Prerequisites

  * Rudder CLI tool [installed and authenticated](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/#install-rudder-cli>) with your access token
  * A CLI project directory with SQL model resources
  * Access to the data warehouses referenced by your models


## Overview

The Rudder CLI provides powerful validation and preview capabilities that help you test your SQL models before deploying them to production.

The preview feature allows you to execute your SQL queries and see the results before applying changes to your workspace — this is helpful for testing query logic and ensuring data quality.

## Preview command

Run the below command to preview a specific SQL model resource:
    
    
    ./rudder-cli retl-sources preview campaigns-cli -l path/to/project --limit 10
    

When you run a preview command, Rudder CLI:

  1. **Validates connection** : Confirms it can connect to the specified data warehouse.
  2. **Executes query** : Runs your SQL query against the warehouse.
  3. **Returns results** : Shows you a sample of the query results.


> ![success](/docs/images/tick.svg)
> 
> You can also use the `preview` command to validate that the primary key column is present in the result set.

### Command parameters

The following table lists the parameters for the preview command:

Parameter| Description  
---|---  
Resource ID| The first argument specifies which SQL model to preview — it uses the `id` value from your YAML file  
`-l` or `--location`| Path to your project directory  
`--limit`| Number of rows to fetch  
  
**Default value** : 100 — RudderStack returns an error if this value is exceeded  
`-j` or `--json`| Output results in JSON format instead of table format  
`--interactive`| Controls whether output should be in interactive mode  
  
**Default value** : true  
  
### Preview command examples

The following example demonstrates the key parameters available with the preview command:
    
    
    ./rudder-cli retl-sources preview api-test-10 --location path/to/project --limit 5 -j --interactive=false
    

The above command:

  * Previews the SQL model with ID `api-test-10`
  * Uses `path/to/project` as the location for the CLI project directory
  * Limits results to 5 rows using `--limit 5`
  * Outputs results in JSON format using `-j`
  * Runs in non-interactive mode using `--interactive=false`


## Validation

Validation ensures your SQL model configurations are correct before deployment. It performs comprehensive checks without executing the full query.

### Validate a specific resource
    
    
    ./rudder-cli retl-sources validate campaigns-cli -l path/to/project
    

### What validation checks

The validation process verifies:

**SQL Syntax**

  * Ensures your SQL query is syntactically correct
  * Validates it’s compatible with your specified warehouse type


**Connectivity**

  * Tests connection to the specified account/warehouse
  * Verifies authentication and permissions


**Configuration integrity**

  * Validates all required fields are present and properly formatted
  * Ensures account ID references exist and are accessible


**Query execution (limited)**

  * Tests that the query can execute without errors
  * May run a limited version of the query to validate structure


## Best practices

This section provides best practices for using validation and preview in your development and CI/CD workflows.

### Development workflow

  * **Write query** : Create or modify your SQL in the YAML or SQL file.
  * **Validate first** : Run validation to check syntax and configuration.
  * **Dry run** : Use `--dry-run` with `apply` commands to see what will change.
  * **Preview results** : Use preview to verify query logic and results.
  * **Iterate** : Refine your query based on preview results.
  * **Final validation** : Run validation once more before committing.


### CI/CD pipeline

  * **Always validate** : Include validation in your automated checks.
  * **Limited preview** : Use preview sparingly in CI/CD due to performance implications.


## Troubleshooting

This section provides troubleshooting tips for common issues you may encounter when using validation and preview.

### Common validation errors

Issue| Resolution steps  
---|---  
Account not found| 

  * Verify the `account_id` exists in your workspace
  * Check your CLI is authenticated with the correct workspace

  
SQL Syntax Error| 

  * Review your query syntax for the specific warehouse type
  * Test the query directly in your warehouse’s query interface

  
Primary Key Column Missing| 

  * Ensure your query returns a column with the name specified in `primary_key`
  * Check for typos in column names

  
Connection Timeout| 

  * Verify network connectivity to your warehouse
  * Check if warehouse credentials need renewal

  
  
### Error handling

Error| Resolution steps  
---|---  
Connection issues| Check account credentials and network connectivity  
SQL errors| Review query syntax and warehouse-specific SQL dialect requirements  
Primary key issues| Ensure the specified primary key column exists in your query results  
Timeout issues| Simplify complex queries for validation, optimize for production  
  
### Performance considerations

Issue| Resolution steps  
---|---  
Large result sets| 

  * Use smaller `--limit` values for initial testing
  * Consider adding `WHERE` clauses to reduce data volume during development

  
Complex queries| 

  * Break down complex queries into simpler parts for testing
  * Use preview to validate intermediate steps

  
Resource usage| 

  * Preview commands consume warehouse compute resources
  * Be mindful of costs when running against production warehouses

  
  
## See also

  * [Create new SQL model resources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/create-new-resource/>)
  * [Import existing SQL model resources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/import-existing-resource/>)
  * [YAML reference](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/yaml-reference/>)