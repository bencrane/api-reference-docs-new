# Yandex.Metrica

Send your event data from RudderStack to Yandex.Metrica.

* * *

  * __5 minute read

  * 


[Yandex.Metrica](<https://metrica.yandex.com/>) is a web analytics platform that lets you get an in-depth understanding of your audience’s behavior and use the insights to drive business growth.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/YandexMetrica>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Yandex.Metrica** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Yandex.Metrica, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Yandex.Metrica**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

To successfully set up Yandex.Metrica as a destination, you need to configure the following settings:

  * **Tag ID** : Enter your Yandex.Metrica tag ID.
  * **Enable Clickmap** : Enable this setting to collect data for [click mapping](<https://yandex.com/support/metrica/code/counter-initialize.html#:~:text=a%20child%20window-,clickmap,-true>).
  * **Enable Tracklinks** : Enable this setting to track user clicks on the [outbound links](<https://yandex.com/support/metrica/code/counter-initialize.html#:~:text=browser%27s%20address%20bar-,trackLinks,-true>).
  * **Enable Accurate Track Bounce** : This setting enables the accurate bounce rate with a non-bounce event that is registered after 15 seconds (15000 ms). For more information on this setting, refer to the [Yandex.Metrica documentation](<https://yandex.com/support/metrica/code/counter-initialize.html#:~:text=Description-,accurateTrackBounce,-true>).
  * **Enable WebVisor** : Enable this setting to use Yandex.Metrica’s [sesssion replay feature](<https://yandex.com/support/metrica/code/counter-initialize.html#:~:text=1%20for%20YAN-,webvisor,-false>).
  * **Container name** : Enter the name of your Yandex.Metrica ecommerce data container that you set while [creating a new counter](<https://yandex.ru/support/metrica/general/creating-counter.html>). If not specified, RudderStack sets it to `dataLayer` by default.
  * **Map your event name with supported Yandex.Metrica event name** : Use this setting to map the RudderStack event to the Yandex.Metrica event selected from the dropdown.
  * **Goal ID** : Enter your Yandex.Metrica goal ID.
  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Yandex.Metrica. For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


> ![info](/docs/images/info.svg)
> 
> Refer to the FAQ section for more information on obtaining the Yandex.Metrica tag ID, container name, and goal ID.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user in Yandex.Metrica. If a contact already exists, RudderStack updates the contact details.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4el9Z', {
          firstName: 'Alex',
          lastName: 'Keener',
          email: "alex@example.com"
        }
    

RudderStack uses Yandex.Metrica’s [`setUserID`](<https://yandex.com/support/metrica/objects/set-user-id.html?lang=en>) method to associate the `userId` with the user’s client ID during a particular session. To update the information of a user with a specfic `userId`, RudderStack uses the [`userParams`](<https://yandex.com/support/zout_metrica-de-2k55914b38f571cgc45c3db06adedbd0/objects/user-params.html?lang=en>) method.

### Supported mappings

The following table lists the mappings between the RudderStack attributes and the Yandex.Metrica properties:

RudderStack property| Yandex.Metrica property  
---|---  
`userId`  
`anonymousId`  
Required| `UserID`  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to send your [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) to Yandex.Metrica.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      order_id: "34897497",
      coupon: "BB20",
      currency: "INR",
      products: [{
          product_id: "43521",
          currency: "INR",
          name: "Rudder Bag",
          price: 3700.99,
          brand: "Nice",
          category: "Bags",
          quantity: 3,
        },
        {
          product_id: "37333",
          currency: "INR",
          name: "RudderStack T-shirt",
          price: 1651.55,
          brand: "Adidas",
          category: "Bags",
          quantity: 3,
        },
      ],
    });
    

### Event mapping

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

The following table lists the default mappings between the RudderStack events and the Yandex.Metrica events:

RudderStack property| Yandex.Metrica property| Description  
---|---|---  
`Product Viewed`| `detail`| View the full description of the product.  
`Product List Viewed`| `detail`| View the full description of the product list.  
`Product Added`| `add`| Add an item to the basket.  
`Product Removed`| `remove`| Remove an item from the basket.  
`Order Completed`| `purchase`| Complete the product purchase.  
  
You can also map any other event to the above Yandex.Metrica events via the dashboard settings.

### Supported property mappings

The following table lists the properties mapping for Yandex.Metrica’s `detail`, `add`, and `remove` events:

RudderStack property| Yandex.Metrica property  
---|---  
`properties.product_id`  
`properties.sku`  
`properties.products[index].product_id`  
`properties.products[index].sku`  
Required, if name is not present.| `id`  
`properties.name`  
`properties.products[index].name`  
Required, if product_id/sku is not present.| `name`  
`properties.brand`  
`properties.products[index].brand`| `brand`  
`properties.category`  
`properties.products[index].category`| `category`  
`properties.coupon`  
`properties.products[index].coupon`| `coupon`  
`properties.position`  
`properties.products[index].position`| `position`  
`properties.price`  
`properties.products[index].price`| `price`  
`properties.quantity`  
`properties.products[index].quantity`| `quantity`  
`properties.variant`  
`properties.products[index].variant`| `variant`  
  
The following mappings are applicable only for the `purchase` event:

RudderStack property| Yandex.Metrica property  
---|---  
`properties.order_id`  
Required| `id`  
`properties.revenue`| `revenue`  
  
## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to send all page view data to Yandex.Metrica.

A sample `page` call is shown below:
    
    
    rudderanalytics.page(
      "Cart",
      "Cart Viewed", {
        referrer: "https://www.mysite.com/search?q=bestseller",
        title: "The best seller items",
        url: "https://www.mysite.com/bestseller/1"
      });
    

RudderStack uses Yandex.Metrica’s [`hit`](<https://yandex.com/support/metrica/objects/hit.html>) method to send all page view data.

### Supported mappings

The following table lists the mappings between the RudderStack attributes and the Yandex.Metrica properties:

RudderStack property| Yandex.Metrica property  
---|---  
`context.page.url`  
Required| `url`  
`context.page.title`| `title`  
`context.page.referrer`| `referer`  
  
## FAQ

#### What is the Yandex.Metrica container name? Where can I find it?

You can set your Yandex.Metrica data container name while setting up your counter for your website:

[![Yandex.Metrica container name](/docs/images/event-stream-destinations/yandex-metrica-container-name.webp)](</docs/images/event-stream-destinations/yandex-metrica-container-name.webp>)

#### Where can I find my Yandex.Metrica tag ID?

To obtain your Yandex.Metrica tag ID, follow these steps:

  1. Log into your [Yandex.Metrica](<https://metrica.yandex.com/>) dashboard.
  2. From the left sidebar, click **Visitors**. You can see the tag ID listed in the dashboard as well as in the URL:

[![Yandex.Metrica tag ID](/docs/images/event-stream-destinations/yandex-metrica-tag-id.webp)](</docs/images/event-stream-destinations/yandex-metrica-tag-id.webp>)

#### Where can I find my Yandex.Metrica goal ID?

To obtain your Yandex.Metrica tag ID, follow these steps:

  1. Log into your [Yandex.Metrica](<https://metrica.yandex.com/>) dashboard.
  2. From the left sidebar, click **Goals**. You can see the goal ID listed in the dashboard against your created targets/goals:

[![Yandex.Metrica goal ID](/docs/images/event-stream-destinations/yandex-metrica-goal-id.webp)](</docs/images/event-stream-destinations/yandex-metrica-goal-id.webp>)