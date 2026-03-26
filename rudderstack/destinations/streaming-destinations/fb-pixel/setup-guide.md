# Facebook Pixel Destination Setup Guide

Set up Facebook Pixel as a destination in RudderStack.

* * *

  * __8 minute read

  * 


This guide will help you set up Facebook Pixel as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Facebook Pixel.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Facebook Pixel** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Facebook Pixel native SDK from the `https://connect.facebook.net/` domain.
> 
> Based on your website’s content security policy, you will need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Facebook Pixel SDK successfully.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Facebook Pixel** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in RudderStack.  
Pixel ID| Enter your Facebook Pixel ID — this is required for sending events in both cloud and device modes.  
  
See the FAQ section below for more information on obtaining your Facebook Pixel ID.  
Business Access Token| Specify your Facebook business access token — it is required to send events **only** in cloud mode.  
  
See the FAQ section below for more information on obtaining this token.  
  
## Configuration settings

Configure the settings in the below sections to receive your data correctly in Facebook Pixel.

### Event settings

Setting| Description  
---|---  
Enable Standard Event (PageView) for all Page and Screen Calls| If toggled on, RudderStack sets `pageview` as a standard event for all `page` and `screen` calls.  
Value Field Identifier| Set this field to either `properties.price` or `properties.value` from the dropdown — RudderStack maps it to Facebook’s `value` field. You can use this setting for the **Product Viewed** or **Product Added** events.  
Enable Advanced Matching| Toggle on this setting to update user information in Facebook Pixel device mode.  
Use Updated Mapping| This setting is applicable only in device mode.  
  
See Web device mode settings for more information on this setting.  
  
### Event mapping settings

