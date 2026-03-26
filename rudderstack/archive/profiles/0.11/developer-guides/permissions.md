# Warehouse Permissions

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Warehouse Permissions

Grant RudderStack the required permissions on your data warehouse.

* * *

  * __5 minute read

  * 


RudderStack supports **Snowflake** , **Redshift** , **Databricks** , and **BigQuery** for creating unified user profiles.

To read and write data to the warehouse, RudderStack requires specific warehouse permissions as explained in the following sections.

> ![warning](/docs/images/warning.svg)
> 
> Keeping separate schemas for projects running via CLI and web is recommended. This way projects run from the CLI will never risk overwriting your production data.

## Snowflake

Snowflake uses a combination of DAC and RBAC models for [access control](<https://docs.snowflake.com/en/user-guide/security-access-control-overview.html>). However, RudderStack chooses an RBAC-based access control mechanism as multiple users can launch the [Profile Builder CLI](<https://www.rudderstack.com/docs/archive/profiles/0.11/get-started/profile-builder/>).

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

When working with Redshift, the required privileges are different compared to Snowflake.

Suppose the inputs/edge sources are in a single schema `website_eventstream` and the name of the newly created PB user is `rudderstack_admin`. In this case, the requirements are as follows:

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
    

## Databricks

The steps are as follows:

  1. Open the Databricks UI.
  2. Create a new user.
  3. Reuse an existing catalog or create a new one by clicking **Create Catalog**.
  4. Grant `USE SCHEMA` privilege on the catalog.
  5. Create a separate schema to write objects created by RudderStack Profiles.
  6. Grant all privileges on this schema.
  7. Grant privileges to access relevant schemas for the input tables. For example, if an input schema is in a schema named `website_eventstream`, then you can run the following commands to assign a blanket grant to all schemas or only specific tables/views referred in your Profiles project:


    
    
    CREATE USER rudderstack_admin WITH PASSWORD <strong_unique_password>;
    GRANT USE SCHEMA ON CATALOG <catalog name> TO rudderstack_admin;
    CREATE SCHEMA RS_PROFILES;
    GRANT ALL PRIVILEGES ON SCHEMA RS_PROFILES TO rudderstack_admin;
    GRANT SELECT ON SCHEMA website_eventstream TO rudderstack_admin;
    
    
    
    GRANT SELECT ON ALL TABLES IN SCHEMA "website_eventstream" TO rudderstack_admin;
    

To give access to only specific input tables/views referred in your Profiles project, use the below command:
    
    
    GRANT SELECT ON TABLE public.input_table TO rudderstack_admin; 
    

## BigQuery

> ![info](/docs/images/info.svg)
> 
> For BigQuery, RudderStack recommends you to use a view instead of table for streaming data sets.

  1. Open the [BigQuery UI](<https://console.cloud.google.com/>) (Google Cloud Console) and select your project (for example, `rudderstack`).
  2. Click **Query Editor** from the left sidebar.
  3. Execute the following command to create a schema for a dataset (for example, `prod_dataset`):


    
    
    CREATE SCHEMA rudderstack.prod_dataset.rs_profiles;
    

  4. Grant read access to all your input source tables:


    
    
    GRANT SELECT ON ALL TABLES IN SCHEMA rudderstack.prod_dataset.rs_profiles;
    

  5. Grant permission to your user (for example, `rudder_user`) for creating tables/views in the schema:


    
    
    GRANT CREATE ON SCHEMA rudderstack.prod_dataset.rs_profiles TO rudder_user;
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/developer-guides/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/developer-guides/site-configuration/>)