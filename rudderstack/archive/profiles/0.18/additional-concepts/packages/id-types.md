# ID Types

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# ID Types

Extend Profiles packages to modify the existing ID types or add custom ID types.

* * *

  * __2 minute read

  * 


You can extend the [Profiles packages](<https://www.rudderstack.com/docs/archive/profiles/0.18/additional-concepts/packages/>) to modify the existing ID types or add custom ID types to the default list.

## Add custom ID types

To have a custom list of ID types other than the ones provided in the default package, you can modify your list as follows:
    
    
    entities:
      - name: user
        id_types:
          - user_id
          - anonymous_id
          - email
    id_types:
      - name: user_id
      - name: anonymous_id
        filters:
          - type: exclude
            value: ""
          - type: exclude
            value: "unknown"
          - type: exclude
            value: "NaN"
      - name: email
        filters:
        - type: include
          regex: "[A-Za-z0-9+_.-]+@(.+)"
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure that the ID types are also defined in the `entity` definition.

## Modify existing ID types

For the `id_type` you want to modify, add the key `extends:` followed by name of the same/different `id_type` that you wish to extend and the `filters` with `include`/`exclude` values.
    
    
    packages:
      - name: corelib
        url: "https://github.com/rudderlabs/rudderstack-profiles-corelib/tag/schema_{{best_schema_version}}"
    id_types:
      - name: user_id
        extends: user_id
        filters:
          - type: exclude
            value: 123456
    id_types:
      - name: customer_id
        extends: user_id
        filters:
          - type: include
            regex: sample
    

  * **id_types**


Enlists the type of identifiers to be used for creating ID stitcher/`entity_var`/`input_var`. For example, you can define anonymous IDs that do not include the value `undefined` or email addresses in the proper format.

Field| Data type| Description  
---|---|---  
`name`| String| Name of the ID type like email, user ID, etc.  
`extends`| List| (Optional) Name of the ID type you wish to extend.  
[`filters`](<https://www.rudderstack.com/docs/archive/profiles/0.18/cli-user-guide/structure/#filters>)| List| Filter(s) the ID types to include/exclude specific values. The filters are processed in the defined order.  
  
  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.18/additional-concepts/packages/git-url/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.18/additional-concepts/input-sources/>)