# Profile Builder CLI

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profile Builder CLI

Create a Profiles project using the Profile Builder (PB) tool.

* * *

  * __10 minute read

  * 


> ![info](/docs/images/info.svg)
> 
> While creating a Profiles project, you can choose either of the below:
> 
>   * **Profile Builder (PB) CLI** which gives you the flexibility to create, develop, and debug your Profiles project using various commands in fine detail. You can explore and implement the exhaustive list of features and functionalities offered by Profiles.
>   * **Profiles UI** which provides a step-by-step intuitive workflow in the RudderStack dashboard. You can configure your project, schedule its run, explore the outputs and the user profiles.
> 


**Profile Builder (PB)** is a command-line interface (CLI) tool that simplifies data transformation within your warehouse. It generates customer profiles by stitching data together from multiple sources.

This guide lists the detailed steps to install and use the Profile Builder (PB) tool to create, configure, and run a new project.

## Prerequisites

You must have:

  * [Python 3](<https://www.python.org/downloads/>) installed on your machine.
  * Admin privileges on your machine.


## Steps

To set up a project using the PB tool, follow these steps:

### 1: Install PB

Install the Profile Builder tool by running the following command:
    
    
    pip3 install profiles-rudderstack
    

If you have already installed PB, use the following command to update its version:
    
    
    pip3 install profiles-rudderstack -U
    

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using a Python virtual environment to maintain an isolated and clean environment.
>     
>     
>     pipx install profiles-rudderstack
>     

Validate Profile Builder’s version after install using:
    
    
    pb version
    

See also: [Setup and installation FAQ](<https://www.rudderstack.com/docs/archive/profiles/0.13/faq/#setup-and-installation>)

> ![info](/docs/images/info.svg)
> 
> If you are an existing user, migrate your project to the new schema. See Migrate your existing project for more information.

### 2: Create warehouse connection

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports **Snowflake** , **Redshift** , **BigQuery** , and **Databricks** warehouses for Profiles. You must grant certain [warehouse permissions](<https://www.rudderstack.com/docs/archive/profiles/0.13/permissions/>) to let RudderStack read from schema having the source tables (for example, `tracks` and `identifies` tables generated via Event Stream sources), and write data in a new schema created for Profiles.

Create a warehouse connection to allow PB to access your data:
    
    
    pb init connection
    

Then, follow the prompts to enter details about your warehouse connection.

A sample connection for a Snowflake account is as follows:
    
    
    Enter Connection Name: test
    Enter target:  (default:dev):  # Press enter, leaving it to default
    Enter account: ina13147.us-east-1
    Enter warehouse: rudder_warehouse
    Enter dbname: your_rudderstack_db 
    Enter schema: rs_profiles # A segregated schema for storing tables/views created by Profiles
    Enter user: profiles_test_user
    Enter password: <password>
    Enter role: profiles_role
    Append to /Users/<user_name>/.pb/siteconfig.yaml? [y/N]
    y
    

  * **Connection Name** : Name of the connection in the project file.
  * **Target** : Environment name, such as `dev`, `prod`, `test`, etc. You can specify any target name and create a separate connection for the same.
  * **Account** : See [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/admin-account-identifier.html>) for more information.
  * **Warehouse** : Name of the warehouse.
  * **Database name** : Name of the database inside warehouse where model outputs will be written.
  * **Schema** : Name of the schema inside database where you’ll store identity stitcher and entity features.
  * **User** : Name of the user in data warehouse.
  * **Password** : Password for the above user.
  * **Role** : Name of the user role.


RudderStack supports various user authentication mechanisms for Redshift:
    
    
    Enter Connection Name: test
    Enter target:  (default:dev):  # Press enter, leaving it to default
    Enter dbname: your_rudderstack_db 
    Enter schema: rs_profiles # A segregated schema for storing tables/views created by Profiles
    Enter user: profiles_test_user
    Enter sslmode: options - [disable require]: disable # Enter "require" in case your Redshift connection mandates sslmode. 
    How would you like to authenticate with the warehouse service? Please select your method by entering the corresponding number:
    y
    [1] Warehouse Credentials: Log in using your username and password.
            Format: [Username, Password]
    [2] AWS Programmatic Credentials: Authenticate using one of the following AWS credentials methods:
            a) Direct input of AWS Access Key ID, Secret Access Key, and an optional Session Token.
                    Format: [AWS Access Key ID, Secret Access Key, Session Token (Optional)]
            b) AWS configuration profile stored on your system.
                    Format: [AWS Configuration Profile Name]
            c) Use an AWS Secrets Manager ARN to securely retrieve credentials.
                    Format: [Secret ARN]
    

  * **Connection Name** : Name of the connection in the project file.
  * **Target** : Environment name, such as `dev`, `prod`, `test`, etc. You can specify any target name and create a separate connection for the same.
  * **Host** : Log in to AWS Console and go to **Clusters** to know about host.
  * **Port** : Port number to connect to the warehouse.
  * **Database name** : Name of the database inside warehouse where model outputs will be written.
  * **Schema** : Name of the schema inside database where you’ll store identity stitcher and entity features.
  * **User** : Name of the user in data warehouse.
  * **Password** : Password for the above user.


