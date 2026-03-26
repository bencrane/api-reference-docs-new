# Connect Reverse ETL Source to Marketo Static Lists Beta

Configure a Reverse ETL source with your Marketo Static Lists destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Marketo Static Lists destination.

## Set up connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Marketo Static Lists destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/marketo-static-lists/setup-guide/#connection-settings>) for Marketo Static Lists destination and click **Continue**.
  2. In the [Data Mapping](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) section, select **Lead Ids** from the **Object** dropdown.
  3. Set the [sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to **Mirror**. This setting specifies how RudderStack syncs the data to Marketo.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records. You can map this warehouse column to the **Lead Id** destination field.


## Considerations for sending data

Note the following while syncing data from your warehouse to Marketo:

  * The data to be synced to Marketo as the **Lead ID** needs to be an integer or string that can be cast to a number. Otherwise, you will get an error.
  * The lead ID should already be present in Marketo as the Marketo Static Lists destination can only add or remove a lead from the list.


## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.