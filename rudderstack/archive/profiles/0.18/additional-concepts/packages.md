# Packages

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Packages

Utilize existing Profiles library projects containing predefined features.

* * *

  * __3 minute read

  * 


Profiles gives you the flexibility to utilize models from existing library projects while defining your own models and inputs within the PB project. This approach allows for a seamless integration of library of pre-existing features, which are readily available and can be applied directly to data streamed into your warehouse.

In the absence of any explicitly defined models, the PB project is capable of compiling and running models from the library package given that inputs are present in the warehouse as assumed in the lib package.

The following list of packages are currently available in Profiles. You can [contact the RudderStack team](<mailto:support@rudderstack.com>) to access these:

  * [profiles-corelib](<https://github.com/rudderlabs/profiles-corelib>)
  * [profiles-base-features](<https://github.com/rudderlabs/profiles-base-features>)
  * [profiles-shopify-features](<https://github.com/rudderlabs/profiles-shopify-features>)
  * [profiles-ecommerce-features](<https://github.com/rudderlabs/profiles-ecommerce-features>)
  * [profiles-stripe-features](<https://github.com/rudderlabs/profiles-stripe-features>)
  * [profiles-multieventstream-features](<https://github.com/rudderlabs/profiles-multieventstream-features>)


> ![warning](/docs/images/warning.svg)
> 
> Some of the above-listed packages might not work for certain warehouses.

Generally, there will be some deviations in terms of the database name and schema name of input models - however, you can easily handle this by remapping inputs.

A sample `pb_project.yaml` file may look as follows:
    
    
    name: app_project
    schema_version: 80
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


For example, to import a library package named `shopify_features`:
    
    
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
    

To import packages hosted on Amazon S3:
    
    
    packages:
      - name: sample_pkg
        url: s3://bucket/packages/sample
    

In `models`/`inputs.yaml`, define these inputs with table names present in the warehouse.
    
    
    inputs:
      - name: rsWarehouseCartCreate
        app_defaults:
          table: YOUR_DB.YOUR_SCHEMA.CART_CREATE_TABLE_NAME_IN_YOUR_WH
        occurred_at_col: timestamp
        ids:
          - select: "anonymous_id"
            type: anonymous_id
            entity: user
          - select: "id2"
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "id3"
            type: exclude_id
            entity: user
            to_default_stitcher: true
      - name: rsIdentifies
        app_defaults:
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
    

Note that the name of the table/view is changed to the appropriate name in your warehouse. If tables are present with the same name (including database name and schema name) then no remapping is required.

### Best schema version (tags)

It is recommended to use git-tags instead of the latest commit on main branch of your library projects. Also, you can use a specific tag, for example: `https://github.com/org-name/lib-name/tag/schema_<n>`.

If you want Profile Builder to figure out the best schema version for every run, you can use the placeholder {{best_schema_version}}, for example, `https://github.com/org-name/lib-name/tag/schema_{{best_schema_version}}`. The selection of compatible git tags is done by PB, that is, it will figure out the best compatible version for the lib package.

A sample project file:
    
    
    packages:
      - name: shopify_features
        url: https://github.com/org-name/lib-names/tag/schema_{{best_schema_version}}
        inputsMap:
          rsCartUpdate: inputs/rsCartUpdate
          rsIdentifies: inputs/rsIdentifies
    

Using this will make Profiles use the best compatible version of the library project in case of any schema updates.

> ![info](/docs/images/info.svg)
> 
> You don’t have to replace the placeholder `{{best_schema_version}}`. For instance, if `https://github.com/org-name/lib-names/tags/` has a tag for schema_44, then `https://github.com/org-name/lib-names/tag/schema_44` will be automatically used. In any case, if you replace the placeholder with actual tag name, the project will work without any issues.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.18/additional-concepts/macros-window-functions/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.18/additional-concepts/packages/git-url/>)