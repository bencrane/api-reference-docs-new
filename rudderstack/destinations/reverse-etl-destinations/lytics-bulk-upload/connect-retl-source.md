# Connect Reverse ETL Source to Lytics Bulk Upload Beta

Configure a Reverse ETL source with your Lytics Bulk Upload destination.

* * *

  * __less than a minute

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Lytics Bulk Upload destination.

## Set up connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Lytics Bulk Upload destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/lytics-bulk-upload/setup-guide/#connection-settings>) for Lytics Bulk Upload destination and click **Continue**.

  2. In the **Data Mapping** section, specify the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>). RudderStack supports syncing to this destination only via the **Upsert** mode.

  3. Select `track` event type to send the event data to downstream destinations.


> ![info](/docs/images/info.svg)
> 
> RudderStack uses the [BulkCSVUpload Lytics API endpoint](<https://docs.lytics.com/reference/bulkcsvupload>) to send `track` calls to Lytics.

  4. In **Choose identifier** , choose at least one user identifier from `user_id` and `anonymous_id` from the dropdown.


Refer [Mapping configuration](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/json-data-mapping/#mapping-configuration>) section for more information on above settings.

## Next steps

  * [Configure advanced settings for Lytics Bulk Upload destination](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/lytics-bulk-upload/configuration-settings/>)


## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.