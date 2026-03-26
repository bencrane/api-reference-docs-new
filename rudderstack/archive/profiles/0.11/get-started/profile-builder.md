# Profile Builder CLI

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profile Builder CLI

Create a Profiles project using the Profile Builder (PB) tool.

* * *

  * __7 minute read

  * 


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
    

See also: [Setup and installation FAQ](<https://www.rudderstack.com/docs/archive/profiles/0.11/faq/#setup-and-installation>)

### 2: Create warehouse connection

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports **Snowflake** , **Redshift** , **BigQuery** , and **Databricks** warehouses for Profiles. You must grant certain [warehouse permissions](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/permissions/>) to let RudderStack read from schema having the source tables (for example, `tracks` and `identifies` tables generated via Event Stream sources), and write data in a new schema created for Profiles.

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
    

> ![info](/docs/images/info.svg)
> 
> See the [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/admin-account-identifier.html>) to learn more about the account identifier.

A sample connection for a Redshift account is as follows:

**Using warehouse credentials**
    
    
     How would you like to connect with warehouse? [1] Using the warehouse credentials[Username, Password]
    [2] Using access key security credentials values [AWS Access Key ID and Secret Access Key].
    1
    Please enter the following details for creating a new connection, that will enable pb to connect to your redshift account.
    The created connections details will be stored in the file /Users/rudderstack/.pb/siteconfig.yaml
    Enter Connection Name: test
    Enter target:  (default:dev):  # Press enter, leaving it to default
    Enter host: warehouseabc.us-west-1.redshift.amazonaws.com
    Enter port: 5439
    Enter dbname: your_rudderstack_db 
    Enter schema: rs_profiles # A segregated schema for storing tables/views created by Profiles
    Enter user: profiles_test_user
    Enter password: <password>
    Enter sslmode: options - [disable require]: # Enter "require" in case your Redshift connection mandates sslmode. 
    Append to /Users/rudderstack/.pb/siteconfig.yaml? [y/N]
    y
    

**Using access key security credentials**
    
    
     How would you like to connect with warehouse? [1] Using the warehouse credentials[Username, Password]
    [2] Using access key security credentials values [AWS Access Key ID and Secret Access Key].
    2
    Please enter the following details for creating a new connection, that will enable pb to connect to your redshift account.
    The created connections details will be stored in the file /Users/rudderstack/.pb/siteconfig.yaml
    Enter Connection Name: test
    Enter target:  (default:dev):  # Press enter, leaving it to default
    Enter host: warehouseabc.us-west-1.redshift.amazonaws.com
    Enter dbname: your_rudderstack_db 
    Enter schema: rs_profiles # A segregated schema for storing tables/views created by Profiles
    Enter user: profiles_test_user
    Enter shared_profile: as
    Append to /Users/rudderstack/.pb/siteconfig.yaml? [y/N]
    y
    

> ![info](/docs/images/info.svg)
> 
> To know more about host, log in to your AWS Console and go to **Clusters**.

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
    

This creates a [site configuration file](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/site-configuration/>) inside your home directory: `~/.pb/siteconfig.yaml`. If you don’t see the file, enable the **View hidden files** option.

### 3: Create project

Run the following command to create a sample project:
    
    
    pb init pb-project -o MyProfilesProject
    

The above command creates a new project in the **MyProfilesProject** folder with the following structure:

[![Project structure](/docs/images/profiles/project-structure.webp)](</docs/images/profiles/project-structure.webp>)

See [Project structure](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/structure/>) for more information on the PB project files.

Navigate to the `pb_project.yaml` file and set the value of `connection:` to the connection name as defined in the previous step.

### 4: Change input sources

  * Navigate to your project and open the `models/inputs.yaml` file. Here, you will see a list of tables/views along with their respective ID types.
  * Replace the placeholder table names with the actual table names in the `table` field.


See [Project structure](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/structure/#inputs>) for more information on setting these values.

### 5: Validate project

Navigate to your project and validate your warehouse connection and input sources:
    
    
    pb validate access
    

If there are no errors, proceed to the next step. In case of errors, check if your warehouse schemas and tables have the [required permissions](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/permissions/>).

> ![warning](/docs/images/warning.svg)
> 
> Currently, this command is not supported for BigQuery warehouse.

### 6: Generate SQL files

Compile the project:
    
    
    pb compile
    

This generates SQL files in the `output/` folder that you can run directly on the warehouse.

### 7: Generate output tables

Run the project and generate [material tables](<https://www.rudderstack.com/docs/archive/profiles/0.11/glossary/#material-tables>):
    
    
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

You can run the `pb show models` command to get the exact name and path of the generated ID stitcher/feature table. See [show](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/commands/#show>) command for more information.

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

To migrate an existing PB project to the [schema version](<https://www.rudderstack.com/docs/archive/profiles/0.11/glossary/#schema-versions>) supported by your PB binary, navigate to your project’s folder. Then, run the following command to replace the contents of the existing folder with the new one:
    
    
    pb migrate auto --inplace
    

A confirmation message appears on screen indicating that the migration is complete. A sample message for a user migrating their project from version 25 to 44:
    
    
    2023-10-17T17:48:33.104+0530	INFO	migrate/migrate.go:161	
    Project migrated from version 25 to version 44
    

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/get-started/quickstart-ui/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/data-modeling/>)