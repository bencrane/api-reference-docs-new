# ID Types

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# ID Types

Learn about the Entity ID types in your Profiles project.

* * *

  * __less than a minute

  * 


You can use [`id_types`](<https://www.rudderstack.com/docs/archive/profiles/0.20/concepts/id/>) to list the type of identifiers used in an ID stitcher. You can also use this parameter for creating `entity_var` and `input_var`.
    
    
    id_types:
        - name: id_type_name
          filters:
              - type: include/exclude
                value: "value"
              - type: include/exclude
                regex: "regex expression"
    

Field| Description  
---|---  
`name`  
Required| Name of the ID type.  
`filters`| Filter(s) the ID types to include/exclude specific values. The filters are processed in the listed order.  
`type`| Filter type - accepted values are `include` or `exclude`.  
`value`| Specify the value that should be matched exactly.  
`regex`| Regular expression to match.  
  
## Example
    
    
    entities:
        - name: user
          id_column_name: user_rud_id
          id_types:
              - user_id
              - anonymous_id
              - email
    id_types:
        - name: user_id
        - name: anonymous_id
          extends: user_id
          filters:
              - type: exclude
                value: "unknown"
              - type: exclude
                value: "NaN"
        - name: email
          filters:
              - type: include
                regex: "[A-Za-z0-9+_.-]+@(.+)"
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.20/dev-docs/pb-project-yaml/entities/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.20/dev-docs/profiles-yaml/>)