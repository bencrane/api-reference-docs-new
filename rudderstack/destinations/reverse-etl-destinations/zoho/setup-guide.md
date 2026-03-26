# Setup Guide Beta

Send your event data from RudderStack to Zoho.

* * *

  * __less than a minute

  * 


This guide will help you set up Zoho as a destination in RudderStack when connecting to a [Reverse ETL source](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/connect-retl-source/>).

> ![info](/docs/images/info.svg)
> 
> This guide assumes you have already set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in RudderStack.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Warehouse
  * Refer to it as **ZOHO** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a Reverse ETL source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.
  3. Select **Zoho** from the list of destinations. Then, click **Continue**.


### Connection settings

Setting| Description  
---|---  
Name| Specify a name to uniquely identify the destination in RudderStack.  
oAuth settings| Click **Create Account** > **Connect with Zoho** and give RudderStack the required permissions to access your Zoho account. You can add multiple accounts and choose any one to proceed with the setup.  
Data Center Region| Select your Zoho data center region from the dropdown.  
  
## Next steps

  * [Connect your Reverse ETL source to Zoho](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/zoho/connect-retl-source/>)