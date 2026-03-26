# Additional Concepts

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Additional Concepts

Additional concepts related to Profiles like packages, best practices, partial feature tables, etc.

* * *

  * __19 minute read

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
  * [profiles-base-features](<https://github.com/rudderlabs/profiles-base-features>)
  * [profiles-shopify-features](<https://github.com/rudderlabs/profiles-shopify-features>)
  * [profiles-ecommerce-features](<https://github.com/rudderlabs/profiles-ecommerce-features>)
  * [profiles-stripe-features](<https://github.com/rudderlabs/profiles-stripe-features>)
  * [profiles-multieventstream-features](<https://github.com/rudderlabs/profiles-multieventstream-features>)


Generally, there will be some deviations in terms of the database name and schema name of input models - however, you can easily handle this by remapping inputs.

A sample `pb_project.yaml` file may look as follows:
    
    
    name: app_project
    schema_version: 67
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
    

  * **id_types**


Enlists the type of identifiers to be used for creating ID stitcher/`entity_var`/`input_var`. For example, you can define anonymous IDs that do not include the value `undefined` or email addresses in proper format.

Field| Data type| Description  
---|---|---  
`name`| String| Name of the ID type like email, user ID, etc.  
`extends`| List| (Optional) Name of the ID type you wish to extend.  
`filters`| List| Filter(s) the ID types to include/exclude specific values. The filters are processed in the defined order.  
  
  * **filters**

Field| Data type| Description  
---|---|---  
`type`| String| Type of filter. Allowed values are `include` or `exclude`.  
`value`| String| Value to match, for example, you can reject certain invalid ID values like `NaN`, `unknown`, `test@domain.com`, etc.  
`regex`| String| Regular expression with which to match the values.  
`sql`| List| SQL statement with `select` and `from` keys.  
  
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

You can use the `contract` field to specify the constraints your model should adhere to while using the warehouse data.

Suppose a model (`M1`) is dependent on model (`M2`). Now, `M1` can specify a contract defining the columns and entities that it needs from `M2` to be executed successfully. Also, it becomes mandatory for `M2` to provide the required columns and entities for contract validation.

**Example 1**

The following `inputs.yaml` file defines a contract:
    
    
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
    

Here, the contract specifies that:

  * The input table (`rsIdentifies`) must exist in the warehouse.
  * The model is an event stream model where every row in the table must be an event.
  * There must be a column in the inputs table (`rsIdentifies`) which represents the user identifier for `user` entity.
  * The input table (`rsIdentifies`) must have the `timestamp`, `user_id`, and `anonymous_id` columns.


**Example 2**

Let’s consider a SQL model, `rsSessionTable` which takes `shopify_session_features` as an input:
    
    
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
            - name: anonymous_id
              type: string
    

There are two contracts defined in the above example:

  * Contract for `shopify_session_features` model which dictates that the `user_id`, and `anonymous_id` columns must be present.
  * Contract for `rsSessionTable` model which dictates that it must have a column representing the user identifier for `user` entity. Also, the `user_id`, and `anonymous_id` columns must be present.


This helps in improving the data quality, error handling, and enables static and dynamic validation of the project.

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
    

## Associate SSH key to Git project

To add public SSH key to your Git project:

  1. Open your Profile project’s Git repository in the browser and click **Settings**.
  2. Click **SSH Keys**.
  3. Assign a name (say `Sample Profiles Key`) and paste the key generated from the RudderStack dashboard or a public-key generated using CLI.
  4. Click **Add Key**.


For more information, see:

  * [GitHub documentation](<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#deploy-keys>)
  * [GitLab documentation](<https://docs.gitlab.com/ee/user/project/deploy_keys/#create-a-project-deploy-key>)
  * [BitBucket documentation](<https://confluence.atlassian.com/bitbucketserver/ssh-access-keys-for-system-use-776639781.html>)


## Use private Git repos via CLI

Follow these steps:

  1. [Generate the SSH Key](<https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key>).
  2. Associate the SSH Key to your Git Project.
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

## Best schema version (tags)

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

## View model dependencies

You can create a DAG to see all the model dependencies, that is, how a model is dependent on other models by using any one of the following commands:

`pb show dataflow`  
OR  
`pb show dependencies`

Further, you can use the `pb show models` command to view information about the models in your project. See [show](<https://www.rudderstack.com/docs/archive/profiles/0.14/cli-user-guide/commands/#show>) command for more information.

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

Make sure that the version of Profiles project is the same in your environment and the `pb_project.yaml` file. Otherwise, RudderStack will throw an error.

## Reuse models output

> ![warning](/docs/images/warning.svg)
> 
> This is an experimental feature.

You can define the `time_grain` parameter for a model to ensure the model runs only once in that time period. It lets you reuse the output material of that model within the time period, preventing unnecessary recalculations⁠.

For example, if you set the `time_grain` value for an ID stitcher model to a `day` and run the feature table model (based on the ID stitcher) multiple times during a day, the feature table model will reuse the ID stitcher’s output to compute the features. This will save a large amount of time and computations whenever you run the feature table model within that day.

Similarly, you can choose to run a feature such as `weekly_spends` only once a week, or `last_active_day` on a daily basis.

> ![warning](/docs/images/warning.svg)
> 
> Setting `time_grain` parameter does not mean that the model will run automatically at the specified time period. It just ensures that the model runs only once during that time period and its outputs are reused within that duration. To schedule your project run, you must use the RudderStack dashboard.
> 
> For example, if `time_grain` for a model is set to a `week`, its outputs will be reused throughout the week and running it twice within the week won’t change its results.

You can define the `time_grain` parameter in the `profiles.yaml` file of your project:
    
    
    models:
      - name: user_id_graph
        model_type: id_stitcher
        model_spec:
          entity_key: user
          time_grain: "hour"
          materialization:
            run_type: incremental
          edge_sources:
            - from: inputs/rsIdentifies
            - from: inputs/rsTracks
    var_groups:
      - name: user_daily_vars
        time_grain: "day"
        entity_key: user
        vars:
          - entity_var:
              name: days_since_last_seen
              select: "{{macro_datediff('{{user.Var(\"max_timestamp\")}}')}}"
      - name: user_weekly_vars
        time_grain: "week"
        entity_key: user
        vars:
          - entity_var:
             name: weekly_amt_spent
             select: sum(total_price_usd) - coalesce(sum(total_price_usd_order_cancelled), 0)
             from: models/rsOrderCreatedOrderCancelled
             where: "{{macro_datediff_n('timestamp','7')}}"
    

In the above example, suppose you schedule your Profiles project to run every hour. The output for `user_id_graph` model will be computed every hour, the output for `user_daily_vars` will be computed once a day, and the output for `user_weekly_vars` will be computed once a week.

For a default ID stitcher model, you can define the `time_grain` value in the `entities` section as shown below:
    
    
    entities:
      - name: user
        id_types:
          - test_id
          - exclude_id
        default_id_stitcher:
          time_grain: "day"
    

#### Supported values

You can set the following values for the `time_grain` field:

  * `tick`: Considers all the data up to the current moment (default value).
  * `10minutes`: Considers data up to the last 10-minute interval.
  * `hour`: Considers data up to the end of the previous hour.
  * `day`: Considers data up to the end of the previous day.
  * `week`: Considers data up to the end of the previous week.
  * `month`: Considers data up to the end of the previous month.
  * `year`: Considers data up to the end of the previous year.


## Enable/disable model run

When you have various interdependent models, you might want to run only the required ones for a specific output.

RudderStack provides the `enable_status` parameter which lets you specify whether to run a model or not. Using it, you can exclude the unnecessary models from the execution process. You can assign the following values to the `enable_status` field in your `pb_project.yaml` file:

  * `good_to_have` (default): It will not execute or cause a failure when it is not possible to execute the model.
  * `must_have`: It will cause a failure when is not possible to execute the model.
  * `only_if_necessary`: The model gets disabled if it has no dependency on the final output. It is the default value for a default ID stitcher model and ensures that the model is not executed if it is not required.
  * `disabled`: The model gets disabled and is not executed.


A sample `pb_project.yaml` file with `enable_status` parameter:
    
    
    name: app_project
    schema_version: 67
    connection: test
    model_folders:
      - models
    entities:
      - name: user
        id_types:
          - user_id
          - anonymous_id
        default_id_stitcher:
          validity_time: 24h # 1 day
          materialization:
            run_type: incremental
            enable_status: good_to_have
          incremental_timedelta: 12h # half a day
    
    id_types:
      - name: user_id
        filters:
          - type: include
            regex: "([0-9a-z])*"
          - type: exclude
            value: ""
      - name: anonymous_id
    

**Use-case**

Consider a scenario where an ID stitcher model (`ids`) is dependent on `tbl_a` and `tbl_b`, and a feature table model (`ft1`) depends on the ID Stitcher (`ids`) and an input model `tbl_a`.

  * If the ID stitcher and feature table models are marked as `only_if_necessary`, there is no need to execute either of them. However, if the feature table is marked as `good_to_have`/`must_have`, then all the models must run to create final output.
  * If `tbl_a` is set to `disabled`, the ID stitcher and feature table will not run. If either of them is marked as `must_have`, the project will run into an error.


## Window functions

A window function operates on a window (group) of related rows. It performs calculation on a subset of table rows that are connected to the current row in some way. The window function has the ability to access more than just the current row in the query result.

The window function returns one output row for each input row. The values returned are calculated by using values from the sets of rows in that window. A window is defined using a window specification, and is based on three main concepts:

  * Window partitioning, which forms the groups of rows (`PARTITION BY` clause)
  * Window ordering, which defines an order or sequence of rows within each partition (`ORDER BY` clause)
  * Window frames, which are defined relative to each row to further restrict the set of rows (`ROWS` specification). It is also known as the frame clause.


**Snowflake** does not enforces users to define the cumulative or sliding frames, and considers `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` as the default cumulative window frame. However, you can override this by defining the frame manually.

On the **Redshift** aggregate window function list given below, specify the `frame_clause` while using any function from the list:

  * `AVG`
  * `COUNT`
  * `CUME_DIST`
  * `DENSE_RANK`
  * `FIRST_VALUE`
  * `LAG`
  * `LAST_VALUE`
  * `LEAD`
  * `LISTAGG`
  * `MAX`
  * `MEDIAN`
  * `MIN`
  * `NTH_VALUE`
  * `PERCENTILE_CONT`
  * `PERCENTILE_DISC`
  * `RATIO_TO_REPORT`
  * `STDDEV_POP`
  * `STDDEV_SAMP` (synonym for `STDDEV`)
  * `SUM`
  * `VAR_POP`
  * `VAR_SAMP` (synonym for `VARIANCE`)


In the Redshift ranking window functions given below, **do not** specify the `frame_clause` while using any function from the list:

  * `DENSE_RANK`
  * `NTILE`
  * `PERCENT_RANK`
  * `RANK`
  * `ROW_NUMBER`


> ![warning](/docs/images/warning.svg)
> 
> Use `frame_clause` carefully when using a window function. While It is not very critical for Snowflake, using it incorrectly in Redshift can lead to errors.

Example of using `frame_clause`:
    
    
    - entity_var:
        name: first_num_b_order_num_b
        select: first_value(tbl_c.num_b) # Specify frame clause as aggregate window function is used
        from: inputs/tbl_c
        default: -1
        where: tbl_c.num_b >= 10
        window:
            order_by:
            - tbl_c.num_b desc
            frame_clause: ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    - entity_var:
        name: first_num_b_order_num_b_rank
        select: rank() # DO NOT specify frame clause as ranking window function is used
        window:
            order_by:
            - first_num_b_order_num_b asc
    

Note how `frame_clause` is specified in first `entity_var` and not in the second one.

## Macros

Macros are the reusable functions that encapsulate complex processing logic directly within the SQL expression. You can create macros to perform computations and use them in multiple models. For example:
    
    
    macros:
      - name: subtract_range
        inputs:
          - first_date
          - second_date
        value: "{{first_date}} - {{second_date}}"
      - name: multiplyBy10_add
        inputs:
          - first_number
          - second_number
        value: "{{first_number}} * 10 + {{second_number}}"
    

You can create a file (say `macros.yaml`) file under the `models` folder and refer them using the macro name in the `profiles.yaml` file:
    
    
    - entity_var:
        name: days_since_first_sale
        select: "{{ subtract_range('{{user.Var(\"first_sale_time\")}}') }}"
    

Field| Data type| Description  
---|---|---  
`name`| String| Name to uniquely identify the macro.  
`inputs`| List| Defines the input variables to be used by the macro function.  
`value`| String| Contains the reusable function in the form of a SQL expression. Any reference to the inputs must be encapsulated within double curly brackets.  
  
See a sample [Profiles library project](<https://github.com/rudderlabs/profiles-stripe-features>) that creates user features from Stripe tables using Macros.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.14/example/predictive-features-snowflake/custom-code/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.14/changelog/>)