### Warehouse credentials

If you choose to use the warehouse credentials (option 1), enter the following details:
    
    
    Enter host: warehouseabc.us-west-1.redshift.amazonaws.com
    Enter port: 5439
    Enter password: <password>
    Enter tunnel_info: Do you want to use SSH Tunnel to connect with the warehouse? (y/n): y
    Enter ssh user: user
    Enter ssh host: 1234
    Enter ssh port: 12345
    Enter ssh private key file path: /Users/alex/.ssh/id_ed25519.pub
    Append to /Users/alex/.pb/siteconfig.yaml? [y/N] y
    

### AWS Programmatic Credentials

If you choose to use AWS Access Key ID, Secret Access Key, and an optional Session Token from AWS Programmatic Credentials (option 2a), enter the following details:

**For Redshift Cluster**
    
    
     Which Redshift Service you want to connect with?
            [c]Redshift Cluster
            [s]Redshift Serverless
    c
    Enter Redshift Cluster Identifier: cluster-id
    Enter access_key_id: aid
    Enter secret_access_key: ***
    Enter session_token: If you are using temporary security credentials, please specify the session token, otherwise leave it empty.
    stoken
    Append to /Users/alex/.pb/siteconfig.yaml? [y/N] y
    

**For Redshift Serverless**
    
    
     Which Redshift Service you want to connect with?
            [c]Redshift Cluster
            [s]Redshift Serverless
    s
    Enter Redshift Serverless Workgroup Name: wg-name
    Enter access_key_id: aid
    Enter secret_access_key: ***
    Enter session_token: If you are using temporary security credentials, please specify the session token, otherwise leave it empty.
    Append to /Users/alex/.pb/siteconfig.yaml? [y/N] y
    

If you choose to use AWS configuration profile stored on your system from AWS Programmatic Credentials (option 2b), enter the following details:

**For Redshift Cluster**
    
    
     Which Redshift Service you want to connect with?
            [c]Redshift Cluster
            [s]Redshift Serverless
    c
    Enter Redshift Cluster Identifier: ci   
    Enter shared_profile: default
    Enter region: us-east-1
    Append to /Users/alex/.pb/siteconfig.yaml? [y/N] y
    

**For Redshift Serverless**
    
    
     Which Redshift Service you want to connect with?
            [c]Redshift Cluster
            [s]Redshift Serverless
    s
    Enter Redshift Serverless Workgroup Name: serverless-wg
    Enter shared_profile: default
    Append to /Users/alex/.pb/siteconfig.yaml? [y/N] y
    

If you choose to use an AWS Secrets Manager ARN to securely retrieve credentials from AWS Programmatic Credentials (option 2c), enter the following details:

**For Redshift Cluster**
    
    
     Which Redshift Service you want to connect with?
            [c]Redshift Cluster
            [s]Redshift Serverless
    c
    Enter Redshift Cluster Identifier: cluster-identifier
    Enter secrets_arn: ************************
    Append to /Users/alex/.pb/siteconfig.yaml? [y/N] y
    

A sample connection for a Databricks account is as follows:
    
    
    Enter Connection Name: test
    Enter target:  (default:dev):  # Press enter, leaving it to default
    Enter host: a1.8.azuredatabricks.net # The hostname or URL of your Databricks cluster
    Enter port: 443 # The port number used for establishing the connection. Usually it is 443 for https connections.
    Enter http_endpoint: /sql/1.0/warehouses/919uasdn92h # The path or specific endpoint you wish to connect to.
    Enter access_token: <password> # The access token created for authenticating the instance.
    Enter user: profiles_test_user # Username of your Databricks account.
    Enter schema: rs_profiles # A segregated schema for storing tables/views created by Profiles
    Enter catalog: your_rudderstack_db # The database or catalog having data that you’ll be accessing.
    Append to /Users/<user_name>/.pb/siteconfig.yaml? [y/N]
    y
    

  * **Connection Name** : Name of the connection in the project file.
  * **Target** : Environment name, such as `dev`, `prod`, `test`, etc. You can specify any target name and create a separate connection for the same.
  * **Host** : Host name or URL of your Databricks cluster.
  * **Port** : Port number for establishing the connection, usually `443` for `https` connections.
  * **http_endpoint** : Path or specific endpoint you wish to connect to.
  * **access_token** : Access token for authenticating the instance.
  * **User** : Username of your Databricks account.
  * **Schema** : Name of the schema to store your output tables/views.
  * **Catalog** : Name of the database or catalog from where you want to access the data.


> ![info](/docs/images/info.svg)
> 
> RudderStack currently supports Databricks on Azure. To get the Databricks connection details:
> 
>   1. Log in to your Azure’s Databricks Web UI.
>   2. Click on **SQL Warehouses** on the left.
>   3. Select the warehouse to connect to.
>   4. Select the **Connection Details** tab.
> 


