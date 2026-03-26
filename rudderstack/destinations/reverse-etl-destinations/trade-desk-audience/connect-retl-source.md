# Connect Reverse ETL Source to The Trade Desk Audience Beta

Configure a Reverse ETL source with your The Trade Desk Audience destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the The Trade Desk Audience destination. Once set up, you can sync your first-party data from the warehouse to The Trade Desk data segments.

## Set up the connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your The Trade Desk Audience destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/trade-desk-audience/setup-guide/#connection-settings>) for The Trade Desk Audience destination and click **Continue**.

  2. In the **Where do you want to sync data to?** section:

     * Select **Create New audience** if you want to create a new data segment in The Trade Desk Audience. Specify the name and description of the data segment in the respective fields.
[![](/docs/images/event-stream-destinations/fb-custom-audience-new.webp)](</docs/images/event-stream-destinations/fb-custom-audience-new.webp>)
     * Select **Use Existing Audience** if you have an existing data segment in The Trade Desk Audience and specify the segment name under **Audience ID**.
[![](/docs/images/event-stream-destinations/fb-custom-audience-existing.webp)](</docs/images/event-stream-destinations/fb-custom-audience-existing.webp>)
  3. Set the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to The Trade Desk Audiences.

  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.


[![](/docs/images/event-stream-destinations/trade-desk-1.webp)](</docs/images/event-stream-destinations/trade-desk-1.webp>)

  5. Map your warehouse columns to specific The Trade Desk Audience fields using the **Map fields** setting and click **Continue**.

[![](/docs/images/event-stream-destinations/trade-desk-2.webp)](</docs/images/event-stream-destinations/trade-desk-2.webp>)

If you have selected **Create New audience** option in Step 2, the new audience will be created in the destination with the same **Audience ID** as in the **Schema** tab of the Reverse ETL connection.

[![](/docs/images/retl-sources/audience-id.webp)](</docs/images/retl-sources/audience-id.webp>)

## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.