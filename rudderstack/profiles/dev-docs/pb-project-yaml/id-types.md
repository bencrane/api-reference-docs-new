# ID Types

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# ID Types

Learn about the Entity ID types in your Profiles project.

* * *

  * __less than a minute

  * 


You can use [`id_types`](<https://www.rudderstack.com/docs/profiles/concepts/id/>) to list the type of identifiers used in an ID stitcher. You can also use this parameter for creating `entity_var` and `input_var`. The data type of these identifiers must be `string`.
    
    
    id_types:
      - name: user_id
        filters:
          - type: include/exclude
            value: "value"
          - type: include/exclude
            regex: "regex expression"
      - name: email
        maximum_edges:
          - user_id: 1
    

Field| Description  
---|---  
`name`  
Required| Name of the ID type.  
`filters`| Filter(s) the ID types to include/exclude specific values. The filters are processed in the listed order.  
`maximum_edges`| Defines cardinality rules that limit how many connections a node of an ID type can have to another node of other ID types.  
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
        maximum_edges:
          - email: 2
          - anonymous_id: 5
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
    

  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/pb-project-yaml/entities/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/profiles-yaml/>)