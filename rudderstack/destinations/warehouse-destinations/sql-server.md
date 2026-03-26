# Microsoft SQL Server

Sync data from RudderStack to Microsoft SQL Server.

* * *

  * __5 minute read

  * 


[Microsoft SQL Server](<https://www.microsoft.com/en-in/sql-server/sql-server-downloads>) is a popular relational database management system (RDBMS). ideal for a variety of data workloads - from small-scale, single-machine data applications to large data applications with thousands of concurrent users.

> ![info](/docs/images/info.svg)
> 
> Refer to the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) guide for more information on how the events are mapped to the tables in SQL Server.

> ![success](/docs/images/tick.svg)
> 
> Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/mssql>).

## Setting user permissions in SQL Server

After setting up your SQL Server database, create a user with the necessary privileges to create schemas and temporary tables in this database.

To create a SQL Server instance on Docker, run the following commands:
    
    
    docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=Test@123" -p 1433:1433 --name rudder_mssql -h rudder_mssql -d mcr.microsoft.com/mssql/server:2019-latest
    
    
    
    docker exec -it rudder_mssql "bash" /opt/mssql-tools/bin/sqlcmd -S localhost -U SA [-P "Test@123"]
    

In the above commands, the user is `SA` (System Admin) and password is `Test@123`.

The following queries let you create a user and grant the above-mentioned privileges (creating schemas and temporary tables on the database) to that user:
    
    
    CREATE LOGIN testuser WITH PASSWORD = 'Test@123';
    CREATE USER testuser FOR LOGIN testuser ;
    
    CREATE DATABASE test_db
    USE test_db
    -- GRANT individual permissions like this or
    GRANT CREATE TABLE TO testuser
    -- Provides owner permissions to user
    EXEC sp_addrolemember N'db_owner', N'testuser'
    

### Using AWS RDS instance

You can execute the same commands via Azure Studio or using the **sqlcmd** utility (`cmdline sqlcmd`).

## Configuring SQL Server destination in RudderStack

To send event data to SQL Server, you first need to add it as a destination in RudderStack and connect it to your data source. Once the destination is enabled, events will automatically start flowing to SQL Server via RudderStack.

To configure SQL Server as a destination in RudderStack, follow these steps:

  1. In your [RudderStack dashboard](<https://app.rudderstack.com>), set up the data source. Then, select **Microsoft SQL Server** from the list of destinations.
  2. Assign a name to your destination and then click **Next**.


### Connection settings

  * **Host** : The host name of your SQL Server service.
  * **Database** : The database name in your SQL Server instance where the data will be sent.
  * **User** : The name of the user with the required read/write access to the above database.
  * **Password** : The password for the above user.
  * **Port** : The port number associated with the SQL Server database instance.
  * **Namespace** : Enter the schema name where RudderStack will create all tables. If you don’t specify any namespace, RudderStack will set this to the source name, by default.


> ![warning](/docs/images/warning.svg)
> 
> You cannot change the namespace later.

  * **SSL Mode** : Choose the SSL mode through which RudderStack will connect to your SQL Server instance. RudderStack provides three options - **disable** , **true** , and **false**.
  * **Sync Frequency** : Specify how often RudderStack should sync the data to your SQL Server database.- **Sync Starting At** : This optional setting lets you specify the particular time of the day (in UTC) when you want RudderStack to sync the data to the warehouse.
  * **Exclude Window** : This optional setting lets you set a time window when RudderStack will **not sync** the data to your database.


### Configuring the object storage

RudderStack lets you configure the following object storage configuration settings while setting up your Microsoft SQL Server destination:

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

#### How does RudderStack handle cases when loading the data into SQL Server?

RudderStack converts the event keys into lower case before exporting the data into SQL Server, so that it does not create two tables if the event name has two different cases.

#### How are reserved words handled by RudderStack?

There are some limitations when it comes to using [reserved words](<https://docs.microsoft.com/en-us/sql/t-sql/language-elements/reserved-keywords-transact-sql?view=sql-server-ver15>) in a schema, table, or column names. If such words are used as event names, traits or properties, they will be prefixed with a `_` when RudderStack creates tables or columns for them in your schema.

Also, it is important to note that integers are not allowed at the start of the schema or table name. Hence, RudderStack prefixes such schema, column or table names with a `_`.

For instance, `'25dollarpurchase'` will be changed by RudderStack to `'_25dollarpurchase`'.

#### What are the SSL mode options provided by RudderStack?

While setting up the SQL Server destination, RudderStack provides the following three SSL options:

  * **disable** : The data sent from RudderStack to your database is not encrypted.
  * **false** : The data sent from RudderStack to your database is not encrypted beyond the login packet.
  * **true** : The data sent from RudderStack to your database is encrypted.


> ![info](/docs/images/info.svg)
> 
> For a more comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.