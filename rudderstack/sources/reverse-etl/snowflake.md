# Snowflake Reverse ETL Source

Send data from Snowflake to your entire stack.

* * *

  * __10 minute read

  * 


[Snowflake](<https://www.snowflake.com/>) is a cloud-based data warehouse provided as Software-as-a-Service (SaaS). It offers all features of a modern data warehouse, including scalability, ease of use, secure data access, and much more.

RudderStack supports Snowflake as a data source from which you can ingest data and route it to your desired downstream destinations.

## Grant permissions

Before you set up Snowflake as a source, you must grant certain permissions on your Snowflake warehouse for RudderStack to access data from it.

Run the queries listed in the following sections in the **exact order** to grant the required permissions:

> ![warning](/docs/images/warning.svg)
> 
> You must have the **ACCOUNTADMIN** role to grant these permissions.

![Snowflake account admin role](/docs/images/warehouse-actions-sources/snowflake-accountadmin.webp)

### Step 1: Create a new role and user in Snowflake

  1. In your Snowflake console, run the following command to create a role `RUDDER_ROLE` in Snowflake. After creating the role, you can [grant object privileges](<https://docs.snowflake.com/en/sql-reference/sql/grant-privilege.html>) to it.


    
    
    CREATE ROLE RUDDER_ROLE;
    

  2. Verify if the role `RUDDER_ROLE` is successfully created.


    
    
    SHOW ROLES;
    

  3. Create a new user `RUDDER` with a password `<strong_unique_password>`.


    
    
    CREATE USER RUDDER PASSWORD = '<strong_unique_password>' DEFAULT_ROLE = 'RUDDER_ROLE';
    

> ![info](/docs/images/info.svg)
> 
> You can assign some other role to this user in the RudderStack dashboard settings later. See Configuring the connection credentials section for more information.

  4. Verify if the user `RUDDER` is successfully created.


    
    
    SHOW USERS;
    

### Step 2: Create RudderStack schema and grant permissions to the role

  1. Create a dedicated schema `_RUDDERSTACK` in your database `<YOUR_DATABASE>`.


    
    
    CREATE SCHEMA "<YOUR_DATABASE>"."_RUDDERSTACK";
    

> ![warning](/docs/images/warning.svg)
> 
> The `_RUDDERSTACK` schema is used by RudderStack for storing the state of each data sync. **Do not change this name**.

  2. Grant full access to the schema `_RUDDERSTACK` for the previously created role `RUDDER_ROLE`.


    
    
    GRANT ALL PRIVILEGES ON SCHEMA "<YOUR_DATABASE>"."_RUDDERSTACK" TO ROLE RUDDER_ROLE;
    

Replace `<YOUR_DATABASE>` with the exact name of your Snowflake database

### Step 3: Grant permissions on warehouse, database, schema, and table

  1. Enable the user `RUDDER` to perform all operations allowed for the role `RUDDER_ROLE`(via the privileges granted to it).


    
    
    GRANT ROLE RUDDER_ROLE TO USER RUDDER;
    

  2. Run the following commands to allow the role `RUDDER_ROLE` to look up the objects within your warehouse, database, schema, and the specific table or view:


    
    
    GRANT USAGE ON WAREHOUSE "<YOUR_WAREHOUSE>" TO ROLE RUDDER_ROLE;
    GRANT USAGE ON DATABASE "<YOUR_DATABASE>" TO ROLE RUDDER_ROLE;
    GRANT USAGE ON SCHEMA "<YOUR_DATABASE>"."<YOUR_SCHEMA>" TO ROLE RUDDER_ROLE;
    GRANT SELECT ON TABLE "<YOUR_DATABASE>"."<YOUR_SCHEMA>"."<YOUR_TABLE>" TO ROLE  RUDDER_ROLE;
    GRANT SELECT ON VIEW "<YOUR_DATABASE>"."<YOUR_SCHEMA>"."<YOUR_VIEW>" TO ROLE  RUDDER_ROLE;
    

Replace `<YOUR_WAREHOUSE>`, `<YOUR_DATABASE>`, `<YOUR_SCHEMA>`, `<YOUR_TABLE>`, and `<YOUR_VIEW>` with the exact names of your Snowflake warehouse, database, schema, table, and view respectively.

#### **Optional commands**

> ![warning](/docs/images/warning.svg)
> 
> Run the following commands **only** if you’re okay with RudderStack being able to access all current or future tables/views within your specified schema.

  * To allow the role `RUDDER_ROLE` to read data from **all** the tables in the schema `<YOUR_SCHEMA>`.


    
    
    GRANT SELECT ON ALL TABLES IN SCHEMA "<YOUR_DATABASE>"."<YOUR_SCHEMA>" TO ROLE RUDDER_ROLE;
    

  * To allow the role `<RUDDER_ROLE>` to read data from all **future tables** in the schema `<YOUR_SCHEMA>`.


    
    
    GRANT SELECT ON FUTURE TABLES IN SCHEMA "<YOUR_DATABASE>"."<YOUR_SCHEMA>" TO ROLE RUDDER_ROLE;
    

  * To allow the role `RUDDER_ROLE` to read data from **all** the views in the schema `<YOUR_SCHEMA>`.


    
    
    GRANT SELECT ON ALL VIEWS IN SCHEMA "<YOUR_DATABASE>"."<YOUR_SCHEMA>" TO ROLE RUDDER_ROLE;
    

  * To allow the role `<RUDDER_ROLE>` to read data from all **future views** in the schema `<YOUR_SCHEMA>`.


    
    
    GRANT SELECT ON FUTURE VIEWS IN SCHEMA "<YOUR_DATABASE>"."<YOUR_SCHEMA>" TO ROLE RUDDER_ROLE;
    

Replace `<YOUR_DATABASE>` and `<YOUR_SCHEMA>` with the exact Snowflake database and the schema names.

## Set up Snowflake source in RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. On the **Connections** page, click **Add source**.
  3. Under **Sources** , click **Reverse ETL** and select **Snowflake**.


### Configure warehouse credentials

You can choose to proceed with your existing warehouse credentials if you have configured them in the RudderStack dashboard previously. Otherwise, click **Add new credentials** to add new credentials for your warehouse.

  * **Authentication Type** : Select the user authentication mechanism from the dropdown. RudderStack supports the following methods:
    * **Username Password Authentication**
    * **Key Pair Authentication**


> ![info](/docs/images/info.svg)
> 
> For enhanced security, RudderStack recommends using the key pair authentication over the basic authentication mechanism (username and password).
> 
>   * See the [Migration Guide](<https://www.rudderstack.com/docs/user-guides/migration-guides/snowflake-key-pair-migration/>) to migrate from the username/password authentication to the key pair authentication.
> 
>   * Refer to the following sections in the [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/key-pair-auth#configuring-key-pair-authentication>) to generate and use the key pair:
> 
>     * [Generate private key](<https://docs.snowflake.com/en/user-guide/key-pair-auth#generate-the-private-key>)
>     * [Generate public key](<https://docs.snowflake.com/en/user-guide/key-pair-auth#generate-a-public-key>)
>     * [Assign public key to Snowflake user](<https://docs.snowflake.com/en/user-guide/key-pair-auth#assign-the-public-key-to-a-snowflake-user>)
> 


  * **Account** : Your warehouse account ID is part of your Snowflake URL. The following examples illustrate the slight differences in the account ID for various cloud providers:

Account ID sample| Snowflake URL| Snowflake cloud provider  
---|---|---  
**qya56091.us-east-1**| `https://`**`qya56091.us-east-1`**`.snowflakecomputing.com`| AWS  
**rx18795.east-us-2.azure**| `https://`**`rx18795.east-us-2.azure`**`.snowflakecomputing.com`| Microsoft Azure  
**ah76025.us-central1.gcp**| `https://`**`ah76025.us-central1.gcp`**`.snowflakecomputing.com`| Google Cloud Platform  
  * **Database** : Enter the name of the database in which your data resides.

  * **Warehouse** : Specify the name of your data warehouse.

  * **User** : Enter the name of the user that has the required read/write access to the above database.

  * **Role** : Enter a role you want to assign to the above user. For syncing the data, you can use this role apart from the default role (`RUDDER_ROLE`) assigned in the Create a new role and user section.


If you have set **Authentication Type** to **Username Password Authentication** :

  * **Password** : Enter the password for the user specified in the **User** field.


If you have set **Authentication Type** to **Key Pair Authentication** :

  * **Private Key** : Specify the private key generated above. Make sure to include the delimiters.

  * **Private Key Passphrase** : Specify the password you set while encrypting the private key. Note that:

    * RudderStack requires a non-empty passphrase for encrypted private keys.
    * You can leave this field blank if your private key is not encrypted.


> ![danger](/docs/images/danger.svg)
> 
> The user authentication will fail if your private key is encrypted and you do not specify the passphrase.

Click the **Verify** button on the top right. RudderStack will then verify and validate your credentials. Once verified, click **Continue** to proceed.

### Specify name and source type

Specify the source name and type in this step.

  * **Source name** : Assign a name to uniquely identify the source in the RudderStack dashboard.
  * **Select your source type** : RudderStack lets you set up a Reverse ETL source from a warehouse **Table** , **Model** , or **Audience**.

Source type| Description  
---|---  
Table| Use an existing warehouse table as a data source.  
  
See Use warehouse table as source for detailed setup.  
Model| Use custom SQL queries to fetch specific warehouse data and send them to your destinations.  
  
See Use model as source for detailed setup.  
Audience| Filter data in your warehouse tables to create target customer lists and send them to downstream destinations.  
  
See Use audience as source for detailed setup.  
  
#### **Use warehouse table as source**

Under **Select your source type** , choose **Table** and specify the below fields:

  * **Schema** : Select the warehouse schema from the dropdown.
  * **Table** : Choose the required table from which RudderStack syncs the data.
  * **Primary key** : Select the column from the above table that uniquely identifies your records in the warehouse.


> ![info](/docs/images/info.svg)
> 
> RudderStack uses the primary key column for diffing in case of incremental syncs. You can generate it by:
> 
>   * Generating your table with a primary key, OR
>   * Creating a table view
> 

> 
> You can use a composite key in cases where one column cannot be considered as a primary key. For example, you can a declare a composite key of `user_id` and `timestamp` by creating a view on your warehouse table.

[![Use table as source](/docs/images/retl-sources/wh-table-source.webp)](</docs/images/retl-sources/wh-table-source.webp>)

Finally, review and complete your source setup.

#### **Use model as source**

Under **Select your source type** , choose **Model** and click **Continue**.

To configure a model as source:

  1. Enter an optional description and specify the custom SQL query in **Query** section.
  2. Click **Run Query** to fetch the data preview.
  3. Select the **Primary key** to use a column that uniquely identifies your warehouse records.


> ![warning](/docs/images/warning.svg)
> 
> You can set a primary key only after you run the SQL query successfully using the **Run Query** option.

> ![info](/docs/images/info.svg)
> 
> RudderStack uses the primary key column for diffing in case of incremental syncs. You can generate it by:
> 
>   * Generating your table with a primary key, OR
>   * Creating a table view
> 

> 
> You can use a composite key in cases where one column cannot be considered as a primary key. For example, you can a declare a composite key of `user_id` and `timestamp` in SQL query of the model.

[![Model configuration](/docs/images/data-pipelines/model-source-configuration.webp)](</docs/images/data-pipelines/model-source-configuration.webp>)

Finally, review and complete your source setup.

#### **Use audience as source**

Under **Select your source type** , choose **Audience** and follow these steps:

  1. Configure your audience source by specifying the below fields:

     * **Schema** : Select the warehouse schema from the dropdown.
     * **Table** : Choose the required table from which RudderStack syncs the data.
     * **Primary key** : Select the column from the above table that uniquely identify your records in the warehouse.

[![Use audience as source](/docs/images/retl-sources/audience-source.webp)](</docs/images/retl-sources/audience-source.webp>)

> ![info](/docs/images/info.svg)
> 
> RudderStack uses the primary key column for diffing in case of incremental syncs. You can generate it by:
> 
>   * Generating your table with a primary key, OR
>   * Creating a table view
> 

> 
> You can use a composite key in cases where one column cannot be considered as a primary key. For example, you can a declare a composite key of `user_id` and `timestamp` by creating a view on your warehouse table.

  2. Set your [audience conditions](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/audiences/#set-your-conditions>).
  3. Click **Preview** to see the resulting data. Then, click **Continue** to proceed.

[![Audience configuration](/docs/images/retl-sources/audience-source-configuration.webp)](</docs/images/retl-sources/audience-source-configuration.webp>)

Finally, review and complete your source setup.

### Review and complete setup

To make any changes to the warehouse credentials or source configuration, click the edit icon present next to those sections.

[![Edit source configuration](/docs/images/retl-sources/edit-source-configuration.webp)](</docs/images/retl-sources/edit-source-configuration.webp>)

Review your configuration and click **Create source** to complete the setup.

## Connect destination

To start using the newly-created source, you can connect it to:

  * A new [destination](<https://www.rudderstack.com/docs/destinations/overview/>), or
  * An existing destination that is **not already connected** to any other source.


To connect to a destination later, click **Done** on the top right:

[![Next steps](/docs/images/retl-sources/created-source.webp)](</docs/images/retl-sources/created-source.webp>)

You will then be redirected to the **Overview** page of the source where you will see the option of connecting it to a new or existing destination.

[![Add destination](/docs/images/retl-sources/add-destination.webp)](</docs/images/retl-sources/add-destination.webp>)

See [Set up Reverse ETL Connection](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/>) section for more information.

## Update source configuration and settings

Go to the **Configuration** tab of your Reverse ETL source to update the configuration depending on your source type:

> ![warning](/docs/images/warning.svg)
> 
> You cannot change the source type on this page.

[![Update source configuration](/docs/images/retl-sources/update-source-configuration.webp)](</docs/images/retl-sources/update-source-configuration.webp>)

The below table lists the options you can update:

Source type| Configurable options  
---|---  
Table| Schema, Table, Primary key  
Model| 

  * Model settings
  * Primary key

**Note** : You can set the primary key only after the SQL query runs successfully.  
Audience| 

  * Schema, Table, Primary key
  * Audience conditions

  
  
> ![info](/docs/images/info.svg)
> 
> After updating the configuration, the next sync will be a full sync.

Go to the **Settings** tab to:

  * Get your source ID.
  * Change your warehouse credentials.
  * [Set up custom alerts](<https://www.rudderstack.com/docs/data-governance/alerts/>) for your Reverse ETL source.
  * Delete the source permanently.


> ![warning](/docs/images/warning.svg)
> 
> You cannot delete a source that is connected to any destination.

[![Edit source settings](/docs/images/retl-sources/source-settings.webp)](</docs/images/retl-sources/source-settings.webp>)

## FAQ

#### **What do the three validations under Verifying Credentials imply?**

When setting up a Reverse ETL source, you will see the following three validations under the **Verifying Credentials** option once you proceed after entering the warehouse credentials:

[![Validating credentials](/docs/images/retl-sources/retl-credentials-validate.webp)](</docs/images/retl-sources/retl-credentials-validate.webp>)

These options are explained below:

  * **Verifying Connection** : This option indicates that RudderStack is trying to connect to the warehouse with the provided warehouse credentials.


> ![warning](/docs/images/warning.svg)
> 
> If this option gives an error, it means that one or more fields specified in the warehouse credentials are incorrect. Verify your credentials in this case.

  * **Able to List Schema** : This option checks if RudderStack is able to fetch all schema details by using the provided credentials.
  * **Able to Access RudderStack Schema** : This option implies that RudderStack is able to access the `_rudderstack` schema you have created by running all commands in the User Permissions section.


> ![warning](/docs/images/warning.svg)
> 
> If this option gives an error, verify if you have successfully created the `_rudderstack` schema and given RudderStack the required permissions to access it.

#### **What is the difference between the Table, Model, and Audience options when creating a Reverse ETL source?**

When creating a new Reverse ETL source, you are presented with the following options from which RudderStack syncs the data:

Source type| Description  
---|---  
Table| RudderStack uses an existing warehouse table as a data source.  
  
See Use warehouse table as source for detailed setup.  
Model| RudderStack uses custom SQL queries to fetch specific warehouse data and sends them to your destinations.  
  
See Use model as source for detailed setup.  
Audience| RudderStack filters data in your warehouse tables to create target customer lists and sends them to downstream destinations.  
  
See Use audience as source for detailed setup.