# Project Structure

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Project Structure

Know the specifications of a site configuration file, PB project structure, configuration files, and their parameters.

* * *

  * __8 minute read

  * 


Once you complete the [Profile Builder CLI](<https://www.rudderstack.com/docs/archive/profiles/0.12/get-started/profile-builder/>) steps, you will be able to see the Profiles project on your machine.

## Site configuration file

RudderStack creates a site configuration file (`~/.pb/siteconfig.yaml`) while [creating a warehouse connection](<https://www.rudderstack.com/docs/archive/profiles/0.12/get-started/profile-builder/#2-create-warehouse-connection>). It contains the following details including secrets (if any):

  * Warehouse connection details and its credentials.
  * Git repository connection credentials (if any).


> ![success](/docs/images/tick.svg)
> 
> If you have multiple Profiles projects and they use different warehouse connections, you can store the details for multiple connections in the same site configuration file.

A sample site configuration file containing multiple warehouse connection details is shown below:
    
    
    connections:
      prod-db-profile:
          target: dev
          outputs:
              dev:
                  account: inb828.us-west-3
                  dbname: MAT_STORE
                  password: password
                  role: PROFILES_ROLE
                  schema: AB_SCHEMA
                  type: snowflake
                  user: rik
                  warehouse: PROD_WAREHOUSE
      test-db-profile:
          target: test
          outputs:
              db:
                  access_token: dabasihasdho
                  catalog: rs_dev
                  host: adb-98.18.azuredatabricks.net
                  http_endpoint: /sql/1.0/warehouses/919uasdn92h
                  port: 443
                  schema: rs_profiles
                  type: databricks
                  user: johndoe@abc.onmicrosoft.com
              dev:
                  account: uk12.us-west-1
                  dbname: RUDDERSTACK_DB
                  password: password
                  role: RS_ROLE
                  schema: RS_PROFILES
                  type: snowflake
                  user: johndoe
                  warehouse: RS_WAREHOUSE
              redshift_v1:
                  dbname: warehouse_rs
                  host: warehouse.abc.us-east-3.redshift.amazonaws.com
                  password: password
                  port: 5419
                  schema: rs_profiles
                  type: redshift
                  user: redshift_user
              redshift_v2:
                  workgroup_name: warehouse_workgroup
                  region: us-east-1
                  driver: v2
                  sslmode: require
                  dbname: warehouse_rs
                  schema: rs_profiles
                  type: redshift
                  access_key_id: ******************
                  secret_access_key: ******************************
               big:
                  credentials:
                    auth_provider_x509_cert_url: https://www.googleapis.com/oauth2/v1/certs
                    auth_uri: https://accounts.google.com/o/oauth2/auth
                    client_email: johndoe@big-query-integration-poc.iam.gserviceaccount.com
                    client_id: "123345678909872"
                    client_x509_cert_url: https://www.googleapis.com/robot/v1/metadata/x509/johndoe%40big-query-integration-poc.iam.gserviceaccount.com
                    private_key: |
                        -----BEGIN PRIVATE KEY-----                    
                       ## private key
                        -----END PRIVATE KEY-----
                    private_key_id: <PRIVATE_KEY_ID>
                  project_id: big-query-integration-poc
                    token_uri: https://oauth2.googleapis.com/token
                    type: service_account
                    project_id: rs_profiles
                  schema: rs_profiles
                  type: bigquery
                  user: johndoe@big-query-integration-poc.iam.gserviceaccount.com
    gitcreds:
     - reporegex: "git@github.com:REPO_OWNER/*" # in case of ssh url
       key: |
           -----BEGIN OPENSSH PRIVATE KEY-----
           **********************************************************************
           **********************************************************************
           **********************************************************************
           **********************************************************************
           ****************************************************************
           -----END OPENSSH PRIVATE KEY-----       
     - reporegex: "https://github.com/rudderlabs/*" # https url
       basic_auth:
         username: oauth2
         password: ... # your GitHub access token with read permission
    py_models:
        enabled: true # in case you are using Python models in your project, else set it to false
        python_path: /opt/anaconda3/bin/python # the path where Python is installed (run `which python` to get the full path). If `py_models` is not enabled, set it to `""`. For Windows, you may pass the path value as: python.exe
        credentials_presets: null
        allowed_git_urls_regex: ""
    cache_dir: /Users/YOURNAME/.pb/WhtGitCache/ # For Windows, the directory path will have forward slash (\)
    filepath: /Users/YOURNAME/.pb/siteconfig.yaml # For Windows, the file path will have forward slash (\)
    

## Profiles project structure

The following image shows the folder structure of the project:

[![Project structure](/docs/images/profiles/project-structure.webp)](</docs/images/profiles/project-structure.webp>)

### `pb_project.yaml`

The `pb_project.yaml` file contains the project details like the name, schema version, warehouse connection, [entityEntity refers to a digital representation of a class of real world distinct objects for which you can create a profile.](</docs/resources/glossary/#entity>) names along with ID types, etc.

A sample `pb_project.yaml` file with entity type as `user`:
    
    
    name: sample_attribution
    schema_version: 54
    connection: test
    include_untimed: true
    model_folders:
      - models
    entities:
      - name: user
        id_types:
          - main_id
          - user_id
          - anonymous_id
          - email
    packages:
      - name: corelib
        url: "https://github.com/rudderlabs/rudderstack-profiles-corelib/tag/schema_{{best_schema_version}}"
    
    # Profiles can also use certain model types defined in Python.
    # Examples include ML models. Those dependencies are specified here.
    python_requirements:
      - profiles-pycorelib==0.1.0
    

The following table explains the fields used in the above file:

Field| Data type| Description  
---|---|---  
`name`| String| Name of the project.  
`schema_version`| Integer| Project’s YAML version. Each new schema version comes with improvements and added functionalities.  
`connection`| String| Connection name from [`siteconfig.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.12/cli-user-guide/structure/>) used for connecting to the warehouse.  
`include_untimed`| Boolean| Determines if inputs having no timestamps should be allowed. If true, data without timestamps is included when running the models.  
`model_folders`| String| Names of folders where model files are stored.  
`entities`| List| Lists all the entities used in the project for which you can define models. Each entry for an entity here is a JSON object specifying entity’s name and attributes.  
`packages`| List| List of packages with their name and URL. Optionally, you can also extend ID types filters for including or excluding certain values from this list.  
  
##### `entities`

Field| Data type| Description  
---|---|---  
`name`| String| Name of the entity used in the project.  
`id_types`| List| List of all identifier types associated with the current entity.  
  
> ![warning](/docs/images/warning.svg)
> 
> The identifiers listed in `id_types` may have a many-to-one relationship with an entity but each ID must belong to a single entity.
> 
> For example, a `user` entity might have `id_types` as the `salesforce_id`, `anonymous_id`, `email`, and `session_id` (a user may have many session IDs over time). However, it should not include something like `ip_address`, as a single IP can be used by different users at different times and it is not considered as a user identifier.

##### `packages`

You can import library packages in a project signifying where the project inherits its properties from.

Field| Data type| Description  
---|---|---  
`name`| String| Specify a name.  
`url`| String| HTTPS URL of the lib package, with a tag for the best schema version.  
  
### `inputs.yaml`

The `inputs.yaml` file lists all the input sources (tables/views) which should be used to obtain values for models and eventually create output tables.

It also specifies the table/view along with column name and SQL expression for retrieving values. The input specification may also include metadata, and the constraints on those columns.

A sample `inputs.yaml` file:
    
    
    inputs:
      - name: salesforceTasks
        contract:
          is_optional: false
          is_event_stream: true
          with_entity_ids:
            - user
          with_columns:
            - name: activitydate
            - name: whoid
        app_defaults:
          table: salesforce.task
          # For BigQuery, it is recommended to use view (view: _views_<view_name>) instead of table for event streaming data sets.
          occurred_at_col: activitydate
          ids:
            # column name or sql expression
            - select: "whoid" 
              type: salesforce_id
              entity: user
              to_default_stitcher: true
      - name: salesforceContact
        contract:
          is_optional: false
          is_event_stream: true
          with_entity_ids:
            - user
          with_columns:
            - name: createddate
            - name: id
            - name: email
        app_defaults:
          table: salesforce.contact
          # For BigQuery, it is recommended to use view (view: _views_<view_name>) instead of table for event streaming data sets.
          occurred_at_col: createddate
          ids:
            - select: "id"
              type: salesforce_id
              entity: user
              to_default_stitcher: true
            - select: "case when lower(email) like any ('%gmail%', '%yahoo%') then lower(email)  else split_part(lower(email),'@',2) end"
              type: email
              entity: user
              to_default_stitcher: true
      - name: websitePageVisits
        contract:
          is_optional: false
          is_event_stream: true
          with_entity_ids:
            - user
          with_columns:
            - name: timestamp
            - name: anonymous_id
            - name: context_traits_email
            - name: user_id
        app_defaults:
          table: autotrack.pages
          # For BigQuery, it is recommended to use view (view: _views_<view_name>) instead of table for event streaming data sets.
          occurred_at_col: timestamp
          ids:
            - select: "anonymous_id"
              type: rudder_anon_id
              entity: user
              to_default_stitcher: true
            # below sql expression check the email type, if it is gmail and yahoo return email otherwise spilt email return domain of email.  
            - select: "case when lower(coalesce(context_traits_email, user_id)) like any ('%gmail%', '%yahoo%') then lower(coalesce(context_traits_email, user_id))  \
                  else split_part(lower(coalesce(context_traits_email, user_id)),'@',2) end"
              type: email
              entity: user
              to_default_stitcher: true
    

The following table explains the fields used in the above file:

Field| Data type| Description  
---|---|---  
`name`| String| Name of the input model.  
`contract`| Dictionary| A model contract provides essential information about the model like the necessary columns and entity IDs that it should contain. This is crucial for other models that depend on it, as it helps find errors early and closer to the point of their origin.  
`app_defaults`| Dictionary| Values that input defaults to when you run the project directly. For library projects, you can remap the inputs and override the app defaults while importing the library projects.  
  
##### `contract`

Field| Data type| Description  
---|---|---  
`is_optional`| Boolean| Whether the model’s existence in the warehouse is mandatory.  
`is_event_stream`| Boolean| Whether the table/view is a series/stream of events. A model that has a `timestamp` column is an event stream model.  
`with_entity_ids`| List| List of all entities with which the model is related. A model M1 is considered related to model M2 if there is an ID of model M2 in M1’s output columns.  
`with_columns`| List| List of all ID columns that this contract is applicable for.  
  
##### `app_defaults`

Field| Data type| Description  
---|---|---  
`table`/`view`| String| Name of the warehouse table/view containing the data. You can prefix the table/view with an external schema or database in the same warehouse, if applicable. Note that you can specify either a table or view but not both.  
`occurred_at_col`| String| Name of the column in table/view containing the timestamp.  
`ids`| List| Specifies the list of all IDs present in the source table along with their column names (or column SQL expressions).  
  
**Note** : Some input columns may contain IDs of associated entities. By their presence, such ID columns associate the row with the entity of the ID. The ID Stitcher may use these declarations to automatically discover ID-to-ID edges.  
  
##### `ids`

Field| Data type| Description  
---|---|---  
`select`| String| Specifies the column name to be used as the identifier. You can also specify a SQL expression if some transformation is required.  
  
**Note** : You can also refer table from another Database/Schema in the same data warehouse. For example, `table: <database_name>.<schema_name>.<table_name>`.  
`type`| String| Type of identifier. All the ID types of a project are declared in `pb_project.yaml`. You can specify additional filters on the column expression.  
  
**Note** : Each ID type is linked only with a single entity.  
`entity`| String| Entity name defined in the `pb_project.yaml` file to which the ID belongs.  
`to_default_stitcher`| Boolean| Set this **optional** field to `false` for the ID to be excluded from the default ID stitcher.  
  
### `profiles.yaml`

The `profiles.yaml` file lists entity_vars / input_vars used to create the output tables under `var_groups:`.

Field| Data type| Description  
---|---|---  
`name`| String| A unique name for the var_group.  
`entity_key`| String| The entity to which the var_group belongs to.  
`vars`| Object| This section is used to specify variables, with the help of `entity_var` and `input_var`. Aggregation on stitched ID type is done by default and is implicit.  
  
Optionally, you can create models using the above vars. The following fields are common for all the model types:

Field| Data type| Description  
---|---|---  
`name`| String| Name of the model. Note that a table with the same name is created in the data warehouse. For example, if you define the name as `user_table`, the output table will be named something like `Material_user_table_<rest-of-generated-hash>_<timestamp-number>`.  
`model_type`| String| Defines the type of model. Possible values are: `id_stitcher`, `feature_table_model`, and `sql_template`.  
`model_spec`| Object| Creates a detailed configuration specification for the target model. Different schema is applicable for different model types as explained in each section below.  
  
RudderStack supports the following model types:

  * [Feature Views/Feature Table](<https://www.rudderstack.com/docs/archive/profiles/0.12/example/feature-table/>)
  * [SQL Template](<https://www.rudderstack.com/docs/archive/profiles/0.12/example/sql-model/>)
  * [ID Stitcher](<https://www.rudderstack.com/docs/archive/profiles/0.12/example/id-stitcher/>)
  * [ID Collator](<https://www.rudderstack.com/docs/archive/profiles/0.12/example/id-collator/>)
  * [Python models](<https://www.rudderstack.com/docs/archive/profiles/0.12/predictions/python-models/>)
  * [Packages](<https://www.rudderstack.com/docs/archive/profiles/0.12/example/packages/>)


### `README.md`

The `README.md` file provides a quick overview on how to use PB along with SQL queries for data analysis.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.12/cli-user-guide/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.12/cli-user-guide/commands/>)