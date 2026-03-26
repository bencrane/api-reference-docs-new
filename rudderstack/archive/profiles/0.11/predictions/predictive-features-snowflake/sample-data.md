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


RudderStack provides a sample data set for users walking through the Snowflake guide to implement the Predictions feature. This dataset is available in the [Snowflake marketplace](<https://app.snowflake.com/marketplace/listing/GZT0Z856CMJ/rudderstack-inc-rudderstack-event-data-for-quickstart>).

The tables provide all of the needed data to run Profiles and Predictions jobs through the automated UI process as well as the code-based YAML workflow.

## What tables are included in the data set?

The data set includes 4 tables of RudderStack event data:

  * `PAGES` \- page view events from anonymous and known users
  * `TRACKS` \- summarized tracked user actions (like login, signup, order_completed, etc.)
  * `IDENTIFIES` \- identify calls run when a user provides a unique identifier (i.e., upon singup)
  * `ORDER_COMPLETED` \- detailed payloads from tracked order_completed events


As of January 2023, here are the approximate number of rows in each table:

  * `PAGES`: ~43k
  * `TRACKS`: ~14k
  * `IDENTIFIES`: ~4.8k
  * `ORDER_COMPLETED`: ~2.2k


These volumes follow the pattern of a normal eCommerce conversion funnel (pageview, signup, order). Specifically, here’s a rough breakdown of the user journey by volume:

  * 30% - never sign in
  * 10% - sign in but never add an item to cart
  * 40% - add to cart and abandon
  * 20% - make purchases


> ![info](/docs/images/info.svg)
> 
> Note that this data includes _future_ data until Apr 2024, and starts in June 2023. This is to ensure that future users can still run the project with ‘current’ data. Our team will refresh the data periodically throughout the year.

## What properties are included in the data set?

This data set includes a _subset_ of the standard properties found in our [Warehouse Schema Spec](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) for each table.

The required columns for running Profiles and Predictions projects are present.

Note that we intentionally limited the number of columns to make the data set easily understandable.

### What user information is included in the data set?

This data set contains a total of ~10k unique users by `anonymousId`. About half of those unique users (~4.8k) are known users (with an associated `identify` call).

User data includes a subset of our standard properties for `identify` calls. (We intentionally limited the number of columns to make the data set easily understandable. )

All of the email addresses were randomly generated and no PII was used in the generation of this data set.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/predictions/predictive-features-snowflake/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/predictions/predictive-features-snowflake/prerequisite/>)