# Setup Guide Beta

Send your event data from RudderStack to LinkedIn Audience.

* * *

  * __less than a minute

  * 


This guide will help you set up LinkedIn Audience as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to LinkedIn Audience.

## Setup

  1. Set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in the RudderStack dashboard.
  2. In the **Overview** tab, click **Add destination** > **Create new destination**.

[![Connect new destination to Reverse ETL source](/docs/images/reverse-etl-destinations/add-destination.webp)](</docs/images/reverse-etl-destinations/add-destination.webp>)

  3. From the list of destinations, search for **LinkedIn Audience** and click **Continue**.


### Connection settings

Setting| Description  
---|---  
Name| Specify a unique name to identify the destination in RudderStack.  
oAuth settings| 

  1. Click **Create Account** > **Connect with LinkedIn Audience** and give RudderStack the required permissions to access your LinkedIn Ads account.
  2. Select the account and click **Save**.

  
  
> ![info](/docs/images/info.svg)
> 
> **Why do I see a request for Conversions API permissions while authorizing RudderStack?**
> 
> Since the [LinkedIn Ads](<https://www.rudderstack.com/docs/destinations/streaming-destinations/linkedin-ads/>) and LinkedIn Audience destination integrations share a common OAuth app in the backend, RudderStack requests all the necessary permissions needed for both integrations to work correctly.
> 
> RudderStack will **not** make any Conversions API-related calls when sending data to your LinkedIn Audience destination.

## Next steps

  * [Connect Reverse ETL source to LinkedIn Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/linkedin-audience/connect-retl-source/>)