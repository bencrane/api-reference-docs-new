# MySQL Reverse ETL Source

Send data from MySQL to your entire stack.

* * *

  * __6 minute read

  * 


[MySQL](<https://www.mysql.com/>) is a popular open source relational DBMS.

RudderStack supports MySQL as a data source from which you can ingest data and route it to your desired downstream destinations.

> ![info](/docs/images/info.svg)
> 
> This source is compatible with MySQL v8.0.0 and above.

## Grant permissions

Before you set up MySQL as a source, you must grant certain permissions on your MySQL database for RudderStack to access data from it.

Run the SQL queries listed in the following sections in the **exact order** to grant these permissions:

### Step 1: Create user

Create a new user `RUDDER` with a password `<password>` in MySQL:
    
    
    CREATE USER RUDDER IDENTIFIED BY '<password>';
    

> ![warning](/docs/images/warning.svg)
> 
> Set a strong and unique password for creating the user in MySQL.

### Step 2: Create RudderStack schema and grant permissions

  1. Create a dedicated schema `_rudderstack`.


    
    
    CREATE SCHEMA _rudderstack;
    

> ![warning](/docs/images/warning.svg)
> 
> The `_rudderstack` schema is used by RudderStack for storing the state of each data sync. **Do not change this name**.

  2. Grant full access to the schema `_rudderstack` for the user `RUDDER`.


    
    
    GRANT ALL PRIVILEGES ON _rudderstack.* TO RUDDER;
    

### Step 3: Grant permissions on schema and table

  1. Grant access to the user `RUDDER` to read data from tables in `<YOUR_SCHEMA>`:


    
    
    GRANT SELECT ON  <YOUR_SCHEMA>.* TO RUDDER;
    

## Set up MySQL source in RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. On the **Connections** page, click **Add source**.
  3. Under **Sources** , click **Reverse ETL** and select **MySQL**.


### Configure warehouse credentials

You can choose to proceed with your existing warehouse credentials if you have configured them in the RudderStack dashboard previously. Otherwise, click **Add new credentials** to add new credentials for your warehouse.

  * **Host** : Enter the host name of your MySQL instance.
  * **Port** : Enter the port number associated with the MySQL database instance.
  * **Database** : Enter the database name in your MySQL instance from where RudderStack ingests the data.
  * **User** : Enter the user name of your MySQL instance.
  * **Password** : Enter the password for the above user.
  * **SSL Mode** : Select the SSL mode from **false** or **skip-verify** depending on how RudderStack should connect to your MySQL instance.


Click the **Verify** button on the top right. RudderStack will then verify and validate your credentials. Once verified, click **Continue** to proceed.

### Specify name and source type

  * **Source name** : Assign a name to uniquely identify the source in the RudderStack dashboard.
  * **Select your source type** : RudderStack lets you set up a Reverse ETL source from a warehouse **Table** or **Model**.

Source type| Description  
---|---  
Table| Use an existing warehouse table as a data source.  
  
See Use warehouse table as source for detailed setup.  
Model| Use custom SQL queries to fetch specific warehouse data and send them to your destinations.  
  
See Use model as source for detailed setup.  
  
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