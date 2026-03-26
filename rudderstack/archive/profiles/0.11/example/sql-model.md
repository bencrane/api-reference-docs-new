# SQL Models

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# SQL Models

Step-by-step tutorial on how to create a SQL Template model.

* * *

  * __5 minute read

  * 


This guide provides a detailed walkthrough on how to use a PB project and create SQL Template models using custom SQL queries.

## Prerequisites

  * Familiarize yourself with:

    * A basic Profile Builder project by following the [Profile Builder CLI](<https://www.rudderstack.com/docs/archive/profiles/0.11/get-started/profile-builder/>) steps.
    * [Structure](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/structure/>) of a Profile Builder project and the parameters used in different files.


## Sample project

The following sections describe how to define your PB project files:

### Project detail

The [`pb_project.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/structure/#project-details>) file defines the project details such as name, schema version, connection name and the entities which represent different identifiers.

You can define all the identifiers from different input sources you want to stitch together as a single ID (`main_id` in this example):
    
    
    name: sample_test
    schema_version: 54
    connection: test
    model_folders:
      - models
    entities:
      - name: user
        id_stitcher: models/test_id__
        id_types:
          - test_id
          - exclude_id
    include_untimed: true
    id_types:
      - name: test_id
        filters:
          - type: include
            regex: "([0-9a-z])*"
          - type: exclude
            value: ""
      - name: exclude_id
    

### Input

The [input file](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/structure/#inputs>) (`models/inputs.yaml`) file includes the input table references and corresponding SQL for the above-mentioned entities:
    
    
    inputs:
      - name: tbl_a
        app_defaults:
          table: Temp_tbl_a
        occurred_at_col: insert_ts
        ids:
          - select: TRIM(COALESCE(NULL, id1))
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "id2"
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "id3"
            type: exclude_id
            entity: user
            to_default_stitcher: true
      - name: tbl_b
        app_defaults:
          view: Temp_view_b
        occurred_at_col: timestamp
        ids:
          - select: "id1"
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "id2"
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "id3"
            type: test_id
            entity: user
            to_default_stitcher: true
      - name: tbl_c
        app_defaults:
          table: Temp_tbl_c
        ids:
          - select: "id1"
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "id2"
            type: test_id
            entity: user
            to_default_stitcher: true
    

### Model

Profiles **SQL model** lets you write custom SQL queries to achieve advanced use-cases to create desired output tables.

A sample `profiles.yaml` file specifying a SQL model (`test_sql`):
    
    
    models:
    - name: test_sql
      model_type: sql_template
      model_spec:
        validity_time: 24h# 1 day
        materialization:                 // optional
          run_type: discrete             // optional [discrete, incremental]
        single_sql: |
            {%- with input1 = this.DeRef("inputs/tbl_a") -%}
              select id1 as new_id1, id2 as new_id2, {{input1}}.*
                from {{input1}}
            {%- endwith -%}        
        occurred_at_col: insert_ts        // optional
        ids:
          - select: "new_id1"
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "new_id2"
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "id3"
            type: test_id
            entity: user
            to_default_stitcher: true
    

##### Model specification fields

Field| Data type| Description  
---|---|---  
`validity_time`| Time| Time Specifies the validity of the model with respect to its timestamp. For example, a model run as part of a scheduled nightly job for 2009-10-23 00:00:00 UTC with `validity_time`: `24h` would still be considered potentially valid and usable for any run requests, which do not require precise timestamps between 2009-10-23 00:00:00 UTC and 2009-10-24 00:00:00 UTC. This specifies the validity of generated feature table. Once the validity is expired, scheduling takes care of generating new tables. For example: 24h for 24 hours, 30m for 30 minutes, 3d for 3 days.  
`materialization`| List| Adds the key `run_type`: `incremental` to run the project in incremental mode. This mode considers row inserts and updates from the edge_sources input. These are inferred by checking the timestamp column for the next run. One can provide buffer time to consider any lag in data in the warehouse for the next incremental run like if new rows are added during the time of its run. If you do not specify this key then it’ll default to `run_type`: `discrete`.  
`single_sql`| List| Specifies the SQL template which must evaluate to a single SELECT SQL statement. After execution, it should produce a dataset which will materialize based on the provided materialization.  
`multi-sql`| List| Specifies the SQL template which can evaluate to multiple SQL statements. One of these SQL statements (typically the last one) must be a CREATE statement which shall be responsible for materializing the model into a table.  
  
**Note** : You should set only one of `single_sql` or `multi_sql`.  
`occurred_at_col`| List| Name of the column which contains the timestamp value in the output of sql template.  
`ids`| List| Specifies the list of all IDs present in the source table along with their column names (or column SQL expressions). It is required in case you want to use SQL models as an input to the `input_var` or `entity_var` fields.  
  
## SQL template

You can pass custom SQL queries to the `single_sql` or `multi_sql` fields, which is also known as a **SQL template**. It provides the flexibility to write custom SQL by refering to any of the input sources listed in the `inputs.yaml` or any model listed in `models/profiles.yaml`.

The SQL templates follow a set query syntax which serves the purpose of creating a model. Follow the below rules to write SQL templates:

  * Write SQL templates in the [pongo2 template engine](<https://pkg.go.dev/github.com/flosch/pongo2#readme-first-impression-of-a-template>) syntax.

  * Avoid circular referencing while referencing the models. For example, `sql_model_a` references `sql_model_b` and `sql_model_b` references `sql_model_a`.

  * Use `timestamp` variable (refers to the start time of the current run) to filter new events.

  * `this` refers to the current model’s material. You can use the following methods to access the material properties available for `this`:

    * `DeRef("path/to/model")`: Use this syntax `{{ this.DeRef("path/to/model") }}` to refer to any model and return a database object corresponding to that model. The database object, in return, gives the actual name of the table/view in the warehouse. Then, generate the output, for example:
    
    {% with input_table = this.DeRef("inputs/tbl_a") %}
        select a as new_a, b as new_b, {{input_table}}.*
          from {{input_table}}
    {% endwith %}
    

    * `GetMaterialization()`: Returns a structure with two fields: `MaterializationSpec{OutputType, RunType}`.
      * `OutputType`: You must use `OutputType` with `ToSQL()` method:  
For example, `CREATE OR REPLACE {{this.GetMaterialization().OutputType.ToSQL()}} {{this.GetSelectTargetSQL()}} AS ...`
      * `RunType`: For example, `this.GetMaterialization().RunType`


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/example/entity-traits-360/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/example/packages/>)