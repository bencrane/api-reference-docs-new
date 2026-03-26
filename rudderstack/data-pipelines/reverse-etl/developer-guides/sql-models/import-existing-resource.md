# Import Existing SQL Model Resource using Rudder CLI Alpha

Import an existing SQL model resource using Rudder CLI.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


This guide explains how to import existing SQL model resources from your workspace into your CLI project. This allows you to bring existing resources under version control and manage them through Git workflows.

## Prerequisites

  * Rudder CLI tool [installed and authenticated](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/#install-rudder-cli>) with your access token
  * A CLI project directory for storing the SQL model YAML resources
  * Existing SQL model resources in your workspace


## List available SQL model resources

First, identify which SQL model resources are available in your workspace for import:
    
    
    ./rudder-cli workspace retl-sources list
    

This command lists all SQL model resources in your workspace. Make note of the `source_id` for the resource you want to import — you will need this in the next step.

## Import the resource

Use the `import` command to bring an existing resource into your CLI project — this command creates a YAML file that describes the imported resource.

RudderStack provides two ways to import an existing resource:

  * Import the resource with inline SQL
  * Import the resource with an external SQL file


#### Import the resource with inline SQL

To import the resource with inline SQL, use the `import` command without the `--sql-location` flag, as shown:
    
    
    ./rudder-cli import retl-sources --local-id api-test-10 --remote-id 2zMxxCKnGqkQLHffzCCIAvvxBso -l ./path/to/project
    

By default, the generated file will have the following format with inline SQL:
    
    
    version: "rudder/v0.1"
    kind: "retl-source-sql-model"
    metadata:
      import:
        workspaces:
          - workspace_id: "2dgUfFqnI6LFhlDmYPd8mA4Xrnc"
            resources:
              - local_id: "api-test-10"
                remote_id: "2zMwvwOG8zYJoJRHdmtN2ka1VUY"
      name: "api-test-10"
    spec:
      account_id: "2rzPI1ARibivIvNH5DSpAKGTATy"
      description: ""
      display_name: "api-test-10"
      enabled: true
      id: "api-test-10"
      primary_key: "id"
      source_definition: "postgres"
      sql: |
        SELECT 
          user_id, 
          event_name, 
          timestamp
        FROM 
          user_events
        WHERE 
          timestamp >= CURRENT_DATE() - INTERVAL 30 DAY    
    

#### Import the resource with an external SQL file

To store the SQL query in a separate file while importing the resource, use the `--sql-location` parameter, as shown:
    
    
    ./rudder-cli import retl-sources --local-id api-test-10 --remote-id 2zMxxCKnGqkQLHffzCCIAvvxBso -l ./path/to/project --sql-location ./sql/api-test-10.sql
    

This command creates a YAML file that references the external SQL file:
    
    
    version: "rudder/v0.1"
    kind: "retl-source-sql-model"
    metadata:
      import:
        workspaces:
          - workspace_id: "2dgUfFqnI6LFhlDmYPd8mA4Xrnc"
            resources:
              - local_id: "api-test-10"
                remote_id: "2zMwvwOG8zYJoJRHdmtN2ka1VUY"
      name: "api-test-10"
    spec:
      account_id: "2rzPI1ARibivIvNH5DSpAKGTATy"
      description: ""
      display_name: "api-test-10"
      enabled: true
      id: "api-test-10"
      primary_key: "id"
      source_definition: "postgres"
      file: "./sql/api-test-10.sql"
    

See the [SQL Model YAML reference](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/yaml-reference/#import-metadata>) for more details on the above parameters.

### Important considerations

  * The `metadata.import` section tracks the relationship between your local CLI resource and the remote workspace resource. This enables the CLI to sync changes properly.
  * By default, the SQL query is stored inline in the YAML file using the `sql` field.
  * If you use the `--sql-location` parameter, the import process creates a separate `.sql` file containing the SQL query and references it using the `file` field.
  * All current settings from your workspace resource are captured in the `spec` section.


## Import command parameters

The following table lists the parameters for the `import` command:

Parameter| Description  
---|---  
`--local-id`  
Required| The name you want to use for this resource in your CLI project  
`--remote-id`  
Required| The source ID from your workspace obtained from the list command  
`-l` or `--location`  
Required| Path to your project directory  
`--sql-location`| Path where you want to save the SQL query as an external file. If not provided, the SQL query will be stored inline in the YAML file  
  
## Sync the imported resource

After generating the resource file, run the `apply` command to complete the import process:
    
    
    ./rudder-cli validate -l path/to/project      # Validate changes
    ./rudder-cli apply -l path/to/project --dry-run  # Preview changes
    ./rudder-cli apply -l path/to/project         # Apply changes
    

After successful application, the SQL model will be created in your workspace and you can manage it through the CLI.

Once imported, you can modify any field in the YAML file. Changes are applied to the workspace resource when you run the `apply` command.

### Delete resources

If you remove the YAML file from your project, the next `apply` command will delete the SQL model from your workspace. Therefore, be cautious with this operation.

## Troubleshooting

Issue| Resolution steps  
---|---  
Import fails| 

  * Verify the `remote-id` exists and is accessible in your workspace
  * Ensure you have proper permissions to read the resource
  * Confirm that the `local-id` does not conflict with existing resources

  
Apply command fails after import| 

  * Ensure the YAML file is present and properly formatted
  * If using the `--sql-location` flag, ensure both the YAML file and the generated SQL file are present
  * Verify your CLI is authenticated and has access to the workspace
  * Confirm that no manual changes were made to the resource in the UI after import

  
  
## Best practices

  * **Consistent naming** : Use descriptive `local-id` values that reflect the resource’s purpose.
  * **Immediate sync** : Always run the apply command immediately after import to establish proper tracking.
  * **Commit together** : If using the `--sql-location` flag, commit both the YAML and SQL files together to maintain consistency.
  * **Environment planning** : Consider how to handle different environments before importing multiple resources.


## Next steps

  * [Create new SQL model resources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/create-new-resource/>)
  * [Validate and preview your SQL models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/validate/>)
  * [YAML reference](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/yaml-reference/>)