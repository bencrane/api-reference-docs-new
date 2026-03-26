# Google Cloud Storage Data Lake

Sync data from RudderStack to GCS Data Lake.

* * *

  * __5 minute read

  * 


The [Google Cloud Storage (GCS) data lake](<https://cloud.google.com/architecture/build-a-data-lake-on-gcp>) leverages [Google Cloud Storage](<https://cloud.google.com/storage>) for storing and accessing your data in the GCP infrastructure.

## Setting user permissions

To set up GCS data lake as a destination in RudderStack, you will need to create a new user role and grant the required permissions to create schemas and temporary tables.

### Creating the role and adding permissions

  1. Go to the [Google Cloud IAM Admin console](<https://console.cloud.google.com/iam-admin/roles>) and click **CREATE ROLE**.
  2. Then, fill in the details as shown:

[![Role details](/docs/images/dw-integrations/gcs-datalake-2.webp)](</docs/images/dw-integrations/gcs-datalake-2.webp>)

  3. Fill the details and click **ADD PERMISSIONS**.
  4. Under **Filter permissions by role** , select **Storage Object Admin** and grant the required permissions:

[![Setting permissions](/docs/images/dw-integrations/gcs-datalake-3.webp)](</docs/images/dw-integrations/gcs-datalake-3.webp>)

  5. The permission required to successfully use the GCS data lake destination is shown:


    
    
    storage.objects.create
    storage.object.get
    

  6. Then, click **CREATE**. This will successfully create the role.


### Creating the service account and attaching the role

  1. Go to the **Service Accounts** option in the [Google Cloud IAM Admin console](<https://console.cloud.google.com/iam-admin/serviceaccounts>).
  2. Then, select the project containing the dataset that you want to use.
  3. Next, click **CREATE SERVICE ACCOUNT**.
  4. Fill in the details as shown below and click **CREATE**.

[![Service account details](/docs/images/dw-integrations/gcs-datalake-4.webp)](</docs/images/dw-integrations/gcs-datalake-4.webp>)

  5. Then, select the previously created role and click **CONTINUE**.

[![Role details](/docs/images/dw-integrations/gcs-datalake-5.webp)](</docs/images/dw-integrations/gcs-datalake-5.webp>)

  6. Finally, click **DONE**.


### Creating and downloading the JSON key

  1. Click the three dots under **Actions** in the service account that you just created and select **Manage keys** :

[![Manage keys option](/docs/images/dw-integrations/gcs-datalake-6.webp)](</docs/images/dw-integrations/gcs-datalake-6.webp>)

  2. Click **ADD KEY** , followed by **Create new key** :

[![Creating new key](/docs/images/dw-integrations/gcs-datalake-7.webp)](</docs/images/dw-integrations/gcs-datalake-7.webp>)

  3. In the resulting pop-up, select **JSON** and click **CREATE**.

[![Downloading JSON key](/docs/images/dw-integrations/gcs-datalake-8.webp)](</docs/images/dw-integrations/gcs-datalake-8.webp>)

  4. Finally, download this JSON file. This file is required while setting up the GCS data lake destination in RudderStack.


## Configuring GCS data lake destination in RudderStack

To send event data to GCS data lake, you first need to add it as a destination in RudderStack and connect it to your data source. Once the destination is enabled, events will automatically start flowing to GCS data lake via RudderStack.

To configure GCS data lake as a destination in RudderStack, follow these steps:

  1. In your [RudderStack dashboard](<https://app.rudderstack.com>), set up the data source. Then, select **Google Cloud Storage Data Lake** from the list of destinations.
  2. Assign a name to your destination and then click **Next**.


### Connection settings

  * **GCS Storage Bucket Name** : The name of the GCS bucket used to store data before loading it into the GCS data lake.
  * **Prefix** : If specified, RudderStack will create a folder in the bucket with this prefix and push all data within that folder. For example, `https://storage.googleapis.com/<bucketName>/<prefix>/`.
  * **Namespace** : If specified, all data for the destination will be pushed to `https://storage.googleapis.com/<bucketName>/<prefix>/rudder-datalake/<namespace>`. If you don’t specify a namespace in the settings, RudderStack sets it to the source name, by default.


> ![warning](/docs/images/warning.svg)
> 
> You cannot change the namespace later.

  * **Table Suffix** : This optional setting lets you define a custom path under which your table data is stored. For example, if you set this field to `rs`, your data will be pushed to `https://storage.googleapis.com/<bucketName>/<prefix>/rudder-datalake/<namespace>/<table-name>/rs`.
  * **Clean up object storage files after successful sync** : Turn on this toggle to delete the object storage files after the sync has completed successfully.
  * **Choose time window layout** : This option lets you set the timestamp-defined layout structure under which the table data will be stored.

[![GCS data lake destination settings in RudderStack](/docs/images/dw-integrations/gcs-datalake-time-window-layout.webp)](</docs/images/dw-integrations/gcs-datalake-time-window-layout.webp>)

For example, if you choose the option **Upto Hour (year=YYYY/month=MM/day=DD/hour=HH)** and an event called `Product Clicked` is received at `2022-08-06T17:30:00.000T`, then the data will be stored in the following location:
    
    
    https://storage.googleapis.com/<bucketName>/<prefix>/rudder-datalake/<namespace>/<table_name>/<table_suffix>/year=2022/month=08/day=06/hour=17/
    

> ![info](/docs/images/info.svg)
> 
> The default value for this setting is **YYYY/MM/DD/HH**.

  * **Credentials** : Enter the content of the downloaded credentials JSON file in this field.
  * **Sync Frequency** : Specify how often RudderStack should sync the data to your GCS data lake.
  * **Sync Starting At** : This optional setting lets you specify the particular time of the day (in UTC) when you want RudderStack to sync the data to the data lake.


### Advanced settings

  * **Skip User Table** : This setting is toggled on by default and sends events exclusively to the [`identifies`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table while skipping the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table. This eliminates the need for a merge operation on the `users` table. If toggled off, RudderStack sends the events to both the `identifies` and `users` tables.
  * **Skip Tracks Table** : Toggle on this setting to skip sending events to the [`tracks`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table.


## Finding your data in the GCS data lake

RudderStack converts your events into Parquet files and dumps them into the configured GCS bucket. Before dumping the events, RudderStack groups the files by the event name based on the time (in UTC) they were received.

The folder structure is similar to the following format:
    
    
    https://storage.googleapis.com/<bucketName>/<prefix>/rudder-datalake/<namespace>/<tableName>/YYYY/MM/DD/HH
    

As specified in the Connection settings section above:

  * `<prefix>` is the GCS prefix used while configuring the GCS data lake destination in RudderStack. If not specified, RudderStack will omit this value.
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
Product Purchased| `https://storage.googleapis.com/<bucketName>/<prefix>/rudder-datalake/<namespace>/product_purchased/2019/10/12/08`  
Cart Viewed| `https://storage.googleapis.com/<bucketName>/<prefix>/rudder-datalake/<namespace>/cart_viewed/2019/11/12/09`  
  
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

#### What are the files written in the location `<namespace>/rudder-warehouse-staging-logs/`?

RudderStack collects all unprocessed data flowing to the warehouse destinations as staging files. It stores these files in the object storage at the location `https://storage.googleapis.com/rudder-warehouse-staging-logs/`.

Once the staging files are processed, RudderStack separates them by the event name and sends them to the specified destination in the following format:

`https://storage.googleapis.com/<bucketName>/<prefix>/rudder-datalake/<namespace>/<tableName>`.

> ![info](/docs/images/info.svg)
> 
> For a more comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.