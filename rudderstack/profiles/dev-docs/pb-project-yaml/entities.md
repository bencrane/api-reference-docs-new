# Entity

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Entity

Define the entities used in a Profiles project.

* * *

  * __2 minute read

  * 


[`Entities`](<https://www.rudderstack.com/docs/profiles/concepts/entities/>) are defined in the [`pb_project.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/>) file. They are used throughout a Profiles project and consist of names for the entities and the types of [`ids`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/id-types/>) associated with each for ID stitching and feature creation.

You can also assign a custom ID stitcher and/or a feature view with specific `id_types` as the view’s primary key.
    
    
    entities:
       - name: entity_name
         id_column_name: column_name
         id_stitcher: models/custom_ID_stitcher_path   # Optional
         id_types:
             <id_types-config>
         feature_views:     # Optional
             using_ids:
                - id: id_type
                  name: view_name
    

Key| Description  
---|---  
`name`  
Required| `Entity` name.  
`id_column_name`| Name of the main ID column for an entity. If not provided explicitly, its value is set to `<entity_name>_main_id`.  
`id_stitcher`| Model path to the ID stitcher for this entity. When you define a custom `id_stitcher` model in [`profiles.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/>), set this key so the entity uses that model. If left blank, the default ID stitcher is used.  
[`id_types`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/id-types/>)  
Required| List of the identifier types associated with the `entity`.  
[`feature_views`](<https://www.rudderstack.com/docs/profiles/concepts/feature-views/>)| List of `name` and `id_type` (primary key) for each view.  
  
> ![warning](/docs/images/warning.svg)
> 
> **Always set`id_stitcher` on each entity that has a custom ID stitcher model defined in `profiles.yaml`.**
> 
> If you have an `id_stitcher` model in `profiles.yaml` (for example, `user_id_stitcher` for the user entity) but do not set `id_stitcher` on the entity, the intended ID stitcher is not used and you may see get unintended results.
> 
> Set `id_stitcher` to the model path (for example, `id_stitcher: models/user_id_stitcher`).

## Example
    
    
    # Case 1: Minimal example
    entities:
        - name: user
          id_column_name: user_rud_id
          id_types:
             - email
             - user_id
    
    # Case 2: With a custom ID stitcher
    entities:
        - name: user
          id_stitcher: models/custom_id_stitcher
          id_types:
             - email
             - user_id
    
    # Case 3: With a feature view
    entities:
        - name: user
          id_types:
             - email
             - user_id
          feature_views:
             using_ids:
                - id: email
                  name: customer_profile_by_email
    

Note that for the first case in the above example, the `id_column_name` is explicitly set to `user_rud_id`.

In the other cases, `id_column_name` is not explicitly specified, so this field is set to `user_main_id` by default.

  


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/pb-project-yaml/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/pb-project-yaml/id-types/>)