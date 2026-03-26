# Shopify App Identity Stitching

Learn how RudderStack implements identity management depending on your Shopify store setup.

* * *

  * __3 minute read

  * 


RudderStack’s **Shopify Source Solution** includes two main components that leverage Shopify’s webhook topics - tracking events from the **client** and **server**. As these two components are separate, the identities for the tracked events will likely not align - leading to duplicate user profiles created in downstream tools and fragmented user journeys.

This guide explains how to implement identity management based on your Shopify store setup.

## RudderStack’s ID stitching approach

The common factor that ties the tracked events on the client-side to the events tracked via Shopify’s webhook topics is the [Shopify Cart](<https://shopify.dev/docs/api/ajax/reference/cart>).

By following the steps corresponding to your store setup, you can make sure RudderStack can do the following:

  * Use the **cart token** to ensure the `anonymousId` is the same for client-side events and for the webhook events.
  * Map the `anonymousId` to `userId` (if available) to unify anonymous activity with known user data across client-side events and webhook events.


### Store fully hosted on a Shopify template

If you have installed the RudderStack Shopify Source Solution by following [these instructions](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/scenarios/#1-store-fully-hosted-on-shopify-template>), then RudderStack automatically stitches the identities from the client and the server and no additional configuration is required.

> ![warning](/docs/images/warning.svg)
> 
> Make sure you have enabled the **RudderStack App Embed Script** during the [RudderStack Shopify App setup](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/scenarios/#setup-shopify-template>) as it is **required** for effective identity stitching.

[![RudderStack App Embed Script setting](/docs/images/event-stream-sources/shopify/rudderstack-app-embed-script.webp)](</docs/images/event-stream-sources/shopify/rudderstack-app-embed-script.webp>)

#### Buy Now race condition

For Shopify stores fully hosted on a Shopify template, there is a scenario where RudderStack cannot immediately stitch identities due to a race condition that occurs when a user clicks the **Buy Now** button on a product page. When this happens, Shopify creates a new cart token and triggers webhook events **before** RudderStack can update the cache with the newly created cart token.

In this case, RudderStack hashes the cart token and provides that as the `anonymous_id` for those events, so they can be ingested properly. Soon after the user clicks **Buy Now** and the race condition is complete, RudderStack is able to update the cache with the new cart token and all subsequent events are properly stitched.

For all events coming from the webhook topics, RudderStack hashes the cart token and provides the hashed value in the `traits` object so that these events can be resolved in downstream tools, irrespective of whether the user identity could be stitched or not.

### Headless setups

The approach for ensuring accurate identity stitching is the same regardless of whether your Shopify store has a [hybrid headless setup](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/scenarios/#hybrid-headless-store>) with a Shopify-hosted checkout or a [fully headless store](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/scenarios/#fully-headless-store>).

In these setups, as the recommend approach is to not use the **Client Side Event Tracking using Web Pixel** setting, RudderStack is not able to stitch the identities automatically. Hence, you will need to make a manual HTTP request instead.

The steps for making the requests are as follows:

  1. Note your **cart token** when you create a Shopify cart on your site.
  2. Make a request to your RudderStack Shopify source endpoint. This HTTP `POST` request leverages the details persisted by RudderStack and uses the **cart token** to ensure the RudderStack `anonymousId` is the same for client-side events and for the webhook events:


    
    
    curl --location --globoff 'https://{dataplane-url}/v1/webhook?writeKey={writekey}' \
    --header 'Content-Type: application/json' \
    --data '{
      "event": "rudderIdentifier",
      "pixelEventLabel": true,
      "anonymousId": <rudderAnonymousId-value>,
      "action": "stitchCartTokenToAnonId",
      "cartToken": <cart_token>,
      "cart": <cart_object>
    }'
    

  3. Make the following HTTP `POST` request to map the `anonymousId` to `userId` to unify anonymous activity with known user data across client-side events and webhook events.


    
    
    curl --location --globoff 'https://{dataplane-url}/v1/webhook?writeKey={writekey}' \
    --header 'Content-Type: application/json' \
    --data '{
      "event": "rudderIdentifier",
      "pixelEventLabel": true,
      "anonymousId": <rudderAnonymousId-value>,
      "action": "stitchUserIdToAnonId",
      "userId": <userId>,
    }'
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to replace the placeholders in the above requests with their actual values.