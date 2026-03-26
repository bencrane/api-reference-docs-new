# Site Configuration

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Site Configuration

Know the detailed specifications mentioned in a site configuration file.

* * *

  * __2 minute read

  * 


RudderStack creates a site configuration file (`~/.pb/siteconfig.yaml`) while [creating a warehouse connection](<https://www.rudderstack.com/docs/archive/profiles/0.11/get-started/profile-builder/#2-create-warehouse-connection>). It contains the following details including secrets (if any):

  * Warehouse connection details and its credentials.
  * Git repository connection credentials (if any).


> ![success](/docs/images/tick.svg)
> 
> If you have multiple PB projects and they use different warehouse connections, you can store the details for multiple connections in the same site configuration file.

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
              red:
                  dbname: warehouse_rs
                  host: warehouse.abc.us-east-3.redshift.amazonaws.com
                  password: password
                  port: 5419
                  schema: rs_profiles
                  type: redshift
                  user: redshift_user
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
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/developer-guides/permissions/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/developer-guides/structure/>)