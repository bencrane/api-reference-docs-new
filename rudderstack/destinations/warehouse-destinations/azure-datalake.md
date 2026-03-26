# Azure Data Lake

Sync data from RudderStack to Azure Data Lake.

* * *

  * __4 minute read

  * 


[Azure Data Lake](<https://azure.microsoft.com/en-in/solutions/data-lake/>) is Microsoft’s secure and scalable data lake functionality that lets you store data of varying sizes and complexity and facilitates fast, cross-platform data processing and analytics.

> ![info](/docs/images/info.svg)
> 
> Refer to the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) guide for more information on how the events are mapped to the tables in the Azure data lake.

> ![success](/docs/images/tick.svg)
> 
> Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/azure_datalake>).

## Configuring Azure data lake destination in RudderStack

To send event data to Azure data lake, you first need to add it as a destination in RudderStack and connect it to your data source. Once the destination is enabled, events will automatically start flowing to Azure data lake via RudderStack.

To configure Azure data lake as a destination in RudderStack, follow these steps:

  1. In your [RudderStack dashboard](<https://app.rudderstack.com>), set up the data source. Then, select **Azure Data Lake** from the list of destinations.
  2. Assign a name to your destination and then click **Next**.


### Connection settings

  * **Azure Blob Storage Container Name** : Enter the name of your Blob Storage container used to store the data before loading it into the data lake.
  * **Prefix** : If specified, RudderStack will create a folder in the bucket with this prefix and push all data within that folder. For example, `https://<account_name>.blob.core.windows.net/<container_name>/<prefix>/`
  * **Namespace** : If specified, all data for the destination will be pushed to `https://<account_name>.blob.core.windows.net/<bucketName>/<prefix>/rudder-datalake/<namespace>`. If you don’t specify a namespace in the settings, RudderStack sets it to the source name, by default.


> ![warning](/docs/images/warning.svg)
> 
> You cannot change the namespace later.

  * **Azure Blob Storage Account Name** : Enter your Azure Blob Storage account name.
  * **Azure Blob Storage Account Key** : Enter your Blob Storage account key.
  * **Use shared access signature (SAS) Tokens** : Enable this setting to grant limited access to your Azure Storage resources. When enabled, you can use a Shared Access Signatures (SAS) token instead of your storage account access key:

[![Azure Blob Storage SAS token](/docs/images/dw-integrations/azure-sas-token.webp)](</docs/images/dw-integrations/azure-sas-token.webp>)

  * **Azure Blob Storage SAS** : Enter the generated SAS token.


> ![info](/docs/images/info.svg)
> 
> For more information on setting up your Azure Blob Storage account, refer to the [Azure Blob Storage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/microsoft-azure-blob-storage/#setting-up-azure-blob-storage>) guide.

  * **Clean up object storage files after successful sync** : Turn on this toggle to delete the object storage files after the sync has completed successfully.
  * **Sync Frequency** : Specify how often RudderStack should sync the data to your Azure data lake.
  * **Sync Starting At** : This optional setting lets you specify the particular time of the day (in UTC) when you want RudderStack to sync the data to the warehouse.


### Advanced settings

  * **Skip User Table** : This setting is toggled on by default and sends events exclusively to the [`identifies`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table while skipping the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table. This eliminates the need for a merge operation on the `users` table. If toggled off, RudderStack sends the events to both the `identifies` and `users` tables.
  * **Skip Tracks Table** : Toggle on this setting to skip sending events to the [`tracks`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table.


## Finding your data in the Azure data lake

RudderStack converts your events into Parquet files and dumps them into the configured Azure bucket. Before dumping the events, RudderStack groups the files by the event name based on the time (in UTC) they were received.

The folder structure is similar to the following format:

`https://<account_name>.blob.core.windows.net/<prefix>/rudder-datalake/<namespace>/<tableName>/YYYY/MM/DD/HH`

As specified in the Connection settings section above:

  * `<prefix>` is the Azure prefix used while configuring the Azure data lake destination in RudderStack. If not specified, RudderStack will omit this value.
  * `<namespace>` is the namespace specified in the destination settings. If not specified, RudderStack sets it to the source name.
  * `<tableName>` is set to the event name.
  * `YYYY`, `MM`, `DD`, and `HH` are replaced by the actual time values.


> ![info](/docs/images/info.svg)
> 
> A combination of the `YYYY`, `MM`, `DD`, and `HH` values represents the UTC time.

### Use case

Suppose that RudderStack tracks the following two events:

Event Name| Timestamp  
---|---  
Product Purchased| `"2019-10-12T08:40:50.52Z" UTC`  
Cart Viewed| `"2019-11-12T09:34:50.52Z" UTC`  
  
RudderStack then converts these events into Parquet files and dumps them into the following folders:

Event Name| Folder Location  
---|---  
Product Purchased| `https://<account_name>.blob.core.windows.net/<prefix>/rudder-datalake/<namespace>/product_purchased/2019/10/12/08`  
Cart Viewed| `https://<account_name>.blob.core.windows.net/<prefix>/rudder-datalake/<namespace>/cart_viewed/2019/11/12/09`  
  
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

For a comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.