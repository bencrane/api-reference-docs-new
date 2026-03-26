# Trino Reverse ETL Source

Send data from Trino to your entire stack.

* * *

  * __8 minute read

  * 


[Trino](<https://trino.io/>) is a distributed SQL query engine for efficient, low-latency big data analytics.

RudderStack supports Trino as a data source from which you can ingest data and route it to your desired downstream destinations.

## Prerequisites: Trino server setup

Before you set up Trino as a source in RudderStack, make sure your Trino server is configured correctly by following these sections:

  * RudderStack supports only [password file authentication](<https://trino.io/docs/current/security/password-file.html>) mechanism for this source. Make sure to enable [password file authentication](<https://trino.io/docs/current/security/password-file.html#password-authenticator-configuration>) for your Trino instance and [create a password file](<https://trino.io/docs/current/security/password-file.html#creating-a-password-file>).
  * RudderStack uses the [file-based access control](<https://trino.io/docs/current/security/file-system-access-control.html>) mechanism for Trino. To use the access control plugin, see [Configuration](<https://trino.io/docs/current/security/file-system-access-control.html#configuration>) section.
  * This integration supports only the [Apache Hive connector](<https://trino.io/docs/current/connector/hive.html>) currently. To use this connector, make sure to add the following [configuration](<https://trino.io/docs/current/connector/hive.html#general-configuration>) in the catalog properties file using the Hive connector:


    
    
    hive.allow-drop-table=true
    hive.metastore.thrift.delete-files-on-drop=true
    

## Grant permissions

Before you set up Trino as a source, you must grant certain permissions on your Trino instance for RudderStack to access data from it.

Run the SQL queries listed in the following sections in the **exact order** to grant these permissions:

### Step 1: Assign read access to tables

This step gives RudderStack the necessary permissions to read the relevant table records in Trino.

> ![info](/docs/images/info.svg)
> 
> RudderStack uses the [file-based access control](<https://trino.io/docs/current/security/file-system-access-control.html>) mechanism for this integration.

To sync a table `sample_table` in `user_schema` for a user `test`, copy the below JSON in to your [access control config](<https://trino.io/docs/current/security/file-system-access-control.html#configuration>) JSON file:
    
    
    {
      "tables": [{
        "user": "test",  // Replace with your RudderStack user name
        "catalog": "catalog_name ", // Replace with the catalog you wish to sync
        "schema": "user_schema ", 
        "table": "sample_table ",
        "privileges": ["SELECT"]
      }]
    }
    

### Step 2: Create RudderStack schema and grant permissions
    
    
    CREATE SCHEMA "_rudderstack"
    

To add this schema to a particular location, run the following query:
    
    
    CREATE SCHEMA "_rudderstack" WITH (location = "s3://<your_location>/")
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to create the `_rudderstack` schema before syncing your data.

### Step 3: Grant ownership to `_rudderstack` schema

The following grants RudderStack the necessary permissions to perform relevant actions on the tables in the `_rudderstack` schema:
    
    
    {
      "catalogs": [{
        "user": "test",
        "catalog": "catalog_name ",
        "allow": "all"
      }],
      "schemas": [{
        "user": "test",
        "catalog": "catalog_name ",
        "schema": "_rudderstack ",
        "owner": true
      }],
      "tables": [{
        "user": "test",
        "catalog": "catalog_name ",
        "schema": "_rudderstack ",
        "privileges": ["SELECT",
          "INSERT",
          "DELETE",
          "UPDATE",
          "OWNERSHIP"
        ]
      }]
    }
    

## Set up Trino source in RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. On the **Connections** page, click **Add source**.
  3. Under **Sources** , click **Reverse ETL** and select **Trino**.


### Configure warehouse credentials

You can choose to proceed with your existing warehouse credentials if you have configured them in the RudderStack dashboard previously. Otherwise, click **Add new credentials** to add new credentials for your warehouse.

  * **Host** : Enter the host name or IP address of your Trino coordinator server.


> ![warning](/docs/images/warning.svg)
> 
> Make sure to enter only the host name and not the complete URL. Otherwise, you will encounter an error.
> 
> For example, if the URL is `https://trino-server.example.com`, host name should be `trino-server.example.com`.

  * **Catalog Name** : Specify the catalog to use when RudderStack executes queries in Trino.
  * **User** : Enter the user with relevant access to the above settings.
  * **Password** : Enter the password for the above user.
  * **Port** : Enter the port number of your Trino coordinator server. This is an optional setting.


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

#### **Which Trino connectors are supported for the Trino source integration?**

The Trino source supports only the [Apache Hive connector](<https://trino.io/docs/current/connector/hive.html>) currently.

To use this connector, make sure to add the following [configuration](<https://trino.io/docs/current/connector/hive.html#general-configuration>) in your object store:
    
    
    hive.allow-drop-table=true
    hive.metastore.thrift.delete-files-on-drop=true
    

#### **Which data types are supported for this integration?**

The Trino source supports all data types listed in the [Trino documentation](<https://trino.io/docs/current/language/types.html>) except the [Row data type](<https://trino.io/docs/current/language/types.html#row>).

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