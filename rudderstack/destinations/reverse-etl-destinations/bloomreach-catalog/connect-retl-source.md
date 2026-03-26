# Connect Reverse ETL Source to Bloomreach Catalog Beta

Configure a Reverse ETL source with your Bloomreach Catalog destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Bloomreach Catalog destination and specify the data mappings correctly.

> ![info](/docs/images/info.svg)
> 
> See the [Bloomreach](<https://www.rudderstack.com/docs/destinations/streaming-destinations/bloomreach/>) destination documentation if you want to sync the customer data from your warehouse to Bloomreach.

## Set up connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your Bloomreach Catalog destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/bloomreach-catalog/setup-guide/#connection-settings>) for your Bloomreach Catalog destination and click **Continue**.
  2. In the **Where do you want to sync data to?** section, select the object **Catalog** from the dropdown.

[![](/docs/images/reverse-etl-destinations/bloomreach-catalog-object.webp)](</docs/images/reverse-etl-destinations/bloomreach-catalog-object.webp>)

  3. RudderStack supports only [Mirror mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>) for this integration.
  4. In **Choose identifier** section, specify the warehouse column that RudderStack uses to identify your records.
  5. Map the other warehouse columns to specific Bloomreach Catalog fields using the **Map fields** setting.

[![](/docs/images/reverse-etl-destinations/bloomreach-catalog-identifier-map-fields.webp)](</docs/images/reverse-etl-destinations/bloomreach-catalog-identifier-map-fields.webp>)

  6. To create a new destination field and map it to a warehouse column, click **Map another field** and type the name of the new field you want to create. Then, select the warehouse column to map to this field.


> ![success](/docs/images/tick.svg)
> 
> The newly created fields are stored in Bloomreach for later use once you click **Continue**.

[![](/docs/images/reverse-etl-destinations/bloomreach-new-field.webp)](</docs/images/reverse-etl-destinations/bloomreach-new-field.webp>)

## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.