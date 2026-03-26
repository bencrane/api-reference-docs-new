# ProfitWell Web Device Mode Integration

Send events to ProfitWell using RudderStack web device mode.

* * *

  * __3 minute read

  * 


RudderStack lets you send your event data to ProfitWell via the web [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), that is, using the native web SDK.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **ProfitWell** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the ProfitWell native SDK from the `https://public.profitwell.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the ProfitWell SDK successfully.

Once you have confirmed that the source platform supports sending events to ProfitWell, follow the steps below:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. From the list of destinations, select **ProfitWell**.
  * Assign a name to the destination, and click **Next**. You will then see the following **Connection Settings** window:

[![Profitwell connection settings](/docs/images/event-stream-destinations/profitwell-connection.webp)](</docs/images/event-stream-destinations/profitwell-connection.webp>)

### Connection Settings

To successfully configure ProfitWell as a Device Mode destination, enter the following connection settings:

  * **Public API Key** : Enter your ProfitWell public API key here. To obtain the **Public API Key** , log into your ProfitWell account. Then, navigate to the **Account Settings** \- **Integration** option. Here, you can get your API key under [API Keys/Dev Kit](<https://www2.profitwell.com/app/account/integrations>), as shown in the following image:

[![Profitwell API key](/docs/images/event-stream-destinations/profitwell-key.webp)](</docs/images/event-stream-destinations/profitwell-key.webp>)

> ![info](/docs/images/info.svg)
> 
> The **Private API Key** field is **not** required if you want to send the events via device mode.

  * **Site Type** : Choose the site type from the dropdown. If the site type is **Web App** , then RudderStack will start the ProfitWell service either with `email` or `userId`. For the type **Marketing** , RudderStack will start the ProfitWell service anonymously.
  * **Use device-mode to send events** : Enable this option to send events via the web [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).


> ![warning](/docs/images/warning.svg)
> 
> The **Private API Key** field is **not** required if you want to send the events via device mode.

  * Finally, click **Next** to complete the setup. ProfitWell should now be configured and enabled as a destination in RudderStack.


## Identify

For the **Web App** site type, the `identify` call will start the ProfitWell Service using the customer’s `email`. If no email is provided, then RudderStack will start the service with the user’s `userId`. For the **Marketing** type, RudderStack will start the ProfitWell service anonymously.

A sample `identify` call is as shown:
    
    
      rudderanalytics.identify( "userId", {email: "sample@domain.com"});
    

For the `identify` call to trigger user engagements, you need to first create [Customers](<https://www2.profitwell.com/app/customers>) within ProfitWell.