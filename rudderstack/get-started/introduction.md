# Introduction to RudderStack

Build flexible, secure, end-to-end data pipelines on your warehouse.

* * *

  * __3 minute read

  * 


RudderStack is a **warehouse native customer data platform** that helps data teams deliver value across the entire data activation lifecycle - from collection to unification and activation.

With RudderStack, you can:

  * Deploy enterprise-grade SDKs and streaming pipelines to collect behavioral events from all of your websites, apps, and backend systems.
  * Forward event data to your entire stack using 200+ destination integrations.
  * Solve identity resolution and model a comprehensive customer 360 data set in your data warehouse.
  * Sync customer 360 data from your warehouse to business tools.
  * Build powerful use cases like attribution, propensity scoring, and real-time personalization on top of your customer 360 data.


> ![success](/docs/images/tick.svg)
> 
> RudderStack is warehouse-native, meaning it does not store or persist any data. All the data loads and modeling happen with full transparency in your data warehouse or data lake.

## Overview

The following self-guided tour gives you a detailed overview of the RudderStack platform:

## Collect

  * Gather event stream data using the state-of-the art [SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) and [cloud app sources](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/>).
  * Enforce strict [data quality and compliance](<https://www.rudderstack.com/docs/data-governance/overview/>) controls at the source, eliminating expensive cleanup and simplifying regulatory compliance.
  * Transform and enrich your event data by implementing custom logic in JavaScript or Python using RudderStack’s robust [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) framework.
  * Sync data to over 200 [destinations](<https://www.rudderstack.com/docs/destinations/overview/>) including data warehouses, data lakes, and all kinds of business tools.


## Unify

  * Use [Profiles](<https://www.rudderstack.com/docs/profiles/overview/>) to centralize and resolve customer identities and build features on top of it to create a 360 view of the customer.


## Activate

  * Sync enriched warehouse data to various business tools using [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>).
  * Simplify generation of attribution data sets for your first and last touch paid campaigns using the [Attribution Data App](<https://www.rudderstack.com/docs/profiles/data-apps/attribution/>).
  * Leverage the [Propensity Scores Data App](<https://www.rudderstack.com/docs/profiles/data-apps/propensity/>) to predict the likelihood of certain user actions like product purchases, churn, etc.
  * Use the [Real-time Personalization Data App](<https://www.rudderstack.com/docs/profiles/data-apps/real-time-personalization/>) to make your customer 360 data available for your personalization use cases.


## Platform features

The RudderStack platform comes in two flavors:

  * **RudderStack Cloud** : RudderStack Cloud is a managed platform, including APIs and an intuitive UI, that enables your team to take advantage of all RudderStack features across the collection, unification, and activation products.


> ![success](/docs/images/tick.svg)
> 
> See the features walkthrough, [sign up for free](<https://app.rudderstack.com/signup/>), and check out our [pricing page](<https://www.rudderstack.com/pricing/>) to select the RudderStack Cloud plan that best suits your needs.

  * **RudderStack Open Source** : RudderStack Open Source includes only our event streaming and integrations features, with limited access to features like [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>). Running RudderStack Open Source for event streaming requires you to set up your own [data plane](<https://www.rudderstack.com/docs/resources/rudderstack-architecture/>) and is ideal for highly technical data teams with platform engineering resources.


Some other platform-specific features are:

  * **Production-ready** : Many companies like StatPearls, Wyze, Joybird, and more, use RudderStack for their data collection and activation use cases.
  * **No event cap per MTU** : RudderStack is fully pay-as-you-use with no cap on events per MTU. You can send billions of events without worrying about overrunning your event budget.
  * **High Availability** : With a sophisticated error handling and retry system, RudderStack ensures your data is delivered even during network or destination downtime.
  * **Segment-compatible** : RudderStack is fully compatible with Segment, making it easy for you to integrate the RudderStack SDKs into your app without any complex instrumentation. Your events will keep flowing to the destinations (including data warehouses) as before. See the [Segment Migration Guide](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/>) for more information.