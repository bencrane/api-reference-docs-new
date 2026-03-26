# Profiles Quickstart

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles Quickstart

Create a Profiles project using the Profile Builder (PB) tool.

* * *

  * __3 minute read

  * 


## Prerequisites

  * [Python 3](<https://www.python.org/downloads/>) installed on your computer.
  * Admin privileges on your computer.


## 1\. Install Profile Builder

[Create](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/create-new-project/#create-virtual-environment>) and activate the virtual environment:
    
    
    python3 -m venv .venv
    source .venv/bin/activate
    

[Install](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/create-new-project/#install-profiles>) the Profiles Builder (PB) package:
    
    
    pip install profiles-rudderstack
    

Verify the installation was successful:
    
    
    pb version
    

## 2\. Create warehouse connection

Profiles supports Snowflake, Redshift, BigQuery and Databricks. The user in your connection configuration must have permission to read from schemas containing source data and write to the schema created for Profiles.

Create a warehouse connection:
    
    
    pb init connection
    

Follow the prompts to enter details about your warehouse connection:
    
    
    Select a warehouse: s
    Enter Connection Name: my_warehouse
    Enter target: (default:dev): # Press enter, leaving it to default
    Enter account: company.us-east-1
    Enter warehouse: RUDDER_WAREHOUSE
    Enter dbname: RUDDER_EVENTS
    Enter schema: RUDDER_PROFILES
    Enter user: <YOUR_USERNAME>  // Optional for Databricks
    Enter password: <YOUR_PASSWORD>
    Enter role: <YOUR_ROLE>
    Append to /Users/<user_name>/.pb/siteconfig.yaml? [y/N] y
    

This creates a local site configuration file inside your home directory: `~/.pb/siteconfig.yaml`. Your Profiles project uses this file to access the warehouse, git credentials, and other details. If you don’t see the file, enable the **view hidden files** option.

## 3\. Create Profiles project

Initialize a new Profiles project:
    
    
    pb init pb-project -o my-project
    

This creates a new project in the `my-project` folder with the [initial project structure](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/project-structure/#initial-project-structure>).

If you would like to create a project in the current folder instead, run:
    
    
    pb init pb-project -o .
    

Open the `pb_project.yaml` file at the root of your project and set the value of `connection:` to the connection name as defined in the previous step.

## 4\. Add inputs

Open the `inputs.yaml` file in the `models` folder. This file is where you will define your inputs.

Each input has a `name`, source `table` (in the format `database.schema.table`), `occurred_at_col` (timestamp column if available), and list of entity `ids`. Each ID inclues a `select` (column name), `type` (ID type as defined in `pb_project.yaml`) and `entity` name (defined in `pb_project.yaml`).

Edit the two sample inputs to use your own data. This may only require changing the `table` fields to point to your `identifies` and `tracks` tables. If your `identifies` table does not include email addresses, remove that ID. If email address is included under a different column name, change the `select` field accordingly.

## 5\. Validate warehouse access

Validate your warehouse connection has the necessary access:
    
    
    pb validate access
    

If there are no errors, proceed to the next step. In case of errors, make sure to provide the necessary [warehouse permissions](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/create-new-project/#grant-warehouse-permissions>).

## 6\. Run project

[Run the project](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/run-project/>) on your data warehouse:
    
    
    pb run
    

This compiles your project into SQL files stored in the `output` folder, then runs that SQL on your warehouse.

## 7\. Add feature

Open the `profiles.yaml` file in the `models` folder. There should be a var group with four entity vars, two of which are features (included in feature views).

Add a new entity var / feature that gets the event count for each user:
    
    
    - entity_var:
        name: event_count
        select: COUNT(*)
        from: inputs/rsTracks
        description: No. of events tracked for customer
    

Profiles automatically groups data by customer, so you only need to specify the aggregate function.

If you run the project again, you will see this `event_count` feature in your feature views.

## 8\. Add cohort

The feature views in your warehouse contain features for all customers. A cohort can be used to create feature views for a subset of customers.

In the `profiles.yaml` file, add a cohort for power users:
    
    
    models:
      - name: power_users
        model_type: entity_cohort
        model_spec:
          extends: user/all
          materialization:
            output_type: view
          filter_pipeline:
            - type: include
              value: "{{ user.event_count }} > 45"
    

This `power_users` cohort uses the `event_count` entity var defined above, only including customers with more than 45 events tracked.

Feature views for this cohort will be automatically generated during the next project run.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.23/overview/how-profiles-works/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.23/concepts/>)