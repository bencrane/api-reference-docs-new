# Manage models

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Manage models

Manage Profiles models efficiently by performing different model operations.

* * *

  * __6 minute read

  * 


While using the Profiles models, you can apply certain operations on them by defining the model contracts, enable/disable run of a model, reuse models output, etc.

## Model contracts

You can use the `contract` field to specify the constraints your model should adhere to while using the warehouse data.

Suppose a model (`M1`) is dependent on model (`M2`). Now, `M1` can specify a contract defining the columns and entities that it needs from `M2` to be executed successfully. Also, it becomes mandatory for `M2` to provide the required columns and entities for contract validation.

**Example 1**

The following `inputs.yaml` file defines a contract:
    
    
    - name: rsIdentifies
      contract:
        is_optional: false
        is_event_stream: true
        with_entity_ids:
          - user
        with_columns:
          - name: timestamp
          - name: user_id
          - name: anonymous_id
    

Here, the contract specifies that:

  * The input table (`rsIdentifies`) must exist in the warehouse.
  * The model is an event stream model where every row in the table must be an event.
  * There must be a column in the inputs table (`rsIdentifies`) which represents the user identifier for `user` entity.
  * The input table (`rsIdentifies`) must have the `timestamp`, `user_id`, and `anonymous_id` columns.


**Example 2**

Let’s consider a SQL model, `rsSessionTable` which takes `shopify_session_features` as an input:
    
    
    models:
    - name: rsSessionTable
      model_type: sql_template
      model_spec:
        ... # model specifications
        single_sql: |
          {% set contract = BuildContract('{"with_columns":[{"name":"user_id"}, {"name":"anonymous_id"}]}') %}
          {% with SessionFeature = this.DeRef("models/shopify_session_features",contract)%}
              select user_id as id1, anonymous_id as id2 from {{SessionFeature}}      
        contract:
          with_entity_ids:
            - user
          with_columns:
            - name: user_id
              type: string
            - name: anonymous_id
              type: string
    

There are two contracts defined in the above example:

  * Contract for `shopify_session_features` model which dictates that the `user_id`, and `anonymous_id` columns must be present.
  * Contract for `rsSessionTable` model which dictates that it must have a column representing the user identifier for `user` entity. Also, the `user_id`, and `anonymous_id` columns must be present.


This helps in improving the data quality, error handling, and enables static and dynamic validation of the project.

## Enable/disable model run

When you have various interdependent models, you might want to run only the required ones for a specific output.

RudderStack provides the `enable_status` parameter which lets you specify whether to run a model or not. Using it, you can exclude the unnecessary models from the execution process. You can assign the following values to the `enable_status` field in your `pb_project.yaml` file:

  * `good_to_have` (default): It will not execute or cause a failure when it is not possible to execute the model.
  * `must_have`: It will cause a failure when is not possible to execute the model.
  * `only_if_necessary`: The model gets disabled if it has no dependency on the final output. It is the default value for a default ID stitcher model and ensures that the model is not executed if it is not required.
  * `disabled`: The model gets disabled and is not executed.


A sample `pb_project.yaml` file with `enable_status` parameter:
    
    
    name: app_project
    schema_version: 71
    connection: test
    model_folders:
      - models
    entities:
      - name: user
        id_types:
          - user_id
          - anonymous_id
        default_id_stitcher:
          validity_time: 24h # 1 day
          materialization:
            run_type: incremental
            enable_status: good_to_have
          incremental_timedelta: 12h # half a day
    
    id_types:
      - name: user_id
        filters:
          - type: include
            regex: "([0-9a-z])*"
          - type: exclude
            value: ""
      - name: anonymous_id
    

**Use-case**

Consider a scenario where an ID stitcher model (`ids`) is dependent on `tbl_a` and `tbl_b`, and a feature table model (`ft1`) depends on the ID Stitcher (`ids`) and an input model `tbl_a`.

  * If the ID stitcher and feature table models are marked as `only_if_necessary`, there is no need to execute either of them. However, if the feature table is marked as `good_to_have`/`must_have`, then all the models must run to create final output.
  * If `tbl_a` is set to `disabled`, the ID stitcher and feature table will not run. If either of them is marked as `must_have`, the project will run into an error.


