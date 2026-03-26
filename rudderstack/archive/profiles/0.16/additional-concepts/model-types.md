# Model Types

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Model Types

Know more about the types of models in RudderStack Profiles.

* * *

  * __2 minute read

  * 


Each Profiles model is a prepackaged SQL model that takes your inputs and runs in the warehouse to generate the defined views and tables. RudderStack provides the following model types for Profiles:

## Identity Stitcher

[Identity stitcher](<https://www.rudderstack.com/docs/archive/profiles/0.16/example/id-stitcher/>) model stitches the different identifiers of an entity to create unified and comprehensive profiles.
    
    
    model_type: id_stitcher
    

## Var groups

Var groups are the group of variables which contain individual entity variables within them. You can have multiple var groups where each `var_group` is directly connected to either an entity or a cohort of an entity.
    
    
    var_groups:
      - name: user_vars
        entity_key: user
        vars:
          - entity_var:
              name: first_seen
              select: min(timestamp::date)
              from: inputs/rsTracks
              where: properties_country is not null and properties_country != ''
          - input_var:
              name: num_c_rank_num_b_partition
              select: rank()
              from: inputs/tbl_c
              where: "{{tbl_c}}.num_b >= 10"
    

### Entity_vars

The `entity_var` model outputs the computed traits per `main_id`, and adds it back to the entity var table. This table then serves as the base for other feature creation models. See [Input Var Vs. Entity Var](<https://www.rudderstack.com/docs/archive/profiles/0.16/additional-concepts/input-entity-var/>) for more information.

### Input_vars

The `input_var` model takes the input var table, derives a new column, and adds it back to the input var table. For example, if your original input var table had 20 columns and you defined an `input_var` where the input was the same source, then after the next run, your input var table would have 21 columns. The model modifies the original input var table by adding an additional column which can be used for feature calculation if needed. See [Input Var Vs. Entity Var](<https://www.rudderstack.com/docs/archive/profiles/0.16/additional-concepts/input-entity-var/>) for more information.

## Feature table (Deprecated)

[Feature table](<https://www.rudderstack.com/docs/archive/profiles/0.16/example/feature-table/>) model creates features from the `entity_var` definitions and outputs a table/view that has the `main_id` as the primary key (one unique row per entity).
    
    
    model_type: feature_table_model
    

## Feature view

[Feature view](<https://www.rudderstack.com/docs/archive/profiles/0.16/example/feature-views/>) model collects and displays all the computed traits for your entity. You can activate them later directly, or use a filter pipeline to create a smaller subset of users as a cohort.
    
    
    model_type: feature_view
    

## Cohort

You can use [cohorts](<https://www.rudderstack.com/docs/archive/profiles/0.16/cohorts/>) to create a subset of entity instances meeting a specified set of characteristics, behaviors, or attributes.
    
    
    model_type: entity_cohort
    

## SQL model

[SQL models](<https://www.rudderstack.com/docs/archive/profiles/0.16/example/sql-model/>) are suited for advanced use cases where you want to have a model that does some intermediary transformations, joins, or unions before that data is consumed by the identity stitcher or feature creation models.
    
    
    model_type: sql_template
    

## Python model

You can use the [python model](<https://www.rudderstack.com/docs/archive/profiles/0.16/predictions/#python-model>) to generate predictive features.
    
    
    model_type: python_model
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.16/additional-concepts/packages/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.16/additional-concepts/manage-models/>)