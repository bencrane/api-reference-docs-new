# Snowflake Sample Data

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Snowflake Sample Data

Sample data for Snowflake

* * *

  *  __2 minute read

  * 


RudderStack provides a sample data set for the Snowflake warehouse, available in the [Snowflake marketplace](<https://app.snowflake.com/marketplace/listing/GZT0Z856CMJ/rudderstack-inc-rudderstack-event-data-for-quickstart>). You can use this data to run the Profiles project and [Predictive features](<https://www.rudderstack.com/docs/archive/profiles/0.14/predictions/>) through the UI or the CLI.

> ![info](/docs/images/info.svg)
> 
> The number of columns in this data set are intentionally limited to make the data set easily understandable. Also, all email addresses are generated randomly and no PII is used in the generation of this data set.

The following tables, properties, and user information is included in the data set:

## Tables

This data set includes below-mentioned RudderStack event data tables:

  * `PAGES` \- Page view events from anonymous and known users.
  * `TRACKS` \- Summarized tracked user actions (like `login`, `signup`, `order_completed`, etc.).
  * `IDENTIFIES` \- Identify calls run when a user provides a unique identifier (i.e., upon `signup`).
  * `ORDER_COMPLETED` \- Detailed payloads from tracked `order_completed` events.


As of January 2023, here are the approximate number of rows in each table:

  * `PAGES`: ~43k
  * `TRACKS`: ~14k
  * `IDENTIFIES`: ~4.8k
  * `ORDER_COMPLETED`: ~2.2k


These volumes follow the pattern of a normal eCommerce conversion funnel (pageview, signup, order). Specifically, here’s a rough breakdown of the user journey by volume:

  * 30% - Never sign in
  * 10% - Sign in but never add an item to cart
  * 40% - Add to cart and abandon
  * 20% - Make purchases


> ![info](/docs/images/info.svg)
> 
> Note that this data includes _future_ data until Apr 2024, and starts in June 2023. This is to ensure that future users can still run the project with ‘current’ data. RudderStack team will refresh the data periodically throughout the year.

## Properties

This data set includes a _subset_ of the standard properties found in the [Warehouse schema spec](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) for each table. The required columns for running Profiles and Predictions projects are also present.

### User information

The user data includes a subset of our standard properties for `identify` calls.

This data set contains a total of ~10k unique users by `anonymousId`. About half of these unique users (~4.8k) are known users (with an associated `identify` call).

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.14/get-started/import-from-git/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.14/core-concepts/>)