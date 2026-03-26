# ClickHouse Destination

Sync data from RudderStack to ClickHouse.

* * *

  * __4 minute read

  * 


[ClickHouse](<https://clickhouse.tech/>) is an open-source, column-oriented database management system mainly used for online analytical processing (OLAP). It is fast, and allows for real-time analysis of your data.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/clickhouse>).

> ![info](/docs/images/info.svg)
> 
> See the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) guide for more information on how the events are mapped to the tables in ClickHouse.

## Set user permissions in ClickHouse

Before setting up ClickHouse as a destination, create a new user in ClickHouse. Make sure to replace `<username>` and `<password>` in the below command with the appropriate values:
    
    
    CREATE USER <username> IDENTIFIED BY '<password>';
    

Then, grant the above user the necessary permissions to create new tables in the database. Make sure to replace the placeholders with the actual values:
    
    
    GRANT SELECT ON system.databases TO <username>;
    GRANT SELECT ON system.columns TO <username>;
    GRANT SELECT, INSERT, ALTER TABLE, CREATE DATABASE, CREATE TABLE, DROP TABLE ON <database>.* TO <username>;
    

You also to need to set `date_time_input_format` to `best_effort` for ClickHouse to parse all [ISO 8601](<https://en.wikipedia.org/wiki/ISO_8601>) date and time formats:
    
    
    set date_time_input_format = 'best_effort';
    

Note that:

  * RudderStack uses the `UInt8` data type to set Boolean values and map `UInt8`to Boolean internally. RudderStack automatically treats `UInt8` as Boolean when a schema is fetched from ClickHouse.
  * If you are creating tables in the same database where RudderStack loads, it is highly recommended to not use `UInt8`as a data type except for Boolean values (0,1).


## Configure ClickHouse destination in RudderStack

  1. In your [RudderStack dashboard](<https://app.rudderstack.com>), set up the data source. Then, select **ClickHouse** from the list of destinations.
  2. Assign a name to your destination and then click **Next**.


### Connection Settings

  * **Host** : The host name of your ClickHouse database.
  * **Port** : The TCP port of your ClickHouse host. If you want the connection to be secure, use the secure TCP port `9440`. Refer to the [ClickHouse guide](<https://clickhouse.tech/docs/en/operations/server-configuration-parameters/settings/#server_configuration_parameters-tcp_port>) for more information.
  * **Database** : The database name in your ClickHouse instance where the data gets loaded.
  * **Cluster** : The name of your ClickHouse cluster. **If you are running a single host ClickHouse cluster, leave this field blank.**
  * **User** : The name of the user with the required read/write access to the above database.
  * **Password** : The password for the above user.
  * **Secure** : Enable this setting to establish a secure connection.
  * **Sync Frequency** : Specify how often RudderStack should sync the data to your ClickHouse database.
  * **Sync Starting At** : This optional setting lets you specify the particular time of the day (in UTC) when you want RudderStack to sync the data to the warehouse.
  * **Exclude Window** : This optional setting lets you set a time window when RudderStack will **not sync** the data to your database.


### Object storage settings

RudderStack lets you configure the following object storage configuration settings while setting up your ClickHouse destination:

  * **Use RudderStack-managed object storage** : Enable this setting to use RudderStack-managed buckets for object storage.


> ![warning](/docs/images/warning.svg)
> 
> This option is applicable only for RudderStack-hosted data planes. For [self-hosted data planes](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/data-plane-setup/>), you will have to specify your own object storage configuration settings.

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

#### How does RudderStack de-duplicate the events that are loaded into the warehouse?

RudderStack creates tables with the engine `ReplacingMergeTree order by (received_at, id)` and column `dataType` as `Nullable(dataType)`.[`ReplacingMergeTree`](<https://clickhouse.tech/docs/en/engines/table-engines/mergetree-family/replacingmergetree/>) replaces the latest event which has the same `received_at, id` while merging. Note that `Nullable` is not applicable for `sortKeys`.

#### How does RudderStack merge the user properties in the user’s table?

For the user’s table, RudderStack creates a table with an engine `AggregatingMergeTree` ordered by `id` and a column `dataType` as `SimpleAggregateFunction(anyLast, Nullable(dataType))`. Merging the columns with the same`id`picks the last value which is not null. Note that `Nullable` is not applicable for `sortKeys`.

#### How does RudderStack handle cases when loading data into ClickHouse?

RudderStack converts the event keys into the lower case before exporting the data into ClickHouse. This is so that it does not create two tables in case the event name has two different cases.

> ![info](/docs/images/info.svg)
> 
> For a more comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.