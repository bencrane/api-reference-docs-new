# Hotjar

Send your event data from RudderStack to Hotjar.

* * *

  * __2 minute read

  * 


[Hotjar](<https://www.hotjar.com/>) is a popular [behavioral analytics](<https://www.rudderstack.com/learn/data-analytics/what-is-behavioral-analytics/>) platform, suitable for marketing teams and product managers to better understand and improve their product. It allows them to understand the behavior of their website’s visitors through heat maps, surveys, and conversion funnels.

RudderStack helps you integrate your website with Hotjar to auto-track your user data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Hotjar** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Hotjar native SDK from the`https://static.hotjar.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Hotjar SDK successfully.

## Get started

Once you have confirmed that Hotjar supports the source, perform the steps below:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, select **Hotjar** from the list of destinations.
  * Assign a name to your destination and click **Next**. You should see the following screen:

[![Hotjar connection settings](/docs/images/event-stream-destinations/hotjar-connection-settings.webp)](</docs/images/event-stream-destinations/hotjar-connection-settings.webp>)

### Connection settings

To successfully configure Hotjar as a destination in RudderStack, enter the following connection settings:

  * **Site ID** : Enter your Hotjar site ID. You can get your site ID by logging into your Hotjar account and navigating to **Settings** > **Sites & Organizations**.


Finally, click **Next** to complete the configuration. Hotjar will now be added and enabled as a destination in RudderStack.

## Track

The `track` call leverages Hotjar’s [Events API](<https://help.hotjar.com/hc/en-us/articles/4405109971095>) to track specific user actions.

A sample `track` call is as shown below:
    
    
    rudderanalytics.track("custom_event");
    

> ![info](/docs/images/info.svg)
> 
> To use the Hotjar Events API, you must be on Hotjar’s Plus, Business, or Scale plans.

## Identify

The `identify` call lets you pass your user data to Hotjar, sending them as [User Attributes](<https://help.hotjar.com/hc/en-us/articles/4402892526487-What-are-User-Attributes->).

> ![warning](/docs/images/warning.svg)
> 
> Before you start making `identify` calls, make sure that [User Attributes](<https://insights.hotjar.com/settings/user-attributes>) are enabled in your Hotjar dashboard for each site. Refer to this [Hotjar support page](<https://help.hotjar.com/hc/en-us/articles/360033640653-Identify-API-Reference#making_calls_to_identify>) for more information on enabling and disabling User Attributes.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("userId", {
      total_spend: 500
    });