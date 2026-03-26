# Additional Concepts

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Additional Concepts

Additional concepts related to Profiles like packages, best practices, partial feature tables, etc.

* * *

  * __13 minute read

  * 


This guide explains some of the advanced concepts related to Profiles.

## Packages

Profiles gives you the flexibility to utilize models from existing library projects while defining your own models and inputs within the PB project. This approach allows for a seamless integration of library of pre-existing features, which are readily available and can be applied directly to data streamed into your warehouse.

In the absence of any explicitly defined models, the PB project is capable of compiling and running models from the library package given that inputs are present in the warehouse as assumed in the lib package.

> ![warning](/docs/images/warning.svg)
> 
> Packages currently work only on Snowflake.

The following list of packages are currently available in Profiles. You can [contact the RudderStack team](<mailto:support@rudderstack.com>) to access these:

  * [profiles-corelib](<https://github.com/rudderlabs/profiles-corelib>)
  * [profiles-base-features](<https://github.com/rudderlabs/rudderstack-profiles-base-features>)
  * profiles-shopify-features
  * profiles-ecommerce-features
  * profiles-stripe-features
  * profiles-multieventstream-features


Generally, there will be some deviations in terms of the database name and schema name of input models - however, you can easily handle this by remapping inputs.

A sample `pb_project.yaml` file may look as follows:
    
    
    name: app_project
    schema_version: 54
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

### Modify ID types

#### Extend existing package

You can add custom ID types to the default list or modify an existing one by extending the package to include your specifications.

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


#### Custom list of ID types

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

## Model Contracts

With model contracts, you can declare constraints that the model adheres to. A model having a dependency on another model would also need to declare a contract specifying what columns and entities the input model must have. For contract validation, these columns should be present in the referenced model.

For an input of a project like a library project, the model contract is used to enforce constraints on tables/views that get wired to it downstream.
    
    
    # inputs.yaml
      - name: rsIdentifies
        contract:
          is_optional: false
          is_event_stream: true
          with_entity_ids:
            - user
          with_columns:
            - name: timestamp
            - name: user_id
            - name: anonymous_id
            - name: email
    

In SQL model, the contract would contain all the columns from IDs and features. Each internal model also publishes the contract it promises to adhere to. Suppose `rsSessionTable` has an input `shopify_session_features`. Model contracts enable `rsSessionTable` to specify the constraints that `shopify_session_features` must adhere to.
    
    
    models:
    - name: rsSessionTable
      model_type: sql_template
      model_spec:
        ... # model specifications
        single_sql: |
          {% set contract = BuildContract('{"with_columns":[{"name":"user_id"}, {"name":"anonymous_id"}]}') %}
          {% with SessionFeature = this.DeRef("models/shopify_session_features",contract)%}
              select user_id as id1, anonymous_id as id2 from {{SessionFeature}}
      	contract:
        with_entity_ids:
          - user
        with_columns:
          - name: user_id
            type: string
            is_optional: true # false being default
          - name: anonymous_id
            type: string
            is_optional: true # false being default
    

Here, `rsSessionTable` declares that its input `shopify_session_features` must have columns `user_id` and `anonymous_id`. This helps in improving data quality and error handling. Internally, this requested contract is validated against `shopify_session_features`’s actual contract. For validation to pass, `input_shopify_session_features_contract` must be a subset of `shopify_session_features`’s published contract.

This enables more comprehensive static and dynamic validations of our projects.

## Partial feature tables

Partial feature tables are created when only a few input sources are available.

For example, lets say that you import a library package and some of the input models assumed in the package are not present in your warehouse.

When you remap some of these input models to nil, those inputs and the features directly or indirectly dependent upon those inputs are disabled. In such cases, a partial feature table is created from the rest of the available inputs. Similarly, ID stitcher also runs even if few of the edge sources are not present in the warehouse or remapped to nil.

## Pre and post hooks

A pre hook enables you to execute an SQL before running a model, for example, if you want to change DB access, create a DB object, etc. Likewise, a post hook enables you to execute an SQL after running a model. The SQL can also be templatized. Here’s an example code snippet:
    
    
    models:
      - name: test_id_stitcher
        model_type: id_stitcher
        hooks:
          pre_run: "CREATE OR REPLACE VIEW {{warehouse.ObjRef('V1')}} AS (SELECT * from {{warehouse.ObjRef('Temp_tbl_a')}});"
          post_run: 'CREATE OR REPLACE VIEW {{warehouse.ObjRef("V2")}} AS (SELECT * from {{warehouse.ObjRef("Temp_tbl_a")}});'
        model_spec:
          - # rest of model specs go here
    

## Use Amazon S3 bucket as input

> ![warning](/docs/images/warning.svg)
> 
> This is an experimental feature.

If you store data in your Amazon S3 bucket in a CSV file format, you can use it as an input for the Profiles models. The S3 URI path must be specified in the `app_defaults.s3`:
    
    
    name: s3_table
    contract:
      is_optional: false
      is_event_stream: true
      with_entity_ids:
        - user
      with_columns:
        - name: insert_ts
          datatype: timestamp
        - name: num_a
          datatype: integer
    app_defaults:
      s3: "s3://bucket-name/prefix/example.csv"
      occurred_at_col: insert_ts
      ids:
        - select: "id1"
          type: test_id
          entity: user
        - select: "id2"
          type: test_id
          entity: user
    

Ensure that the CSV file follows the standard format with the first row as the header containing column names, for example:
    
    
    ID1,ID2,ID3,INSERT_TS,NUM_A
    a,b,ex,2000-01-01T00:00:01Z,1
    D,e,ex,2000-01-01T00:00:01Z,3
    b,c,ex,2000-01-01T00:00:01Z,2
    NULL,d,ex,2000-01-01T00:00:01Z,4
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * To escape comma (`,`) from any cell of the CSV file, enclose that cell with double quotes `" "` .
>   * Double quotes (`" "`) enclosing a cell are ignored.
> 


Follow the below steps to grant PB the required permissions to access the file in S3 Bucket:

### Private S3 bucket

Add `region`, `access key id`, `secret access key`, and `session token` in your `siteconfig` file so that PB can access the private bucket. By default, the region is set to `us-east-1` unless specified otherwise.
    
    
    aws_credential:
        region: us-east-1
        access_key: **********
        secret_access_key: **********
        session_token: **********
    

#### Generate `access key id` and `secret access key`

  1. Open the AWS IAM console in your AWS account.
  2. Click **Policies**.
  3. Click **Create policy**.
  4. In the Policy editor section, click the JSON option.
  5. Replace the existing JSON policy with the following policy and replace the <bucket_name> with your actual bucket name:


    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:GetObject",
                    "s3:GetObjectVersion"
                ],
                "Resource": "arn:aws:s3:::<bucket_name>/*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "s3:ListBucket",
                    "s3:GetBucketLocation"
                ],
                "Resource": "arn:aws:s3:::<bucket_name>",
                "Condition": {
                    "StringLike": {
                        "s3:prefix": [
                            "*"
                        ]
                    }
                }
            }
        ]
    }
    

  6. Click **Review policy**.
  7. Enter the policy name. Then, click **Create policy** to create the policy.


