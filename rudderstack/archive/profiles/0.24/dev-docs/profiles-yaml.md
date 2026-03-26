# profiles.yaml

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# profiles.yaml

Learn about the `profiles.yaml` file that defines the Profiles semantic models.

* * *

  * __less than a minute

  * 


The `profiles.yaml` file defines the Profiles semantic models using `models` and `var_groups`.

  * `models` are defined by the `model_type` and consist of prepackaged SQL code that takes your inputs and runs it in your warehouse to output the defined views and tables.
  * `var_groups` define `entity_var` and `input_var` used to define the [features](<https://www.rudderstack.com/docs/archive/profiles/0.24/concepts/features/>) for [feature views](<https://www.rudderstack.com/docs/archive/profiles/0.24/concepts/feature-views/>).


    
    
    models:
      <model-config>
    var_groups:
      <var-group-config>
    

Key| Description  
---|---  
`model_config`  
Required| Model configuration - see the specific model for details.  
[`var_group`](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/profiles-yaml/var-groups/>)  
Required| Configuration for the features.  
  
## Models

  * [`identity_stitcher`](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/profiles-yaml/id-stitcher/>)
  * [`entity_cohort`](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/profiles-yaml/cohorts/>)
  * [`sql_template`](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/sql-model-yaml/sql-model-config/>)
  * [Data Apps](<https://www.rudderstack.com/docs/archive/profiles/0.24/data-apps/>)


## Example
    
    
    models:
        - name: user_id_stitcher
            model_type: identity_stitcher
            model_spec:
                entity_key: user
                materialization:
                   run_type: incremental
                edge_sources:
                    - from: inputs/rsIdentifies
                    - from: inputs/rsTracks
    var_groups:
        name: user_features
        entity_key: user #Name as defined in the project file.
        vars:
            - entity_var:
              name: first_seen
              select: min(timestamp::date)
              from: inputs/rsTracks
              description: First user appearance
            - entity_var:
              name: last_seen
              select: max(timestamp::date)
              from: inputs/rsTracks
              is_feature: false
            - entity_var:
              name: user_lifespan
              select: '{{user.last_seen}} - {{user.first_seen}}'
              description: Lifespan of a user
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.24/dev-docs/pb-project-yaml/id-types/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.24/dev-docs/profiles-yaml/id-stitcher/>)