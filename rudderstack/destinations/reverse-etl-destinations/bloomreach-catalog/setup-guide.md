# Setup Guide Beta

Set up and configure Bloomreach Catalog as a destination in RudderStack.

* * *

  * __less than a minute

  * 


This guide will help you set up Bloomreach Catalog as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Bloomreach Catalog.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>).
  2. In the **Overview** tab of the source, click **Add Destination** > **Create New Destination**.

[![](/docs/images/reverse-etl-destinations/retl-add-destination.webp)](</docs/images/reverse-etl-destinations/retl-add-destination.webp>)

  3. From the list of destinations, select **Bloomreach Catalog** and click **Continue**.


### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination.  
API Base URL| Enter your Bloomreach instance URL found under **Project settings** > **Access management** > **API** in your Bloomreach dashboard.  
API Key| Enter the [Bloomreach API key](<https://documentation.bloomreach.com/engagement/reference/authentication#private-api-access>).  
API Secret| Enter the [Bloomreach API secret](<https://documentation.bloomreach.com/engagement/reference/authentication#private-api-access>).  
Project Token| Enter the [project token](<https://documentation.bloomreach.com/engagement/docs/project-settings-2#project---general>) for your project under the Bloomreach instance. You can find it under the **Project settings** > **Access management** > **API** in your Bloomreach dashboard.  
Catalog ID| Enter the Bloomreach catalog ID that RudderStack uses for syncing your catalog data.  
  
## Next steps

  * [Set up Reverse ETL connection](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/bloomreach-catalog/connect-retl-source/>)


## FAQ

#### Where can I find the Bloomreach catalog ID?

  1. Log in to your Bloomreach dashboard.
  2. Go to **Data & Assets** > **Catalogs** and select your catalog.
  3. Note the catalog ID present in the resulting browser URL, as shown:

[![](/docs/images/reverse-etl-destinations/bloomreach-catalog-id.webp)](</docs/images/reverse-etl-destinations/bloomreach-catalog-id.webp>)