Further, create an IAM user by following the below steps:

> ![info](/docs/images/info.svg)
> 
> An IAM user requires the following permissions on an S3 bucket and folder to access files in the folder (and sub-folders):
> 
>   * s3:GetBucketLocation
>   * s3:GetObject
>   * s3:GetObjectVersion
>   * s3:ListBucket
> 


  1. In AWS IAM console, Click **Users**.
  2. Click **Create user**.
  3. Enter a name for the user.
  4. Select Programmatic access as the access type, then click **Next: Permissions**.
  5. Click **Attach existing policies directly** , and select the policy you created earlier. Then click **Next**.
  6. Review the user details, then click **Create user**.
  7. Copy the access key ID and secret access key values.


#### Generate `session token`

  1. Use the AWS CLI to create a named profile with the AWS credentials that you copied in the previous step.
  2. To get the session token, run the following command:


    
    
     $ aws sts get-session-token --profile <named-profile>
    

See [Snowflake](<https://docs.snowflake.com/en/user-guide/data-load-s3-config-aws-iam-user>), [Redshift](<https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-access-permissions.html>), and [Databricks](<https://docs.databricks.com/en/ingestion/copy-into/generate-temporary-credentials.html>) for more information.

### Public S3 Bucket

You **must** have the following permissions on the S3 bucket and folder to access files in the folder (and sub-folders):

  * s3:GetBucketLocation
  * s3:GetObject
  * s3:GetObjectVersion
  * s3:ListBucket


You can use the following policy in your bucket to grant the above permissions:

  1. Go to the **Permissions** tab of your S3 bucket.
  2. Edit bucket policy in **Permissions** tab and add the following policy. Replace the <bucket_name> with your actual bucket name:


    
    
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject",
                    "s3:GetObjectVersion"
                ],
                "Resource": "arn:aws:s3:::<bucket_name>/*"
            },
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:ListBucket",
                    "s3:GetBucketLocation"
                ],
                "Resource": "arn:aws:s3:::<bucket_name>"
            }
        ]
    }
    

