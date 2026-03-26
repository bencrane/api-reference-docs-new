# Connect Reverse ETL Source to Klaviyo Bulk Upload Beta

Configure a Reverse ETL source with your Klaviyo Bulk Upload destination.

* * *

  * __less than a minute

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Klaviyo Bulk Upload destination.

## Set up connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Klaviyo Bulk Upload destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/klaviyo-bulk-upload/setup-guide/#connection-settings>) for Klaviyo Bulk Upload destination and click **Continue**.

  2. In the [Data Mapping](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) section, select the **Object** as **User Profiles** .

  3. Specify the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>). RudderStack supports syncing to this destination only via the **Upsert** mode.

  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.


[![](/docs/images/event-stream-destinations/klaviyo-bulk-upload-2.webp)](</docs/images/event-stream-destinations/klaviyo-bulk-upload-2.webp>)

> ![info](/docs/images/info.svg)
> 
> You can map this warehouse column either to the **User ID** , **ID** , or **Email** Klaviyo fields.

  5. Map the other warehouse columns to specific Klaviyo Bulk Upload fields using the **Map fields** setting.

[![](/docs/images/event-stream-destinations/klaviyo-bulk-upload-1.webp)](</docs/images/event-stream-destinations/klaviyo-bulk-upload-1.webp>)

## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.