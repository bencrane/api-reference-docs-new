# SQL Models

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# SQL Models

Step-by-step tutorial on how to create a SQL Template model.

* * *

  * __9 minute read

  * 


This guide provides a detailed walkthrough on how to use a PB project and create SQL Template models using custom SQL queries.

## Why use SQL models?

You can use the custom SQL models to achieve the advanced use cases. For example, you can use a model that performs some intermediary transformations, joins, or unions on some data before feeding it to the ID stitcher or feature creation models. This model can then act as an input to the downstream models.

You can also configure the custom SQL models to produce features which are further used by the feature view model. However, you must ensure that the output of SQL model contains single row for each entity-item in that case.

## Use cases

**Example 1**  


Let’s assume that your company has an iOS app as well as a website. Within your data plane, you have both the sources feeding data via the native SDKs to your database. Further, Profiles takes that data as an input to generate profiles.

You want to create a `first_seen` feature so that you know the timestamp when each user was first seen. You could select an input and do a min(timestamp) function in the `entity_var` definition.

However, to be truly accurate, you need to take into account the timestamp for both the app and the website. Did a user first download the app and later visited the website? Or did a visit to the website lead to the download of app? Where were they truly seen first? This is where a SQL model should be used.

The solution would be to union the `PAGE` and `TRACKS` tables together into a new model. Then, use that model as the `entity_var` data input. Now, when the `first_seen` feature is calculated, it will take into account both the data sources where the user would have been discovered.

A sample SQL model is shown below:
    
    
    models:
      - name: rsTracksUnionPages
        model_type: sql_template
        model_spec:
          materialization:
            output_type: ephemeral
            run_type: discrete
          single_sql: |
            {% with Tracks = this.DeRef("models/rsTracks") Pages = this.DeRef("models/rsPages") %}
                select user_id, anonymous_id, context_session_id, timestamp from (
                select ANONYMOUS_ID::text as ANONYMOUS_ID,USER_ID::text as USER_ID,timestamp::date as dt,CONTEXT_SESSION_ID,min(timestamp) as timestamp from {{Tracks}} group by user_id, anonymous_id, context_session_id, timestamp::date
                union all
                select ANONYMOUS_ID::text as ANONYMOUS_ID,USER_ID::text as USER_ID,timestamp::date as dt,CONTEXT_SESSION_ID,max(timestamp) as timestamp from {{Tracks}} group by user_id, anonymous_id, context_session_id, timestamp::date)
                union all
                select user_id, anonymous_id, context_session_id, timestamp from
                (select ANONYMOUS_ID::text as ANONYMOUS_ID,USER_ID::text as USER_ID,timestamp::date as dt,CONTEXT_SESSION_ID, min(timestamp) as timestamp from {{Pages}} group by user_id, anonymous_id, context_session_id, timestamp::date
                union all
                select ANONYMOUS_ID::text as ANONYMOUS_ID,USER_ID::text as USER_ID,timestamp::date as dt,CONTEXT_SESSION_ID,  max(timestamp) as timestamp from {{Pages}} group by user_id, anonymous_id, context_session_id, timestamp::date)
            {% endwith %}        
          ids:
            - select: "user_id"
              type: user_id
              entity: ce_user
            - select: "anonymous_id"
              type: anonymous_id
              entity: ce_user
          contract:
            is_optional: false
            is_event_stream: false
            with_entity_ids:
              - ce_user
            with_columns:
              - name: user_id
              - name: anonymous_id
    

**Example 2**  


Consider that you have an online retail B2C company that has a Shopify store. Now, you want to create a suite of features based off of customer’s carts for things like, `most_recent_cart_items`, `most_recent_purchase`, `total_gross_sales`, etc.

RudderStack provides a custom `tracks` table for an `ORDER_COMPLETED` event. However, the cart `items` property is a nested array of json objects in string format. This is not compatible for feature calculations. Additionally, depending on the features, the data level that the source table is on might also be incompatible. The source table is on the order level but you may need this on the line item level.

