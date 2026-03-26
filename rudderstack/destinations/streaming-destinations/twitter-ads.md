# X Ads (formerly Twitter Ads) Beta

Send your event data from RudderStack to X Ads.

* * *

  * __3 minute read

  * 


[X Ads](<https://ads.twitter.com/>) (formerly Twitter Ads) is an advertising platform that lets you track and monitor ad campaigns, clicks, CTRs, etc. You can also implement efficient ad retargeting for your customers.

Find the open source transformation code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/blob/main/src/v0/destinations/twitter_ads/transform.js>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **X Ads (formerly Twitter Ads)** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **X Ads**.
  2. Assign a name to the destination and click **Continue**.


### Account settings

  1. Click the **Create Account** button.
  2. Under **Choose an account** , click the **Connect with X Ads** button and give RudderStack the required permissions to access your account. Then, click **Save**.
  3. To verify or change your account, click the **Edit Credentials** button.

[![X Ads account settings](/docs/images/event-stream-destinations/twitter-ads-account-settings.webp)](</docs/images/event-stream-destinations/twitter-ads-account-settings.webp>)

### Connection settings

Setting| Description  
---|---  
Pixel ID| Enter the Universal Website Tag (UWT) ID for your X Ads account.  
  
See FAQ for more information on obtaining the Pixel ID.  
Map RudderStack event name to X event ID| This setting lets you map your **RudderStack Event Name** to a specific **Twitter Event ID**.  
  
See FAQ for more information on obtaining the Twitter Event ID.  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events and send them as conversion events for a single Universal Website Tag pixel ID.

The following snippet highlights a sample `track` call:
    
    
    rudderanalytics.track("Product Purchased", {
      "quantity": "3",
      "currency": "USD",
      "value": 251,
      "email": "alex@example.com",
      "conversionId": "56342424234"
      "description": "Shoes",
      "contents": [{
          "id": "1",
          "price": "50.00",
          "quantity": 1
        },
        {
          "id": "2",
          "price": "100.55",
          "quantity": 2
        }
      ]
    })
    

### Supported mappings

The following table details the mappings between RudderStack and X Ads properties:

RudderStack property| X Ads property| Data type  
---|---|---  
`properties.eventId`| `event_id`| String  
`properties.conversionTime`| `conversion_time`| Datetime in ISO 8601 format.  
`properties.quantity`  
`properties.numberItems`| `number_items`| String  
`properties.currency`| `price_currency`| String  
`properties.value`  
`properties.price`  
`properties.revenue`| `value`| String  
`properties.conversionId`| `conversion_id`| String  
`properties.description`| `description`| String  
`properties.contents`| `contents`| Object  
`properties.pixelId`| NA| String  
  
Note that each event must contain **at least one** of the following identifier fields:

RudderStack property| X Ads property| Data type  
---|---|---  
`properties.email`| `identifiers.hashed_email`| String  
`properties.phone`| `identifiers.hashed_phone_number`| String  
`properties.twclid`| `identifiers.twclid`| String  
`properties.ip_address`| `identifiers.ip_address`| String  
`properties.user_agent`| `identifiers.user_agent`| String  
  
> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * If you want to send the `ip_address` field in your events, you must also include at least one of the other identifier fields (`email`, `phone`, `twclid`, or `user_agent`).
>   * If you want to send the `user_agent` field in your events, you must also include at least one of the other identifier fields (`email`, `phone`, `twclid`, or `ip_address`).
> 


The following table lists the mappings between the `properties.contents` object fields and X Ads properties:

`properties.contents` field| X Ads property| Data type  
---|---|---  
`id`| `content_id`| String  
`groupId`| `content_group_id`| String  
`name`| `content_name`| String  
`price`| `content_price`| String  
`type`| `content_type`| String  
`quantity`| `num_items`| String  
  
## FAQ

#### Where can I find the X Ads Pixel ID and Event ID?

  1. Sign in to your [X Ads account](<https://ads.twitter.com>).
  2. Go to **Tools** > **Event Manager**.
  3. Set up your X pixel and add the associated events. For more information, see [Conversion tracking for websites](<https://business.twitter.com/en/help/campaign-measurement-and-analytics/conversion-tracking-for-websites.html>).
  4. You can find the pixel ID and event ID under your pixel name and created events.

[![X Ads pixel ID and event ID](/docs/images/event-stream-destinations/twitterads-pixelid-eventid.webp)](</docs/images/event-stream-destinations/twitterads-pixelid-eventid.webp>)