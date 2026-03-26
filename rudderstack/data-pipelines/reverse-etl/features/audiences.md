# Audiences

Build audiences on the warehouse sources and activate them in downstream destinations.

Available Plans

  * growth
  * enterprise


* * *

  *  __5 minute read

  * 


RudderStack’s **Audiences** feature lets you create target customer lists or a subset of users satisfying specific criteria with easy-to-use filters on your warehouse tables. Once created, you can connect and activate them in the supported destinations.

For example, you can create an audience and send that data to the downstream digital advertising destinations to:

  * Retarget all users from a specific city/state/region to improve repeat sales.
  * Prompt active customers on your sports website to buy season tickets.
  * Run campaigns to grow product usage and retain users.


## Key features

RudderStack provides audience-building capabilities in its Reverse ETL pipeline where you can:

  * Create and sync a single audience to multiple downstream systems, which is very time-consuming to do manually.
  * Analyze the results of multichannel campaigns in a single place at the data warehouse.
  * Trust the audience data as a single source of truth and have complete control over the ecosystem.
  * Fast-track the process for marketing teams who would otherwise need to work with SQL and warehouses or rely on data engineers to query and sync audiences.
  * Avoid updating the audience every time or debugging issues while building audiences using proprietary tools, saving time.


## Create audience

RudderStack provides a visual **Audience builder tool** which you can use to build audiences without any prior knowledge of SQL or how to store the data.

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com>).
  2. From the left navigation bar, go to **Activate** > **Audiences** and click **New audience**.
  3. Configure the settings explained in the following sections:


### Select source

