# Entity

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Entity

Define the entities used in a Profiles project.

* * *

  * __2 minute read

  * 


[`Entities`](<https://www.rudderstack.com/docs/archive/profiles/0.22/concepts/entities/>) are defined in the [`pb_project.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/pb-project-yaml/>) file. They are used throughout a Profiles project and consist of names for the entities and the types of [`ids`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/pb-project-yaml/id-types/>) associated with each for ID stitching and feature creation.

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
`id_stitcher`| Model path for customer ID stitcher. If left blank, the default ID stitcher is used.  
[`id_types`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/pb-project-yaml/id-types/>)  
Required| List of the identifier types associate with the `entity`.  
[`feature_views`](<https://www.rudderstack.com/docs/archive/profiles/0.22/concepts/feature-views/>)| List of `name` and `id_type` (primary key) for each view.  
  
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

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.22/dev-docs/pb-project-yaml/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.22/dev-docs/pb-project-yaml/id-types/>)