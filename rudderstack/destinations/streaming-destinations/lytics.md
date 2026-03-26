# Lytics

Send your event data from RudderStack to Lytics.

* * *

  * __4 minute read

  * 


[Lytics](<https://www.lytics.com/>) is a popular customer data platform built for marketers. It allows you to efficiently leverage your first-party customer data to deliver tailored customer journeys.

RudderStack supports Lytics as a destination to which you can seamlessly send your event data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/lytics>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Lytics** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Lytics native SDK from the`http(s)://c.lytics.io/api/tag/$${this.accountId}/latest.min.js` domain. The value for `accountId` is taken from the **Account ID** RudderStack dashboard setting.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Lytics SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to Lytics, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Lytics**.
  2. Assign a name to your destination and click **Next**.


### Connection settings

To successfully configure Lytics as a destination, you need to configure the following settings:

[![Lytics connection settings](/docs/images/event-stream-destinations/lytics-connection-settings-1.webp)](</docs/images/event-stream-destinations/lytics-connection-settings-1.webp>)

  * **API Token** : Create an API token in your Lytics dashboard and enter the details here.


> ![info](/docs/images/info.svg)
> 
> To get the API token, go to your Lytics dashboard and navigate to **Account** > **Account Settings** > **API Token**. You can create an API token here and use this information to configure Lytics as a destination.

  * **Stream Name** : Enter the name of the Lytics stream where you want to send the events.
  * **Client-side Event Filtering** : This setting is applicable **only if** you are sending events to Lytics via device mode.


> ![info](/docs/images/info.svg)
> 
> Refer to the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information on this setting.

If you are using the JavaScript SDK to send the events to Lytics, enter the following settings:

[![Lytics connection settings](/docs/images/event-stream-destinations/lytics-connection-settings-2.webp)](</docs/images/event-stream-destinations/lytics-connection-settings-2.webp>)

  * **Account ID** : Enter the the Lytics account ID obtained from your Lytics dashboard. For more information on obtaining the account ID, refer to the [Lytics support page](<https://support.lytics.com/hc/en-us/articles/115001231351-How-do-I-find-my-Lytics-account-ID->). **This is a mandatory field**.
  * **Allow UID Sharing Across Multiple Domains** : When enabled, this option lets you identify users across domains.
  * **Ensure Entity** : When this option is enabled, RudderStack gets your most updated audience membership and profile data, before sending it to Lytics.
  * **Use native SDK to send events** : Enable this setting if you are sending events via the web [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).


## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call captures the relevant details about the visiting user.

A sample `identify` payload is as shown in the snippet below:
    
    
    rudderanalytics.identify("1hKOm4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
    })
    

## Page

With the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) method, RudderStack makes a call to Lytics to record a page view.

A sample `page` call is as shown:
    
    
    rudderanalytics.page("Popular", "Bestseller", {
      url: "https://www.estore.com/search/best-seller/1",
      path: "/best-seller/1",
    })
    

Similarly, you can also make [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) calls. However, this is supported only in the [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

A sample screen call is as shown:
    
    
    [[RSClient sharedInstance] screen:@"Home"];
    

## Track

With the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) API, RudderStack makes a call to Lytics to track user actions and their associated properties.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Order Completed", {
      order_id: "1a2b3c4d",
      category: "category",
      revenue: 99.9,
      shipping: 13.99,
      tax: 20.99,
      promotion_id: "PROMO_1234",
    })
    

## FAQ

#### How do I obtain the Lytics API token?

Go to your Lytics dashboard, and navigate to **Account** > **Account Settings** > **API Token**. You can create an API token here, which can be used to configure the destination on the RudderStack dashboard.

For more information, refer to the [Lytics documentation](<https://learn.lytics.com/documentation/product/features/account-management/managing-api-tokens#managing-api-tokens>).

#### How do I obtain the Lytics account ID?

To obtain your Lytics account ID, follow these steps:

  1. Log into your Lytics dashboard.
  2. Click the account name on the top right and go to **Manage Accounts**.


Here, you will see the account ID associated with your Lytics account.

For more information, refer to this [Lytics support page](<https://support.lytics.com/hc/en-us/articles/115001231351-How-do-I-find-my-Lytics-account-ID->).