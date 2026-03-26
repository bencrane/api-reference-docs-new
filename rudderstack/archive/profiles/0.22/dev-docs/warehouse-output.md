# Warehouse Output

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Warehouse Output

Learn about the tables and views generated in your warehouse once your Profiles project runs successfully.

* * *

  * __less than a minute

  * 


Upon a successful run, the Profiles project creates a series of tables and views in your warehouse.

## Views

The final output from Profiles are views that, after each run, are updated to the most recent materialized tables. This allows you to always work with the most recent data without having to change code.

### ID Graph

The name of your ID graph’s output is the name defined in your model spec. The name of the resolved `rudder_id` is `{ENTITY}_MAIN_ID` by default.
    
    
    USER_MAIN_ID,
    OTHER_ID,
    OTHER_ID_TYPE,
    VALID_AT,
    FIRST_SEEN_AT
    

### Cohorts

`{ENTITY}_ALL`

`{ENTITY}_{COHORT_NAME}`

Using the names defined in [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/cohorts/>).
    
    
    USER_MAIN_ID
    

### Feature views

`{ENTITY}_{FEATURE_VIEW_NAME}`

Using the names defined in [`pb_project.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/pb-project-yaml/entities/>) for entities and [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/cohorts/>) for cohorts.
    
    
    USER_MAIN_ID,
    <FEATURES>
    

Features named defined in [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/>).

## Tables

Profiles creates a series of materialized tables that feed into the final views. RudderStack **does not recommend** using these tables directly as they are tied to individual runs.

These table include:

  * [Entity var](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/entity-var/>) tables
  * [Input var](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/input-var/>) tables
  * Edges tables
  * Mapping tables


Note that the tables use the format: `Material_<name>_<HASH>_<seq_no>`.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.22/dev-docs/run-project/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.22/dev-docs/activation-api/>)