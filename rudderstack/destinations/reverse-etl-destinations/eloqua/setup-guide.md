# Setup Guide Beta

Send your event data from RudderStack to Eloqua.

* * *

  * __less than a minute

  * 


This guide will help you set up Eloqua as a destination in RudderStack when connecting to a [Reverse ETL source](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/eloqua/connect-retl-source/>).

> ![info](/docs/images/info.svg)
> 
> This guide assumes you have already set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in RudderStack.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Eloqua**.

### Connection settings

To successfully configure Eloqua as a destination, you need to configure the following settings:

  * **Name** : Specify a unique name to identify the destination in RudderStack.
  * **Company Name** : Enter the company name used to [log in to Eloqua](<https://login.eloqua.com>).
  * **Username** : Enter the username used to log in to Eloqua.
  * **Password** : Enter the corresponding password.


## Sync data to custom Eloqua objects

RudderStack syncs all the data from your Reverse ETL source to your [contacts](<https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/op-api-rest-1.0-data-contact-post.html>) or [custom objects](<https://docs.oracle.com/en/cloud/saas/marketing/eloqua-rest-api/op-api-rest-2.0-data-customobject-parentid-instance-post.html>) in Eloqua using their Bulk API.

> ![warning](/docs/images/warning.svg)
> 
> Before syncing the data, make sure to [create a custom object](<https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/CustomObjects/Tasks/CreatingCustomObjects.htm>) in your Eloqua account.