RudderStack maps some events to the Facebook custom events by default. You can use this option to override the [default mappings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-pixel/cloud-mode/#standard-events>) and map your events to specific Facebook custom events.

### PII properties settings

The following settings help you control how RudderStack handles personally identifiable information (PII) before sending events to Facebook Pixel, helping you comply with Facebook’s data policies and privacy requirements.

Setting| Description  
---|---  
Denylist PII Properties| Specify the PII properties to exclude completely or hash before sending events to Facebook. You can configure each property individually to either exclude or hash it.  
Hash Denylist PII Property| Toggle on this setting to hash-encrypt the PII properties mentioned in the **Denylist PII Properties** field in SHA-256 format before sending them to Facebook.  
  
If this setting is toggled off, the PII property specified in the **Denylist PII Properties** field is excluded from the events sent to Facebook.  
Input PII properties you want to allowlist| Specify PII properties that RudderStack should include in events sent to Facebook.  
  


> ![warning](/docs/images/warning.svg)Note the following:  
>   
> 
> 
>   * This setting is applicable only for the default denylisted PII properties (listed below).
>   * Whitelisted properties **override** denylist settings.
>   * RudderStack sends these allowlisted properties to Facebook **without** hashing.
> 
  
  
#### Default denylisted PII properties

Click **here** to see the complete list of PII properties that RudderStack denylists by default.  


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


### Destination settings

Setting| Description  
---|---  
Limited Data Usage| If toggled on, RudderStack takes the data processing information from the event payload and sends it to Facebook.  
  
See Limited data usage section below for more information on using this setting.  
Use as Test Destination| Toggle on this setting to use the destination for testing purposes and enter the **Test Event Code**.  
  
You can find this code in your Facebook Pixel dashboard. When enabled, you can check your events in the Facebook Pixel dashboard in real time.  
Don’t send external_id for user| If toggled on, RudderStack does not send either `userId` or `anonymousId` as the `external_id` to Facebook Pixel.  
  
### Other settings

Setting| Description  
---|---  
Client-side Events Filtering| This setting lets you specify which events should be blocked or allowed to flow through to Facebook Pixel.  
  
See the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide for more information.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  


> ![info](/docs/images/info.svg)When consent management is enabled, RudderStack only sends events to Facebook Pixel when the user has provided appropriate consent.  
  
### Web device mode settings

Setting| Description  
---|---  
Use Updated Mapping| This setting is toggled off by default, causing RudderStack to send user traits to Facebook Pixel **without** any modification.  
  
See the Use updated mappings section for more information on this setting.  
Legacy Conversion Pixel IDs| With this setting, you can send specific events to a legacy conversion Pixel by specifying the event-Pixel ID mapping.  
Enable Automatic Configuration| Toggled on by default, this setting sends button click and page metadata from your website to improve your ads delivery and measurement and automate your Pixel setup.  
  
See the [Meta documentation](<https://developers.facebook.com/docs/meta-pixel/advanced/#automatic-configuration>) for more information on this feature.  
  
## Use updated mappings

If you toggle on the **Use Updated Mappings** dashboard setting, RudderStack takes the following traits:
    
    
    {
      firstName: "Alex",
      lastName: "Keener",
      email: "alex@example.com",
      phone: "12345678910",
      gender: "Male",
      birthday: "01012001",
      city: "New Orleans",
      country: "USA",
      zip: "90009", // You can also send postalCode instead
      state: "Louisiana",
      foo: "bar",
    }
    

It then sends the above traits to Facebook Pixel in the following format:
    
    
    {
      fn: "Alex",
      ln: "Keener",
      em: "alex@example.com",
      ph: "12345678910",
      ge: "Male",
      db: "01012001",
      ct: "New Orleans",
      country: "USA",
      zp: "90009",
      state: "Louisiana",
      foo: "bar"
    }
    

> ![info](/docs/images/info.svg)
> 
> If you enable both the **Enable Advanced Matching** and **Use Updated Mapping** settings, RudderStack maps `external_id` from the following fields, in the specified order:
> 
>   1. `userId`
>   2. `context.traits.userId`
>   3. `context.traits.id`
>   4. `anonymousId`
> 


## Limited data usage

If you toggle on the **Limited Data Usage** dashboard setting, RudderStack takes the data processing information from the event payload and sends it to Facebook.

Note that the data in the RudderStack event payload should be as shown:
    
    
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
    

You can send the value of [`fbc`](<https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/fbp-and-fbc/#fbc>) parameter via `context.fbc` as shown in the above payload. If not provided, RudderStack autogenerates it using the following values:

  * Fetches `fbclid` from `context.page.url`
  * Uses `originalTimestamp` as the creation time
  * Sets `subdomainIndex` to `1`
  * Sets `version` to `fb`


> ![info](/docs/images/info.svg)
> 
> The `context.dataProcessingOptions` will be mapped to `data_processing_options` in Facebook as is mentioned in the [Facebook developer docs](<https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event#data-processing-options>).

## FAQ

#### Where can I find the Pixel ID?

  1. Go to **Facebook Events Manager**.
  2. Click the **Datasets** icon in the left navigation bar and click **Datasets**. All the Pixels associated with your account will be listed here along with their IDs.

[![](/docs/images/event-stream-destinations/fb-pixel/facebook-pixel-id.webp)](</docs/images/event-stream-destinations/fb-pixel/facebook-pixel-id.webp>)

#### Where can I find the Business Access Token?

  1. Go to **Facebook Events Manager** and select the Facebook Pixel.
  2. Click the **Settings** tab.

[![](/docs/images/event-stream-destinations/fb-pixel/facebook-pixel-settings.webp)](</docs/images/event-stream-destinations/fb-pixel/facebook-pixel-settings.webp>)

  3. In the Conversions API section, click **Generate access token** under **Set up direct integration**.

[![](/docs/images/event-stream-destinations/fb-pixel/facebook-business-access-token.webp)](</docs/images/event-stream-destinations/fb-pixel/facebook-business-access-token.webp>)

See the [Facebook documentation](<https://developers.facebook.com/docs/marketing-api/conversions-api/get-started/#via-events-manager>) for more information on how to use this access token or to generate your access token via your own app.

#### Can I hash my user data before sending it to RudderStack?

Yes. Facebook Pixel requires all user data, data coming from `context.traits`, to be hashed. This includes `email`, `phone`, `birthday`, `address`, etc. By default, RudderStack will automatically hash all of the necessary properties for you. However, if you would like to hash these traits before sending to RudderStack then you need to add this code to the event.
    
    
    rudderanalytics.track(
      "some_event_name",
      { some_properties },
      {
        integrations: {
          "Facebook Pixel": {
            hashed: true,
          },
        },
      }
    )
    

The `integrations` object with these key-values will tell RudderStack not to hash the traits in `context.traits` because they are already hashed. Otherwise, RudderStack will hash your data again and Facebook will not be able to match the traits. Please keep in mind that Facebook will not accept un-hashed data.

#### I can see my events being sent in the RudderStack dashboard but are not visible in the Facebook Pixel dashboard. What could be the reason?

It may take up to 24 hours for your events to reflect in the Facebook Pixel dashboard.  
You can also verify if your events are flowing correctly by enabling the **Use as Test Destination** setting in the RudderStack dashboard. It reflects the events in the Facebook Pixel dashboard in real time.