Select the warehouse source for which you want to create an audience. RudderStack supports the Audiences feature for the following sources:

  * [BigQuery](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/>)
  * [Databricks](<https://www.rudderstack.com/docs/sources/reverse-etl/databricks/>)
  * [Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/>)
  * [Snowflake](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/>)
  * [Trino](<https://www.rudderstack.com/docs/sources/reverse-etl/trino/>)


### Specify warehouse credentials

Specify the warehouse credentials to authenticate RudderStack. See the **Configure warehouse credentials** section of the [source-specific documentation](<https://www.rudderstack.com/docs/sources/reverse-etl/#supported-reverse-etl-sources>) (for example, [Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/#configuring-the-connection-credentials>)) for more details.

### Specify audience name and source

  * **Source name** : Assign a name to uniquely identify the source in the RudderStack dashboard.

  * Configure your audience source by specifying the below fields:

    * **Schema** : Select the warehouse schema from the dropdown.
    * **Table** : Choose the required table from which RudderStack syncs the data.
    * **Primary key** : Select the column from the above table that uniquely identify your records in the warehouse.


### Set audience conditions

You can set the required filtering conditions, view the corresponding SQL query and preview the resultant data from your data filters:

[![Set conditions in audience](/docs/images/warehouse-actions-sources/set-condition-audience.gif)](</docs/images/warehouse-actions-sources/set-condition-audience.gif>)

You can add multiple filters within a condition by clicking **Add condition** or add multiple group filters by clicking **Add group condition**. Select **All** or **Any** to implement the AND or OR operator respectively between different filtering conditions.

[![AND/OR conditions in audience](/docs/images/warehouse-actions-sources/and-or-condition-audience.webp)](</docs/images/warehouse-actions-sources/and-or-condition-audience.webp>)

Click **Preview** to see the results and verify if the audience conditions are correct. Click **Continue** to proceed.

### Review and complete setup

To make any changes to the warehouse credentials or audience configuration, click the edit icon present next to those sections.

[![Edit audience configuration](/docs/images/data-pipelines/edit-audience-configuration.webp)](</docs/images/data-pipelines/edit-audience-configuration.webp>)

Once you have reviewed your configuration, click **Create source** to complete the setup.

### Connect audience to destination

To start using the newly-created source, you can connect it to:

  * A new [destination](<https://www.rudderstack.com/docs/destinations/overview/>), or
  * An existing destination that is **not already connected** to any other source.


To connect to a destination later, click **Done** on the top right:

[![Next steps](/docs/images/retl-sources/created-source.webp)](</docs/images/retl-sources/created-source.webp>)

You will then be redirected to the **Overview** page of the source where you will see the option of connecting it to a new or existing destination.

[![Add destination](/docs/images/retl-sources/add-destination.webp)](</docs/images/retl-sources/add-destination.webp>)

See [Set up Reverse ETL Connection](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/retl-connection-setup/>) section for more information.

## Update audience

  1. Go to the **Configuration** tab of the audience source.
  2. Click the edit icon in the **Configuration settings** to update the source configuration and audience description


> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You can update the **Schema** and **Table** fields only if your audience source is **not** connected to any destination. Otherwise, you can only update the **Primary key** and **Description**.
>   * Your audience conditions will be reset if you change the warehouse schema or table.
> 


[![Update audience](/docs/images/data-pipelines/update-audience-1.webp)](</docs/images/data-pipelines/update-audience-1.webp>)

To update the audience conditions, click the **Edit conditions** button and update the conditions. Make sure to preview the data before saving the updated conditions.

[![Update audience conditions](/docs/images/data-pipelines/update-audience-2.webp)](</docs/images/data-pipelines/update-audience-2.webp>)

## Audience identifier

RudderStack requires an audience identifier when mapping your audience to destinations that don’t support audiences by default, for example, Salesforce, Customer.io, HubSpot, etc. It picks up this identifier from the **Audience identifier** setting in the dashboard while setting up the data mapping.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You will see the **Audience identifier** setting while connecting your audience to all the supported destinations **except** Facebook Custom Audience and Google Ads Remarketing Lists, which have audience support by default.
>   * The value of **Audience identifier** is pre-populated in the dashboard. However, you can change it as required.
> 


[![Audience identifier](/docs/images/warehouse-actions-sources/audience-identifier.webp)](</docs/images/warehouse-actions-sources/audience-identifier.webp>)

RudderStack sets the user traits with the provided **Audience identifier** as the key. It sets the value of the trait to either `true` or `false` depending on whether the user is a member of the defined audience.

## Supported destinations

You can connect an audience to the following destinations:

  * [ActiveCampaign](</docs/destinations/streaming-destinations/activecampaign/>)
  * [Amazon Audience](</docs/destinations/reverse-etl-destinations/amazon-audience/>)
  * [Bing Ads Audience](</docs/destinations/reverse-etl-destinations/bing-ads-audience/>)
  * [Braze](</docs/destinations/streaming-destinations/braze/>)
  * [Criteo Audience](</docs/destinations/reverse-etl-destinations/criteo-audience/>)
  * [Customer.io](</docs/destinations/streaming-destinations/customer.io/>)
  * [Customer.io Audience](</docs/destinations/reverse-etl-destinations/customerio-audience/>)
  * [Facebook Custom Audience](</docs/destinations/reverse-etl-destinations/facebook-custom-audience/>)
  * [Google Ads Remarketing Lists (Customer Match)](</docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/>)
  * [Heap.io](</docs/destinations/streaming-destinations/heap.io/>)
  * [HubSpot](</docs/destinations/streaming-destinations/hubspot/>)
  * [Intercom](</docs/destinations/streaming-destinations/intercom/>)
  * [Iterable](</docs/destinations/streaming-destinations/iterable/>)
  * [Klaviyo](</docs/destinations/streaming-destinations/klaviyo/>)
  * [LaunchDarkly Segments](</docs/destinations/reverse-etl-destinations/launchdarkly-segments/>)
  * [Linkedin Audience](</docs/destinations/reverse-etl-destinations/linkedin-audience/>)
  * [Marketo](</docs/destinations/streaming-destinations/marketo/>)
  * [Marketo Static Lists](</docs/destinations/reverse-etl-destinations/marketo-static-lists/>)
  * [Salesforce](</docs/destinations/streaming-destinations/salesforce/>)
  * [SendGrid](</docs/destinations/streaming-destinations/sendgrid/>)
  * [Snapchat Custom Audience](</docs/destinations/reverse-etl-destinations/snapchat-custom-audience/>)
  * [The Trade Desk Audience](</docs/destinations/reverse-etl-destinations/trade-desk-audience/>)
  * [TikTok Audiences](</docs/destinations/reverse-etl-destinations/tiktok-audiences/>)
  * [X Audience](</docs/destinations/reverse-etl-destinations/x-audience/>)
  * [HTTP Webhook](</docs/destinations/http-webhook/>)


## FAQ

#### Can I create a filter on the JSON columns in my warehouse table?

Yes, you can. Select the **Custom SQL filter** option from the dropdown and enter the corresponding SQL query, which includes the relevant filtering condition for the JSON column:

[![Connect audience](/docs/images/warehouse-actions-sources/custom-sql-filter.webp)](</docs/images/warehouse-actions-sources/custom-sql-filter.webp>)

#### **What do the three validations under Verifying Credentials imply?**

Once you proceed after entering the connection credentials, you will see the following validations under the **Verifying Credentials** option:

[![Validating credentials](/docs/images/retl-sources/retl-credentials-validate.webp)](</docs/images/retl-sources/retl-credentials-validate.webp>)

These options are explained below:

  * **Verifying Connection** : Indicates that RudderStack is trying to connect to the warehouse with the information specified in the connection credentials.


> ![warning](/docs/images/warning.svg)
> 
> If this option gives an error, it means that one or more fields specified in the connection credentials are incorrect. Verify your credentials in this case.

  * **Able to List Schema** : Checks if RudderStack is able to fetch all schema details using the provided credentials.

  * **Able to Access RudderStack Schema** : Checks if RudderStack has the required access to the `_RUDDERSTACK` / `_rudderstack` schema (depending on your warehouse). To create the schema, run all commands listed in the **Permissions** section of the respective Reverse ETL source documentation:

    * [BigQuery](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/#granting-permissions>)
    * [Databricks](<https://www.rudderstack.com/docs/sources/reverse-etl/databricks/#granting-permissions>)
    * [PostgreSQL](<https://www.rudderstack.com/docs/sources/reverse-etl/postgresql/#granting-permissions>)
    * [Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/#granting-permissions>)
    * [Snowflake](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/#granting-permissions>)
    * [Trino](<https://www.rudderstack.com/docs/sources/reverse-etl/trino/#granting-permissions>)


> ![warning](/docs/images/warning.svg)
> 
> If this option gives an error, verify if you have successfully created the `_RUDDERSTACK` / `_rudderstack` schema and given RudderStack the required permissions to access it.