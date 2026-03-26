# Connect Reverse ETL Source to Amazon Audience

Configure a Reverse ETL source with your Amazon Audience destination.

* * *

  * __less than a minute

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Amazon Audience destination.

## Set up the connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Amazon destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/amazon-audience/setup-guide/#connection-settings>) for Amazon Audience and click **Continue**.
  2. In the [Data Mapping](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) section, select **Create New Audience** or **Use Existing Audience** in the **Where do you want to sync data to?** section.
  3. RudderStack supports only [Mirror mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>) for this integration.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.
  5. Map your warehouse columns to specific Amazon fields using the **Map fields** setting and click **Continue**.

[![](/docs/images/event-stream-destinations/amazon-identifier-map-fields.webp)](</docs/images/event-stream-destinations/amazon-identifier-map-fields.webp>)

## Next steps

  * [Configure advanced settings for Amazon Audience destination](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/amazon-audience/configuration-settings/>)


## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.