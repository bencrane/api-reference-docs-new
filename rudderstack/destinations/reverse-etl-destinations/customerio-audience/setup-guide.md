# Setup Guide Beta

Send your event data from RudderStack to Customer.io Audience.

* * *

  * __2 minute read

  * 


This guide will help you set up Customer.io Audience as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Customer.io.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Warehouse
  * Refer to it as **Customer.io Audience** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. Set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in the RudderStack dashboard.
  2. In the **Overview** tab, click **Add destination** > **Create new destination**.

[![Connect new destination to Reverse ETL source](/docs/images/reverse-etl-destinations/add-destination.webp)](</docs/images/reverse-etl-destinations/add-destination.webp>)

  3. From the list of destinations, search for **Customer.io Audience** and click **Continue**.


## Connection settings

Configure the following settings to set up Customer.io Audience as a destination in RudderStack:

Setting| Description  
---|---  
Name| Specify a unique name to identify the destination in RudderStack.  
Site ID| Specify your Customer.io site ID by going to **Settings** > **Account Settings** > **API Credentials** > **Track App Keys** > **Site ID** in your Customer.io dashboard.  
API Key| Specify the API key corresponding to the site ID specified above.  
App API Key| Specify your Customer.io app API key by going to **Settings** > **Account Settings** > **API Credentials** > **App API Keys** > **API Key** in your Customer.io dashboard.  
Region| Choose your Customer.io data center from **US** or **EU**.  
  


> ![info](/docs/images/info.svg)RudderStack uses the **US** region by default .  
  
## Next steps

  * [Connect Reverse ETL source to Customer.io Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/customerio-audience/connect-retl-source/>)