The solution is to create a SQL model to take the original input, and transform it into the format compatible for downstream feature calculations. In this case, you need to cast the `products` object as JSON and flatten it. The output table will be a line item table where each order ID may be duplicated if there is more than one line item purchased.

A sample SQL model is shown below:
    
    
    models:
      - name: cart_line_items
        model_type: sql_template
        model_spec:
          materialization:
            output_type: table
            run_type: discrete
          single_sql: |
            {% with CartUpdate = this.DeRef("inputs/CART_UPDATE") %}
            SELECT to_char(t.value['brand']) AS brand,
                t.value['discounted_price'] AS discounted_price,
                to_char(t.value['gift_card']) AS gift_card,
                t.value['grams'] AS grams,
                to_char(t.value['id']) AS id,
                to_char(t.value['key']) AS KEY,
                t.value['line_price'] AS line_price,
                t.value['original_line_price'] AS original_line_price,
                t.value['original_price'] AS original_price,
                t.value['price'] AS price,
                to_char(t.value['product_id']) AS product_id,
                to_char(t.value['properties']) AS properties,
                t.value['quantity'] AS quantity,
                to_char(t.value['sku']) AS sku,
                to_char(t.value['taxable']) AS taxable,
                to_char(t.value['title']) AS title,
                t.value['total_discount'] AS total_discount,
                to_char(t.value['variant']) AS _VARIANT_,
                products,
                anonymous_id,timestamp,
                token
            FROM
            (SELECT *
            FROM
                (SELECT *,
                        row_number() over(PARTITION BY anonymous_id, token
                                                    ORDER BY timestamp DESC) AS rn
                FROM {{CartUpdate}} where products is not null)
            WHERE rn = 1), table(flatten(parse_json(products))) t
                    {% endwith %}        
          ids:
            - select: "anonymous_id"
              type: anonymous_id
              entity: shopify_customer
          contract:
            is_optional: false
            is_event_stream: false
            with_entity_ids:
              - shopify_customer
            with_columns:
              - name: anonymous_id
    