> ![info](/docs/images/info.svg)
> 
> In Redshift, you additionally need to set an IAM role as **default** for your cluster, unless access keys are provided. It is necessary because more than one IAM role can be associated with the cluster, and Redshift needs explicit permission granted through an IAM role to access the S3 bucket (Public or Private).
> 
> Follow [Redshift Documentation](<https://docs.aws.amazon.com/redshift/latest/mgmt/default-iam-role.html#set-default-iam>) for setting an IAM role as default.

## Use CSV file as input

An input file (`models/inputs.yaml`) contains details of input sources such as tables, views, or CSV files along with column name and SQL expression for retrieving values.

You can read data from a CSV file by using `csv: <path_to_filename>` under `app_defaults` in the input specs. CSV data is loaded internally as a single SQL select query, making it useful for seeding tests.

A sample code is as shown:
    
    
        app_defaults:
          csv: "../common.xtra/Temp_tbl_a.csv"
          # remaining syntax is same for all input sources
    

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support CSV files with more than a few hundred rows.

## Filter data

You can filter out any data by using the `filters` field in your projects file:

For example, if you want to exclude all the blacklisted email addresses, you can create an input model (for example, `csv_email_blacklist`) with CSV file as a source, that contains all such email addresses:
    
    
    id_types:
      - name: email
        filters:
          - type: exclude
            sql:
              select: email
              from: inputs/csv_email_blacklist
    

Another example, if you want to exclude all the user_ids, you can create an SQL model (for example, `sql_exclusion_model`) that contains a specific logic to enlist all such IDs:
    
    
    id_types:
      - name: user_id
        filters:
          - type: exclude
            sql:
              select: user_id
              from: inputs/models/sql_exclusion_model
    

## Best schema version (tags)

It is recommended to use git-tags instead of the latest commit on main branch of your library projects. You can use a specific tag, for example: `https://github.com/org-name/lib-name/tag/schema_<n>`. If you want Profile Builder to figure out the best schema version for every run, you can use the placeholder {{best_schema_version}}, for example, `https://github.com/org-name/lib-name/tag/schema_{{best_schema_version}}`. The selection of compatible git tags is done by PB, that is it will figure out the best compatible version for the lib package.

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

## Use private Git repos via CLI

Follow these steps:

  1. [Generate the SSH Key](<https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key>).
  2. Associate the SSH Key to your Git Project. Check the section on [Profile Builder CLI](<https://www.rudderstack.com/docs/archive/profiles/0.12/get-started/quickstart-ui/>).
  3. Add private keys as credentials in the `siteconfig.yaml` file:


    
    
    gitcreds:
      - reporegex: git@<provider-host>:<org-name>/*
        key: |
        -----BEGIN OPENSSH PRIVATE KEY-----
        b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEb..........
        -----END OPENSSH PRIVATE KEY-----    
    

## Supported Git URLs

Profiles supports Git URLs for packages and scheduling via UI. You can host the repos at:

  * GitHub
  * GitLab
  * BitBucket


[Contact the RudderStack team](<mailto:support@rudderstack.com>) if your preferred host isn’t included.

For private repos, RudderStack only supports SSH Git URLs. You need to add credentials to the `siteconfig.yaml` and public ssh key manually to the platforms. See Use private Git repos via CLI.

The URL scheme doesn’t depend on individual Git provider host. You can use the below-mentioned Git URLs:

**1\. URL for the default branch of a repository**

  * **Syntax:**

`https://<provider-host>/<org-name>/<repo-name>/path/to/project`

  * **Example:**

`https://github.com/rudderlabs/librs360-shopify-features/shopify-features` `https://gitlab.com/rudderlabs/librs360-shopify-features/shopify-features` `https://bitbucket.org/rudderlabs/librs360-shopify-features/shopify-features`


**For private repos, RudderStack support SSH URLs:**

  * **Syntax:**

`git@<provider-host>:<org-name>/<repo-name>/path/to/project`

  * **Example:**

`git@github.com:rudderlabs/librs360-shopify-features/shopify-features` `git@gitlab.com:rudderlabs/librs360-shopify-features/shopify-features` `git@gbitbucket.org:rudderlabs/librs360-shopify-features/shopify-features`


**2\. URL for a specific branch of a repository**

  * **Syntax:**

`https://<provider-host>/<org-name>/<repo-name>/tree/<branch-name>/path/to/project`

  * **Example:**

`https://github.com/rudderlabs/librs360-shopify-features/tree/main/shopify-features` `https://gitlab.com/rudderlabs/librs360-shopify-features/tree/main/shopify-features` `https://bitbucket.org/rudderlabs/librs360-shopify-features/tree/main/shopify-features`


**3\. URL for a specific tag within the repository**

  * **Syntax:**

`https://<provider-host>/<org-name>/<repo-name>/tag/<tag-name>/path/to/project`

  * **Example:**

`https://github.com/rudderlabs/librs360-shopify-features/tag/wht_test/shopify-features` `https://gitlab.com/rudderlabs/librs360-shopify-features/tag/wht_test/shopify-features` `https://bitbucket.org/rudderlabs/librs360-shopify-features/tag/wht_test/shopify-features`


**4\. URL for a specific commit within the repository**

  * **Syntax:**

`https://<provider-host>/<org-name>/<repo-name>/commit/<commit-hash>/path/to/project`

  * **Example:**

`https://github.com/rudderlabs/librs360-shopify-features/commit/b8d49/shopify-features` `https://gitlab.com/rudderlabs/librs360-shopify-features/commit/b8d49/shopify-features` `https://bitbucket.org/rudderlabs/librs360-shopify-features/commit/b8d49/shopify-features`


> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports the git SSH URL with following pattern only in the dashboard:
> 
>   * `git@<provider-host>:<org-name>/<repo-name>/tree/<branch-name>`
>   * `git@<provider-host>:<org-name>/<repo-name>`
>   * `git@<provider-host>:<org-name>/<repo-name>/tree/main/path/to/project`
> 

> 
> RudderStack supports any subfolder in git project without .git extension.

## View model dependencies

You can create a DAG to see all the model dependencies, that is, how a model is dependent on other models by using any one of the following commands:

`pb show dataflow`  
OR  
`pb show dependencies`

Further, you can use the `pb show models` command to view information about the models in your project. See [show](<https://www.rudderstack.com/docs/archive/profiles/0.12/cli-user-guide/commands/#show>) command for more information.

## Multi-version support

> ![info](/docs/images/info.svg)
> 
> This feature is supported for the Profiles versions 0.10.8, 0.11.5, and 0.12.0 onwards.

You can constraint your Profiles project to run only on specific version(s) by specifying it in the `pb_project.yaml` file, under `python_requirements` key. For example, use the below snippet to run your project on v0.10.8:
    
    
    python_requirements:
      - profiles-rudderstack==0.10.8
    

Use the below snippet to stay on any minor version between 0.12.0 and 0.13.0. If a new minor version is released, your project will be auto-migrated to that version:
    
    
    python_requirements:
      - profiles-rudderstack>=0.12.0,<0.13.0
    

If you do not specify any version in `pb_project.yaml`, the latest Profiles version is used by default. The version constraints follow the same syntax as those of [Python dependency specifiers](<https://packaging.python.org/en/latest/specifications/dependency-specifiers/>).

Make sure that the version of Profiles project is the same in your environment and the `pb_project.yaml` file otherwise, RudderStack will throw an error.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.12/example/predictive-features-snowflake/custom-code/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.12/faq/>)