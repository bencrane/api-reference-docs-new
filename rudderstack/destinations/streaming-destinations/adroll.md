# AdRoll Beta

Send your event data from RudderStack to AdRoll.

* * *

  * __5 minute read

  * 


[AdRoll](<https://www.adroll.com/>) is a digital and growth marketing platform that lets you display relevant ads, engage with your customers, and grow your revenue.

RudderStack supports AdRoll as a destination to which you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Web
  * Refer to it as **Adroll** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the AdRoll native SDK from the `https://s.adroll.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the AdRoll SDK successfully.

## Getting started

Once you have confirmed that the source platform supports sending events to AdRoll, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **AdRoll**.
  2. Assign a name to the destination and click **Next**.


### Connection settings

To successfully configure AdRoll as a destination, you will need to configure the following settings:

[![AdRoll connection settings](/docs/images/event-stream-destinations/adroll-connection-settings.webp)](</docs/images/event-stream-destinations/adroll-connection-settings.webp>)

  * **Advertiser ID** : Enter your AdRoll advertiser ID here.
  * **Pixel ID** : Enter your AdRoll pixel ID here.


> ![info](/docs/images/info.svg)
> 
> For more information on getting your AdRoll advertiser ID and pixel ID, refer to the FAQ section below.

  * **Mapping to trigger the AdRoll Segment ID for the resepective event name** : Enter the event names which you want to map to specific AdRoll audience segments.


> ![info](/docs/images/info.svg)
> 
> For more information on creating new audiences in AdRoll and getting the audience segment ID, refer to the FAQ section below.

> ![info](/docs/images/info.svg)
> 
> When sending events via device mode, RudderStack lets you specify which events should be discarded or allowed to flow through. For more information, refer to the [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.

  * **Use device mode to send events** : As this is a web device mode-only destination, this setting is enabled by default and cannot be disabled.


## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method lets you identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      email: "alex@example.com"
    });
    

RudderStack uses the `identify` call to set a `userId` which is passed to AdRoll every time a subsequent `track` call is made.

> ![info](/docs/images/info.svg)
> 
> `email` is a required attribute for successfully making an `identify` call. RudderStack maps `email` to AdRoll’s `window._adroll_email` property.

> ![info](/docs/images/info.svg)
> 
> It is not mandatory to make an `identify` call every time before making a `track` call.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method lets you capture user events along with the properties associated with them.

RudderStack uses `track` events to segment your users in AdRoll.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      order_id: "123454387",
      products: [
        {
          product_id: "345676543",
          sku: "G214",
          name: "Cards",
          price: 14.99,
          position: 1,
          category: "Games",
          url: "https://www.estore.com/best-seller/1"
        }
      ]
    });
    

To use the RudderStack `track` calls to segment users in AdRoll, you must first create an audience segment in AdRoll. Then, you need to map the audience ID to your corresponding event in the RudderStack dashboard:

[![AdRoll event mapping to audience](/docs/images/event-stream-destinations/adroll-event-mapping.webp)](</docs/images/event-stream-destinations/adroll-event-mapping.webp>)

> ![info](/docs/images/info.svg)
> 
> For more information on creating an audience in AdRoll and mapping it to your events, refer to the FAQ section below.

When the mapped event is triggered, the appropiate pixel is fired in AdRoll and the user is segmented in the audience.

### Property mapping

RudderStack maps the following event properties to the corresponding AdRoll attributes:

RudderStack property| AdRoll attribute| Comments  
---|---|---  
`revenue`| `adroll_conversion_value`| -  
`userId`| `user_id`| -  
`price`| `adroll_conversion_value`| Mapped only for the product type events, for example, `Product Clicked`, `Product Viewed`, `Product Added`.  
`orderId`| `order_id`| -  
`currency`| `adroll_currency`| -  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) method lets you record your website’s page views with any additional relevant information about the viewed page.

RudderStack internally uses the `page` and `track` calls to segment your users.

> ![warning](/docs/images/warning.svg)
> 
> For RudderStack to successfully send both `page` and `track` calls to AdRoll, the events must be mapped to the AdRoll audience segment ID in the RudderStack dashboard.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("Best Seller", {
      path: "/best-seller/1",
      referrer: "https://www.google.com/search?q=estore+bestseller",
      search: "estore bestseller",
      title: "The best sellers offered by EStore",
      url: "https://www.estore.com/best-seller/1"
    });
    

## FAQ

#### Where can I find the AdRoll advertiser ID and pixel ID?

To find the AdRoll advertiser ID and pixel ID, follow these steps:

  1. Log into your [AdRoll dashboard](<https://app.adroll.com/>).
  2. In the left sidebar, go to **Website** under **Audiences**.
  3. Under the **AdRoll Pixel** section, click **View Pixel** :

[![AdRoll view Pixel](/docs/images/event-stream-destinations/adroll-pixel.webp)](</docs/images/event-stream-destinations/adroll-pixel.webp>)

  4. In the resulting pop-up, you can find your AdRoll advertiser ID associated with the `adroll_adv_id` parameter. You can also find the AdRoll pixel ID associated with the `adroll_pix_id` parameter:

[![AdRoll advertiser ID and Pixel ID](/docs/images/event-stream-destinations/adroll-details.webp)](</docs/images/event-stream-destinations/adroll-details.webp>)

#### How do I create a new audience segment in AdRoll?

To create a new audience segment in AdRoll, follow these steps:

  1. Log into your [AdRoll dashboard](<https://app.adroll.com/>).
  2. In the left sidebar, go to **Website** under **Audiences**.
  3. Click **New Audience** :

[![AdRoll new audience](/docs/images/event-stream-destinations/adroll-new-audience.webp)](</docs/images/event-stream-destinations/adroll-new-audience.webp>)

  4. Enter the name of the audience segment in the **Audience Name** field.


> ![info](/docs/images/info.svg)
> 
> Make sure you copy the ID before creating the audience by clicking the **Copy ID to clipboard** link.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports only the **conversion audience** type, so make sure you check the **This is a conversion audience** option.

[![AdRoll new audience](/docs/images/event-stream-destinations/adroll-new-audience-settings.webp)](</docs/images/event-stream-destinations/adroll-new-audience-settings.webp>)

  5. Specify the **Conversion Value** and the duration for which the user should be a part of this audience segment.
  6. Finally, click **Create Audience**.


You can then specify the ID you copied above in the RudderStack dashboard to map specific events to your audience segment:

[![AdRoll event mapping to audience](/docs/images/event-stream-destinations/adroll-event-mapping.webp)](</docs/images/event-stream-destinations/adroll-event-mapping.webp>)