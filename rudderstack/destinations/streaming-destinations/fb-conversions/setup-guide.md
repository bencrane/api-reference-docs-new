# Setup Guide

Send your event data from RudderStack to Facebook Pixel.

* * *

  * __6 minute read

  * 


This guide will help you set up Facebook Conversions as a destination in RudderStack.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Facebook Conversions**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Facebook Conversions as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **Dataset ID** : Enter the dataset ID. If an existing pixel is linked to your dataset, your dataset ID will be the same as your [Pixel ID](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-pixel/setup-guide/#where-can-i-find-the-pixel-id>).
  * **Business Access Token** : Enter the business access token from your Facebook business account. This is required to send events in cloud mode. For more information on obtaining the business access token, see the FAQ.


### Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Facebook Conversions** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
### Configuration settings

After completing the initial setup, configure the following settings to correctly receive your data in Facebook:

#### Event settings

  * **Action Source** : From the dropdown, select the fallback `action_source` value you want to set **if** `action_source` is not present in your event properties. RudderStack provides the following options:

[![Action source setting](/docs/images/event-stream-destinations/fb-conversions-action-source.webp)](</docs/images/event-stream-destinations/fb-conversions-action-source.webp>)

#### Destination settings

  * **Limited Data Usage** : If turned on, RudderStack takes the data processing information from the payload and sends it to Facebook. The data in the RudderStack payload should be in the following format:


    
    
    "context": {
      "dataProcessingOptions": [
        [
          "LDU"
        ],
        1,
        1000
      ],
      "fbc": "fb.1.1554763741205.AbCdEfGhIjKlMnOpQrStUvWxYz1234567890",
      "fbp": "fb.1.1554763741205.234567890",
      "fb_login_id": "fb_id",
      "lead_id": "lead_id",
      "device": {
        "id": "df16bffa-5c3d-4fbb-9bce-3bab098129a7R",
        "manufacturer": "Xiaomi",
        "model": "Redmi 6",
        "name": "xiaomi"
      },
      "network": {
        "carrier": "AirCarrier"
      },
      "os": {
        "name": "android",
        "version": "8.1.0"
      },
      "screen": {
        "height": "100",
        "density": 50
      },
      "traits": {
        "email": "john@example.com",
        "anonymousId": "c82cbdff-e5be-4009-ac78-cdeea09ab4b1"
      }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> If this setting is turned on, RudderStack maps the values in the `context.dataProcessingOptions` array to `commonData.data_processing_options`, `commonData.data_processing_options_country`, and `commonData.data_processing_options_state` fields.

You can set the value of the [`fbc`](<https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/fbp-and-fbc/#fbc>) parameter using the `context.fbc` field as shown in the above payload.

If not set explicitly, RudderStack autogenerates it using the following values:

  * Fetches `fbclid` from `context.page.url`.

  * Uses `originalTimestamp` as the creation time.

  * Sets `subdomainIndex` to `1`.

  * Sets `version` to `fb`.  
  


  * **Use as Test Destination** : Turn on this setting if you are using this destination for testing purposes and enter the **Test Event Code**. You can find this code in your Facebook dashboard. When turned on, you can check your events in the Facebook dashboard in realtime.


> ![info](/docs/images/info.svg)
> 
> RudderStack maps the `context.dataProcessingOptions` to `data_processing_options` in Facebook according to the [Facebook developer documentation](<https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event#data-processing-options>).

  * **Don’t send external_id for user** : If turned on, RudderStack does not send either `userId` or `anonymousId` as the `external_id` to Facebook.


#### Other settings

  * **Client-side event filtering** : Specify the events to be discarded or allowed to flow through. For more information, see [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>).
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


#### Event mapping

Click the **Set up mapping** button to map your RudderStack events and properties to specific Facebook custom events. You can also use the JSON mapper to set these mappings.

##### **PII properties**

> ![info](/docs/images/info.svg)
> 
> The allowlist/denylist settings control only the standard Facebook PII fields listed below. They **do not affect** other mapped properties or top-level RudderStack identifiers like `userId` or `anonymousId`.
> 
> To control whether RudderStack sends `userId` or `anonymousId` as `external_id`, use the Don’t send external_id for user setting.

  * **Denylist PII Properties** : RudderStack drops the PII properties specified in this field. However, if you toggle on the **Denylist PII Hash Property** setting, RudderStack encrypts the properties in SHA256 format before sending them to Facebook. Facebook identifies the following standard fields as PII properties and they are **denylisted by default** :

    * `email`
    * `firstName`
    * `lastName`
    * `firstname`
    * `lastname`
    * `first_name`
    * `last_name`
    * `gender`
    * `city`
    * `country`
    * `phone`
    * `state`
    * `zip`
    * `postalCode`
    * `birthday`


> ![info](/docs/images/info.svg)
> 
> To hash and send any of the above properties instead of denylisting them, enter the property name in the **Denylist PII Properties** field and toggle on the **Hash Denylist PII Property** toggle.

  * **Allowlist PII Properties** : The PII properties mentioned in this field are sent to Facebook if they are present in the event’s properties.

[![PII settings](/docs/images/event-stream-destinations/fb-conversions-pii-settings.webp)](</docs/images/event-stream-destinations/fb-conversions-pii-settings.webp>)

## FAQ

#### Where can I find the dataset ID?

To get your dataset ID, go to your Facebook Ads Manager account. From the left navigation bar, select **Business Tools** , and click **Events Manager** under **Manage Business**.

[![Dataset ID](/docs/images/event-stream-destinations/fb-conversions-dataset-id-1.webp)](</docs/images/event-stream-destinations/fb-conversions-dataset-id-1.webp>)

You should be able to see the ID underneath your site name under **Data Sources** :

[![Dataset ID](/docs/images/event-stream-destinations/fb-conversions-dataset-id-2.webp)](</docs/images/event-stream-destinations/fb-conversions-dataset-id-2.webp>)

#### Where can I find the Business Access Token?

In order to use the Facebook Conversions API, you need to generate an access token using the Facebook Events Manager:

  1. Choose the relevant Facebook Pixel and click the **Settings** tab.
  2. In the Conversions API section, click **Generate access token** under the **Set up manually** section:

[![FB Conversions generate access token](/docs/images/event-stream-destinations/fb-conversions-generate-access-token.webp)](</docs/images/event-stream-destinations/fb-conversions-generate-access-token.webp>)

> ![info](/docs/images/info.svg)
> 
> For more information on how to use this access token or to generate your access token via your own app, see the [Facebook developer documentation](<https://developers.facebook.com/docs/marketing-api/conversions-api/get-started/#via-events-manager>).

#### Can I hash my event data before sending it to RudderStack?

Yes. Facebook requires all user data, including data coming from `context.traits`, to be hashed. This includes `email`, `phone`, `birthday`, `address`, etc. By default, RudderStack automatically hashes all of the necessary properties for you. However, to hash these traits before sending to RudderStack, you need to send your event as follows:
    
    
    rudderanalytics.track(
      "event_name", {
        properties
      }, {
        integrations: {
          "Facebook Conversions": {
            hashed: true,
          },
        },
      }
    )
    

> ![info](/docs/images/info.svg)
> 
> RudderStack accepts any of the following names for Facebook Conversions in the `integrations` object:
> 
>   * `fb_conversions`
>   * `fb conversions`
>   * `FacebookConversions`
>   * `Facebook Conversions`
>   * `FB Conversions`
>   * `Facebook_Conversions`
> 


The `integrations` object with these key-values notifies RudderStack to not hash the traits in `context.traits` as they are already hashed. Otherwise, RudderStack will hash your data again and Facebook will not be able to match the traits. Keep in mind that Facebook rejects any un-hashed data.

#### Why can I see my events in the RudderStack dashboard but not in the Facebook dashboard?

It may take up to 24 hours for your events to reflect in the Facebook dashboard.

You can also verify if your events are flowing correctly by toggling on the **Use as Test Destination** setting in the RudderStack dashboard - this reflects the events in the Facebook dashboard in real time.