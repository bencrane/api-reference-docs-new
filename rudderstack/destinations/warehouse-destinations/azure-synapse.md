# Azure Synapse

Sync data from RudderStack to Azure Synapse.

* * *

  * __5 minute read

  * 


[Azure Synapse Analytics](<https://azure.microsoft.com/en-in/services/synapse-analytics/>) is an analytics service that combines data warehousing capabilities with Big Data analytics. If offers a unified data engineering platform to ingest, explore, manage, and serve your data for analytics and Business Intelligence.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack only supports the dedicated SQL pool in Azure Synapse Analytics and **not** the [serverless SQL pool](<https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/on-demand-workspace-overview>). See [Microsoft documentation](<https://learn.microsoft.com/en-us/azure/synapse-analytics/sql/overview-features>) to know more about the differences.

> ![info](/docs/images/info.svg)
> 
> Refer to the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) guide for more information on how the events are mapped to the tables in Azure Synapse.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/azure_synapse>).

## Prerequisites

Before setting up Azure Synapse as a destination in RudderStack, make sure you have an Azure subscription and created the [Azure Synapse Workspace](<https://docs.microsoft.com/en-in/azure/synapse-analytics/quickstart-create-workspace>).

Additionally, you need to create a dedicated SQL pool in Azure Synapse. You can create it by following the [Azure Synapse documentation](<https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/create-data-warehouse-portal>).

To create a user-defined schema on your dedicated SQL pool, run the following SQL command on your pool:
    
    
    CREATE SCHEMA <schema_name>;
    

## Configuring Azure Synapse destination in RudderStack

To send event data to Azure Synapse, you first need to add it as a destination in RudderStack and connect it to your data source. Once the destination is enabled, events will automatically start flowing to Azure Synapse via RudderStack.

To configure Azure Synapse as a destination in RudderStack, follow these steps:

  1. In your [RudderStack dashboard](<https://app.rudderstack.com>), set up the data source. Then, select **Azure Synapse** from the list of destinations.
  2. Assign a name to your destination and then click **Next**.


### Connection settings

  * **Host** : The host name of your Azure Synapse service.
  * **Database** : The database name in your Azure Synapse instance where the data will be sent.
  * **User** : The name of the user with the required read/write access to the above database.
  * **Password** : The password for the above user.
  * **Port** : The port number associated with the Azure Synapse database instance.
  * **Namespace** : Enter the name of the schema created in the Prerequisites section, where RudderStack creates all tables.


> ![warning](/docs/images/warning.svg)
> 
> You cannot change the namespace later.

  * **SSL Mode** : Choose the SSL mode through which RudderStack will connect to your Azure Synapse instance. RudderStack provides three options - **disable** , **true** , and **false**. See the FAQ section below for more information on these SSL modes.
  * **Sync Frequency** : Specify how often RudderStack should sync the data to your PostgreSQL database.
  * **Sync Starting At** : This optional setting lets you specify the particular time of the day (in UTC) when you want RudderStack to sync the data to the warehouse.
  * **Exclude Window** : This optional setting lets you set a time window when RudderStack will **not sync** the data to your database.


### Configuring the object storage

RudderStack lets you configure the following object storage configuration settings while setting up your Azure Synapse destination:

  * **Use RudderStack-managed object storage** : Enable this setting to use RudderStack-managed buckets for object storage.


> ![warning](/docs/images/warning.svg)
> 
> This option is applicable only for RudderStack-hosted data planes. For self-hosted data planes, you will have to specify your own object storage configuration settings.

  * **Choose your storage provider** : If **Use RudderStack-managed object storage** is **disabled** in the dashboard, select the cloud provider for your object storage and enter the relevant settings:

    * [Amazon S3 bucket storage settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/#connection-settings>)
    * [Azure Blob Storage settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/microsoft-azure-blob-storage/#setting-up-azure-blob-storage>)
    * [Google Cloud Storage bucket settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-cloud-storage/#setting-up-google-cloud-storage>)
    * [MinIO bucket storage settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/minio/#setting-up-minio>)


See [How RudderStack stores data in an object storage platform](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/#how-does-rudderstack-store-data-in-an-object-storage-platform>) for more information.

  * **Clean up object storage files after successful sync** : Turn on this toggle to delete the object storage files after the sync has completed successfully.


### Advanced settings

  * **Skip User Table** : This setting is toggled on by default and sends events exclusively to the [`identifies`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table while skipping the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table. This eliminates the need for a merge operation on the `users` table. If toggled off, RudderStack sends the events to both the `identifies` and `users` tables.
  * **Skip Tracks Table** : Toggle on this setting to skip sending events to the [`tracks`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table.


## IPs to be allowlisted

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

#### How are reserved words handled by RudderStack?

There are some limitations when it comes to using [reserved words](<https://docs.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver15>) in a schema, table, or column names. If such words are used as event names, traits or properties, they will be prefixed with a `_` when RudderStack creates tables or columns for them in your schema.

Also, note that integers are not allowed at the start of the schema or table name. Hence, RudderStack prefixes such schema, column, or table names with a `_`.

For instance, `'25dollarpurchase'` will be changed by RudderStack to `'_25dollarpurchase`'.

#### How does RudderStack handle cases when loading the data into Azure Synapse?

RudderStack converts the event keys into lower case before exporting the data into Azure Synapse, so that it does not create two tables if the event name has two different cases.

#### What are the SSL mode options provided by RudderStack?

While setting up the Azure Synapse destination, RudderStack provides the following three SSL options:

  * **disable** : The data sent from RudderStack to your database is not encrypted.
  * **false** : The data sent from RudderStack to your database is not encrypted beyond the login packet.
  * **true** : The data sent from RudderStack to your database is encrypted.


> ![info](/docs/images/info.svg)
> 
> For a more comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.