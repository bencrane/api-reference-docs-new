# RudderStack Shopify Source Solution Offerings

Learn about the different product offerings in the RudderStack Shopify Source Solution.

* * *

  * __2 minute read

  * 


This guide walks you through the different product offerings as a part of the RudderStack Shopify Source Solution.

## RudderStack Pixel

You can install the [RudderStack Pixel](<https://apps.shopify.com/rudderstack-pixel?show_store_picker=1>) app directly to your Shopify store. This app gives you the option to track Shopify’s [standard pixel events](<https://shopify.dev/docs/api/web-pixels-api/standard-events>). RudderStack automatically tracks these events and transforms them so that they adhere to the [RudderStack Ecommerce Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

Also, this app automatically subscribes you to several of Shopify’s standard webhook topics for server-side ecommerce tracking. RudderStack transforms the event names and properties so that they adhere to the [RudderStack Ecommerce Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

> ![info](/docs/images/info.svg)
> 
> You can find the raw event name (pre-transformation) in the `context.shopifyDetails` object of the event payload.

## Shopify Custom Pixel

[Shopify Custom Pixel](<https://github.com/rudderlabs/shopify-custom-pixel/blob/main/src/index.js>) is a script created and maintained by RudderStack. It listens for Shopify’s [standard pixel events](<https://shopify.dev/docs/api/web-pixels-api/standard-events>) and triggers RudderStack events when they occur.

Because it is a custom pixel, it has relaxed permissions and is able to load the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) on your Shopify store. It also lets you edit the code and add additional events, as required.

### Setup

  1. Copy the code from the [Custom Pixel Github repository](<https://github.com/rudderlabs/shopify-custom-pixel/blob/main/src/index.js>). Alternatively, you can also fork this repo so you can make any changes to the code as per your business requirements.
  2. Paste the code into a custom pixel that you create in your Shopify store.
  3. Specify the [data plane URL](<https://www.rudderstack.com/docs/resources/glossary/#data-plane-url>) and the [Shopify source write key](<https://www.rudderstack.com/docs/resources/glossary/#write-key>) at the top of the code script, as shown:


    
    
    // Mandatory credentials for RudderStack to connect this pixel to your account source.
    // Replace the below values with your own values.
    const DATAPLANE_URL = "<DATA_PLANE_URL>";
    const WRITE_KEY = "<SOURCE_WRITE_KEY>";