# Snowflake Sample Data

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Snowflake Sample Data

Sample Snowflake data you can use to run a Profiles project.

* * *

  * __2 minute read

  * 


RudderStack provides a sample dataset for the Snowflake warehouse, available in the [Snowflake marketplace](<https://app.snowflake.com/marketplace/listing/GZT0Z856CMJ/rudderstack-inc-rudderstack-event-data-for-quickstart>). You can use this data to run the Profiles project and [Propensity Scores](<https://www.rudderstack.com/docs/archive/profiles/0.23/data-apps/propensity/>) through the UI or the CLI.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The number of columns in this dataset is intentionally limited to make the dataset easy to understand.
>   * All email addresses are generated randomly.
>   * **No PII is used in the dataset generation**.
> 


The following tables, properties, and user information is included in the dataset:

## Tables

This dataset includes the following RudderStack event data tables and the **approximate** number of rows in each table:

Table| Description| Number of rows  
---|---|---  
`PAGES`| Page view events from anonymous and known users.| ~172k  
`TRACKS`| Summarized tracked user actions (like `login`, `signup`, `order_completed`, etc.).| ~56k  
`IDENTIFIES`| Associated with `identify` calls when the user provides a unique identifier.| ~22k  
`ORDER_COMPLETED`| Detailed payloads from tracked `order_completed` events.| ~1.2k  
  
The events that generate these tables follow the pattern of a standard ecommerce conversion funnel (pageview, signup, order).

> ![info](/docs/images/info.svg)
> 
> This data starts from June 2023 and is valid until mid 2027, ensuring that future users can still use it to run their Profiles projects.

## Properties

This dataset includes a subset of the standard properties found in the [RudderStack Warehouse Schema spec](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) for each table. The required columns for running Profiles and Predictions projects are also present.

### User information

The user data includes a subset of our standard properties for `identify` calls.

This dataset contains a total of ~10k unique users by `anonymousId`. About 5.8k of these unique users are known users (with an associated `identify` call).

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.23/additional-resources/multi-version/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.23/additional-resources/git-url/>)