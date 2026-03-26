# Packages

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Packages

Utilize existing Profiles library projects containing predefined features.

* * *

  * __5 minute read

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
    schema_version: 69
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

You can also extend the package to modify the existing ID types or add custom ID types to the default list:

### Modify existing ID types

For the corresponding `id_type`, add the key `extends:` followed by name of the same/different `id_type` that you wish to extend and the `filters` with `include`/`exclude` values.
    
    
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


Enlists the type of identifiers to be used for creating ID stitcher/`entity_var`/`input_var`. For example, you can define anonymous IDs that do not include the value `undefined` or email addresses in proper format.

Field| Data type| Description  
---|---|---  
`name`| String| Name of the ID type like email, user ID, etc.  
`extends`| List| (Optional) Name of the ID type you wish to extend.  
[`filters`](<https://www.rudderstack.com/docs/archive/profiles/0.15/cli-user-guide/structure/#filters>)| List| Filter(s) the ID types to include/exclude specific values. The filters are processed in the defined order.  
  
### Add custom ID types

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

### Supported Git URLs

Profiles supports Git URLs for packages. You can host the repos at:

  * GitHub
  * GitLab
  * BitBucket


[Contact the RudderStack team](<mailto:support@rudderstack.com>) if your preferred host isn’t included.

For private repos, RudderStack only supports SSH Git URLs. You need to add credentials to the [`siteconfig.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.15/cli-user-guide/structure/#site-configuration-file>) and public ssh key manually to the platforms.

The URL scheme doesn’t depend on individual Git provider host. You can use the below-mentioned Git URLs:

| URL Syntax| Format (Example)  
---|---|---  
URL for the default branch of a repository| `https://<provider-host>/<org-name>/<repo-name>/path/to/project`| **Github** : `https://github.com/rudderlabs/librs360-shopify-features/shopify-features`  
  
**Gitlab** : `https://gitlab.com/rudderlabs/librs360-shopify-features/shopify-features`  
  
**Bitbucket** :`https://bitbucket.org/rudderlabs/librs360-shopify-features/shopify-features`  
SSH URL for the default branch of a private repository| `git@<provider-host>:<org-name>/<repo-name>/path/to/project`| **Github** : `git@github.com:rudderlabs/librs360-shopify-features/shopify-features`  
  
**Gitlab** : `git@gitlab.com:rudderlabs/librs360-shopify-features/shopify-features`  
  
**Bitbucket** :`git@gbitbucket.org:rudderlabs/librs360-shopify-features/shopify-features`  
URL for a specific branch of a repository| `https://<provider-host>/<org-name>/<repo-name>/tree/<branch-name>/path/to/project`| **Github** : `https://github.com/rudderlabs/librs360-shopify-features/tree/main/shopify-features`  
  
**Gitlab** : `https://gitlab.com/rudderlabs/librs360-shopify-features/tree/main/shopify-features`  
  
**Bitbucket** :`https://bitbucket.org/rudderlabs/librs360-shopify-features/tree/main/shopify-features`  
URL for a specific tag within the repository| `https://<provider-host>/<org-name>/<repo-name>/tag/<tag-name>/path/to/project`| **Github** : `https://github.com/rudderlabs/librs360-shopify-features/tag/wht_test/shopify-features`  
  
**Gitlab** : `https://gitlab.com/rudderlabs/librs360-shopify-features/tag/wht_test/shopify-features`  
  
**Bitbucket** :`https://bitbucket.org/rudderlabs/librs360-shopify-features/tag/wht_test/shopify-features`  
URL for a specific commit within the repository| `https://<provider-host>/<org-name>/<repo-name>/commit/<commit-hash>/path/to/project`| **Github** : `https://github.com/rudderlabs/librs360-shopify-features/commit/b8d49/shopify-features`  
  
**Gitlab** : `https://gitlab.com/rudderlabs/librs360-shopify-features/commit/b8d49/shopify-features`  
  
**Bitbucket** :`https://bitbucket.org/rudderlabs/librs360-shopify-features/commit/b8d49/shopify-features`  
  
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

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.15/additional-concepts/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.15/additional-concepts/model-types/>)