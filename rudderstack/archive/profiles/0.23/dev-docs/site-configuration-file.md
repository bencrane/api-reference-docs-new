# Site Configuration File

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Site Configuration File

Understand the site configuration file specifications.

* * *

  * __3 minute read

  * 


RudderStack creates a site configuration file (`~/.pb/siteconfig.yaml`) while [creating a warehouse connection](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/create-new-project/#create-warehouse-connection>).

This guide walks you through the site configuration file spec in detail.

## Overview

The site configuration file (`~/.pb/siteconfig.yaml`) contains the following details including secrets (if any):

  * Warehouse connection details and its credentials.

  * Git repository connection credentials (if any). Follow these steps to add the credentials:

    1. [Generate the SSH Key](<https://git-scm.com/book/en/v2/Git-on-the-Server-Generating-Your-SSH-Public-Key>).
    2. Associate the SSH key to your Git project.
    3. Add private key as credentials in the `siteconfig.yaml` file under `key` field in the `gitcreds` field.


> ![success](/docs/images/tick.svg)
> 
> You can store the details for multiple warehouse connections in the same site configuration file. This is helpful in cases where you have multiple Profiles projects with different warehouse connections.

## Example

A sample site configuration file containing multiple warehouse connection details is shown below:
    
    
    connections:
      # connection name
      prod-db-profile:
          target: dev
          outputs:
              dev:
                  account: inb828.us-west-3
                  dbname: MAT_STORE_DEV
                  password: password_dev
                  role: PROFILES_ROLE_DEV
                  schema: AB_SCHEMA_DEV
                  type: snowflake
                  user: profiles_demo
                  warehouse: DEV_WAREHOUSE
              prod:
                  account: inc654.us-west-3
                  dbname: MAT_STORE
                  password: password
                  role: PROFILES_ROLE
                  schema: AB_SCHEMA
                  type: snowflake
                  user: profiles_demo
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
              snowflake-keypair: # example of an unencrypted Snowflake key-pair
                  type: snowflake
                  account: vb8.us-east-1
                  dbname: PROD_DB
                  role: PROFILES_ROLE
                  warehouse: RUDDER
                  schema: RS_PROFILES
                  user: PROFILES_USER_UNC
                  useKeyPairAuth: true
                  privateKey: <YOUR_COMPLETE_ENCRYPTED_PRIVATE_KEY>
              snowflake-encrypted-keypair: # example of an encrypted Snowflake key-pair
                  type: snowflake
                  account: vb8.us-east-1
                  dbname: PROD_DB
                  role: PROFILES_ROLE
                  warehouse: RUDDER
                  schema: RS_PROFILES
                  user: PROFILES_USER_EC
                  useKeyPairAuth: true
                  privateKey: <YOUR_COMPLETE_ENCRYPTED_PRIVATE_KEY>
                  privateKeyPassphrase: valuegoeshere!
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
                  access_key_id: <YOUR_ACCESS_KEY_ID>
                  secret_access_key: <YOUR_SECRET_ACCESS_KEY>
               big:
                  credentials:
                    auth_provider_x509_cert_url: https://www.googleapis.com/oauth2/v1/certs
                    auth_uri: https://accounts.google.com/o/oauth2/auth
                    client_email: johndoe@big-query-integration-poc.iam.gserviceaccount.com
                    client_id: "123345678909872"
                    client_x509_cert_url: https://www.googleapis.com/robot/v1/metadata/x509/johndoe%40big-query-integration-poc.iam.gserviceaccount.com
                    private_key: <YOUR_COMPLETE_PRIVATE_KEY>
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
       key: <YOUR_COMPLETE_OPENSSH_PRIVATE_KEY>
     - reporegex: "https://github.com/rudderlabs/*" # https url
       basic_auth:
         username: oauth2
         password: ... # your GitHub access token with read permission
    block_store_creds:
      - type: minio # type Minio
        bucket: test
        endpoint: https://localhost:9000/
        access_key_id: access_key_id
        secret_access_key: secret_access_key
      - type: s3 # S3 credentials with access key
        bucket: shubham # Optional; use creds for this bucket
        region: us-east-1
        access_key_id: access_key_id
        secret_access_key: secret_access_key
        session_token: session_token
      - type: s3 # S3 credentials with ARN
        bucket: shopify
        region: us-east-1
        secrets_arn: secrets_arn
      - type: s3 # S3 credentials with shared profile
        bucket: shopify
        region: us-east-1
        shared_profile: shared_profile
    py_models:
        enabled: true # in case you are using Python models in your project, else set it to false
        python_path: /opt/anaconda3/bin/python # the path where Python is installed (run `which python` to get the full path). If `py_models` is not enabled, set it to `""`. For Windows, you may pass the path value as: python.exe
        credentials_presets: null
        allowed_git_urls_regex: ""
    cache_dir: /Users/YOURNAME/.pb/WhtGitCache/ # For Windows, the directory path will have forward slash (\)
    filepath: /Users/YOURNAME/.pb/siteconfig.yaml # For Windows, the file path will have forward slash (\)
    

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends defining two `target` within a single connection- one for dev/staging and the other for production.
> 
> For example, see the connection named `prod-db-profile` in the sample file above. The default target is set to `dev`, as specified by the `target` key. To change the output to production, you can run `pb run -t prod`.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.23/dev-docs/project-structure/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.23/dev-docs/ide/>)