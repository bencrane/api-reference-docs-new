# Feature Views

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Feature Views

Step-by-step tutorial on creating an feature view models.

* * *

  * __9 minute read

  * 


Once you have done [identity stitching](<https://www.rudderstack.com/docs/archive/profiles/0.12/core-concepts/identity-stitching/>) to unify the identity of your users across all the cross-platforms, you can evaluate and maintain the required features/traits for each identified user in a feature views.

This guide provides a detailed walkthrough on how to use a PB project and create output tables in a warehouse for an feature views model.

## Prerequisites

  * A basic Profile Builder project by following the [Profile Builder CLI](<https://www.rudderstack.com/docs/archive/profiles/0.12/get-started/profile-builder/>) steps.
  * [Structure](<https://www.rudderstack.com/docs/archive/profiles/0.12/cli-user-guide/structure/>) of a Profile Builder project and the parameters used in different files.
  * [Identity Stitching](<https://www.rudderstack.com/docs/archive/profiles/0.12/example/id-stitcher/>) model as Feature Views reuses its output to extract the required features/traits.


## Feature Views Model

Once traits are defined on an entity, we need the means to use them.

A primary application to send them to the downstream destinations. The destination could either be the [Activation API](<https://www.rudderstack.com/docs/archive/profiles/0.12/activation-api/>) or via any of the [rETL destinations](<https://www.rudderstack.com/docs/sources/reverse-etl/>) that RudderStack supports. Each such destination requires data in the form of a table with an ID column and 1 or more feature columns. This is possible using Feature Views.

Feature Views provides a way to access entity features based on any of the given ID types, including the entity main ID as the identifier column. It creates a view which will have all or a specified set of features on that entity from across the project.

To configure the creation of a specific set of feature views model, add `feature_views` section in the entity. You need to provide a list of ID types as `id_served`. Optionally, you can also give a name which specifies the name of the generated model. If you don’t specify a name, it will create the model with a default name. By default, it will add all available features on the entity into the view.

If you want finer control, you can also include or exclude any features from any models by defining a custom feature views model and add the reference to the `feature_views` section like `model_served: models/name_of_custom_traits_model`. See below on more examples of this.

### Default feature views model

`pb_project.yaml`:
    
    
    ...
    entities:
      - name: user
        id_types:
          - main_id
          - user_id
        feature_views:
          using_ids:
            - id: email
              name: features_by_email
            - id: salesforce_id
              name: salesforce_id_stitched_features
          features:
            - from: models/cart_feature_table
              include:
                - "*"
    

**Custom feature views model:**

This is an example of custom feature views model. Here we include or exclude features from models of choice.

`pb_project.yaml`:
    
    
    ...
    entities:
      - name: user
        id_types:
          - main_id
          - user_id
        feature_views:
          using_ids:
            - id: email
              name: features_by_email
            - id: salesforce_id
              name: salesforce_id_stitched_features
          features:
            - from: models/cart_feature_table
              include:
                - "*"
    

`models/profiles.yaml`:
    
    
    models:
      - name: cart_feature_views
        model_type: feature_views
        model_spec:
          validity_time: 24h # 1 day
          entity_key: user
          id_served: user_id
          feature_list:
            - from: packages/pkg/models/cart_table # a table created by package
              include: ["*"] # will include all the traits
            - from: models/user_var_table
              include: ["*"]
              exclude: [cart_quantity, purchase_status] # except two, all the other traits will be included
            - from: models/sql_model
              include: [lifetime_value] # will include only one trait
    

## Sample project

This sample project uses the output of an identity stitching model as an input to create a feature views. The following sections describe how to define your PB project files:

### Project detail

The [`pb_project.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.12/cli-user-guide/structure/#project-details>) file defines the project details such as name, schema version, connection name and the entities which represent different identifiers.

You can define all the identifiers from different input sources you want to stitch together as a `user_main_id`:

> ![warning](/docs/images/warning.svg)
> 
> You need to add `main_id` to the list only if you have defined `main_id_type: main_id` in the ID stitcher buildspec.
    
    
    # Project name
    name: sample_id_stitching
    # Project's yaml schema version
    schema_version: 61
    # Warehouse connection
    connection: test
    # Allow inputs without timestamps
    include_untimed: true
    # Folder containing models
    model_folders:
      - models
    # Entities in this project and their ids.
    entities:
      - name: user
        id_types:
          - main_id # You need to add ``main_id`` to the list only if you have defined ``main_id_type: main_id`` in the id stitcher buildspec.
          - user_id # one of the identifier from your data source.
          - email
    # lib packages can be imported in project signifying that this project inherits its properties from there
    packages:
      - name: corelib
        url: "https://github.com/rudderlabs/profiles-corelib/tag/schema_{{best_schema_version}}"
        # if required then you can extend the package definition such as for ID types.
    

### Input

The [input file](<https://www.rudderstack.com/docs/archive/profiles/0.12/cli-user-guide/structure/#inputs>) file includes the input table references and corresponding SQL for the above-mentioned entities:
    
    
    inputs:
    - name: rsIdentifies
      contract: # constraints that a model adheres to
        is_optional: false
        is_event_stream: true
        with_entity_ids:
          - user
        with_columns:
          - name: timestamp
          - name: user_id
          - name: anonymous_id
          - name: email
      app_defaults:
        table: rudder_events_production.web.identifies # one of the WH table RudderStack generates when processing identify or track events.
        occurred_at_col: timestamp
        ids:
          - select: "user_id" # kind of identity sql to pick this column from above table.
            type: user_id
            entity: user # as defined in project file
            to_default_stitcher: true
          - select: "anonymous_id"
            type: anonymous_id
            entity: user
            to_default_stitcher: true
          - select: "lower(email)" # can use sql.
            type: email
            entity: user
            to_default_stitcher: true
    - name: rsTracks
      contract:
        is_optional: false
        is_event_stream: true
        with_entity_ids:
          - user
        with_columns:
          - name: timestamp
          - name: user_id
          - name: anonymous_id
      app_defaults:
        table: rudder_events_production.web.tracks # another table in WH maintained by RudderStack processing track events.
        occurred_at_col: timestamp
        ids:
          - select: "user_id"
            type: user_id
            entity: user
            to_default_stitcher: true
          - select: "anonymous_id"
            type: anonymous_id
            entity: user
            to_default_stitcher: true
    

### Model

Profiles **feature views** model lets you define the specific features/traits you want to evaluate from the huge spread of scattered data in your warehouse tables.

A sample `profiles.yaml` file specifying a feature views model (`user_profile`):
    
    
    var_groups:
      - name: first_group
        entity_key: user
        vars:
          - entity_var:
              name: first_seen
              select: min(timestamp::date)
              from: inputs/rsTracks
              where: properties_country is not null and properties_country != ''
          - entity_var:
              name: last_seen
              select: max(timestamp::date)
              from: inputs/rsTracks
          - entity_var:
              name: user_lifespan
              select: '{{user.Var("last_seen")}} - {{user.Var("first_seen")}}'
              description: Life Time Value of a customer
          - entity_var:
              name: days_active
              select: count(distinct timestamp::date)
              from: inputs/rsTracks
              description: No. of days a customer was active
          - entity_var:
              name: campaign_source
              default: "'organic'"
          - entity_var:
              name: user_rank
              default: -1
          - entity_var:
              name: campaign_source_first_touch
              select: first_value(context_campaign_source)
              window:
                  order_by:
                      - timestamp asc
                  partition_by:
                      - main_id
              from: inputs/rsIdentifies
              where: context_campaign_source is not null and context_campaign_source != ''
          - input_var:
              name: num_c_rank_num_b_partition
              select: rank()
              from: inputs/tbl_c
              default: -1
              window:
                partition_by:
                  - '{{tbl_c}}.num_b'
                order_by:
                  - '{{tbl_c}}.num_c asc'
              where: '{{tbl_c}}.num_b >= 10'
          - entity_var:
              name: min_num_c_rank_num_b_partition
              select: min(num_c_rank_num_b_partition)
              from: inputs/tbl_c
    

**`entity_var`**

The `entity_var` field provides inputs for the feature views model. This variable stores the data temporarily, however, you can choose to store its data permanently by specifying the `name` in it as a feature in the `features` key.

Field| Data type| Description  
---|---|---  
`name`| String| Name of the `entity_var` to identify it uniquely.  
`select`| String| Column name/value you want to select from the table. This defines the actual value that will be stored in the variable. You can use simple SQL expressions or select an `entity_var` as `{{entityName.Var(\"entity_var\")}}`. It has to be an aggregate operation that ensures the output is a unique value for a given `main_id`. For example: min(timestamp), count(*), sum(amount) etc. This holds true even when a window function (optional) is used. For example:: first_value(), last_value() etc are valid while rank(), row_number(), etc. are not valid and give unpredictable results.  
`from`| List| Reference to the source table from where data is to be fetched. You can either refer to another model from the same YAML or some other table specified in input YAML.  
`where`| String| Any filters you want to apply on the input table before selecting a value. This must be SQL compatible and should consider the data type of the table.  
`default`| String| Default value in case no data matches the filter. When defining default values, make sure you enclose the string values in single quotes followed by double quotes to avoid SQL failure. However, you can use the non-string values without any quotes.  
`description`| String| Textual description of the `entity_var`.  
`window`| Object| Specifies the window function. Window functions in SQL usually have both `partition_by` and `order_by` properties. But for `entity_var`, `partition_by` is added with `main_id` as default; so, adding `partition_by` manually is not supported. If you need partitioning on other columns too, check out `input_var` where `partition_by` on arbitrary and multiple columns is supported.  
  
**`input_var`**

The syntax of `input_var` is similar to `entity_var`, with the only difference that instead of each value being associated to a row of the feature views, it’s associated with a row of the specified input. While you can think of an `entity_var` as adding a helper column to the feature views, you can consider an `input_var` as adding a helper column to the input.

Field| Data type| Description  
---|---|---  
`name`| String| Name to store the retrieved data.  
`select`| String| Data to be stored in the name.  
`from`| List| Reference to the source table from where data is to be fetched.  
`where`| String| (Optional) Applies conditions for fetching data.  
`default`| String| (Optional) Default value for any entity for which the calculated value would otherwise be NULL.  
`description`| String| (Optional) Textual description.  
`window`| Object| (Optional) Specifies a window over which the value should be calculated.  
  
**`window`**

Field| Data type| Description  
---|---|---  
`partition_by`| String| (Optional) List of SQL expressions to use in partitioning the data.  
`order_by`| String| (Optional) List of SQL expressions to use in ordering the data.  
  
In window option, `main_id` is not added by default, it can be any arbitrary list of columns from the input table. So if a feature should be partitioned by `main_id`, you must add it in the `partition_by` key.

### Output

After [running the project](<https://www.rudderstack.com/docs/archive/profiles/0.12/get-started/profile-builder/#7-generate-output-tables>), you can view the generated material tables.

  1. Log in to your Snowflake console.
  2. Click **Worksheets** from the top navigation bar.
  3. In the left sidebar, click **Database** and the corresponding **Schema** to view the list of all tables. You can hover over a table to see the full table name along with its creation date and time.
  4. Write a SQL query like `select * from <table_name>` and execute it to see the results:


  1. Open [Postico2](<https://eggerapps.at/postico2/>). If required, create a new connection by entering the relevant details. Click **Test Connection** followed by **Connect**.
  2. Click the **+** icon next to **Queries** in the left sidebar.
  3. You can click **Database** and the corresponding schema to view the list of all tables/views.
  4. Double click on the appropriate view name to paste the name on an empty worksheet.
  5. You can prefix `SELECT *` from the view name pasted previously and suffix `LIMIT 10;` at the end.
  6. Press Cmd+Enter keys, or click the **Run** button to execute the query.


  1. Enter your Databricks workspace URL in the web browser and log in with your username and password.
  2. Click the **Catalog** icon in left sidebar.
  3. Choose the appropriate catalog from the list and click on it to view contents.
  4. You will see list of tables/views. Click the appropriate table/view name to paste the name on worksheet.
  5. You can prefix `SELECT * FROM` before the pasted view name and suffix `LIMIT 10;` at the end.
  6. Select the query text. Press Cmd+Enter, or click the **Run** button to execute the query.


  1. Log in to your [Google Cloud Console](<https://console.cloud.google.com/>)
  2. Search for Bigquery in the search bar.
  3. Select Bigquery from **Product and Pages** to open the Bigquery **Explorer**.
  4. Select the correct project from top left drop down menu.
  5. In the left sidebar, click the project ID, then the corresponding dataset view list of all the tables and views.
  6. Write a SQL query like `select * from <table_name> limit 10;` and execute it to see the results.


A sample output containing the results in Snowflake:

![Generated table \(Snowflake\)](/docs/images/profiles/profiles-feature-table.webp)

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.12/example/feature-table/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.12/example/sql-model/>)