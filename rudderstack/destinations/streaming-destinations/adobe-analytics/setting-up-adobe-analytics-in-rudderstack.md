# Setup Guide

Set up Adobe Analytics as a destination in RudderStack.

* * *

  * __9 minute read

  * 


This guide will help you set up Adobe Analytics as a destination in RudderStack.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Adobe Analytics** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Adobe Analytics native from the `https://cdn.rudderlabs.com` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Adobe Analytics SDK successfully.

## Get started

Once you’ve confirmed that the source platform supports sending data to Adobe Analytics, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Adobe Analytics**.
  2. Assign a name to the destination and click **Continue**.


## Connection Settings

To successfully configure Adobe Analytics as a destination, you will need to configure the following settings:

  * **Tracking Server URL** : Enter the `trackingServer` variable to determine the location where an image request is sent. For example, `jimsbrims.sc.omtrdc.net`. Do not include the `http://` or `https://` in the tracking server URL. Refer to the [Adobe Analytics documentation](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/config-vars/trackingserver.html?lang=en>) for more information.


> ![warning](/docs/images/warning.svg)
> 
> If this variable is defined incorrectly, your implementation may experience data loss.

  * **Tracking Server Secure URL** : Enter the `trackingServerSecure` variable to determine the location where an image request is sent over HTTPS. If this variable is not defined correctly, your implementation may experience data loss. Refer to the [Adobe Analytics documentation](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/config-vars/trackingserversecure.html?lang=en>) for more information.
  * **Report Suite ID(s)** : Enter the Report Suite ID(s) (separated by commas) which can be found in your Adobe Analytics Settings page. For example: `ab.cd`,`ef.gh`,`ij.kl`.
  * **Check for Heartbeat calls to be made over HTTPS** : If this setting is enabled and the Heartbeat Tracking Server URL is present, RudderStack sets the SSL value to `true` so that the calls go over HTTPS.
  * **Heartbeat Tracking Server URL** : If assigned, RudderStack uses this as the tracking server URL instead of the URL assigned in the **Tracking Server URL** field. It sets all the heartbeat configurations if you specify this URL. Refer to the [Adobe Analytics documentation](<https://experienceleague.adobe.com/docs/media-analytics/using/sdk-implement/setup/setup-overview.html?lang=en>) for more information.
  * **Adobe Analytics JavaScript SDK URL/Heartbeat SDK URL** : Enter the proxy URL where you are hosting the `adobe-analytics-js.js` and `adobe-analytics-js-heartbeat.js`. By default, RudderStack hosts them at <https://cdn.rudderlabs.com/adobe-analytics-js/adobe-analytics-js.js> and <https://cdn.rudderlabs.com/adobe-analytics-js/adobe-analytics-js-heartbeat.js> respectively.
  * **Adobe Heartbeat Settings** : This setting is used to map your RudderStack video events to Adobe Heartbeat Events. Refer to the [Adobe Analytics Heartbeat Measurement](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adobe-analytics/adobe-analytics-heartbeat/>) documentation to find more information.


### Identity Resolution

  * **Marketing Cloud Organization ID** : Enter a value in this field if you want to use `visitorAPI.js`. For example: `99887766ABC@AdobeOrg`.
  * **Drop Visitor ID** : If enabled, RudderStack does not assign the `userId` to `visitorID`. Refer to the [Adobe Analytics documentation](<https://experienceleague.adobe.com/docs/id-service/using/implementation/setup-analytics.html?lang=en#section-6053a6b7c16c466a9f9fdbf9cb9db3df>) for more information.


### Timestamps

  * **Timestamp Option** : Adobe Analytics has Report Suites that accept timestamped, non-timestamped or hybrid data. Note that `window.s.timestamp` will be affected. Also, RudderStack sets `visitorID` depending on this value if the **Drop Visitor ID** setting is disabled.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * If the timestamp option is disabled, then `visitorID` will be set.
>   * If timestamp option is set to hybrid and the Prefer Visitor ID setting is on, then `visitorID` will be set.
>   * For all other cases, RudderStack does not set a `visitorID`.
> 

> 
> Also note the following regarding timestamps:
> 
>   * If the timestamp option is enabled, then timestamp will be set.
>   * If the timestamp option is hybrid and Prefer Visitor ID is off, then timestamp will be set.
> 


  * **Send Both Timestamp and VisitorID for Timestamp Optional Reporting Suites** : This setting lets you choose whether to send both the timestamp and the visitor ID when sending server-side events, in case you are using the [Timestamps Optional Reporting Suite](<https://experienceleague.adobe.com/docs/analytics/admin/admin-tools/timestamp-optional.html?lang=en>).


> ![warning](/docs/images/warning.svg)
> 
> Enabling this setting might lead the data to be out of order. Hence, it is not recommended by Adobe. In order to make it work, you need to enable the **Optional Timestamp** setting in **Reporting Suites**.

  * **No Fallbacks for Visitor ID** : Enable this setting to remove the fallbacks. However, it is applicable only for the server-side events when the **Drop Visitor ID** setting is disabled and **marketingCloudId** is sent in the Adobe Analytics `integrations` object. The priority order of setting the Adobe Analytics visitor ID is the destination-specific setting for `visitorId` > `userId` > `anonymousId`.
  * **Prefer Visitor ID** : Adobe does not allow sending both `visitorID` and timestamp. Hence, this option is used when the timestamp option is set as hybrid. Also, note that if this option is enabled, RudderStack sets the `visitorID` field. If disabled, RudderStack sets the timestamp value. Refer to the [Adobe Analytics documentation](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/page-vars/timestamp.html?lang=en>) for more information.
  * **Enable pageName for Track Events** : When enabled, RudderStack only tracks events by sending a `pageName`.


### Mappings

  * **Map Rudder Events to Adobe Custom Events** : This setting allows you to add one or multiple custom Adobe events separated by comma.
  * **Map Rudder Context data to Adobe Context Data** : Context data variables allow you to you define custom variables on each page that the processing rules apply and can read. Instead of explicitly assigning values to the analytics variables, you can send your data in via these context data variables. The processing rules take the values from the context data variables and pass them into the respective analytics variables.


This setting allows you to map the key present under the context/properties of the RudderStack message to the property name you want to send to the Adobe context data. An example is as shown below:
    
    
    "context": {
      "contextProperties": {
        "prop1": "val1",
        "prop2": "val2"
      }
    }
    

If you want to set `prop1` to Adobe’s context data `property1`, then map with `contextProperties.prop1` –> `property1`.

If you want to send top level properties `anonymousId`, `messageId`, `event` then simply enter the key.

Refer to the [Adobe Analytics documentation](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/page-vars/contextdata.html?lang=en>) for more information.

  * **Prefix to add before all contextData property** : Specify a prefix to automatically append to your RudderStack properties before sending them as `contextData`.
  * **Map Rudder Properties to Adobe eVars** : Enter the RudderStack property and the corresponding [eVar’s](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/page-vars/evar.html?lang=en>) index number you want to map before sending to Adobe Analytics. Refer to the mapping section for more information on the different values you can specify in the RudderStack property field.
  * **Map Rudder Properties to Adobe Hierarchy properties** : Enter the RudderStack property and the corresponding [hierarchy variable’s](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/page-vars/hier.html?lang=en>) index number you want to map before sending to Adobe Analytics. Refer to the mapping section for more information on different values you can specify in the Rudder property field.
  * **Map Rudder Properties to Adobe list properties** : Enter the RudderStack property and the corresponding [list’s](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/page-vars/list.html?lang=en>) index number you want to map before sending to Adobe Analytics. You can specify the list properties as an array/string separated by commas. Otherwise, they are dropped.


> ![info](/docs/images/info.svg)
> 
> For all the list properties you mention in this field, it is mandatory to specify their delimiter in the below setting. The delimiter is used to create the list string for the XML payload.

  * **Map Rudder Property with Delimiters for list properties** : Set any of the delimiters from `, ; / : |`. RudderStack sends the list variables as a string. Any list of properties is delimited using these delimiters.
  * **Map Rudder Properties to Adobe Custom properties** : Enter the RudderStack property and the corresponding [prop’s](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/page-vars/prop.html?lang=en>) index number you want to map before sending to Adobe Analytics.


> ![info](/docs/images/info.svg)
> 
> For all the custom properties you mention in this field, it is mandatory to specify their delimiter in the below setting. The delimiter is used to create the props string for the XML payload.

  * **Map Rudder Property with Delimiters for Adobe Custom properties** : Set any of the delimiters from `, ; / : |`. RudderStack sends the list variables as a string. Any list of properties is delimited using these delimiters.


### Merchandise Event Level Settings

  * **Map Rudder Events to Adobe Merchandise events** : This setting lets you map the RudderStack event with an Adobe event of the currency/purchase type. For example: `event5`.
  * **Currency/Incremental properties to add to merchandise events at event level** : Enter the RudderStack property that has a currency/counter value. RudderStack uses this to create the event string like `purchase,event5=19.9`. It also automatically sets the `currencyCode` value where the default is USD. Refer to the [Adobe Analytics documentation](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/page-vars/events/events-overview.html?lang=en>) for more information.


### Merchandise Product Level Settings

  * **Map Rudder Events to Adobe Merchandise events** : This setting lets you map a RudderStack event with an Adobe event of the currency/purchase type.
  * **Currency/Incremental properties to add to merchandise events at product level** : Enter the RudderStack property that has a currency/counter value. This will be used to create a product string like `[category][item][quantity][total][incrementor][merchString]`.
  * **Map Rudder Properties to eVars at product level** : Enter the RudderStack property and the corresponding [eVars](<https://experienceleague.adobe.com/docs/analytics/implementation/vars/page-vars/evar-merchandising.html?lang=en>) index you want to map before sending to Adobe Analytics. RudderStack appends the eVars with `|` and sends it along with the product string. Refer to the mapping section for more information on different values you can specify in the Rudder property field.
  * **Product Identifier** : Choose either of the SKU, ID, or Name of the product as a product identifier.


### Client-side Event Filtering

This setting is applicable **only if** you are sending events to Adobe Analytics via device mode. It lets you specify which events should be blocked or allowed to flow through to Adobe Analytics. Refer to the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.

### Consent Settings

  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Mapping for evars and hierarchy variables

This section is applicable **only** for the following connection settings:

  * Map Rudder Properties to Adobe eVars
  * Map Rudder Properties to eVars at product level
  * Map Rudder Properties to Adobe Hierarchy properties


You can specify any of the following values in the **Rudder property** field of the above settings:

  * **Key name** : Specify a key name as the RudderStack property present in the event payload. RudderStack uses the following priority order to find the key name in the event payload: `properties` > `traits` > `context.traits` > `context`
  * **Absolute path of the key in the event payload** : Specify the exact path of the key in the RudderStack property present in the event payload (in dot notation). For example, `context.library.name`.
  * **Dynamic destination configuration** : Specify the RudderStack property as:  
{{ `path of the property` || “default-value” }}. For example,  
{{ `message.properties.configUrl` || “config.sc.omtrdc.net” }}.


## Override XML tags values

RudderStack sets the default values for the below-mentioned XML tags. However, you can override them by passing the required values in the `integrations` object.

XML tag| Default value  
---|---  
`linktype`| `o`  
`linkName`| `event name`  
`linkURL`| `context.page.url`  
  
Refer to the [Adobe documentation](<https://developer.adobe.com/analytics-apis/docs/1.4/guides/data-insertion/variable-reference/>) for more information on these tags.