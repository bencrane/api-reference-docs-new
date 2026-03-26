# PostgreSQL Reverse ETL Source

Send data from PostgreSQL to your entire stack.

* * *

  * __7 minute read

  * 


PostgreSQL is an enterprise-grade, open source database management system. Many companies use PostgreSQL as a low-cost data warehousing solution to deliver efficient analytics and user insights.

RudderStack supports PostgreSQL as a data source from which you can ingest data and route it to your desired downstream destinations.

## Grant permissions

Before you set up PostgreSQL as a source, you must grant certain permissions on your PostgreSQL warehouse for RudderStack to access data from it.

Run the queries listed in the following sections in the **exact order** to grant the required permissions:

### Step 1: Create user

Create a new user `RUDDER` with a password `<strong_unique_password>` in PostgreSQL:
    
    
    CREATE USER RUDDER WITH PASSWORD '<strong_unique_password>';
    

### Step 2: Create RudderStack schema and grant permissions

  1. Create a dedicated schema `_rudderstack`.


    
    
    CREATE SCHEMA "_rudderstack";
    

> ![warning](/docs/images/warning.svg)
> 
> The `_rudderstack` schema is used by RudderStack for storing the state of each data sync. **Do not change this name**.

  2. Grant full access to the schema `_rudderstack` for the user `RUDDER`.


    
    
    GRANT ALL ON SCHEMA "_rudderstack" TO RUDDER;
    

  3. Grant full access to all objects in the schema `_rudderstack` for the user `RUDDER`.


    
    
    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA "_rudderstack" TO RUDDER;
    

### Step 3: Grant permissions on schema and table

  1. To let the user `RUDDER` look up objects within the schema `<YOUR_SCHEMA>`, run the command below.


    
    
    GRANT USAGE ON SCHEMA "<YOUR_SCHEMA>" TO RUDDER;
    

  2. Grant access to the user `RUDDER` to read data from the required table/view:


    
    
    GRANT SELECT ON TABLE "<YOUR_SCHEMA>"."<YOUR_TABLE>" TO RUDDER;
    

Replace `<YOUR_SCHEMA>` and `<YOUR_TABLE>` with the exact names of your PostgreSQL schema and table, respectively.

#### **Optional commands**

> ![warning](/docs/images/warning.svg)
> 
> Run the following commands only if you’re okay with RudderStack being able to access the data in all current or future tables residing within your specified schema.

  * To allow the user `RUDDER` read the data from **all** the tables in the schema `<YOUR_SCHEMA>`:


    
    
    GRANT SELECT ON ALL TABLES IN SCHEMA "<YOUR_SCHEMA>" TO RUDDER;
    

  * To allow the user `RUDDER` to read data from all future tables created by the user `creator` in your schema:


    
    
    ALTER DEFAULT PRIVILEGES for user creator IN SCHEMA "<YOUR_SCHEMA>" GRANT SELECT ON TABLES TO RUDDER;
    

Replace `<YOUR_SCHEMA>` with the exact name of your PostgreSQL schema.

## Set up PostgreSQL source in RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. On the **Connections** page, click **Add source**.
  3. Under **Sources** , click **Reverse ETL** and select **PostgreSQL**.


### Configure warehouse credentials

You can choose to proceed with your existing warehouse credentials if you have configured them in the RudderStack dashboard previously. Otherwise, click **Add new credentials** to add new credentials for your warehouse.

  * **Host** : Enter the host name of your PostgreSQL instance.
  * **Database** : Enter the database name of your PostgreSQL instance from where RudderStack ingests the data.
  * **User** : Enter the user name of your PostgreSQL instance.
  * **Password** : Enter the password for the above user.
  * **SSL Mode** : Select the SSL mode as **disable** or **require** depending on how RudderStack should connect to your PostgreSQL instance.


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

## IPs to be allowlisted

> ![info](/docs/images/info.svg)
> 
> This section is applicable if you’re setting up your PostgreSQL source on a VPN or VPC and you want to enable network access to RudderStack.

To enable network access to RudderStack, allowlist the following RudderStack IPs depending on your region and [RudderStack plan](<https://www.rudderstack.com/pricing>):

Plan| Region  
---|---  
| **US**| **EU**  
Free, Starter, and Growth| 

  * 3.216.35.97
  * 18.214.35.254
  * 23.20.96.9
  * 34.198.90.241
  * 34.211.241.254
  * 52.38.160.231
  * 54.147.40.62

| 

  * 3.123.104.182
  * 3.125.132.33
  * 18.198.90.215
  * 18.196.167.201

  
Enterprise| 

  * 3.216.35.97
  * 34.198.90.241
  * 44.236.60.231
  * 54.147.40.62
  * 100.20.239.77

| 

  * 3.66.99.198
  * 3.64.201.167
  * 3.123.104.182
  * 3.125.132.33

  
  
> ![info](/docs/images/info.svg)
> 
> All the outbound traffic is routed through these RudderStack IPs.

## FAQ

#### **What are the SSL mode options when setting up the PostgreSQL source in RudderStack?**

When setting up a PostgreSQL source, RudderStack provides the following two SSL options:

  * **disable** : SSL mode is disabled when you select this option. Use it in cases where security is not an issue and you don’t want any encryption overhead.
  * **require** : When you select this option, your data is encrypted and sent to RudderStack. Use it in cases where security is important and you can deal with the resulting encryption overhead.


#### **Is SSH tunneling supported for PostgreSQL when using it as a Reverse ETL source?**

RudderStack does not support SSH tunneling for PostgreSQL as a Reverse ETL source.

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