# Warehouse Permissions

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Warehouse Permissions

Grant RudderStack the required permissions on your data warehouse.

* * *

  * __7 minute read

  * 


RudderStack supports **Snowflake** , **Redshift** , **Databricks** , and **BigQuery** for creating unified user profiles.

To read and write data to the warehouse, RudderStack requires specific warehouse permissions as explained in the following sections.

> ![warning](/docs/images/warning.svg)
> 
> Keeping separate schemas for projects running via CLI and web is recommended. This way projects run from the CLI will never risk overwriting your production data.

## Snowflake

Snowflake uses a combination of DAC and RBAC models for [access control](<https://docs.snowflake.com/en/user-guide/security-access-control-overview.html>). However, RudderStack chooses an RBAC-based access control mechanism as multiple users can launch the [Profile Builder CLI](<https://www.rudderstack.com/docs/archive/profiles/0.17/get-started/profile-builder/>).

Also, it is not ideal to tie the result of an individual user run with that user. Hence, it is recommended to create a generic role (for example, `PROFILES_ROLE`) with the following privileges:

  * Read access to all the inputs to the model (can be shared in case of multiple schemas/tables).
  * Write access to the schemas and common tables as the PB project creates material (output) tables.


If you want to access any material created from the project run, the role (`PROFILES_ROLE`) must also have read access to all of those schemas.

Below are some sample commands which grant the required privileges to the role (`PROFILES_ROLE`) in a Snowflake warehouse:
    
    
    -- Create role
    CREATE ROLE PROFILES_ROLE;
    SHOW ROLES; -- To validate
    
    
    
    -- Create user
    CREATE USER PROFILES_TEST_USER PASSWORD='<StrongPassword>' DEFAULT_ROLE='PROFILES_ROLE';
    SHOW USERS; -- To validate
    
    
    
    -- Grant role to user and database
    GRANT ROLE PROFILES_ROLE TO USER PROFILES_TEST_USER;
    GRANT USAGE ON DATABASE YOUR_RUDDERSTACK_DB TO ROLE PROFILES_ROLE;
    
    
    
    -- Create separate schema for Profiles and grant privileges to role
    CREATE SCHEMA YOUR_RUDDERSTACK_DB.RS_PROFILES;
    GRANT ALL PRIVILEGES ON SCHEMA YOUR_RUDDERSTACK_DB.RS_PROFILES TO ROLE PROFILES_ROLE;
    GRANT USAGE ON WAREHOUSE RUDDER_WAREHOUSE TO ROLE PROFILES_ROLE;
    GRANT USAGE ON SCHEMA YOUR_RUDDERSTACK_DB.EVENTSSCHEMA TO ROLE PROFILES_ROLE;
    

For accessing input sources, you can individually grant select on tables/views, or give blanket grant to all in a schema.
    
    
    -- Assuming we want read access to tables/views in schema EVENTSSCHEMA
    GRANT SELECT ON ALL TABLES IN SCHEMA YOUR_RUDDERSTACK_DB.RS_PROFILES TO PROFILES_ROLE;
    GRANT SELECT ON FUTURE TABLES IN SCHEMA YOUR_RUDDERSTACK_DB.RS_PROFILES TO PROFILES_ROLE;
    GRANT SELECT ON ALL VIEWS IN SCHEMA YOUR_RUDDERSTACK_DB.RS_PROFILES TO PROFILES_ROLE;
    GRANT SELECT ON FUTURE VIEWS IN SCHEMA YOUR_RUDDERSTACK_DB.RS_PROFILES TO PROFILES_ROLE;
    
    
    
    -- Assuming we want read access to tracks and identifies tables in schema EVENTSSCHEMA
    GRANT SELECT ON TABLE YOUR_RUDDERSTACK_DB.RS_PROFILES.TRACKS TO PROFILES_ROLE;
    GRANT SELECT ON TABLE YOUR_RUDDERSTACK_DB.RS_PROFILES.IDENTIFIES TO PROFILES_ROLE;
    

## Redshift

Suppose the inputs/edge sources are in a single schema `website_eventstream` and the name of the newly created Profiles user is `rudderstack_admin`. In this case, the requirements are as follows:

  * A separate schema `rs_profiles` (to store all the common and output tables).
  * The `rudderstack_admin` user should have all the privileges on the above schema and the associated tables.
  * The `rudderstack_admin` user should have `USAGE` privilege on schemas that have the edge sources and input tables (`website_eventstream`) and read (`SELECT`) privileges on specific tables as well. This privilege can extend to the migration schema and other schemas from where data from warehouses comes in.
  * The `rudderstack_admin` user should have privileges to use `plpythonu` to create some UDFs.


The sample commands are as follows:
    
    
    CREATE USER rudderstack_admin WITH PASSWORD '<strong_unique_password>';
    CREATE SCHEMA rs_profiles;
    GRANT ALL ON SCHEMA "rs_profiles" TO rudderstack_admin;
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA "rs_profiles" TO rudderstack_admin;
    GRANT USAGE ON SCHEMA "website_eventstream" TO rudderstack_admin;
    GRANT USAGE ON LANGUAGE plpythonu TO rudderstack_admin;
    
    
    
    GRANT SELECT ON ALL TABLES IN SCHEMA "website_eventstream" TO rudderstack_admin;
    

To give access to only specific input tables/views referred in your Profiles project, use the below command:
    
    
    GRANT SELECT ON TABLE "<YOUR_SCHEMA>"."<YOUR_TABLE>" TO rudderstack_admin;
    

### Supported inputs

RudderStack supports the following input types for Redshift warehouse/serverless:

  * Redshift cluster with DC2 type nodes with following types as inputs:
    * Redshift internal tables
    * External schema and tables only for inputs (not supported as output)
    * CSV files stored on S3 as inputs
  * Redshift cluster with RA3 type nodes with following types as inputs:
    * Redshift internal tables
    * External schema and tables only for inputs (not supported as output)
    * CSV files stored on S3 as inputs
    * Cross DB input tables
  * Redshift serverless with following types as inputs:
    * Redshift internal tables
    * External schema and tables (not supported as output)
    * CSV files stored on S3 as inputs
    * Cross DB input tables RudderStack also supports various authentication mechanisms to authenticate the user running the Profiles project. Refer [Redshift warehouse connection](<https://www.rudderstack.com/docs/archive/profiles/0.17/get-started/profile-builder/#2-create-warehouse-connection>) for more information.


> ![info](/docs/images/info.svg)
> 
> If you are using external tables with Redshift, RudderStack recommends using [AWS Query Editor](<https://aws.amazon.com/redshift/query-editor-v2/>) to query the input tables. Also, you should use the same [authentication method](<https://www.rudderstack.com/docs/archive/profiles/0.17/get-started/profile-builder/#2-create-warehouse-connection>) and service you plan to use with Profiles.

## Databricks

  1. Open the Databricks UI.
  2. [Create a new user](<https://docs.databricks.com/en/admin/users-groups/users.html>).
  3. Add user to the [Databricks workspace](<https://learn.microsoft.com/en-us/azure/databricks/admin/users-groups/users#assign-a-user-to-a-workspace-using-the-account-console>).
  4. Grant `USAGE` permission for the warehouse to the user.
  5. Grant `USE CATALOG` and `BROWSE` privileges to the user on the catalog. [Reference](<https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/#grant-permissions-on-objects-in-a-unity-catalog-metastore>).
  6. Grant `SELECT`, `MODIFY`, `CREATE`, and `USE SCHEMA` privileges to the user on rudder schema. [Reference](<https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/#grant-permissions-on-objects-in-a-unity-catalog-metastore>).
  7. Grant `SELECT` and `USE` privileges to access relevant schemas for the input tables. [Reference](<https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/#grant-permissions-on-objects-in-a-unity-catalog-metastore>).
  8. Grant `SELECT` on the input tables to the user. If you have a view, make sure to give the same privileges to the underlying tables. [Reference](<https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/manage-privileges/#grant-permissions-on-objects-in-a-unity-catalog-metastore>).


    
    
    GRANT USE CATALOG, BROWSE ON CATALOG profiles TO `rudderstack_admin`;
    GRANT SELECT, MODIFY, USE_SCHEMA, CREATE ON SCHEMA website_eventstream TO `rudderstack_admin`;
    GRANT SELECT ON TABLE website_eventstream.rs_profiles TO `rudderstack_admin`;
    GRANT SELECT ON VIEW website_eventstream.view_rs_profiles TO `rudderstack_admin`;
    
    
    
    GRANT SELECT ON ALL TABLES IN SCHEMA "website_eventstream" TO rudderstack_admin;
    

To give access to only specific input tables/views referred in your Profiles project, use the below command:
    
    
    GRANT SELECT ON TABLE public.input_table TO rudderstack_admin; 
    

## BigQuery

> ![info](/docs/images/info.svg)
> 
> For BigQuery, RudderStack recommends you to use a view instead of table for streaming data sets.

You must first assign the `BigQuery Job User` role to your service account. To do so:

  1. Open the [BigQuery UI](<https://console.cloud.google.com/>) (Google Cloud Console).
  2. Select **IAM & Admin** > **IAM** from the left sidebar.
  3. Click **GRANT ACCESS** to grant permissions to your service account.
  4. Enter your service account email in the **New principals** field.
  5. In the **Assign roles** section, select `BigQuery Job User` role from the role list.
  6. Click **Save**.


Alternatively, you can add the following **IAM Policy Binding** :
    
    
    {
      "bindings": [
        {
          "role": "roles/bigquery.jobUser",
          "members": [
            "serviceAccount:your-service-account@your-project.iam.gserviceaccount.com"
          ]
        }
      ]
    }
    

Further, assign the dataset or project level roles to your service account:

  1. Open the [BigQuery UI](<https://console.cloud.google.com/>) (Google Cloud Console).
  2. Select **BigQuery** from the sidebar.
  3. Select the dataset from your schema to which you want to grant access.
  4. In the **Dataset info** window, click **SHARING** > **Permissions**.
  5. Click **Add Principal**.
  6. Enter the service account email in the **New principals** field.
  7. In the **Assign roles** section, select the following roles from the role list:
     * **BigQuery Data Viewer** : Allows read access to the dataset.
     * **BigQuery Data Editor** : Allows read and write access to the dataset.


Alternatively, you can add the following **IAM Policy Binding** :
    
    
    {
      "bindings": [
        {
          "role": "roles/bigquery.dataViewer",
          "members": [
            "serviceAccount:your-service-account@your-project.iam.gserviceaccount.com"
          ],
          "condition": {
            "title": "Access to dataset1",
            "description": "Allow data viewing access to dataset1",
            "expression": "resource.name.startsWith('projects/your-project-id/datasets/dataset1')"
          }
        },
        {
          "role": "roles/bigquery.dataEditor",
          "members": [
            "serviceAccount:your-service-account@your-project.iam.gserviceaccount.com"
          ],
          "condition": {
            "title": "Access to dataset2",
            "description": "Allow data editing access to dataset2",
            "expression": "resource.name.startsWith('projects/your-project-id/datasets/dataset2')"
          }
        }
      ]
    }
    

If you have input relations in many datasets from a single project, you can assign the required privileges for the complete Google Cloud project. This allows your service account to access the relation from all the datasets of the project.

  1. Open the [BigQuery UI](<https://console.cloud.google.com/>) (Google Cloud Console).
  2. Select **IAM & Admin** > **IAM** from the left sidebar.
  3. Click **GRANT ACCESS** to grant permissions to your service account.
  4. Enter the service account email in the **New principals** field.
  5. In the **Assign roles** section, select the following roles from the role list:
     * **BigQuery Data Viewer** : Allows read access to the dataset.
     * **BigQuery Data Editor** : Allows read and write access to the dataset.


Alternatively, you can add the following **IAM Policy Binding** :
    
    
    {
      "bindings": [
        {
          "role": "roles/bigquery.dataViewer",
          "members": [
            "serviceAccount:your-service-account@your-project.iam.gserviceaccount.com"
          ]
        },
        {
          "role": "roles/bigquery.dataEditor",
          "members": [
            "serviceAccount:your-service-account@your-project.iam.gserviceaccount.com"
          ]
        }
      ]
    }
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.17/core-concepts/feature-development/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.17/cli-user-guide/>)