# Matomo

Send your event data from RudderStack to Matomo.

* * *

  * __10 minute read

  * 


[Matomo](<https://matomo.org/>), formerly Piwik, is an open source web analytics platform. It can be used to derive valuable insights into your website’s visitors and marketing campaigns so as to optimize your strategy and online experience for your visitors.

RudderStack supports Matomo as a destination to which you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Matomo** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Matomo native SDK from the`https://cdn.matomo.cloud/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Matomo SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to Matomo, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Matomo**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully setup Matomo as a destination, you will need to configure the following settings:

  * **Matomo Version** : Choose the Matomo version from the dropdown:

    * **Premise Version** : Choose this option if you have an on-premise Matomo setup.
      * **Premise URL** : Enter the SDK’s CDN URL in this field.
    * **Cloud Version** : Choose this option if you are using Matomo Cloud.
      * **Server URL** : Enter your server URL mentioned under the **JavaScript Tracking Code** section in Matomo dashboard.
  * **Site Id** : Enter your site Id mentioned under the **JavaScript Tracking Code** section in Matomo dashboard.


> ![info](/docs/images/info.svg)
> 
> Refer to the FAQ section below for more information on finding the Server URL and Site Id.

### Event settings

[![Matomo connection settings](/docs/images/event-stream-destinations/matomo-connection-settings-1.webp)](</docs/images/event-stream-destinations/matomo-connection-settings-1.webp>)[![Matomo connection settings](/docs/images/event-stream-destinations/matomo-connection-settings-2.webp)](</docs/images/event-stream-destinations/matomo-connection-settings-2.webp>)[![Matomo connection settings](/docs/images/event-stream-destinations/matomo-connection-settings-3.webp)](</docs/images/event-stream-destinations/matomo-connection-settings-3.webp>)

  * **Mapping to trigger the Matomo Goal ID for the respective Events** : Enter the **Event Name** and the [Goal Id](<https://developer.matomo.org/guides/tracking-javascript-guide#manually-trigger-goal-conversions>) to be triggered when that event is called.


> ![success](/docs/images/tick.svg)
> 
> You can specify multiple **Goal Id’s** for one **Event Name** and vice versa.

  * **Mapping to trigger the Matomo standard events for the respective Events** : Enter the event name and pick the standard event from the dropdown to be triggered when that event is called.


> ![success](/docs/images/tick.svg)
> 
> You can specify multiple **Standard Events** for one **Event Name** and vice versa.

  * **Track All Content Impressions** : Enable this setting to scan the entire DOM for all content blocks and track all impressions, once the DOM ready event has been triggered.
  * **Track Visible Content Impressions** : Enable this setting to scan the entire DOM for all content blocks as soon as the page is loaded. It tracks an impression only if a content block is actually visible. If enabled, also enter the following:
    * **Check on Scroll** : Checks whether the previously hidden content blocks became visible meanwhile after a scroll and if yes, then tracks the impression. It is enabled by default.
    * **Time interval in ms** : Enter the time to rescan the entire DOM for new content impressions. By default, the rescan is done every 750ms. To disable it, pass the value as 0.
  * **Log All Content Blocks On Page** : Enable this setting to log all content blocks found within a page to the console. This is useful while debugging/testing the content tracking.
  * **Enable Heart Beat Timer** : Enable this setting to install a heart beat timer to send additional requests to Matomo to measure the time spent in the visit. These requests will be sent only when the user’s tab is active and in focus and will not track additional actions or pageviews. If enabled, also enter the following:
    * **Active Time in seconds** : Enter the time interval after which a ping request should be sent. The default value is 15 seconds, meaning that if a page is viewed for at least 15 seconds, only then a ping request will be sent.
  * **Enable Link Tracking** : Enable this setting to install link tracking on all applicable link elements.
  * **Disable Performance Tracking** : Enable this setting to disable the page performance tracking.
  * **Enable Cross Domain Linking** : Enable this setting to enable cross domain linking. Refer to the [Matomo document](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=enableCrossDomainLinking>) for more information.
  * **Set Cross Domain Linking Timeout** : Enable this setting to set the cross domain linking timeout (in seconds). If enabled, also enter the following:
    * **Timeout** : Enter the timeout interval. By default, the two visits across domains are linked together when the link is clicked and the page is loaded within a 180 seconds timeout window.
  * **Get Cross Domain Linking Url Parameter** : Enable this setting to get the query parameter to append to links to handle cross domain linking. Refer to the [Matomo document](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=getCrossDomainLinkingUrlParameter>) for more information.
  * **Disable Browser Feature Detection** : Enable this setting to disable the browser feature detection. Refer to the [Matomo document](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=disableBrowserFeatureDetection>) for more information.


### Web device mode settings

[![Matomo connection settings](/docs/images/event-stream-destinations/matomo-connection-settings-4.webp)](</docs/images/event-stream-destinations/matomo-connection-settings-4.webp>)

  * **Use device mode to send events** : As this is a device mode-only destination, this setting is enabled by default and cannot be disabled.


## Identify

RudderStack sets the ID value in the cache to the `userId` or `anonymousId` present in the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm");
    

The following table lists the RudderStack and Matomo property to set the `userId` in the `identify` call:

RudderStack property| Matomo property| Presence| Matomo Method  
---|---|---|---  
`userId`/`anonymousId`| `userId`| Required| `_paq.push(["setUserId","user_id"])`  
  
## Track

> ![warning](/docs/images/warning.svg)
> 
> This destination does not strictly adhere to the [RudderStack Ecommerce Event Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method lets you capture user events along with the properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed",{
    "category": "Orders",
    "action": "Pass",
    "value": 15
    });
    

### Generic events

RudderStack sends a generic `track` call which is a not a standard event or an ecommerce event as a Matomo [`trackEvent`](<https://developer.matomo.org/guides/tracking-javascript-guide#manually-trigger-events>) event.

The following table lists the property mappings between RudderStack and Matomo for `trackEvent`:

RudderStack property| Matomo property| Presence  
---|---|---  
`properties.category`| `category`| Required  
`properties.action`| `action`| Required  
`event`| `name`| Optional  
`properties.value`| `value`| Optional  
  
### Standard events

> ![warning](/docs/images/warning.svg)
> 
> For RudderStack to send an event as a standard Matomo event, you need to specify the event mapping under the **Mapping to trigger the Matomo standard events for the respective Events** setting in the RudderStack dashboard. For more information, refer to the Event settings section above.

RudderStack supports the following Matomo standard events:

  * [Ping](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=test%20content%20tracking.-,ping,-%28%29%20%2D%20Send%20a>)
  * [Track Content Impressions](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=trackContentImpression>)
  * [Track Content Impressions Within Node](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=trackContentImpressionsWithinNode>)
  * [Track Content Interaction](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=trackContentInteraction>)
  * [Track Content Interaction Node](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=trackContentInteractionNode>)
  * [Track Link](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=custom%20revenue%20customRevenue.-,trackLink,-%28%20url%2C%20linkType%20%29>)
  * [Track Site Search](<https://developer.matomo.org/api-reference/tracking-javascript#:~:text=optional%20numeric%20value.-,trackSiteSearch,-%28keyword%2C%20%5Bcategory%5D%2C%20%5BresultsCount%29>)


RudderStack first verifies if an event is mapped to a standard Matomo event. If so, it sends the event to Matomo with some specific properties, as listed in the following sections.

> ![warning](/docs/images/warning.svg)
> 
> These properties should be present in the events for RudderStack to successfully send them to Matomo.

#### Ping

Use this event to send a ping request.

> ![info](/docs/images/info.svg)
> 
> The ping requests do not track new actions. Matomo ignores these requests if they’re sent after a standard visit length.

#### Track Content Impressions

Use this event to track a content impression using the specified values.

RudderStack maps the following event properties to the Matomo standard event properties:

RudderStack property| Matomo property| Description  
---|---|---  
`properties.contentName`| `contentName`| Represents a content block visible in the reports. One name can represent different content pieces.  
`properties.contentPiece`| `contentPiece`| Actual displayed content, for example, path to a video, image, etc.  
`properties.contentTarget`| `contentTarget`| URL of the landing page where the user was directed to after interacting with the block.  
  
#### Track Content Impressions Within Node

Use this event to scan a given DOM node and its associated children for content blocks and track impressions for them, if not done already.

RudderStack maps the following event properties to the Matomo standard event properties:

RudderStack property| Matomo property  
---|---  
`properties.domId`/ `properties.dom_id`| `domId`  
  
#### Track Content Interaction

Use this event to track a content interaction with the specified values.

RudderStack maps the following event properties to the Matomo standard event properties:

RudderStack property| Matomo property  
---|---  
`properties.contentInteraction`| `contentInteraction`  
`properties.contentName`| `contentName`  
`properties.contentPiece`| `contentPiece`  
`properties.contentTarget`| `contentTarget`  
  
#### Track Content Interaction Node

Use this event to track the interaction with a given DOM node or a content block.

RudderStack maps the following event properties to the Matomo standard event properties:

RudderStack property| Matomo property  
---|---  
`properties.domId`/ `properties.dom_id`| `domId`  
`properties.contentInteraction`| `contentInteraction`  
  
#### Track Link

Use this event to log a click from your code.

RudderStack maps the following event properties to the Matomo standard event properties:

RudderStack property| Matomo property| Description  
---|---|---  
`properties.url`/ `message.context.page.url`| `url`| The full URL to be tracked as a click.  
`properties.linkType`| `linkType`| Defines the link type. Can either be `link` for an outlink or `download` for the download link type.  
  
#### Track Site Search

Use this event to track an internal site search for a given keyword with an optional category and specifying the optional search results count in the page.

RudderStack maps the following event properties to the Matomo standard event properties:

RudderStack property| Matomo property  
---|---  
`properties.keyword`/`properties.search`/`message.context.page.search`| `keyword`  
`properties.category`| `category`  
`properties.resultsCount`| `resultsCount`  
  
### Ecommerce events

RudderStack supports and maps the following [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) to the corresponding Matomo [ecommerce events](<https://developer.matomo.org/api-reference/tracking-javascript#ecommerce:~:text=most%20recent%20referrer.-,Ecommerce,-Matomo%20provides%20ecommerce>):

RudderStack Event| Matomo Event  
---|---  
`Product Viewed`| `setEcommerceView`  
`Product Added`| `addEcommerceItem`  
`Product Removed`| `removeEcommerceItem`  
`Order Completed`| `trackEcommerceOrder`  
`Cart Cleared`| `clearEcommerceCart`  
`Update Cart`| `trackEcommerceCartUpdate`  
  
For the above-mentioned events, you can also send specific properties as mentioned in the following sections.

#### Product Viewed

RudderStack maps the `Product Viewed` event to [`setEcommerceView`]([https://developer.matomo.org/api-reference/tracking-javascript#ecommerce:~:text=click%20here.-,setEcommerceView,-(%20productSKU%2C%20productName%2C%20categoryName)](<https://developer.matomo.org/api-reference/tracking-javascript#ecommerce:~:text=click%20here.-,setEcommerceView,-%28%20productSKU%2C%20productName%2C%20categoryName%29>). The following event properties are mapped to the Matomo properties:

RudderStack property| Matomo property| Presence  
---|---|---  
`properties.sku`/`properties.product_id`| `productSKU`| Required  
`properties.name`| `productName`| Required  
`properties.category`| `categoryName`| Required  
`properties.price` (Multiplied by quantity)| `price`| Required  
  
> ![info](/docs/images/info.svg)
> 
> You can view the `Product Viewed` event in the Matomo dashboard only when it is followed by a `page` call.

#### Product Added

RudderStack maps the `Product Added` event name to [`addEcommerceItem`]([https://developer.matomo.org/api-reference/tracking-javascript#ecommerce:~:text=category%20page%20view.-,addEcommerceItem,-(%20productSKU%2C%20%5BproductName%5D%2C%20%5BproductCategory)](<https://developer.matomo.org/api-reference/tracking-javascript#ecommerce:~:text=category%20page%20view.-,addEcommerceItem,-%28%20productSKU%2C%20%5BproductName%5D%2C%20%5BproductCategory%29>). The following event properties are mapped to the Matomo properties:

RudderStack property| Matomo property| Presence  
---|---|---  
`properties.sku`/`properties.product_id`| `productSKU`| Required  
`properties.name`| `productName`| Optional  
`properties.category`| `categoryName`| Optional  
`properties.price` (Multiplied by quantity)| `price`| Optional  
`properties.quantity`| `quantity`| Optional  
  
> ![info](/docs/images/info.svg)
> 
> You can view the `Product Added` event in the Matomo dashboard only when it is followed by an `Update Cart` or `Order Completed` event.

#### Product Removed

RudderStack maps the `Product Removed` event name to [`removeEcommerceItem`](<https://developer.matomo.org/api-reference/tracking-javascript#ecommerce:~:text=in%20the%20order.-,removeEcommerceItem,-%28%20productSKU%20%29%20%2D%20Remove>). The following event properties are mapped to the Matomo properties:

RudderStack property| Matomo property| Presence  
---|---|---  
`properties.sku`/`properties.product_id`| `productSKU`| Required  
  
> ![info](/docs/images/info.svg)
> 
> You can view the `Product Removed` event in the Matomo dashboard only when it is followed by an `Update Cart` or `Order Completed` event.

#### Order Completed

RudderStack maps the `Order Completed` event name to [`trackEcommerceOrder`]([https://developer.matomo.org/api-reference/tracking-javascript#ecommerce:~:text=from%20the%20cart.-,trackEcommerceOrder,-(%20orderId%2C%20grandTotal%2C%20%5BsubTotal)](<https://developer.matomo.org/api-reference/tracking-javascript#ecommerce:~:text=from%20the%20cart.-,trackEcommerceOrder,-%28%20orderId%2C%20grandTotal%2C%20%5BsubTotal%29>). The following event properties are mapped to the Matomo properties:

RudderStack property| Matomo property| Presence  
---|---|---  
`properties.order_id`/`properties.orderId`| `orderId`| Required  
`properties.total`/`properties.revenue`| `grandTotal`| Required  
`properties.subtotal`| `subtotal`| Optional  
`properties.tax`| `tax`| Optional  
`properties.shipping`| `shipping`| Optional  
`properties.discount`| `discount`| Optional  
  
> ![info](/docs/images/info.svg)
> 
> `grandTotal` is not a default property in the `Order Completed` event and needs to be provided by the user. If not provided, RudderStack calculates it manually by iterating through the products array, as shown below:
>     
>     
>     grandTotal = products[0].price * products[0].quantity + …
>     grandTotal += tax + shipping;
>     
> 
> Similarly, `subtotal` is calculated as the total value of all sales, excluding shipping and tax.

#### Update Cart

> ![info](/docs/images/info.svg)
> 
> Although `Update Cart` is not a standard [RudderStack Ecommerce Event](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>), you can still send this event to update your cart and view the items that are currently present in it.

RudderStack also maps the `Update Cart` event name to [`trackEcommerceCartUpdate`](<https://developer.matomo.org/api-reference/tracking-javascript#ecommerce:~:text=trackEcommerceCartUpdate>). The following event properties are mapped to the Matomo properties:

RudderStack property| Matomo property| Presence  
---|---|---  
`properties.total/properties.revenue`| `grandTotal`| Required  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("home","games");
    

> ![info](/docs/images/info.svg)
> 
> RudderStack does not consider any parameters inside the `page` call and simply calls the `trackPageView` event for each `page` call.

## Custom dimensions

Custom dimensions can be used to track any information related to any action or visitors.

> ![warning](/docs/images/warning.svg)
> 
> You can send the custom dimensions to Matomo only through the `track` calls.

RudderStack provides `customDimension` field which can be used inside the `integrations` object, as shown below:
    
    
    {
      integrations: {
        Matomo: {
          customDimension: [{
              dimensionId: <dimension_ID>,
              dimensionValue: <dimension_value>
            },
            {
              dimensionId: 1,
              dimensionValue: ENTERPRISE
            }
          ]
        }
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> Refer to the [Matomo help guide](<https://matomo.org/faq/reporting-tools/data-limits-for-custom-dimensions/>) to know about the data limitations for custom dimensions in Matomo.

> ![info](/docs/images/info.svg)
> 
> RudderStack does not support sending custom variables to Matomo. Matomo recommends using custom dimensions instead. For more information, refer to this [Matomo page](<https://plugins.matomo.org/CustomVariables#description:~:text=This%20feature%20used%20to%20be%20part%20of%20Matomo.%20However%2C%20we%20no%20longer%20plan%20to%20further%20develop%20custom%20variables%20and%20only%20fix%20important%20bugs%20or%20security%20issues%20and%20we%20might%20stop%20supporting%20Custom%20Variables%20in%20the%20future>).

## FAQ

#### Where can I find the Server URL and Site Id?

To find the Matomo Server URL and Site Id:

  1. Log into your [Matomo dashboard](<https://matomo.org/login>).
  2. Go to **Settings** > **Website** > **Tracking Code**.
  3. Under **JavaScript Tracking Code** section, you will find the below:

[![Matomo dashboard](/docs/images/event-stream-destinations/matomo-dashboard.webp)](</docs/images/event-stream-destinations/matomo-dashboard.webp>)

Here, the server URL: `https://rudderstacktest.matomo.cloud/` and site Id: `1`