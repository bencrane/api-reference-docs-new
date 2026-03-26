# Event Replay

Replay events in case of failures, or for testing and diagnostics.

Available Plans

  * enterprise


* * *

  *  __3 minute read

  * 


RudderStack’s **Event Replay** feature lets you back up your event data and replay it in case of any failures. You can leverage this feature in the following scenarios:

  * Replay failed events from a particular date to a destination, maybe due to some misconfiguration.
  * Replay all events for a particular source, from a particular date, to a new event stream or warehouse destination.


## Supported event types for replay

> ![warning](/docs/images/warning.svg)
> 
> RudderStack **does not support** replaying data from Reverse ETL sources.

RudderStack can store the following types of event data and replay it to the specified destinations:

### Raw events

RudderStack stores the raw events captured through various sources in batches of 100,000 events.

Note the following:

  * **Upload frequency** : The upload frequency is 100,000 events or 5 minutes (whichever is earlier) for each source.
  * **File format** : RudderStack stores the events in newline-separated gzipped JSON format.


### Delivery failures

RudderStack stores only the metadata of the delivery failures in its own S3 storage, approximately every 30 seconds.

> ![info](/docs/images/info.svg)
> 
> RudderStack does not store any event payloads in case of delivery failures, as the payloads are already stored during archival.

## Data retention options

RudderStack offers the following [data retention options](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#data-retention-options>) for event replay:

Data retention option| Description  
---|---  
Do not store event data| RudderStack does not store any event data and hence it cannot be replayed.  
Store in your own cloud storage| Event data is stored in your object storage. RudderStack currently supports Amazon S3, Google Cloud Storage, Azure Blob Storage, and MinIO as the object storage options.  
  
RudderStack **recommends** using this option.  
RudderStack 7-day cloud storage| RudderStack stores the event data in its S3 bucket on a rolling 7-day basis, that is, RudderStack deletes the data 7 days after it was stored.  
  
This is the **default** setting.  
RudderStack 30-day cloud storage| RudderStack stores the event data in its S3 bucket on a rolling 30-day basis, that is, RudderStack deletes the data 30 days after it was stored.  
  
This option is available only for the [Enterprise](<https://rudderstack.com/pricing/>) plan.  
  
### Object storage setup

If you choose to set up your own object storage for backing up and replaying the events, follow the steps below depending on your cloud provider:

> ![warning](/docs/images/warning.svg)
> 
> The S3 setup for event backup and replay is different to [setting up Amazon S3 as a destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/>).

  1. Create your [object storage bucket](<https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html>).
  2. Configure the relevant [permissions for your bucket](<https://www.rudderstack.com/docs/user-guides/administrators-guide/bucket-configuration-settings/#permissions-for-amazon-s3>).
  3. Connect your storage provider in the RudderStack dashboard. See [Store event data in your own cloud storage](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#2-store-event-data-in-your-own-cloud-storage-recommended>) for details.


  1. Create your [object storage bucket](<https://cloud.google.com/storage/docs/creating-buckets>).
  2. Configure the relevant [permissions for your bucket](<https://www.rudderstack.com/docs/user-guides/administrators-guide/bucket-configuration-settings/#permissions-for-gcs>).
  3. Connect your storage provider in the RudderStack dashboard. See [Store event data in your own cloud storage](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#2-store-event-data-in-your-own-cloud-storage-recommended>) for details.


  1. Login to the [Azure portal](<https://portal.azure.com/>) and create a [storage account](<https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal>).
  2. Click **Containers** under **Blob service** and create a new container.
  3. Connect your storage provider in the RudderStack dashboard. See [Store event data in your own cloud storage](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#2-store-event-data-in-your-own-cloud-storage-recommended>) for details.


  1. Log in to your MinIO service and [set up your bucket](<https://www.rudderstack.com/docs/destinations/streaming-destinations/minio/#setting-up-minio>).
  2. Connect your storage provider in the RudderStack dashboard. See [Store event data in your own cloud storage](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#2-store-event-data-in-your-own-cloud-storage-recommended>) for details.


## Event ordering behavior

RudderStack processes replayed events in the same order they were originally received at the source.

> ![warning](/docs/images/warning.svg)
> 
> **Important consideration**
> 
> While RudderStack processes events in their original order, destinations may overwrite newer data with older replayed data, depending on how each destination handles events. Consider this behavior when replaying your events to avoid unintended data overwrites.

## How can I replay my events?

Depending on how you store your event data (**RudderStack-hosted storage** or your **own object storage**), contact [RudderStack Support](<mailto:support@rudderstack.com>) to safely replay your events and avoid any unfavorable circumstances.