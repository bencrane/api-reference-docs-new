# pb_project.yaml

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# pb_project.yaml

Learn about the Profiles project configuration file.

* * *

  * __2 minute read

  * 


The `pb_project.yaml` file contains the overall project configuration. This includes the [`entities`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/entities/>) and [`id_types`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/id-types/>) that are used throughout the project.

## Video walkthrough

## Overview

The `pb_project.yaml` file is saved in the top level of a Profiles project.
    
    
    name: project_name
    schema_version: version_number
    connection: connection_name
    model_folders:
        - directories
    entities:
        <entity-config>
    id_types:
        <id_type-config>
    python_requirements: # Optional
        - python_package==version
    carry_forward_privileges: true / false
    

Field| Description  
---|---  
`name`  
Required| Project name.  
`schema_version`  
Required| Project’s YAML version.  
`connection`  
Required| Connection name from [`siteconfig.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/site-configuration-file/>).  
`model_folders`  
Required| Path to the folder containing the model files.  
[`entities`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/entities/>)  
Required| List of entities used in the project.  
[`id_types`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/id-types/>)  
Required| Configuration of all ID types across all entities.  
`python_requirements`| List of Python packages and versions required for the project, specifically used for controlling the Profiles version.  
`carry_forward_privileges`| Boolean that determines whether the privileges granted on the views should be retained after the view definitions are updated. This resolves the issue where recreating views for each model in the project led to revoked privileges.  
  
**Note** : Using this key can lead to some performance overhead.  
  
## Example
    
    
    # Project name
    name: sample_attribution
    schema_version: 85
    connection: prod-db-profile
    model_folders:
      - models
    entities:
      - name: user
        id_column_name: user_rud_id # Optional
        id_types:
          - user_id
          - anonymous_id
          - email
        feature_views:
          using_ids:
            - id: email
              name: customer_profile_by_email
    id_types:
      - name: anonymous_id
      - name: email
        filters:
          - type: include
            regex: ".+@.+"
        maximum_edges:
          - anonymous_id: 2
          - user_id: 1
      - name: user_id
        filters:
          - type: exclude
            value: "test"
    
    carry_forward_privileges: false
    

  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/ide/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/pb-project-yaml/entities/>)