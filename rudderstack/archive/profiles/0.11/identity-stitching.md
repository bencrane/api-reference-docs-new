# Identity Stitching

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Identity Stitching

Stitch multiple identifiers together to create a unified and comprehensive profile.

* * *

  * __4 minute read

  * 


## How to perform identity stitching?

You can use the RudderStack’s [identity stitching model](<https://www.rudderstack.com/docs/archive/profiles/0.11/example/id-stitcher/>) to define the identifiers you want to combine together. You can also define the input sources like [Event Stream](<https://www.rudderstack.com/docs/sources/event-streams/>) sources, which automatically produce an identity graph because all the schemas and unique identifiers are known.

## Problem of multiple identities

Companies gather user data across digital touchpoints like websites, mobile apps, enterprise systems like CRMs, marketing platforms, etc. During this process, a single user is identified with multiple identifiers across their product journey, like their email ID, phone number, device ID, anonymous ID, usernames, and more. Also, the user information is spread across dozens of devices, accounts, or products as they often change their devices and use work and personal emails together.

The user data stored in the warehouse contains unstructured objects that represent one or more user (or entity) identities. Competitive businesses seeking to keep an edge with user data need to clarify this mess of data points into an accurate model of customer behavior and build personalized relationships.

To create a unified user profile, it is essential to correlate all of the different user identifiers into one canonical identifier so that all the data related to a particular user or entity can be associated with that user or entity.

This unification step, called **Identity Stitching** , ties all the user data from these tables into a unified view, giving you a 360-degree view of the user.

## Unify identities across all platforms and devices

Identity stitching combines unique identifiers across your digital touchpoints to identify users and create a unified, omnichannel view of your customers.

It matches the different identifiers across multiple devices, digital touchpoints, and other data (like offline point-of-sale interactions) to build a comprehensive identity graph. This identity graph includes nodes (identifiers) and their relationships (edges), and it is generated as a transparent table in the warehouse.

RudderStack performs identity stitching by mapping all the unique identifiers into a single canonical ID (for example, `rudder_id`), then uses that ID to make user feature development easier (for example, summing the payment events against a single `rudder_id`).

[![single identity created from different identities](/docs/images/profiles/id-stitching.webp)](</docs/images/profiles/id-stitching.webp>)

## Identity graph

Identity stitching starts with the creation of an identity graph. The identity graph is a database housing the entity identifiers where you can identify and connect details related to your customer journeys. Further, it stitches them together in one customer profile representing their whole identity.

The most fundamental data in an identity graph is the ID tag associated with a device, account, network, session, transaction, or any other anonymous identifier that can engage with your company. Once you’ve collected this data and associated it with a single customer identity (wherever possible), your customer data becomes more reliable, and you can move on to achieve higher goals.

An identity graph incorporates models that help it in ingesting new information. As you add a new data point with whatever connections are immediately known, the graph database determines if it fits into any existing customer identifier. If there is a clear link - such as a matching device ID or conclusive biographical data like a credit card number - the graph incorporates the data into a relevant user node.

[![identity graph](/docs/images/profiles/identity-graph.webp)](</docs/images/profiles/identity-graph.webp>)

## Notable features

  * Use different input sources like RudderStack’s [Event Stream](<https://www.rudderstack.com/docs/sources/event-streams/>) sources or any existing tables in the warehouse.
  * Merge identities for entities like a user, customer, product, business account, etc.
  * Stitch identities from all the required channels like web, mobile, marketing platforms, etc.
  * Use identity stitching results to develop user features and deliver personalized campaigns.


## Why identity stitching?

  * **Understand user behavior** : Consolidate and connect customer data from various sources to better understand customers’ preferences, behaviors, and interactions across multiple touchpoints.
  * **Provide personalized support** : Deliver personalized marketing messages and experiences to your customers. Ensures that the right message reaches the right person at the right time, increasing the effectiveness of marketing campaigns.
  * **Enrich user profile with features** : Enhance user profiles with additional data points and features. These features can include demographic information, preferences, purchase history, browsing behavior, or any other static or computed data points.


#### See also

  * [Sample identity stitching project](<https://www.rudderstack.com/docs/archive/profiles/0.11/example/id-stitcher/>)
  * [Problem of Identity resolution](<https://www.rudderstack.com/blog/the-tale-of-identity-graph-and-identity-resolution/>)
  * [How to achieve ID mapping in a data warehouse](<https://www.rudderstack.com/blog/identity-graph-and-identity-resolution-in-sql/>)


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/data-modeling/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/feature-development/>)