# Data Management

Manage event retention effectively in RudderStack.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __5 minute read

  * 


RudderStack provides a comprehensive data retention policy and options for opting in or out of data storage.

It provides the following retention options (available only in the above plans) for your event data:

  * Do not store event data
  * Store in your own cloud storage (Recommended)
  * Store in RudderStack on a rolling 7-day basis
  * Store in RudderStack on a rolling 30-day basis (Applicable only for the [Enterprise](<https://rudderstack.com/enterprise-quote>) plan)


The following sections define different types of RudderStack data and provide steps on opting in to the right setup for your needs.

## Data definitions

RudderStack **does not** permanently store any customer data except the following:

  * Aggregate “Count” data on Event Name, Event Type, Source ID, Destination ID.
  * Error codes.
  * RudderStack customers’ records (for example, usernames, billing-related details).


> ![info](/docs/images/info.svg)
> 
> The storage options vary with the nature of the data and your RudderStack plan.
> 
> See Plan-based retention options for more details.

All other customer data can be classified as either **transient** or **non-transient** and it may either be stored in your location, for example, AWS, or by RudderStack for up to 7 days (or 30 days in case of Enterprise plan).

> ![info](/docs/images/info.svg)
> 
> RudderStack’s data retention policy defines data as they pertain to the primary components of its service — the [Data Plane](<https://www.rudderstack.com/docs/resources/glossary/#data-plane>) and [Control Plane](<https://www.rudderstack.com/docs/resources/glossary/#control-plane>).

### Transient customer data

Transient customer data can be defined as all in-transit data, that is, **stored for less than 3 hours** , as an essential part of delivering the RudderStack product experience. This data includes:

  * **Data Plane** : Events that hit the RudderStack gateway. See [Data Plane architecture](<https://www.rudderstack.com/docs/resources/rudderstack-architecture/#data-plane-architecture>) for more details.
  * **Control Plane** : The in-transit data captured in the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) tab of the RudderStack dashboard.


### Non-transient customer data

Non-transient customer data can be defined as data that can persist for more than 3 hours **only if** configured by the RudderStack user. This includes:

  * **Data Plane** : This includes **gateway dumps** , that is, raw data for every successfully-ingested event.
  * **Control Plane** : Data in the reporting service (sample events and responses).


## Data retention options

> ![info](/docs/images/info.svg)
> 
> Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can configure the data retention settings.

RudderStack provides 3 options for your event data storage. To choose how you want to store the event data, follow these steps:

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Settings** > **Workspace** > **Data Management**.
  3. Choose one of the 3 data storage options in the **Data retention** section:

[![Choose your data storage option.](/docs/images/dashboard-guides/data-retention-options.webp)](</docs/images/dashboard-guides/data-retention-options.webp>)

The following sections explain the data retention options in detail.

### 1\. Do not store event data

If you choose this option, RudderStack will not store any of your event data.

[![Do not store event data.](/docs/images/dashboard-guides/no-data-storage.webp)](</docs/images/dashboard-guides/no-data-storage.webp>)

### 2\. Store event data in your own cloud storage (Recommended)

This is the recommended event storage option, and available in the [Starter, Growth, and Enterprise](<https://www.rudderstack.com/pricing/>) plans. Selecting this option will bring up a modal allowing you to connect a storage bucket with your RudderStack data.

[![Store your data with your cloud provider.](/docs/images/dashboard-guides/connect-cloud-storage.webp)](</docs/images/dashboard-guides/connect-cloud-storage.webp>)

> ![info](/docs/images/info.svg)
> 
> RudderStack supports storage via AWS, GCS, Azure, and MinIO if you select this option.

When connecting your cloud storage provider to RudderStack, you will first need to create a storage bucket and configure the credentials for RudderStack to access the datastore. Follow the steps listed below depending on your cloud provider:

  1. Create your [S3 bucket](<https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html>).
  2. In the dashboard, specify the **S3 Bucket Name** and **Prefix**.
  3. **Role Based Authentication** is turned on by default. [Create a RudderStack IAM role](<https://www.rudderstack.com/docs/destinations/aws-iam-role-for-rudderstack/>) and specify the **IAM Role ARN**.


If you have disabled **Role Based Authentication** (not recommended), configure the [permissions for your S3 bucket](<https://www.rudderstack.com/docs/user-guides/administrators-guide/bucket-configuration-settings/#permissions-for-amazon-s3>). Then, enter the **Access key ID** and **Secret Access Key**.

  4. Enable server-side encryption, if needed.

![S3 bucket settings for data retention](/docs/images/dashboard-guides/s3-data-retention-settings.webp)

**If you are self-hosting RudderStack using RudderStack Open Source** :

  1. Create your [S3 bucket](<https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html>).
  2. Configure relevant [permissions for your S3 bucket](<https://www.rudderstack.com/docs/user-guides/administrators-guide/bucket-configuration-settings/#permissions-for-amazon-s3>). Note the **Access key ID** and **Secret Access Key**.
  3. Configure the bucket settings in the dashboard.


  1. Create your [object storage bucket](<https://cloud.google.com/storage/docs/creating-buckets>).
  2. Configure the relevant [permissions for your bucket](<https://www.rudderstack.com/docs/user-guides/administrators-guide/bucket-configuration-settings/#permissions-for-gcs>).
  3. Connect your storage provider in the RudderStack dashboard.


  1. Login to the [Azure portal](<https://portal.azure.com/>) and create a [storage account](<https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal>).
  2. Click **Containers** under **Blob service** and create a new container.
  3. Connect your storage provider in the RudderStack dashboard.


  1. Login to your MinIO service and [set up your bucket](<https://www.rudderstack.com/docs/destinations/streaming-destinations/minio/#setting-up-minio>).
  2. Connect your storage provider in the RudderStack dashboard.


### 3\. Store event data in RudderStack cloud storage

Choosing this option allows RudderStack to store and delete your event data on a rolling 7-day basis. **This is the default setting.**

[![Store in RudderStack cloud storage.](/docs/images/dashboard-guides/rs-cloud-storage-7-day.webp)](</docs/images/dashboard-guides/rs-cloud-storage-7-day.webp>)

If you are on the [Enterprise](<https://rudderstack.com/enterprise-quote>) plan, RudderStack lets you store and delete your event data on a rolling 30-day basis.

[![Store in RudderStack cloud storage.](/docs/images/dashboard-guides/rs-cloud-storage-30-day.webp)](</docs/images/dashboard-guides/rs-cloud-storage-30-day.webp>)

## Sample event data

When the **Sample event data** setting is enabled, RudderStack stores and deletes sample events and responses on a rolling 30-day basis. This data may be helpful for debugging your events.

> ![info](/docs/images/info.svg)
> 
> RudderStack **does not** consider the event name or event type to be Personally Identifiable Information (PII).

[![Opt in to sample event data storage.](/docs/images/dashboard-guides/sample-event-data.webp)](</docs/images/dashboard-guides/sample-event-data.webp>)

## Plan-based retention options

Based on your plan, RudderStack provides different options for event storage, giving you the ability to enable or disable retention for the following kinds of data:

  * **Sample events and responses** : As mentioned above, RudderStack will store and delete sample events and responses on a rolling 30-day basis.
  * **Raw event data** : Events sent to RudderStack, including gateway dumps.


Refer to the below table for the storage items supported by different [RudderStack pricing plans](<https://www.rudderstack.com/pricing/>):

Data type| Free| Starter/Growth| Enterprise  
---|---|---|---  
Sample events/responses|  __| __| __  
Raw event data|  __| 

  * No data storage
  * Connect your own cloud storage
  * RudderStack 7-day storage (default)

| 

  * No data storage
  * Connect your own cloud storage
  * RudderStack 7-day storage (default)
  * RudderStack 30-day storage

  
  
## Data governance

To enable the Event Audit API in the RudderStack dashboard:

  1. Go to **Settings** > **Workspace** and click the **Data Management** tab.
  2. Scroll down to the **Data governance** section and toggle on the **Event audit API** setting.


> ![warning](/docs/images/warning.svg)
> 
> Only [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have the access to this setting.

[![Event Audit API setting in RudderStack dashboard](/docs/images/api/event-audit-api-dashboard.webp)](</docs/images/api/event-audit-api-dashboard.webp>)

When this setting is turned on, you can leverage the Event Audit API to create and manage your [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>). Use these plans to monitor and act on any non-compliant data coming into your RudderStack sources based on predefined rules.

See [Event Audit API](<https://www.rudderstack.com/docs/api/event-audit-api/>) for more information.

## Limit access to PII

See the following sections for information on limiting access to PII-related features depending on whether you are using the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>) or the new [Access Management](<https://www.rudderstack.com/docs/access-management/overview/>) system:

  * **Legacy Permissions Management (RBAC)** : See [Permissions Management](<https://www.rudderstack.com/docs/archive/dashboard-guides/permissions-management/>)
  * **Access Management (PBAC)** : See [PII Permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#pii-permissions>)