## Prerequisites

  * Familiarize yourself with:

    * A basic Profile Builder project by following the [Profile Builder CLI](<https://www.rudderstack.com/docs/archive/profiles/0.18/get-started/profile-builder/>) steps.
    * [Structure](<https://www.rudderstack.com/docs/archive/profiles/0.18/cli-user-guide/structure/>) of a Profile Builder project and the parameters used in different files.


## Sample project

The following sections describe how to define your PB project files:

### Project detail

The [`pb_project.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.18/cli-user-guide/structure/#project-details>) file defines the project details such as name, schema version, connection name and the entities which represent different identifiers.

You can define all the identifiers from different input sources you want to stitch together as a single ID (`main_id` in this example):
    
    
    name: sample_test
    schema_version: 80
    connection: test
    model_folders:
      - models
    entities:
      - name: user
        id_stitcher: models/test_id__
        id_types:
          - test_id
          - exclude_id
    id_types:
      - name: test_id
        filters:
          - type: include
            regex: "([0-9a-z])*"
          - type: exclude
            value: ""
      - name: exclude_id
    

### Input

The [input file](<https://www.rudderstack.com/docs/archive/profiles/0.18/cli-user-guide/structure/#inputs>) (`models/inputs.yaml`) file includes the input table references and corresponding SQL for the above-mentioned entities:
    
    
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

A sample `profiles.yaml` file specifying a `single_sql` type SQL model:
    
    
    models:
    - name: test_sql
      model_type: sql_template
      model_spec:
        materialization:                 // optional
          run_type: discrete             // optional [discrete, incremental]
        single_sql: |
            {%- with input1 = this.DeRef("inputs/tbl_a") -%}
              SELECT 
                  id1 AS new_id1, 
                  id2 AS new_id2, 
                  {{input1}}.*
              FROM {{input1}}
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
    

A sample `profiles.yaml` file specifying a `multi_sql` type SQL model:
    
    
    models:
    - name: test_sql
        model_type: sql_template
        model_spec:
          materialization:
            output_type: table
            run_type: discrete
          multi_sql: |
            {% with input_material1 = this.DeRef("models/test_sql1") input_material2 = this.DeRef("inputs/tbl_a") input_material3 = this.DeRef("inputs/tbl_c") %}
              create {{this.GetMaterialization().OutputType.ToSql()}} {{this}} as (
                select b.id1, b.id2, b.id3, b.insert_ts, a.new_id1, a.num_a, c.num_b, c.num_c
                from {{ input_material1 }} a
                full outer join {{ input_material2 }} b
                on a.id2 = b.id2
                full outer join {{ input_material3 }} c
                on c.id2 = a.id2
              );
            {% endwith  %}        
    

> ![info](/docs/images/info.svg)
> 
> A `multi_sql` type SQL model only creates a table as an output type in a warehouse whereas `single_sql` type SQL model supports all the output types (deafult is `ephemeral`). See [materialization](<https://www.rudderstack.com/docs/archive/profiles/0.18/resources/glossary/#materialization>) for more information.

##### Model specification fields

Field| Data type| Description  
---|---|---  
`name`| String| Name of the SQL model. You can also refer this as an input as `models/test_sql`.  
`model_type`| String| Defines the type of model.  
`model_spec`| Object| Contains the specifications for the target model.  
`materialization`| List| Adds the key `run_type`: `incremental` to run the project in incremental mode. This mode considers row inserts and updates from the edge_sources input. These are inferred by checking the timestamp column for the next run. One can provide buffer time to consider any lag in data in the warehouse for the next incremental run like if new rows are added during the time of its run. If you do not specify this key then it’ll default to `run_type`: `discrete`.  
`single_sql`| List| Specifies the SQL template which must evaluate to a single SELECT SQL statement. After execution, it should produce a dataset which will materialize based on the provided materialization.  
`multi-sql`| List| Specifies the SQL template which can evaluate to multiple SQL statements. One of these SQL statements (typically the last one) must be a CREATE statement which shall be responsible for materializing the model into a table.  
  
**Note** : You should set only one of `single_sql` or `multi_sql`.  
`occurred_at_col`| List| Name of the column which contains the timestamp value in the output of SQL template.  
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
        SELECT
            t.a AS new_a,
            t.b AS new_b,
            t.*
        FROM {{input_table}} AS t
    {% endwith %}
    

  * `GetMaterialization()`: Returns a structure with two fields: `MaterializationSpec{OutputType, RunType}`.
    * `OutputType`: You must use `OutputType` with `ToSQL()` method:  
For example, `CREATE OR REPLACE {{this.GetMaterialization().OutputType.ToSQL()}} {{this.GetSelectTargetSQL()}} AS ...`
    * `RunType`: For example, `this.GetMaterialization().RunType`


## Refer SQL contents from another file

If you want to edit a SQL query in a text editor and not as a field in a YAML file, you can use the `ReadFile` method. It refers to the SQL contents stored in another file:
    
    
    models:
    - name: example_sql_model
      model_type: sql_template
      model_spec:
        materialization:
          output_type: view
          run_type: discrete
        single_sql: "{%exec%} {{ this.ReadFile('models/compute.sql') }} {%endexec%}" # for a SQL file named compute.sql in the models folder
        occurred_at_col: insert_ts
    

## Refer SQL model in a cohort

You can use features of an SQL model while using a cohort. To do so, specify the `entity_key` or `entity_cohort` in the `model_spec` of an SQL model.

## See Also

Create user features using SQL models:

  * [Profiles Stripe features project](<https://github.com/rudderlabs/pb_sample_features>)
  * [Profiles Shopify features project](<https://github.com/rudderlabs/profiles-shopify-features>)


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.18/example/feature-views/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.18/example/predictive-features-snowflake/>)