# Packages

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Packages

Utilize models from existing libary projects.

* * *

  * __4 minute read

  * 


Profiles gives you the flexibility to utilize models from existing library projects while defining your own models and inputs within the PB project. This approach allows for a seamless integration of library of pre-existing features, which are readily available and can be applied directly to data streamed into your warehouse.

In the absence of any explicitly defined models, the PB project is capable of compiling and running models from the library package given that inputs are present in the warehouse as assumed in the lib package.

> ![warning](/docs/images/warning.svg)
> 
> Packages currently work only on Snowflake.

Generally, there will be some deviations in terms of the database name and schema name of input models - however, you can easily handle this by remapping inputs.

A sample `pb_project.yaml` file may look as follows:
    
    
    name: app_project
    schema_version: 49
    profile: test
    packages:
      - name: test_ft
        gitUrl: "https://github.com/rudderlabs/librs360-shopify-features/tree/main"
    

In this case, the PB project imports a single package. It does not require a separate `models` folder or entities as the input and output models will be sourced from the imported packages.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * If non-mandatory inputs required by the model are not present in the warehouse, you can still run the model.
>   * If there is any deviation in the table/view name for input models, that is, if the inputs assumed in library package are present under some other name, make sure to do the remapping.
>   * If some of the assumed inputs are not present at all, they should be remapped to `nil`. This way you can create and run imported packages with minimal set of inputs present.
> 


For example, to import a library package with the name of `shopify_features`:
    
    
    packages: 
      - name: shopify_features
        url: https://github.com/rudderlabs/librs360-shopify-features/tree/main
        inputsMap: 
          rsCartCreate: inputs/rsWarehouseCartCreate
          rsCartUpdate: inputs/rsCartUpdate
          rsIdentifies: inputs/rsIdentifies
          rsOrderCancelled: inputs/rsOrderCancelled
          rsOrderCreated: inputs/rsOrderCreated
          rsPages: nil
          rsTracks: nil
    

In `models`/`inputs.yaml`, these inputs need to be defined with table names present in the warehouse.
    
    
    inputs:
      - name: rsWarehouseCartCreate
        table: YOUR_DB.YOUR_SCHEMA.CART_CREATE_TABLE_NAME_IN_YOUR_WH
        occurred_at_col: timestamp
        ids:
          - select: "anonymous_id"
            type: anonymous_id
            entity: user
        source_metadata:
          role: shopify
          category: webhook
      - name: rsIdentifies
        table: YOUR_DB.YOUR_SCHEMA.IDENTIFIES
        occurred_at_col: timestamp
        ids:
          - select: "user_id"
            type: user_id
            entity: user
          - select: "anonymous_id"
            type: anonymous_id
            entity: user
          - select: "lower(email)"
            type: email
            entity: user
        source_metadata:
          role: shopify
          category: webhook
    

Note that the name of the table/view is changed to the appropriate name in your warehouse. If tables are present with the same name (including database name and schema name) then no remapping is required.

### Available packages

The following list of packages are currently available in Profiles:

  * [profiles-corelib](<https://github.com/rudderlabs/profiles-corelib>)
  * [profiles-base-features](<https://github.com/rudderlabs/rudderstack-profiles-base-features>)
  * profiles-shopify-features
  * profiles-ecommerce-features
  * profiles-stripe-features
  * profiles-multieventstream-features


[Contact us](<mailto:support@rudderstack.com>) to access these packages.

> ![warning](/docs/images/warning.svg)
> 
> Packages currently work only on Snowflake.

## Modify ID types

### Extend existing package

To add custom ID types to the default list or modify an existing one, then you may extend the package to include your specifications.

For the corresponding `id_type`, add the key `extends:` followed by name of the same/different `id_type` that you wish to extend and the `filters` with `include`/`exclude` values.
    
    
    ---pb_project.yaml---
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
    

  * **id_types** : Enlists the type of data to be used for creating ID stitcher / EntityVar / InputVar. For example, anonymous IDs that do not include the value `undefined` or email addresses in proper format.
    * **extends** : Name of the ID type that you wish to extend.
    * **name** : The type of data that will be fetched, like email, user ID, etc. It is different from whatever is present in the table column, like int or varchar.
    * **filters** : Filter(s) that the type should go through before being included. Filters are processed in order. Current filters enable one to include and exclude specific values or regular expressions.


### Custom list of ID types

To have custom list of ID types other than the provisions in the default package, you can remove and add your list as follows:
    
    
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
> Make sure that the ID types are also defined in the entity definition.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.10/example/sql-model/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.10/snowflake-quickstart/>)