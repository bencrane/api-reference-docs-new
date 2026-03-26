# Mailchimp Cloud Extract Source Deprecated

Sync data from Mailchimp to your warehouse destination via RudderStack.

* * *

  * __3 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> This source is deprecated and no longer supported as of **January 10, 2026**.

[Mailchimp](<https://mailchimp.com/>) is a popular email marketing automation platform used worldwide by thousands of businesses. Built specially for eCommerce and retail, Mailchimp allows you to build your audience and send them personalized campaign and marketing messages through web or mobile.

This document guides you in setting up Mailchimp as a source in RudderStack. Once configured, RudderStack automatically ingests your specified Mailchimp data, which can then be routed to your data warehouse destination supported by RudderStack.

> ![info](/docs/images/info.svg)
> 
> All Cloud Extract sources support sending data only to a [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

## Getting Started

To set up Mailchimp as a source on the RudderStack dashboard, follow these steps:

  * Log into your [RudderStack dashboard](<https://app.rudderlabs.com/signup?type=freetrial>).

[![RudderStack Dashboard](/docs/images/1%20%2815%29%20%281%29.webp)](</docs/images/1%20%2815%29%20%281%29.webp>)

  * Then, click the **Directory** option on the left navigation bar and go to **Cloud Extract** under **Sources**.

[![Directory](/docs/images/2%20%2820%29.webp)](</docs/images/2%20%2820%29.webp>)

  * From the list of sources, click **Mailchimp**.
  * Assign a name to your source, and click **Next**.

[![Mailchimp](/docs/images/3%20%2818%29.webp)](</docs/images/3%20%2818%29.webp>)

### Specifying Connection Credentials

  * Next, click the **Connect with Mailchimp** option:

[![Connect with Mailchimp](/docs/images/4%20%2817%29.webp)](</docs/images/4%20%2817%29.webp>)

> ![info](/docs/images/info.svg)
> 
> If you’ve already configured Mailchimp as a source before, you can choose the account visible under the **Use existing credentials** tab.

  * Authorize RudderStack to access your Mailchimp account:

[![Authorize RudderStack](/docs/images/5%20%2818%29.webp)](</docs/images/5%20%2818%29.webp>)

### Configuring the Mailchimp Source

  * Select the **Earliest campaign year** and the **Campaign fetch period** in the settings. The details are as follows:
    * **Earliest campaign year** : The first import will fetch all campaign data since the start of the specified year.
    * **Campaign fetch period** : All the subsequent imports will fetch the campaign data up to this specified period.

[![Earliest Campaign Year](/docs/images/6%20%2816%29.webp)](</docs/images/6%20%2816%29.webp>)

### Setting the Table Prefix, Run Frequency and Data Update Schedule

  * Next, you will be required to set the **Table Prefix**. RudderStack will create a table with this prefix name in your database and load all your Mailchimp data into it.
  * Also, set the **Run Frequency** to schedule the data import from your Mailchimp account to RudderStack. Optionally, you can also specify the time when you want this synchronization to start, by choosing the time under the **Sync Starting At** option.

[![Google Analytics](/docs/images/7%20%2811%29.webp)](</docs/images/7%20%2811%29.webp>)

### Selecting the Data to Import

  * Finally, choose the Mailchimp data that you wish to ingest via RudderStack. You can either select all data, or choose specific Mailchimp attributes, as per your requirement.

[![Ingest via RudderStack](/docs/images/8%20%285%29.webp)](</docs/images/8%20%285%29.webp>)

That’s it! Mailchimp is now successfully configured as a source on your RudderStack dashboard.

RudderStack will start ingesting data from Mailchimp as per the specified frequency. You can further connect this source to your data warehouse by clicking on **Connect Destinations** or **Add Destinations** :

[![Add Destinations](/docs/images/9%20%283%29.webp)](</docs/images/9%20%283%29.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use the **Connect Destinations** option if you have already configured a data warehouse destination in RudderStack. To configure a data warehouse destination from scratch, click the **Add Destination** button.

## FAQ

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

We have implemented a feature wherein RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### How does RudderStack set the table name for the data sent via Cloud Extract sources?

RudderStack sets the table name for the resource you are syncing to the warehouse by adding `rudder_` to the **Table prefix** you set while configuring your Cloud Extract source in the dashboard.

[![Cloud Extract table prefix](/docs/images/cloud-extract-sources/etl-table-prefix.webp)](</docs/images/cloud-extract-sources/etl-table-prefix.webp>)

For example, if you set `test_` as the **Table prefix** in the dashboard, RudderStack sets the table name as `test_rudder_<resource_name>`, where `<resource_name>` is the name of the resource you are syncing (for example, `contacts`, `messages`, etc.).

> ![warning](/docs/images/warning.svg)
> 
> Note that RudderStack does not add the character `_` to the prefix by default. Hence, you need to specify it while setting the prefix.