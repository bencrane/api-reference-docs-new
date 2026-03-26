# Shopify Event Tracking

Learn about the different Shopify event types and how RudderStack tracks them.

* * *

  * __2 minute read

  * 


This guide walks you through the three methods of tracking Shopify events available in RudderStack’s Shopify Source Solution.

## RudderStack Pixel events

  * The RudderStack Pixel Shopify app automatically listens to and tracks all the Shopify [Standard Events](<https://shopify.dev/docs/api/web-pixels-api/standard-events>).
  * Because of the strict permissions applicable on the app, you **cannot** load the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) on your store. Therefore, all the tracked events are sent to RudderStack via raw HTTP requests.
  * You **cannot** make any customizations to the event tracking or track any custom events.
  * This method only supports [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) integrations and does not support [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) integrations.


## Custom pixel events

  * Similar to the RudderStack Pixel events, the [Shopify Custom Pixel](<https://github.com/rudderlabs/shopify-custom-pixel/blob/main/src/index.js>) also listens to and triggers events for all the Shopify [Standard Events](<https://shopify.dev/docs/api/web-pixels-api/standard-events>).
  * Because of the relaxed permissions for the custom pixels, you can load the RudderStack JavaScript SDK on your Shopify store. All the events are sent to RudderStack via the JavaScript SDK.
  * You can add custom events to the custom pixel code script and edit the tracking script as required.
  * This method supports both cloud mode and device mode integrations.


## Webhook events

  * These events come from standard webhook topic events that Shopify triggers from their server. RudderStack automatically subscribes you to many of the [webhook topics](<https://shopify.dev/docs/api/webhooks?reference=toml#list-of-topics>).
  * These events are sent from Shopify’s server so they are more reliable. However, they may miss some of the client-side context that events from the Pixels may have, for example, page URLs, campaign information, user information, etc.
  * RudderStack generally keeps the webhook topic event name the same but transforms the event properties to align with the [RudderStack Ecommerce Spec](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).
  * This method only supports [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) integrations and does not support [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) integrations.


> ![warning](/docs/images/warning.svg)
> 
> Use [Shopify webhook events](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/mappings/#webhook-events-server-side>) (`Order Created`, `Order Paid`, etc.) as the source of truth for order counts and conversions.
> 
> Frontend web pixel events (like [`checkout_completed`](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/mappings/#pixel-events-client-side>)) are not guaranteed to fire because adblockers can block them or they can be restricted due to user’s cookie consent preferences. As a result, web pixel events may undercount orders. Use them for behavioral analysis only, not for total conversions.
> 
> See the following references for more details:
> 
>   * [Pixel is blocked by ad blockers](<https://community.shopify.dev/t/pixel-is-blocked-by-ad-blockers/26771>)
>   * [Web pixels requesting consent](<https://shopify.dev/docs/apps/build/marketing-analytics/pixels#requesting-consent>)
>