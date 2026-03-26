# Connect Reverse ETL Source to SFTP Destination Beta

Configure a Reverse ETL source with your SFTP destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the SFTP destination.

## Set up connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your SFTP destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/sftp/setup-guide/#connection-settings>) for SFTP destination and click **Continue**.
  2. In the [Data Mapping](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) section, select the **Object**.
  3. Specify the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to SFTP.
  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.
  5. Map the other warehouse columns to specific SFTP destination fields using the **Map fields** setting.

[![Map fields in SFTP destination](/docs/images/event-stream-destinations/sftp-map-fields.webp)](</docs/images/event-stream-destinations/sftp-map-fields.webp>)

  6. To create a new destination field and map it to a warehouse column, click **Map another field** and specify the name of the new field.


> ![success](/docs/images/tick.svg)
> 
> The newly created fields are stored in the SFTP destination for later use once you click **Continue**.

[![Create new mappings for SFTP destination](/docs/images/event-stream-destinations/sftp-create-field.webp)](</docs/images/event-stream-destinations/sftp-create-field.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Once you set up the connection and start a sync, RudderStack takes up to 5 minutes to upload data to SFTP.

## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.