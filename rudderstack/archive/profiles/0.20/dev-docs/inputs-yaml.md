# inputs.yaml

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# inputs.yaml

Learn how to define and map input sources for your Profiles project.

* * *

  * __2 minute read

  * 


The [`inputs.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.20/concepts/inputs/>) file contains the configuration of all input sources used in Profiles. This includes the ID graph, entity vars, feature view, etc.
    
    
    inputs:
        - name: input_name
          app_defaults:
            table: schema.table # Key must be only one of table/view/s3/csv
            occurred_at_col: time_series_column
            row_identifier: [list of identifiers for composite key]    # Optional
            ids:
                <id-config>
          where: <filtering_condition>
    

Key| Description  
---|---  
`name`  
Required| The input name.  
`contract`| Helps you handle any potential errors if the required column doesn’t exist.  
  
| Key| Description  
---|---  
`is_optional`| Boolean that indicates if the model is optional.  
`is_event_stream`| Boolean indicating if the data is Event Stream (contains a `timestamp` column).  
`with_entity_ids`| List of all entities.  
`with_columns`| List of all ID columns that the contract is applicable for.  
`app_defaults`  
Required| Input configuration.  
`table`\ `view`\ `s3`\ `csv`  
Required| Source name, see input sources.  
`occurred_at_col`  
Required| Time series column.  
`row_identifier`| List of all the identifiers that combine to create a composite primary key.  
[`ids`](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/inputs-yaml/identifiers/>)  
Required| All IDs in the input source, mapped to `entities` and `id_types`  
`where`| The `WHERE` clause specifying the filtering condition.  
  
**Note** : The filtered row will not be considered for ID stitching as well.  
  
## Input sources

A source can be a warehouse table, view, Amazon S3 bucket, or CSV file. Only one key can be used per source.

Key| Description  
---|---  
`table`| Warehouse table name  
  
You can also refer to tables from other databases/schemas in the same data warehouse.  
`view`| Warehouse view name.  
`csv`| CSV file path. Note that this path should be relative to the project folder.  
  
**Note** : RudderStack recommends using CSV file as an input only if you have limited amount of data.  
[`s3`](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/inputs-yaml/s3-bucket-input/>)| Amazon S3 URI path.  
  
  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.20/dev-docs/profiles-yaml/cohorts/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.20/dev-docs/inputs-yaml/identifiers/>)