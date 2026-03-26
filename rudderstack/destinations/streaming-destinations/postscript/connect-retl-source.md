# Connect Reverse ETL Source to PostScript Beta

Configure a Reverse ETL source with your PostScript destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the PostScript destination.

> ![info](/docs/images/info.svg)
> 
> This destination supports mapping data only via the [JSON Mapper](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/json-data-mapping/>).
> 
> Mapping via [Visual Data Mapper](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) is not supported for this destination.

## Set up the connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your PostScript destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/postscript/setup-guide/#connection-settings>) for PostScript destination and click **Continue**.
  2. Set the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to PostScript.
  3. Choose the **Event Type** — RudderStack supports sending data to PostScript as **Identify** or **Track** events.
  4. In **Choose identifier** , specify the **User ID** and **Anonymous ID** from the dropdown. RudderStack uses these identifiers to identify your records.


You will see the snippet of your data in the resulting preview — you can select and edit the columns you want to send to PostScript.

[![PostScript JSON mapper preview](/docs/images/event-stream-destinations/postscript-json-mapper-preview.webp)](</docs/images/event-stream-destinations/postscript-json-mapper-preview.webp>)

  5. Specify the [Sync Schedule Settings](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>) to specify how and when RudderStack should sync the data to PostScript.
  6. Specify the [Sync Observability Settings](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-observability/#sync-settings>) to specify how RudderStack retains the sync logs and tables, and retries any failed records for this connection.


## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.