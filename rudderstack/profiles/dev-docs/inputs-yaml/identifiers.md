# IDs

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# IDs

Learn how to map source ID to entities and ID types in your Profiles project.

* * *

  * __less than a minute

  * 


The `ids` key specifies the list of all the identifiers present in the source table with their column names (or SQL expression) and `id_type`.
    
    
    ids:
      - select: id-column
        type: id_type
        entity: entity_name
        to_default_stitcher: true/false
    

Field| Description  
---|---  
`select`  
Required| ID column name or SQL expression.  
`type`  
Required| `id_type` from the list of `id_types` in the `entity` section of [`pb_project.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/>).  
`entity`  
Required| Entity name.  
`to_default_stitcher`| Default `true`\- set to `false` to exclude from the default ID stitcher.  
  
### Example
    
    
    # Basic example
    ids:
        - select: "id"
          type: salesforce_id
          entity: user
    
    # Use SQL function on ID column
    ids:
        - select: lower(email_address)
          type: email
          entity: user
    
    # Multiple IDs for an entity
    ids:
        - select: lower(email_address)
          type: email
          entity: user
        - select: "username"
          type: user_name
          entity: user
    
    # IDs for multiple entities
    ids:
        - select: lower(email_address)
          type: email
          entity: user
        - select: "account_id"
          type: account_id
          entity: account
    

  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/inputs-yaml/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/inputs-yaml/s3-bucket-input/>)