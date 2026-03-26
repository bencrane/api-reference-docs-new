# Connect Reverse ETL Source to Snapchat Custom Audience

Configure a Reverse ETL source with your Snapchat Custom Audience destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Snapchat Custom Audience destination.

## Set up the connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Snapchat Custom Audience destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/snapchat-custom-audience/setup-guide/#connection-settings>) for your Snapchat Custom Audience destination and click **Continue**.

  2. In the **Where do you want to sync data to?** section, select the **Object**.


[![](/docs/images/event-stream-destinations/snapchat-custom-audience-retl-settings-2.webp)](</docs/images/event-stream-destinations/snapchat-custom-audience-retl-settings-2.webp>)

  3. Set the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to Snapchat Custom Audience.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.


> ![warning](/docs/images/warning.svg)
> 
> Choose the same field that you set as the **Schema** while configuring your Snapchat Custom Audience destination. For more information, see the **Schema** setting in the [Setup guide](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/snapchat-custom-audience/setup-guide/#connection-settings>).

[![](/docs/images/event-stream-destinations/snapchat-custom-audience-identifier.webp)](</docs/images/event-stream-destinations/snapchat-custom-audience-identifier.webp>)

  5. Map your warehouse columns to specific Snapchat Custom Audience fields using the **Map fields** setting.

[![](/docs/images/event-stream-destinations/snapchat-custom-audience-map-fields.webp)](</docs/images/event-stream-destinations/snapchat-custom-audience-map-fields.webp>)

## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.

#### How do I view the synced segments in Snapchat Custom Audience?

  1. Log in to your [Snapchat Ad Manager](<https://ads.snapchat.com/>).
  2. Click **Audiences**.

[![](/docs/images/event-stream-destinations/snapchat-custom-audience-synced-segments-1.webp)](</docs/images/event-stream-destinations/snapchat-custom-audience-synced-segments-1.webp>)

In the resulting view, you can see the audience and number of synced users.

[![](/docs/images/event-stream-destinations/snapchat-custom-audience-synced-segments-2.webp)](</docs/images/event-stream-destinations/snapchat-custom-audience-synced-segments-2.webp>)