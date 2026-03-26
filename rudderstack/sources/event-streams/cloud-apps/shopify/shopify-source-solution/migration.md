# Shopify App Migration Guide

Learn how to migrate from your existing Shopify implementation to the new Shopify Source Solution.

* * *

  * __less than a minute

  * 


Whether you are migrating from RudderStack’s [legacy Shopify app](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/legacy-app/>) or have another third-party or custom implementation for tracking events on your Shopify store, the migration to RudderStack’s new Shopify app is quick and easy.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack recommends running the new RudderStack Shopify app **in parallel** with your existing implementations for a short period of time to ensure the data flows as expected.

## Migrate from RudderStack’s legacy Shopify app

As RudderStack’s legacy Shopify app uses a different mechanism to track the client-side events, you can install both the apps simultaneously onto your Shopify store. Set up a separate Shopify source in RudderStack for the new app to make sure your events coming from the legacy app and the new app are sent to separate sources during the migration period. You can then eventually disconnect the source configured for the legacy app, as required.

## Migrate from third-party or custom implementations

Similar to above case, you can install RudderStack’s Shopify app in parallel to your other tracking implementations. Ensure that a new Shopify source is created in RudderStack so that the events can be sent through separate sources during the migration period.