## Reuse models output

> ![warning](/docs/images/warning.svg)
> 
> This is an experimental feature.

You can define the `time_grain` parameter for a model to ensure the model runs only once in that time period. It lets you reuse the output material of that model within the time period, preventing unnecessary recalculations⁠.

For example, if you set the `time_grain` value for an ID stitcher model to a `day` and run the feature table model (based on the ID stitcher) multiple times during a day, the feature table model will reuse the ID stitcher’s output to compute the features. This will save a large amount of time and computations whenever you run the feature table model within that day.

Similarly, you can choose to run a feature such as `weekly_spends` only once a week, or `last_active_day` on a daily basis.

> ![warning](/docs/images/warning.svg)
> 
> Setting `time_grain` parameter does not mean that the model will run automatically at the specified time period. It just ensures that the model runs only once during that time period and its outputs are reused within that duration. To schedule your project run, you must use the RudderStack dashboard.
> 
> For example, if `time_grain` for a model is set to a `week`, its outputs will be reused throughout the week and running it twice within the week won’t change its results.

You can define the `time_grain` parameter in the `profiles.yaml` file of your project:
    
    
    models:
      - name: user_id_graph
        model_type: id_stitcher
        model_spec:
          entity_key: user
          time_grain: "hour"
          materialization:
            run_type: incremental
          edge_sources:
            - from: inputs/rsIdentifies
            - from: inputs/rsTracks
    var_groups:
      - name: user_daily_vars
        time_grain: "day"
        entity_key: user
        vars:
          - entity_var:
              name: days_since_last_seen
              select: "{{macro_datediff('{{user.Var(\"max_timestamp\")}}')}}"
      - name: user_weekly_vars
        time_grain: "week"
        entity_key: user
        vars:
          - entity_var:
             name: weekly_amt_spent
             select: sum(total_price_usd) - coalesce(sum(total_price_usd_order_cancelled), 0)
             from: models/rsOrderCreatedOrderCancelled
             where: "{{macro_datediff_n('timestamp','7')}}"
    

In the above example, suppose you schedule your Profiles project to run every hour. The output for `user_id_graph` model will be computed every hour, the output for `user_daily_vars` will be computed once a day, and the output for `user_weekly_vars` will be computed once a week.

For a default ID stitcher model, you can define the `time_grain` value in the `entities` section as shown below:
    
    
    entities:
      - name: user
        id_types:
          - test_id
          - exclude_id
        default_id_stitcher:
          time_grain: "day"
    

#### Supported values

You can set the following values for the `time_grain` field:

  * `tick`: Considers all the data up to the current moment (default value).
  * `10minutes`: Considers data up to the last 10-minute interval.
  * `hour`: Considers data up to the end of the previous hour.
  * `day`: Considers data up to the end of the previous day.
  * `week`: Considers data up to the end of the previous week.
  * `month`: Considers data up to the end of the previous month.
  * `year`: Considers data up to the end of the previous year.


## Execute SQL before/after running a model

A pre hook enables you to execute an SQL before running a model, for example, if you want to change DB access, create a DB object, etc. Likewise, a post hook enables you to execute an SQL after running a model. The SQL can also be templatized. Here’s an example code snippet:
    
    
    models:
      - name: test_id_stitcher
        model_type: id_stitcher
        hooks:
          pre_run: "CREATE OR REPLACE VIEW {{warehouse.ObjRef('V1')}} AS (SELECT * from {{warehouse.ObjRef('Temp_tbl_a')}});"
          post_run: 'CREATE OR REPLACE VIEW {{warehouse.ObjRef("V2")}} AS (SELECT * from {{warehouse.ObjRef("Temp_tbl_a")}});'
        model_spec:
          - # rest of model specs go here
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.16/additional-concepts/model-types/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.16/additional-concepts/multi-version/>)