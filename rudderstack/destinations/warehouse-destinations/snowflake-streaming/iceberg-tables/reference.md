# Snowflake Streaming to Iceberg Tables Reference

Reference for configuring Snowflake Streaming to Iceberg tables, including settings, data types, schemas, and limitations.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


This guide provides a detailed reference for the **Snowflake Streaming to Iceberg tables** integration, including:

  * Data type mappings between RudderStack events and Snowflake-managed Iceberg tables
  * Table schemas and supported events


Use this guide as a lookup when you design schemas, write queries, or troubleshoot issues.

## Data type mappings

The table below describes how RudderStack event properties map to Snowflake-managed Iceberg column types.

RudderStack type| Iceberg column type| Notes  
---|---|---  
String| `VARCHAR`| Standard string representation  
Integer| `NUMBER(10,0)` or `NUMBER(19,0)`| Iceberg requires explicit precision. RudderStack uses integer types with appropriate precision based on the value range  
Float| `DOUBLE`| Double-precision floating point  
Boolean| `BOOLEAN`| Standard boolean type  
Timestamp| `TIMESTAMP_NTZ(6)`| Timestamp without timezone information and with microsecond precision  
JSON / nested objects| `VARCHAR`| JSON is stored as a string because `VARIANT` is not available in Snowflake-managed Iceberg tables  
  
## Work with JSON data

Because Snowflake-managed Iceberg tables do not currently support the `VARIANT` data type, JSON and nested object data are stored as `VARCHAR` columns that contain JSON strings.

To query nested fields, use `PARSE_JSON` in your Snowflake queries. For example:
    
    
    -- Instead of: SELECT payload:event_name FROM my_table
    -- Use:
    SELECT PARSE_JSON(payload):event_name AS event_name
    FROM your_database.your_schema.tracks;
    

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** When Snowflake adds `VARIANT` support to Iceberg tables (for example, via newer Iceberg table versions), JSON handling may change.
> 
> Always refer to the Snowflake documentation for the latest behavior.

## Timestamp behavior

Snowflake-managed Iceberg tables use `TIMESTAMP_NTZ` for timestamps:

  * Timestamps do **not** store timezone information
  * RudderStack sends timestamps in a normalized form, and Snowflake stores them as `TIMESTAMP_NTZ(6)`
  * If you rely on timezone-aware behavior, you must perform conversions explicitly in your queries, for example using `CONVERT_TIMEZONE`


## Supported tables and events

RudderStack creates a set of Iceberg tables based on the event types that your sources send. The following table summarizes the mapping:

Event type| Table created| Notes  
---|---|---  
`track`| `TRACKS` and event-specific tables (for example, `PAGE_VIEWED`)| Standard event tracking  
`page`| `PAGES`| Page view events  
`screen`| `SCREENS`| Screen view events for mobile and other apps  
`identify`| `IDENTIFIES`| Identity events stored in an append-only table  
`group`| `GROUPS`| Group membership events  
`alias`| `ALIASES`| Identity alias events  
—| `USERS`| **Not created** for Iceberg destinations  
  
> ![info](/docs/images/info.svg)
> 
> For Iceberg-enabled destinations, RudderStack does **not** create a `USERS` table.
> 
> The `USERS` table relies on `MERGE` operations for deduplication, which is not supported in this integration.

## FAQ

See the [Snowflake Streaming to Iceberg Tables FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/iceberg-tables/faq/>) for answers to frequently asked questions on this integration.