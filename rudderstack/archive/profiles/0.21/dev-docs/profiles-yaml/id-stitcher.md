# ID Stitcher

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# ID Stitcher

Learn about the ID stitcher model in Profiles.

* * *

  * __less than a minute

  * 


The [ID stitcher](<https://www.rudderstack.com/docs/archive/profiles/0.21/concepts/identity-graph/>) model maps and unifies all the specified identifiers across `inputs`. It tracks the user journey uniquely across all the data sources and stitches them together to a `rudder_id`.

You can define an ID stitcher in the [pb_project.yaml](<https://www.rudderstack.com/docs/archive/profiles/0.21/dev-docs/pb-project-yaml/>) file:
    
    
    models:
        - name: model_name
          model_type: `id_stitcher`
          model_spec:
              entity_key: entity_name
              materialization:
                  run_type: discrete/incremental
              incremental_timedelta: 96h
              edge_sources:
                  - from: path/to_inputs_table
                  - from: path/to_inputs_table
    

Field| Description  
---|---  
`name`| Model name.  
`model_type`| Model type - set this parameter to `id_stitcher` to implement an ID stitcher.  
`model_spec`| Defines the model configuration.  
`entity_key`| Specifies the entity to stitch.  
`run_type`| Run type - set this parameter to `discrete` or `incremental`. (Default is incremental).  
`incremental_timedelta`| In incremental ID stitching, only events from the last run are typically processed to update the ID graph. However, since events can arrive in the warehouse with delays, this parameter adds a buffer period to ensure completeness. The ID stitcher will process events starting from `incremental_timedelta` before the last run timestamp, creating an overlap window to capture any delayed events. Default value: 4 days (96 hours).  
`edge_sources`| List of inputs from [`inputs.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.21/dev-docs/inputs-yaml/>) and [`sql-models.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.21/dev-docs/sql-model-yaml/>) used for identity stitching.  
  
## Example
    
    
    models:
        - name: user_id_stitcher
          model_type: id_stitcher
          model_spec:
              entity_key: user
              materialization:
                  run_type: incremental
              incremental_timedelta: 96h
              edge_sources:
                  - from: inputs/rsIdentifies
                  - from: inputs/rsTracks
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.21/dev-docs/profiles-yaml/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.21/dev-docs/profiles-yaml/var-groups/>)