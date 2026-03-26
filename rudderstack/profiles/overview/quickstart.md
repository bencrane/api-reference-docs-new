# Profiles Quickstart

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Profiles Quickstart

Create a Profiles project using the Profile Builder (PB) tool.

* * *

  * __4 minute read

  * 


This guide walks you through creating a Profiles project using the Profile Builder (PB) tool.

## Prerequisites

  * [Python 3](<https://www.python.org/downloads/>) installed on your computer.
  * Admin privileges on your computer.


## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to manage Profiles projects in RudderStack.
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can have the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) depending on their workspace policy:

Permission| Description  
---|---  
**Edit**|  Make changes to the configuration of Profiles projects  
**Create & Delete**| Create or delete Profiles projects in the workspace  
**Connect**|  Connect a Profiles project to a warehouse destination  
  


> ![info](/docs/images/info.svg)The **Connect** permission also applies on the warehouse source used to create the Profiles project.  
  
**Click here to see how these permissions appear in the workspace policy**.  
![Permissions to manage Profiles projects in RudderStack dashboard](/docs/images/access-management/profiles.webp)  


> ![warning](/docs/images/warning.svg)
> 
> To make a connection, that is, connect a Profiles project to a warehouse destination, the member must have both **Edit** and **Connect** permissions on both the resources.

#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>):

  * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) and members with the [**Connections Admin** role](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#connections>) in their workspace policy can create and delete Profiles projects, manage their configuration, and connect them to a warehouse destination
  * Members with the [**Connections Editor** role](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#connections>) in their workspace policy can only edit the Profiles project configuration and connect Profiles projects to a warehouse destination

[![Profiles permissions in the legacy framework](/docs/images/access-management/tracking-plan-permissions-legacy-framework.webp)](</docs/images/access-management/tracking-plan-permissions-legacy-framework.webp>)

## 1\. Install Profile Builder

Create and activate the virtual environment:
    
    
    python3 -m venv .venv
    source .venv/bin/activate
    

[Install](<https://www.rudderstack.com/docs/profiles/dev-docs/create-new-project/#install-profiles>) the Profiles Builder (PB) package:
    
    
    pip3 install profiles-rudderstack
    

> ![info](/docs/images/info.svg)
> 
> **Install the beta release**
> 
> If you’re interested in trying the Profiles 0.25 (Beta) release, install the specific beta version instead:
> 
> `pip3 install profiles-rudderstack==0.25.0b5`

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
    

This creates a new project in the `my-project` folder with the [initial project structure](<https://www.rudderstack.com/docs/profiles/dev-docs/project-structure/#initial-project-structure>).

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
    

If there are no errors, proceed to the next step. In case of errors, make sure to provide the necessary [warehouse permissions](<https://www.rudderstack.com/docs/profiles/dev-docs/create-new-project/#grant-warehouse-permissions>).

## 6\. Run project

[Run the project](<https://www.rudderstack.com/docs/profiles/dev-docs/run-project/>) on your data warehouse:
    
    
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

  


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/overview/how-profiles-works/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/overview/quickstart-ui/>)