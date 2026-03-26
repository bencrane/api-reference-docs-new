# Woopra

Send your event data from RudderStack to Woopra.

* * *

  * __6 minute read

  * 


[Woopra](<https://www.woopra.com/>) is a customer journey and product analytics tool. It lets you track your customers’ activities across various product, marketing, and sales touchpoints. You can also leverage built-in triggers to take real-time actions based on user behavior.

RudderStack supports Woopra as a destination where you can send your event data seamlessly.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **WOOPRA** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Woopra native SDK from the `https://static.woopra.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Woopra SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to Woopra, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Woopra**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Woopra as a destination, you need to configure the following settings:

[![Woopra connection settings](/docs/images/event-stream-destinations/woopra-connection-settings-1.webp)](</docs/images/event-stream-destinations/woopra-connection-settings-1.webp>)

  * **Project Name** : Enter your Woopra project name. This is the domain name you entered while setting up your project.


> ![info](/docs/images/info.svg)
> 
> For more information on getting your Woopra project name, refer to the FAQ section below.

> ![info](/docs/images/info.svg)
> 
> RudderStack uses this project name as a fallback value if it is not specified in the event’s `integrations` object. For more information, refer to the Identify section below.

To send the events to Woopra via [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), you also need to configure the following settings:

[![Woopra connection settings](/docs/images/event-stream-destinations/woopra-connection-settings-2.webp)](</docs/images/event-stream-destinations/woopra-connection-settings-2.webp>)[![Woopra connection settings](/docs/images/event-stream-destinations/woopra-connection-settings-3.webp)](</docs/images/event-stream-destinations/woopra-connection-settings-3.webp>)

  * **Cookie Name** : Enter the name of the cookie used to identify the visitor.
  * **Cookie Domain** : Enter the domain scope of the Woopra cookie.
  * **Click Tracking** : Enable this setting to track user click interactions via links and buttons.
  * **Cookie Path** : Specify the cookie path that stores all information related to tracking user click interactions via links and buttons.
  * **Download Tracking** : If enabled, this setting lets you track the downloads on your web page.
  * **Hide Campaign** : Enable this setting to remove the captured campaign properties from the URL.
  * **Idle Timeout** : Enter the inactivity time (in ms) after which RudderStack considers the user to be offline.
  * **Ignore Query URL** : If enabled, RudderStack ignores the URL’s query component when the standard page view is called.
  * **Outgoing Ignore Subdomain** : If enabled, RudderStack does not track the links to the subdomains as outgoing links.
  * **Outgoing Tracking** : Enable this setting to track the external link clicks on the web page.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Woopra.


> ![info](/docs/images/info.svg)
> 
> For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.

  * **Use device mode to send events** : This setting **must be enabled** to send the events to Woopra via web device mode.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to update the visitor properties in Woopra.

RudderStack uses the [`identify`](<https://docs.woopra.com/reference/track-identify>) endpoint to send the user information to Woopra.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      state: "Louisiana",
      firstName: "Alex",
      lastName: "Keener",
      country: "USA",
      email: "alex@example.com",
      integrations: {
        "woopra": {
          "projectName": "abc.com"
        }
      }
    });
    

You can specify your Woopra project name within the `integrations` object of the `identify` event, as seen in the above snippet. Alternatively, you can specify the project name via the **Project Name** dashboard setting while configuring the destination.

> ![info](/docs/images/info.svg)
> 
> If you provide the Woopra project name in both the dashboard settings as well as the `integrations` object, RudderStack gives precedence to the name specified in the `integrations` object.

RudderStack uses the below fields to identify a user in the same order of precedence:

Precedence order| RudderStack property| Woopra property  
---|---|---  
1| `userId` / `traits.userId` / `traits.id` / `context.traits.userId` / `context.traits.id`| `cv_id`  
2| `traits.email` / `context.traits.email` / `properties.email`| `cv_email`  
3| `context.externalId.woodpraId` / `anonymousId`| `cookie`  
  
> ![info](/docs/images/info.svg)
> 
> For a detailed list of the supported property mappings, refer to the Standard property mappings section below.

Any user-provided cookie must be mapped to either `email` or `userId` when creating a new user or using the cookie for the first time. Otherwise, Woopra accepts the data but reflects it **only when** that cookie is mapped to any of these identifiers. For example, Woopra accepts the following event but does not reflect the data in the dashboard:
    
    
    rudderanalytics.identify({
      name: "Alex Keener",
      country: "USA",
    } {
      externalId: [{
        id: "some_external_id_1",
        type: "woopraId",
      }, ],
    });
    

When you include a user identifier (`email`) in the subsequent events as shown below, Woopra reflects all user information present in the current and previous events.
    
    
    rudderanalytics.identify({
      name: "Alex Keener",
      email: "alex@example.com",
      country: "USA",
    } {
      externalId: [{
        id: "some_external_id_1",
        type: "woopraId",
      }, ],
    });
    

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to track events in Woopra via the [`ce`](<https://docs.woopra.com/reference/track-ce>) endpoint.

A sample `track` event is as shown below:
    
    
    rudderanalytics.track("Order Completed", {
      orderId: "1234567",
      price: "567",
      currency: "USD",
    });
    

### Supported mappings

The following table lists the supported **optional** property mappings between RudderStack and Woopra for the `track` events:

RudderStack property| Woopra property| Data type  
---|---|---  
`event`| `event`| String (in lower case)  
`originalTimestamp`| `timestamp`| Unix timestamp (in ms)  
`properties.{x}`| `ce_{x}`| -  
  
> ![info](/docs/images/info.svg)
> 
> If the event name is empty, RudderStack sends an empty string to Woopra as well, as a default fallback.

## Page

When you send a [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event, RudderStack converts it to a Woopra [`track`](<https://docs.woopra.com/reference/track-ce#pageviews>) event and sends all page-related information and the associated properties.

### Supported mappings

The following table lists the supported **optional** property mappings between RudderStack and Woopra for the `page` events:

RudderStack property| Woopra property| Data type  
---|---|---  
`properties.{x}`| `ce_{x}`| -  
`Viewed <category> <name> Page`| `event`| String (in lower case)  
  
## Standard property mappings

The following table lists the supported property mappings between RudderStack and Woopra, **common to all above events** :

RudderStack property| Woopra property| Data type| Presence  
---|---|---|---  
`integration.woopra.propertyName`| `property`| Domain| Optional  
`userId` / `traits.userId` / `traits.id` / `context.traits.userId` / `context.traits.id`| `cv_id`| String| Required, if `cv_email` or `cookie` is absent.  
`traits.email` / `context.traits.email` / `properties.email`| `cv_email`| String| Required, if `cv_id` or `cookie` is absent.  
`context.externalId.woodpraId` / `anonymousId`| `cookie`| String| Required, if `cv_email` or `cv_id` is absent.  
`context.ip`| `cv_ip`| IP address| Optional  
`traits.company`| `cv_company`| String| Optional  
`traits.name` / `context.traits.name`| `cv_name`| String| Optional  
`traits.{x}` / `context.traits.{x}`| -| Custom fields| Optional  
`context.device.type`| `device`| String| Optional  
`context.app.name`| `app`| String| Optional  
`ua.browser.name` \+ `ua.browser.version`| `browser`| String| Optional. The visitor profile for a given identifier won’t be published until this field is sent to Woopra.  
`context.os.name`| `os`| String| Optional  
  
## FAQ

#### Where can I find the Woopra project name?

To get your Woopra project name, follow these steps:

  1. Go to your [Woopra dashboard](<https://app.woopra.com/>).
  2. Select your organization and go to **Projects**.
  3. You should be able to see all your projects and the associated domain names (Woopra project name):

[![Woopra project name](/docs/images/event-stream-destinations/woopra-domain-name.webp)](</docs/images/event-stream-destinations/woopra-domain-name.webp>)