# Connect Reverse ETL Source to Eloqua Beta

Configure a Reverse ETL source with your Eloqua destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Eloqua destination.

## Set up the connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Eloqua destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/eloqua/setup-guide/#connection-settings>) for Eloqua destination and click **Continue**.


> ![info](/docs/images/info.svg)
> 
> To sync the data successfully, make sure to enter the **Company Name** , **Username** , and **Password** while configuring your Eloqua destination.

  2. In the **Where do you want to sync data to?** section, select the **Object**.


> ![info](/docs/images/info.svg)
> 
> RudderStack supports two main object types - [contacts](<https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/Contacts/Contacts.htm>) and [custom objects](<https://docs.oracle.com/en/cloud/saas/marketing/eloqua-user/Help/CustomObjects/CustomObjects.htm>). The first option in the dropdown is **Contact**. The rest are the custom objects you have set up in your Eloqua account.

[![](/docs/images/event-stream-destinations/eloqua-object-type.webp)](</docs/images/event-stream-destinations/eloqua-object-type.webp>)

  3. Set the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to Eloqua.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.
  5. Map your warehouse columns to specific Eloqua fields using the **Map fields** setting.

[![](/docs/images/event-stream-destinations/eloqua-identifier-map-fields.webp)](</docs/images/event-stream-destinations/eloqua-identifier-map-fields.webp>)

## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.

#### How do I view the synced data in Eloqua?

Follow these steps to view the synced data for **custom objects** in Eloqua:

  1. Log in to your [Eloqua dashboard](<https://login.eloqua.com>).
  2. From the top navigation bar, go to the contact card and select **Custom Objects**.

[![Custom objects option in Eloqua dashboard](/docs/images/event-stream-destinations/view-synced-data-eloqua-1.webp)](</docs/images/event-stream-destinations/view-synced-data-eloqua-1.webp>)

  3. Select **Custom Object Record Reporting**.

[![Custom object reporting option](/docs/images/event-stream-destinations/view-synced-data-eloqua-2.webp)](</docs/images/event-stream-destinations/view-synced-data-eloqua-2.webp>)

  4. Choose your custom object from the list and click **Select**.

[![Select custom object](/docs/images/event-stream-destinations/view-synced-data-eloqua-3.webp)](</docs/images/event-stream-destinations/view-synced-data-eloqua-3.webp>)

You should see all the data synced from your RudderStack Reverse ETL source to the custom object in the resulting view.

[![View reporting data for custom object](/docs/images/event-stream-destinations/view-synced-data-eloqua-4.webp)](</docs/images/event-stream-destinations/view-synced-data-eloqua-4.webp>)

To view the synced data for your contacts, select **Contacts** from the top navigation bar (Step 2) and search with any identifier.

[![View reporting data for contact](/docs/images/event-stream-destinations/view-synced-data-eloqua-5.webp)](</docs/images/event-stream-destinations/view-synced-data-eloqua-5.webp>)