# Mixpanel Destination Setup Guide

Set up and configure Mixpanel as a destination in RudderStack.

* * *

  * __10 minute read

  * 


This guide will help you set up Mixpanel as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Mixpanel.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Mixpanel** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> Note that for the web device mode integration, that is, when using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Mixpanel native SDK from the `https://cdn.mxpnl.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Mixpanel SDK successfully.

## Setup

Once you have confirmed that your source platform supports sending events to Mixpanel, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Mixpanel**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

Setting| Description  
---|---  
Project Token| Your [Mixpanel Project Token](<https://developer.mixpanel.com/reference/project-token>).  
Data Residency| Select the relevant option among `US`, `EU`, and `IN` (beta). RudderStack will send your event data to the Mixpanel server in that region.  
Identity Merge| Select either **Original ID Merge** or **Simplified ID Merge** from the dropdown to track user journeys across devices. See the [Mixpanel documentation](<https://help.mixpanel.com/hc/en-us/articles/14383975110292>) for more information on the differences between these APIs.  
  
If you select the **Simplified ID Merge** option, make sure to [turn on the Simplified ID Merge API for your project](<https://help.mixpanel.com/hc/en-us/articles/14383975110292-Original-vs-Simplified-ID-Merge-FAQ#how-do-i-enable-the-simplified-api-on-a-project>) before sending the events.  
  
### Configuration settings

Configure the below settings depending on your specified connection mode to receive the data correctly in Mixpanel.

#### Cloud mode

##### **Page settings**

Setting| Description  
---|---  
Use Custom Page Event Name| Toggle on this setting and specify the template for your `page` event names. RudderStack sets the event names for your `page` calls accordingly.  
  
For example, if you set the template as `Viewed {{category}} {{name}} page` and send the below `page` event payload:  
  

    
    
    {  
      “type”: “page”,  
      “name”: “Home”,  
      “properties”: {  
        “category”: “Integration”  
      }  
    }

Then, RudderStack sends the `page` event name as `Viewed Integration Home Page` to Mixpanel.  
  
Note that:  
  


  * This setting is applicable for cloud mode and device mode.
  * You can skip the page category, name, or both while setting the template. For example, `Viewed {{category}} page`, `Viewed {{name}} page`, `Viewed a page` are all valid.
  * If you include the page category in the template, make sure to send it in the event’s `properties` object.

  
  
##### **Screen settings**

Setting| Description  
---|---  
Use Custom Screen Event Name| Toggle on this setting and specify the template for your `screen` event names. RudderStack sets the event names for your `screen` calls accordingly.  
  
For example, if you set the template as `Viewed {{category}} {{name}} screen` and send the below `screen` event payload:  
  

    
    
    {  
      “type”: “page”,  
      “name”: “Home”,  
      “properties”: {  
        “category”: “Integration”  
      }  
    }

Then, RudderStack sends the `screen` event name as `Viewed Integration Home Page` to Mixpanel.  
  
Note that:  
  


  * This setting is applicable for cloud mode only.
  * You can skip the screen category, name, or both while setting the template. For example, `Viewed {{category}} screen`, `Viewed {{name}} screen`, and `Viewed a screen` are all valid.
  * If you include the screen category in the template, make sure to send it in the event’s `properties` object.

  
  
##### **Track settings**

Setting| Description  
---|---  
Drop Traits| Toggle on this setting to drop the persisted user traits (`context.traits`) from the `track` events. If this toggle is off, RudderStack passes the `context.traits` values along with the other `track` event properties.  
  
##### **Mixpanel configuration settings**

Setting| Description  
---|---  
Strict Mode| If turned on, Mixpanel validates the requests and returns errors for each failed event. See [Mixpanel Import Events API](<https://developer.mixpanel.com/reference/import-events>) for more information.  
Properties to increment in People| See [Increment properties in Mixpanel People](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/cloud-mode/#increment-properties-in-mixpanel-people>) for more information.  
Properties to set only once| Specify the `identify` traits as Mixpanel properties whose values you do not want to change at the user profile level. Once specified, Mixpanel will **not** overwrite these fields with new values later.  
  
See [Properties to set only once](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/cloud-mode/#properties-to-set-only-once>) section for more information.  
Properties for Union| Specify the `identify` traits whose values are added to a list property on a Mixpanel user profile so that they appear **only once**.  
  
See [Properties for union](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/cloud-mode/#properties-for-union>) section for more information.  
Properties for Append| Specify the `identify` traits whose values need to be appended in the list property on a Mixpanel user profile.  
  
See [Properties to append](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/cloud-mode/#properties-to-append>) section for more information.  
  
##### **Event mapping settings**

Setting| Description  
---|---  
Use New Mapping| This option is turned off by default. However, RudderStack **recommends** turning it on as support for the current (old) mapping will be deprecated soon.  
  
When turned off, RudderStack sends the first name and last name to Mixpanel as:  

    
    
    $firstName: “John”  
    $lastName: “Keener”

  
If you toggle on this option, RudderStack maps these fields to Mixpanel as:  

    
    
    $first_name : “John”  
    $last_name : “Keener”

  
**Note** : RudderStack lets you pass empty and `null` values for the properties sent to Mixpanel.  
  
##### **Group key settings**

Setting| Description  
---|---  
Group Key Settings| RudderStack sends the `group` calls to Mixpanel only if one or more group keys are specified here. These group keys act as the group identifiers in Mixpanel. For more information, see [Group Key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/cloud-mode/#group-key>).  
  
##### **User deletion settings**

Setting| Description  
---|---  
User Deletion| Select the deletion API from the following options which RudderStack uses to [delete the user profile](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/cloud-mode/#deleting-a-user>) in Mixpanel.  
  


  * **Delete Profile** : RudderStack deletes the user profile in Mixpanel but not the event data associated with it. For more information, see the [Mixpanel documentation](<https://developer.mixpanel.com/reference/delete-profile>).
  * **Delete Profile and Associated Events** : RudderStack deletes the user profile along with the associated data in Mixpanel. Note that it can take up to 60 days for the deletion to come into effect. For more information, see the [Mixpanel documentation](<https://docs.mixpanel.com/docs/other-bits/privacy-and-security#create-a-deletion-task>).
  * **GDPR API Token** : If you select **Delete Profile and Associated Events** for user deletion, enter the GDPR OAuth token. For more information on generating this token, see the [Mixpanel documentation](<https://docs.mixpanel.com/docs/other-bits/privacy-and-security/export-or-delete-end-user-data#generate-oauth-token>).

  
  
##### **Consent settings**

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
##### **Other settings**

Setting| Description  
---|---  
Client-side Events Filtering| Filter events before sending them to Mixpanel. See the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.  
  
#### Web device mode

##### **Page settings**

Setting| Description  
---|---  
Use Custom Page Event Name| Toggle on this setting and specify the template for your `page` event names. RudderStack sets the event names for your `page` calls accordingly.  
  
For example, if you set the template as `Viewed {{category}} {{name}} page` and send the below `page` event payload:  
  

    
    
    {  
      “type”: “page”,  
      “name”: “Home”,  
      “properties”: {  
        “category”: “Integration”  
      }  
    }

Then, RudderStack sends the `page` event name as `Viewed Integration Home Page` to Mixpanel.  
  
Note that:  
  


  * This setting is applicable for cloud mode and device mode.
  * You can skip the page category, name, or both while setting the template. For example, `Viewed {{category}} page`, `Viewed {{name}} page`, `Viewed a page` are all valid.
  * If you include the page category in the template, make sure to send it in the event’s `properties` object.

  
  
##### **Screen settings**

Setting| Description  
---|---  
Use Custom Screen Event Name| Toggle on this setting and specify the template for your `screen` event names. RudderStack sets the event names for your `screen` calls accordingly.  
  
For example, if you set the template as `Viewed {{category}} {{name}} screen` and send the below `screen` event payload:  
  

    
    
    {  
      “type”: “page”,  
      “name”: “Home”,  
      “properties”: {  
        “category”: “Integration”  
      }  
    }

Then, RudderStack sends the `screen` event name as `Viewed Integration Home Page` to Mixpanel.  
  
Note that:  
  


  * This setting is applicable for cloud mode only.
  * You can skip the screen category, name, or both while setting the template. For example, `Viewed {{category}} screen`, `Viewed {{name}} screen`, and `Viewed a screen` are all valid.
  * If you include the screen category in the template, make sure to send it in the event’s `properties` object.

  
  
##### **Mixpanel configuration settings**

Setting| Description  
---|---  
Properties to increment in People| See [Increment properties in Mixpanel People](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/device-mode/#increment-properties-in-mixpanel-people>) for more information.  
  
##### **Group key settings**

Setting| Description  
---|---  
Group Key Settings| RudderStack sends the `group` calls to Mixpanel only if one or more group keys are specified here. These group keys act as the group identifiers in Mixpanel. For more information, see [Group Key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/cloud-mode/#group-key>).  
  
##### **Web SDK settings**

Setting| Description  
---|---  
Use Mixpanel People| Sends all your `identify` calls to Mixpanel People. See the [Mixpanel People](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/device-mode/#mixpanel-people>) section for more information.  
Automatically set all Traits as Super Properties and People properties| When you turn on this setting, RudderStack sets all the `identify` traits as super properties and people properties if **Use Mixpanel People** setting is turned on. See [Setting People Properties and Super Properties](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/device-mode/#setting-people-properties-and-super-properties>) for more information.  
Ignore “Do Not Track”| If turned on, the native Mixpanel SDK ignores the “Do Not Track” setting of your web browser. This setting is applicable when sending events in web device mode.  
  
The Mixpanel SDK cannot send events if `Send a 'Do Not Track' request with your browsing traffic` setting is turned on in the Chrome browser.  
Track All Pages to Mixpanel with a Consolidated Event Name| This setting is turned on by default and tracks the `Loaded a Page` events to Mixpanel for all `page` method calls.  
  
**Note** : Do not turn off this setting as Mixpanel recommends using it to send your events.  
Track Categorized Pages to Mixpanel| Turn on this setting to track events for `page` calls that have an associated category.  
  
For example, a `page` call like `rudderanalytics.page("Docs", "Index")` results in RudderStack sending the event `Viewed Docs Index Page` to Mixpanel.  
Track Named Pages to Mixpanel| Turn on this setting to track events for `page` calls that have an associated name.  
  
For example, a `page` call like `rudderanalytics.page("Signup")` results in RudderStack sending the event `Viewed Signup Page` to Mixpanel.  
Source Name| If specified, RudderStack sends this source name to Mixpanel for every event/`page`/`screen` call.  
Cross Subdomain Cookie| Lets you persist the Mixpanel cookie between different pages of your application.  
Persistence Type| Lets you choose the persistence storage method for your Mixpanel cookies. RudderStack provides the following options:  
  


  * **None** : Mixpanel will not persist the cookie.
  * **Cookie** : Mixpanel persists the cookie in the browser’s cookie storage.
  * **Local Storage** : Mixpanel persists the cookie in local storage.

  
Persistence Name| Specify a name for the Mixpanel cookie. RudderStack adds it as a suffix for the Mixpanel cookie name.  
Secure Cookie| Turn on this option to mark the Mixpanel cookie as secure, that is, it will only transmit over HTTPS.  
Properties to send as Super Properties| Specify the event properties that RudderStack sets as Super Properties in Mixpanel.  
Properties to set only once| Specify the `identify` traits as Mixpanel properties whose values you do not want to change at the user profile level. Once specified, Mixpanel will **not** overwrite these fields with new values later.  
  
See [Properties to set only once](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/device-mode/#properties-to-set-only-once>) section for more information.  
Traits to set as People Properties| Specify the `identify` traits that RudderStack sets as People Properties in Mixpanel.  
Events to increment in People| See [Incrementing events in Mixpanel People](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/device-mode/#increment-events-in-mixpanel-people>) for more information.  
Percentage of SDK Initializations that qualify for Replay Data Capture| Specify the percentage of events (0-100) that Mixpanel considers for session replay. If you do not specify any value, RudderStack sets this field to `0` by default, meaning Mixpanel **does not** consider any events for session replay.  
  
See [Events sent for session replay](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/device-mode/#session-replay>) for more information on using this setting.  
  
##### **Consent settings**

Setting| Description  
---|---  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
##### **Other settings**

Setting| Description  
---|---  
Client-side Events Filtering| Filter events before sending them to Mixpanel. See the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.  
  
## Next steps

  * [Send events to Mixpanel in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/cloud-mode/>)
  * [Send events to Mixpanel in device mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel/device-mode/>)