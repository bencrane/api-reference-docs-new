# TikTok Ads Web Device Mode Integration

Send events to TikTok Ads using RudderStack web device mode.

* * *

  * __3 minute read

  * 


RudderStack lets you send your event data to TikTok Ads via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK.

Find the open source JavaScript SDK code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/TiktokAds>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to identify a user in TikTok ads.

The following snippet highlights a sample `identify` call sent to TikTok Ads:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        email: "alex@example.com",
        name: "Alex Keener"
      }, {
        externalld: [{
            id: "external_id_1",
            type: "tiktokExternalId"
        }]
      }
    );
    

In TikTok Ads, an external ID is an identifier that uniquely represents a user. Use the `externalId` parameter to match the `id` with the TikTok user. Make sure to set the type as `tiktokExternalId`.

Setting an external ID for a user is helpful in increasing match rates across channels and boost your ad measurements and optimization. For more information on using external IDs, see [TikTok documentation](<https://ads.tiktok.com/marketing_api/docs?id=1765942670613506>).

### Traits mappings

RudderStack maps the following traits to the TikTok Ads fields:

RudderStack trait| TikTok Ads trait  
---|---  
`properties.phone`  
`properties.number`| `phone`  
`properties.email`| `email`  
`externalId.tiktokExternalId`| `tiktokExternalId`  
  
## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events along with the associated properties.

A sample `track` call is shown below:
    
    
    rudderAnalytics.track("Add To Cart", {
      eventId: "123",
      category: "cat1",
      product_id: "product",
      contents: [{
          "price": 8,
          "quantity": 2,
          "content_type": "socks",
          "content_id": "1077218"
        },
        {
          "price": 30,
          "quantity": 1,
          "content_type": "dressing",
          "content_id": "1237218"
        }
      ],
      currency: "USD",
      email: "alex@example.com",
      phone: "1234567890"
    });
    

### Event mapping

You can use the [Event mapping settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/tiktok-ads/setup/#event-settings>) in the dashboard to map your events to the below [TikTok standard events](<https://ads.tiktok.com/help/article/supported-standard-events>):

**List of supported TikTok standard events**  


  * `Add Payment Info`
  * `Add to Cart`
  * `Add to Wishlist`
  * `Application Approval`
  * `Click Button`
  * `Complete Payment`
  * `Complete Registration`
  * `Contact`
  * `Customize Product`
  * `Download`
  * `Find Location`
  * `Initiate Checkout`
  * `Lead`
  * `Place an Order`
  * `Purchase`
  * `Schedule`
  * `Search`
  * `Submit Application`
  * `Submit Form`
  * `Subscribe`
  * `Start Trial`
  * `View Content`

  


> ![warning](/docs/images/warning.svg)
> 
> TikTok has recently updated the following standard events:
> 
>   * `Submit Form` is renamed to `Lead`.
>   * `Complete Payment` is renamed to `Purchase`.
> 

> 
> Although TikTok still supports the old events (`Submit Form` and `Complete Payment`), RudderStack recommends using the new events (`Lead` and `Purchase`) to avoid any issues.

### Property mappings

RudderStack maps the following event properties to the corresponding TikTok Ads properties:

RudderStack property| TikTok Ads property  
---|---  
`context.traits.email`  
`traits.email`  
`properties.email`| `email`  
`context.traits.phone`  
`traits.phone`  
`properties.phone`| `phone`  
`testEventCode`| `test_event_code`  
`properties.event_id`| `event_id`  
`properties.contents`| `contents`  
`properties.category`| `category`  
`properties.status`| `status`  
`properties.name`| `content_name`  
`properties.product_id`  
`properties.productId`| `content_id`  
`properties.contentType`  
`properties.content_type`| `content_type`  
`properties.currency`| `currency`  
`properties.value`| `value`  
`properties.description`| `description`  
  
> ![info](/docs/images/info.svg)
> 
> Send the `testEventCode` property to test a connection in TikTok Ads.

For custom events, RudderStack maps only the [standard fields](<https://github.com/rudderlabs/rudder-transformer/blob/0e1429663d167a2c5cded0d9130374eb586a18c0/src/v0/destinations/tiktok_ads/data/TikTokTrack.json>) supported by TikTok Ads and drops all other fields in the event. See [TikTok Ads standard fields](<https://business-api.tiktok.com/portal/docs?id=1741601162187777>) documentation for more information.

## Page

RudderStack does not send any page-related properties to TikTok. Once you make a [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call, TikTok automatically fetches all the page-related properties.

The following snippet highlights a sample `page` call:
    
    
    rudderanalytics.page();