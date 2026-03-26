# Google BigQuery Destination

Sync data from RudderStack to Google BigQuery.

* * *

  * __11 minute read

  * 


[Google BigQuery](<https://cloud.google.com/bigquery>) is an industry-leading, fully-managed cloud data warehouse that lets you efficiently store and analyze petabytes of data.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/bq>).

> ![info](/docs/images/info.svg)
> 
> See the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) guide for more information on how the events are mapped to the tables in BigQuery.

## Setting up the BigQuery project

Before you set up BigQuery as a destination in RudderStack, follow these steps to set up your BigQuery project:

  1. Create a Google Cloud Platform (**GCP**) project if you don’t have one already. For more details, refer to this [BigQuery documentation](<https://cloud.google.com/resource-manager/docs/creating-managing-projects?hl=en&ref_topic=6158848&visit_id=637219216155418807-3094012232&rd=1>).


> ![warning](/docs/images/warning.svg)
> 
> Make sure to enable [billing](<https://cloud.google.com/billing/docs/how-to/modify-project>) for the project to allow RudderStack to load data into your BigQuery cluster.

  2. Enable the BigQuery API for your existing project if not done already. See the [Google Cloud documentation](<https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui>) for more information.
  3. Log into your [BigQuery console](<https://console.cloud.google.com/>). Copy the project **ID** as shown below. This ID is required for configuring BigQuery as a destination in RudderStack.

[![Copy the Project ID](/docs/images/screenshot-2020-04-08-at-11.36.30-am.webp)](</docs/images/screenshot-2020-04-08-at-11.36.30-am.webp>)

  4. Create a new Google Cloud Storage (**GCS**) bucket or provide an existing one to store files before loading the data into your BigQuery instance. Also, ensure that the data loads from GCS to BigQuery by co-locating your GCS storage bucket with BigQuery. For more information, see the [Google Cloud documentation](<https://cloud.google.com/bigquery/docs/loading-data-cloud-storage#data-locations>).


## Setting up the service account for RudderStack

> ![warning](/docs/images/warning.svg)
> 
> Make sure to create the service account for the BigQuery project you set up above.

For RudderStack to successfully send events to your BigQuery instance, you need to set up a service account with a role containing the following permissions:
    
    
    bigquery.datasets.create // Skip if the dataset already exists.
    bigquery.datasets.get
    bigquery.jobs.create
    bigquery.routines.get
    bigquery.routines.list
    bigquery.tables.create
    bigquery.tables.delete
    bigquery.tables.get
    bigquery.tables.getData
    bigquery.tables.list
    bigquery.tables.update
    bigquery.tables.updateData
    storage.objects.create
    storage.objects.get
    storage.objects.list
    

> ![info](/docs/images/info.svg)
> 
> You can skip the `bigquery.datasets.create` permission if the dataset already exists.

Follow these steps to set up a service account:

  1. Create a new service account by going to **IAM & Admin** > **Service Accounts**.
  2. Create a new role with the permissions mentioned above. Then, assign it to the service account.


> ![warning](/docs/images/warning.svg)
> 
> If you do not want to add the above fine-grained permissions to the service account individually, you can add the below roles to your service account:
> 
>   * `Storage Object Creator`
>   * `Storage Object Viewer`
>   * `BigQuery Job User`
>   * `BigQuery Data Owner`
> 

> 
> If the dataset name already exists (configurable by the **Namespace** setting in the RudderStack dashboard), you can assign the **BigQuery Data Editor** role instead of **BigQuery Data Owner**.

  3. Create a key for the service account with **JSON** as the type and store it.

[![Create a key](/docs/images/screenshot-2020-04-08-at-12.09.07-pm%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29.webp)](</docs/images/screenshot-2020-04-08-at-12.09.07-pm%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29%20%281%29.webp>)

  4. Create and download the private JSON key required for configuring BigQuery as a destination in RudderStack:

[![JSON key required for the RudderStack UI](/docs/images/screenshot-2020-04-08-at-12.09.32-pm%20%281%29.webp)](</docs/images/screenshot-2020-04-08-at-12.09.32-pm%20%281%29.webp>)

## IPs to be allowlisted

By default, you can access BigQuery via the Google APIs, which are publicly accessible. As such, allowlisting any IPs is **not required**. However, if your VPC service restricts the BigQuery APIs, you will need to allowlist the below IPs by [setting up network access control for BigQuery](<https://staging.medium.com/setting-up-network-access-control-for-bigquery-3957be554467>).

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

## Configuring Google BigQuery destination in RudderStack

To send event data to BigQuery, you first need to add it as a destination in RudderStack and connect it to your data source. Once the destination is enabled, events will automatically start flowing to BigQuery via RudderStack.

To configure BigQuery as a destination in RudderStack, follow these steps:

  1. In your [RudderStack dashboard](<https://app.rudderstack.com>), set up the data source. Then, select **BigQuery** from the list of destinations.
  2. Assign a name to your destination and then click **Next**.


### Connection settings

  * **Project** : The GCP project ID where the BigQuery database is located.
  * **Location** : The GCP region for your dataset.
  * **Staging GCS Storage Bucket Name** : The name of the storage bucket as specified in the Setting up the BigQuery project section.
  * **Prefix** : If specified, RudderStack creates a folder in the bucket with this prefix and pushes all data within that folder.
  * **Namespace** : Enter the schema name where RudderStack creates all tables. If you don’t specify any namespace, RudderStack sets the namespace to the source name, by default.


> ![warning](/docs/images/warning.svg)
> 
> You cannot change the namespace later.

  * **Credentials** : Your GCP service account credentials JSON as created in the Setting up the service account for RudderStack section.

  * **Clean up object storage files after successful sync** : Turn on this toggle to delete the object storage files after the sync has completed successfully.

  * **Sync Frequency** : Specify how often RudderStack should sync the data to your BigQuery dataset.

  * **Sync Starting At** : This optional setting lets you specify the particular time of the day (in UTC) when you want RudderStack to sync the data to BigQuery.

  * **Exclude Window** : This optional setting lets you set a time window when RudderStack will **not sync** the data to your database.

  * **Partition Column** : Specify how you want to [partition](<https://cloud.google.com/bigquery/docs/partitioned-tables>) your tables by choosing from the following options:

    * **Ingestion Time** : Time at which BigQuery ingests the data. See [Ingestion time partitioning](<https://cloud.google.com/bigquery/docs/partitioned-tables#ingestion_time>) for more information.
    * **Loaded At** : Time at which RudderStack loads the data in the warehouse (`loaded_at` column).
    * **Received At** : Time at which RudderStack receives the data (`received_at` column).
    * **Timestamp** : Timestamp calculated by RudderStack to account for the client-side clock skew (`timestamp` column).
    * **Sent At** : Time at which the data was sent from the client to RudderStack (`sent_at` column).
    * **Original Timestamp** : Time when the data was generated at the source (`original_timestamp` column).

See [Time-unit column partitioning](<https://cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables>) for more information on how BigQuery puts the data into the partition based on the values in the **Loaded At** , **Received At** , **Timestamp** , **Sent At** , and **Original Timestamp** columns.

  * **Partition Type** : Specify the partition’s granularity level from the dropdown. RudderStack provides two options - **Hour** and **Day**.


> ![warning](/docs/images/warning.svg)
> 
> You **cannot** edit the partition settings for existing BigQuery destinations through the dashboard. RudderStack **automatically sets** their partitioning type to [Ingestion time partitioning](<https://cloud.google.com/bigquery/docs/partitioned-tables#ingestion_time>) with a [day level granularity](<https://cloud.google.com/bigquery/docs/partitioned-tables#select_daily_hourly_monthly_or_yearly_partitioning>).
> 
>   * To change your partition configuration, RudderStack recommends creating a new BigQuery destination and deprecating the old one.
>   * To apply partition changes to an existing destination, contact [RudderStack Support](<mailto:support@rudderstack.com>).
> 


### Advanced settings

  * **Skip User Table** : This setting is toggled on by default and sends events exclusively to the [`identifies`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table while skipping the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table. This eliminates the need for a merge operation on the `users` table. If toggled off, RudderStack sends the events to both the `identifies` and `users` tables.
  * **Skip Tracks Table** : Toggle on this setting to skip sending events to the [`tracks`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table.
  * **Skip Views Creation** : Toggle on this setting to disable views creation in BigQuery. See Partitioned tables and views for more information.


> ![warning](/docs/images/warning.svg)
> 
> This setting is configurable only while creating a new BigQuery destination and **cannot** be changed later.

  * **JSON Columns** : Use this setting to specify the required JSON column paths in dot notation separated by commas. This option applies to all incoming `track` events for this destination.


> ![success](/docs/images/tick.svg)
> 
> With the [JSON columns](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/json-column-support/>) feature, you can ingest semi-structured event data not defined by a fixed schema.

## How RudderStack creates the dataset

RudderStack uses the source name (written in snake case, for example, `source_name`) to create a dataset in BigQuery.

See the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) guide for more details on the tables and columns created by RudderStack.

> ![info](/docs/images/info.svg)
> 
> By default, RudderStack uses the partitioned tables method to ingest data into BigQuery.

### Partitioned tables

RudderStack creates ingestion-time [partition tables](<https://cloud.google.com/bigquery/docs/partitioned-tables>) based on the load date, so you can take advantage of it to query a subset of data.

For information on how RudderStack creates these tables on load, see the [Creating partitioned tables](<https://cloud.google.com/bigquery/docs/creating-partitioned-tables#creating_an_ingestion-time_partitioned_table_when_loading_data>) section of the BigQuery documentation.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not discard duplicate data while loading it into BigQuery.

### Views

In addition to tables, RudderStack creates a [view](<https://cloud.google.com/bigquery/docs/views-intro>) (`<table_name>_view`) for every table for de-duplication purposes, ensuring that queried events are unique and contain the latest records.

Note that:

  * RudderStack recommends using the corresponding view (containing the events from the last 60 days) to avoid duplicate events in your query results.
  * Since BigQuery [views](<https://cloud.google.com/bigquery/docs/views-intro#view_pricing>) are merely logical views and are not cached, you can create a native table from it to save costs - by avoiding running the query that defines the view every time.
  * You can modify the view query to change the time window of the view - the default value is set to 60 days.


#### Skip views creation

Toggle on the Skip Views Creation connection setting to disable creating views in BigQuery.

RudderStack recommends skipping views creation only if:

  * You do not need views and want to take care of deduplication by yourself.
  * You have alternative deduplication methods (for example, partition columns and types).
  * You want a [materialized view](<https://cloud.google.com/bigquery/docs/materialized-views-intro>) instead of a [logical view](<https://cloud.google.com/bigquery/docs/views-intro>).
  * You have any security reasons and want to limit access to the tables.


## FAQ

#### I am getting an “Failed to add columns for table <table_name> in the name ” error even though the table column limit is not reached. How do I resolve this issue?

According to [BigQuery documentation](<https://cloud.google.com/bigquery/quotas#:~:text=Maximum%20columns%20in%20a%20table%2C%20query%20result%2C%20or%20view%20definition>), the maximum columns in a table, query result, or view definition cannot exceed 10000 columns. This includes recently deleted columns that persist in the total columns quota until it resets.

To circumvent the “Failed to add columns for table <table_name> in the name ” error when the table column limit is not reached, you can create a new table using `CLONE` and take a backup of the existing table to resolve the issue:

  1. Create new table using `CLONE` by using the below query:


    
    
    CREATE OR REPLACE TABLE <YOUR_PROJECT>.dataset.<NEW_TABLE> CLONE <YOUR_PROJECT>.dataset.<OLD_TABLE>;
    

  2. Rename and keep the current table as backup:


    
    
    ALTER TABLE <YOUR_PROJECT>.dataset.<OLD_TABLE> RENAME TO <OLD_TABLE_BACKUP>;
    

  3. Rename the new table to match the old table name:


    
    
    ALTER TABLE <YOUR_PROJECT>.dataset.<NEW_TABLE> RENAME TO <OLD_TABLE>;
    

#### Where do I add the allowlisted IPs in BigQuery?

By default, BigQuery is accessible via publicly accessible Google APIs. As such, allowlisting any IPs is not required. However, if your VPC service restricts the BigQuery APIs, you will need to allowlist the IPs by [setting up network access control for BigQuery](<https://staging.medium.com/setting-up-network-access-control-for-bigquery-3957be554467>).

#### How are reserved words handled by RudderStack?

There are some limitations when it comes to using [reserved words](<https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#reserved_keywords>) in a schema, table, or column names. If such words are used in event names, traits or properties, they will be prefixed with a `_`when RudderStack creates tables or columns for them in your schema.

Besides, integers are not allowed at the start of the schema or table name. Hence, such schema, column or table names will be prefixed with a `_`.

For instance, `'25dollarpurchase`’ will be changed to `'_25dollarpurchase`'.

#### When sending data into a data warehouse, how can I change the table where this data is sent?

By default, RudderStack sends the data to the table/dataset based on the source it is connected to. For example, if the source is Google Tag Manager, RudderStack sets the schema name as `gtm_*`. However, you can override this behavior by setting the **Namespace** field in the BigQuery destination settings:

[![Namespace](/docs/images/image%20%2879%29.webp)](</docs/images/image%20%2879%29.webp>)

#### I’m looking to send data to BigQuery through RudderStack and I’m trying to understand what data is populated in each column. How do I go about this?

Refer to the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) documentation for details on how RudderStack generates the schema in the warehouse and populates the data in each column.

#### I am trying to load data into my BigQuery destination and I get the error “Cannot read and write in different locations”. What should I do?

Make sure that both your BigQuery dataset and the bucket have the same region.

#### When piping data to a BigQuery destination, I can set the bucket but not a folder within the bucket. Is there a way to put RudderStack data in a specific bucket folder?

Yes, you can set the desired folder name in the **Prefix** field while setting up your BigQuery destination in RudderStack.

#### Does open source RudderStack support near real-time syncing to BigQuery and event replay?

The near-realtime BigQuery syncing feature is currently under development and is planned to be released in the coming months. Unfortunately, Event Replay is not a part of open-source RudderStack currently.

#### What is the current sync frequency for BigQuery?

If you’re using open source RudderStack, the minimum sync frequency is **30 minutes**. If you’re self-hosting the data plane or using RudderStack’s [Enterprise plan](<https://www.rudderstack.com/enterprise-quote/>), you can assign the required value for sync frequency to the `uploadFreqInS` parameter in `config.yaml` file. Note that the minimum value can be `1800` (30 minutes).

For more information, refer to this [FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/#is-there-a-way-to-force-load-my-data-into-the-warehouse>).

#### Do I need to stop the running pipeline to change my sync frequency? Or will the new change be effective even without stopping the pipeline?

To change the sync frequency, you **need not** stop the pipeline.

#### When configuring the BigQuery destination, where does Google use the credentials JSON from?

BigQuery uses the credentials JSON from the dashboard configuration when setting up the destination. For more information, refer to the Setting up the service account for RudderStack section.

#### When configuring the BigQuery destination, should the user permissions be set for the specific dataset or the whole project?

You need to set the user permissions for the whole project. Otherwise, you may encounter issues.

#### How long are the failed syncs retried before being aborted?

RudderStack retries the failed syncs for up to 3 hours before aborting them. For more information, refer to this [FAQ](<https://www.rudderstack.com/docs/resources/faq/#how-does-rudderstack-handle-retries-for-failed-events-in-case-of-destination-failure>).

> ![info](/docs/images/info.svg)
> 
> For a more comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.