A sample connection for a BigQuery account is as follows:
    
    
    Enter Connection Name: test
    Enter target:  (default:dev):  # Press enter, leaving it to default
    Enter credentials: json file path: # File path of your BQ JSON file, for example, /Users/alexm/Downloads/big.json. Entering an incorrect path will exit the program.
    Enter project_id: profiles121
    Enter schema: rs_profiles
    Append to /Users/<user_name>/.pb/siteconfig.yaml? [y/N]
    y
    

This creates a [site configuration file](<https://www.rudderstack.com/docs/archive/profiles/0.13/cli-user-guide/structure/>) inside your home directory: `~/.pb/siteconfig.yaml`. If you don’t see the file, enable the **View hidden files** option.

### 3: Create project

Run the following command to create a sample project:
    
    
    pb init pb-project -o MyProfilesProject
    

The above command creates a new project in the **MyProfilesProject** folder with the following structure:

[![Project structure](/docs/images/profiles/project-structure.webp)](</docs/images/profiles/project-structure.webp>)

See [Project structure](<https://www.rudderstack.com/docs/archive/profiles/0.13/cli-user-guide/structure/>) for more information on the PB project files.

Navigate to the `pb_project.yaml` file and set the value of `connection:` to the connection name as defined in the previous step.

### 4: Change input sources

  * Navigate to your project and open the `models/inputs.yaml` file. Here, you will see a list of tables/views along with their respective ID types.
  * Replace the placeholder table names with the actual table names in the `table` field.


See [Project structure](<https://www.rudderstack.com/docs/archive/profiles/0.13/cli-user-guide/structure/#inputs>) for more information on setting these values.

### 5: Validate project

Navigate to your project and validate your warehouse connection and [inputInputs refers to the input data sources used to create the material (output) tables in the warehouse.](</docs/resources/glossary/#input>) sources:
    
    
    pb validate access
    

If there are no errors, proceed to the next step. In case of errors, check if your warehouse schemas and tables have the [required permissions](<https://www.rudderstack.com/docs/archive/profiles/0.13/permissions/>).

> ![warning](/docs/images/warning.svg)
> 
> Currently, this command is not supported for BigQuery warehouse.

### 6: Generate SQL files

Compile the project:
    
    
    pb compile
    

This generates SQL files in the `output/` folder that you can run directly on the warehouse. In case of any compilation errors, you will see them on your screen and also in the `logs/logfile.log` file.

### 7: Generate output tables

Run the project and generate [material tables](<https://www.rudderstack.com/docs/archive/profiles/0.13/resources/glossary/#material-tables>):
    
    
    pb run
    

This command generates and runs the SQL files in the warehouse, creating the material tables.

### 8: View generated tables

> ![info](/docs/images/info.svg)
> 
> The view `user_default_id_stitcher` will always point to the latest generated ID stitcher and `user_profile` to the latest feature table.

Use the Snowflake web UI and open <https://youraccount.snowflakecomputing.com/console> in the browser.

Use [Amazon Redshift query editor v2](<https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-via-client-tools.html>)

Use a [SQL database tool](<https://learn.microsoft.com/en-us/azure/databricks/dev-tools/index-sql>)

Use Bigquery on [Google Cloud Console](<https://console.cloud.google.com/>)

You can run the `pb show models` command to get the exact name and path of the generated ID stitcher/feature table. See [show](<https://www.rudderstack.com/docs/archive/profiles/0.13/cli-user-guide/commands/#show>) command for more information.

Then, execute the below query to view the generated tables in the warehouse:
    
    
    select * from <table_name> limit 10;
    

Here’s what the columns imply:

![ID Stitcher Table](/docs/images/profiles/idstitcher-table.webp)

  * **user_main_id** : Rudder ID generated by Profile Builder. Think of a one-to-many relationship, with one Rudder ID connected to different IDs belonging to same user such as User ID, Anonymous ID, Email, Phone number, etc.
  * **other_id** : ID in input source tables that is stitched to a Rudder ID.
  * **other_id_type** : Type of the other ID to be stitched (User ID, Anonymous ID, Email, etc).
  * **valid_at** : Date at which the corresponding ID value occurred in the source tables. For example, the date at which a customer was first browsing anonymously, or when they logged into the CRM with their email ID, etc.


![Feature Table](/docs/images/profiles/feature-table.webp)

  * **user_main_id** : Rudder ID generated by Profile Builder.
  * **valid_at** : Date when the feature table entry was created for this record.
  * **first_seen, last_seen, country, first_name, etc.** \- All features for which values are computed.


## Migrate your existing project

To migrate an existing PB project to the [schema version](<https://www.rudderstack.com/docs/archive/profiles/0.13/resources/glossary/#schema-versions>) supported by your PB binary, navigate to your project’s folder. Then, run the following command to replace the contents of the existing folder with the new one:
    
    
    pb migrate auto --inplace
    

A confirmation message appears on screen indicating that the migration is complete. A sample message for a user migrating their project from version 25 to 44:
    
    
    2023-10-17T17:48:33.104+0530	INFO	migrate/migrate.go:161	
    Project migrated from version 25 to version 44
    

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.13/get-started/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.13/get-started/quickstart-ui/>)