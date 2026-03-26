# JSON Column Support

Send event data that is not defined by a fixed schema.

* * *

  * __6 minute read

  * 


This guide shows you how to use the JSON column feature while sending events to your warehouse destinations.

## Overview

With RudderStack’s **JSON column** feature, you can:

  * Ingest semi-structured event data not defined by a fixed schema.
  * Directly store a nested event payload in your warehouse columns without worrying about the length limit.


This JSON column feature is supported for all event types ([`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>), [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>), [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>), [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>), [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>)) and their associated attributes/properties (`context`, `traits`, `properties`, etc.). You can use it to define JSON columns in any of the following scenarios:

  * At the event level
  * In your transformations
  * While configuring a warehouse destination in RudderStack


> ![warning](/docs/images/warning.svg)
> 
> JSON column support is only applicable for new columns — you **cannot** alter or convert existing warehouse columns to JSON columns using this feature.

## Supported destinations

RudderStack supports the JSON column feature for the below destinations:

Destination| Name in the `integrations` object  
---|---  
[Amazon Redshift](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/>)| `RS`  
[Google BigQuery](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/>)| `BQ`  
[PostgreSQL](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/postgresql/>)| `POSTGRES`  
[Snowflake](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>)| `SNOWFLAKE`  
  
## How to use the JSON column feature

You can use the JSON column feature in any of the following scenarios:

### 1\. At the event level

Include the exact path from the event payload in your event code using the SDK’s `integrations` parameter.

Note that your SDK must be configured to load the integration object. See the following guides for more information:

  * [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#loading-options>) (`integrations` object)
  * [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#integrations>)
  * [Android (Java) — Legacy](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#enabledisable-events-for-specific-destinations>)
  * [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/event-payload-customization-options/#integrations>)
  * [iOS (Obj-C) — Legacy](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#filter-events-for-specific-destinations>)


An example that defines JSON columns for the Snowflake warehouse using the JavaScript SDK is shown:
    
    
    "integrations": {
      "SNOWFLAKE": { // Use RS, BQ, or POSTGRES for other warehouses
        "options": {
          "jsonPaths": ["track.properties.testMap.nestedMap", "track.context.ctestMap.cnestedMap"]
        }
      }
    }
    

See Important rules for the `jsonPaths` parameter section for more information on specifying paths for properties to be set as JSON columns.

### 2\. In transformations

You can apply JSON columns through [transformations](<https://www.rudderstack.com/docs/transformations/overview/>) that override event-level declarations:

For example, the following transformation applies the JSON column to the `product_clicked` type of `track` events coming from a particular source:
    
    
    export function transformEvent(event, metadata) {
      const meta = metadata(event);
      if (event.event === 'product_clicked' && meta.sourceId === "source_id" && meta.destinationType === "SNOWFLAKE") { // ex: BQ, POSTGRES, RS
        if (!event.integrations) event.integrations = {};
        event.integrations["SNOWFLAKE"] = {
          options: {
            jsonPaths: ["track.properties.testMap.nestedMap", "track.context.ctestMap.cnestedMap"]
          }
        }
      }
      return event;
    }
    

In the above transformation, `nestedMap` and `cnestedMap` are defined as JSON columns by adding `track.properties.testMap.nestedMap` and `track.context.ctestMap.cnestedMap` in the `jsonPaths` list.

See Important rules for the `jsonPaths` parameter section for more information on specifying paths for properties to be set as JSON columns.

### 3\. While configuring a warehouse destination

You can also configure JSON columns in the RudderStack dashboard by entering comma-separated paths in the **JSON columns** dashboard setting.

[![JSON column setting in RudderStack dashboard](/docs/images/dw-integrations/json-column-setting.webp)](</docs/images/dw-integrations/json-column-setting.webp>)

Note the following:

  * Make sure to specify the full path of the JSON properties in this setting, including the event’s type.
  * This setting applies to all the events (of the specified event type) sent to the warehouse destination.


#### Examples

Click the below examples for more information on how to declare the JSON paths for different event types.

**Track events**  


If your `track` event payload looks as follows:
    
    
    {
      "type": "track",
      "properties": {
        "testMap": {
          "nestedMap": {
              "dynamic_property_1": "value_1",
              "dynamic_property_2": "value_2"
          }
        }
      }
    }
    

Then, specify the JSON path for the `nestedMap` property in the dashboard setting as:

**Option 1** : Specify with event type, as `track.properties.testMap.nestedMap`:

![JSON column setting in RudderStack dashboard](/docs/images/dw-integrations/json-column-dashboard-setting.webp)

**Option 2** : Shorthand (applies to `track.properties` object only), as `testMap.nestedMap`:

![JSON column setting in RudderStack dashboard](/docs/images/dw-integrations/json-column-example.webp)**Other events**  


Consider the following `identify` event payload:
    
    
    {
      "type": "identify",
      "context": {
        "testMap": {
          "nestedMap": {
              "dynamic_property_1": "value_1",
              "dynamic_property_2": "value_2"
          }
        }
      }
    }
    

Then, specify the JSON path as `identify.context.testMap.nestedMap`, as shown:

![JSON column setting in RudderStack dashboard](/docs/images/dw-integrations/json-column-example-2.webp)

> ![warning](/docs/images/warning.svg)
> 
> Specifying just `testMap.nestedMap` would fail here because it would only apply to `track` events by default and **not** the `identify` events.

## Important rules for `jsonPaths`

Note the following critical requirements for using the JSON column feature correctly:

#### Default behavior without event type

If you do not specify the full property path that includes the event type, for example, if you specify just `testMap.nestedMap`, then RudderStack applies the setting **only** to the `properties` object of `track` events.

#### Specifying event type

  * When you include the full path including the event type, for example, `identify.context.testMap.nestedMap`, RudderStack applies the setting to the specified event object (`context` in this case).
  * The objects must be present within the event—**not at the top level**.


#### Exact path matching

The property paths specified in the `jsonPaths` parameter must exist in the event in the exact format.

See the Examples section for more information.

##### **Examples**

Click the below examples for more information on how to declare the JSON paths for different event types.

**Track events**  


For the following `track` event payload:
    
    
    {
      "type": "track",
      "properties": {
        "testMap": {
          "nestedMap": {
              "dynamic_property_1": "value_1",
              "dynamic_property_2": "value_2"
          }
        }
      }
    }
    

**Option 1** : Specify with event type:
    
    
    "integrations": {
      "All": true,
      "SNOWFLAKE": { // RS for Redshift, BQ for BigQuery, POSTGRES for PostgreSQL.
        "options": {
          "jsonPaths": ["track.properties.testMap.nestedMap"]
        }
      }
    }
    

**Option 2** : Shorthand (applies to `track.properties` object only)
    
    
    "integrations": {
      "All": true,
      "SNOWFLAKE": { // RS for Redshift, BQ for BigQuery, POSTGRES for PostgreSQL.
        "options": {
          "jsonPaths": ["testMap.nestedMap"] 
        }
      }
    }
    

**Other events**  


Consider the following `identify` event payload:
    
    
    {
      "type": "identify",
      "context": {
        "testMap": {
          "nestedMap": {
              "dynamic_property_1": "value_1",
              "dynamic_property_2": "value_2"
          }
        }
      }
    }
    

The `jsonPath` declaration must be as follows:
    
    
    "integrations": {
      "All": true,
      "SNOWFLAKE": { // RS for Redshift, BQ for BigQuery, POSTGRES for PostgreSQL.
        "options": {
          "jsonPaths": ["identify.context.testMap.nestedMap"] 
        }
      }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Using just `testMap.nestedMap` would fail here because it would only apply to `track` events by default and **not** the `identify` events.

## Warehouse-specific data types

See the following guides for more information on working with semi-structured data in different warehouses and their limitations:

Warehouse| Data type| Reference  
---|---|---  
Redshift| SUPER| [Documentation](<https://docs.aws.amazon.com/redshift/latest/dg/r_SUPER_type.html>)  
BigQuery| STRING  
  
See more information on how RudderStack treats the JSON columns as strings in this FAQ.| [Documentation](<https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions>)  
PostgreSQL| JSONB| [Documentation](<https://www.postgresql.org/docs/current/datatype-json.html>)  
Snowflake| VARIANT| [Documentation](<https://docs.snowflake.com/en/sql-reference/data-types-semistructured.html#variant>)  
  
## FAQ

#### Which events are supported in the JSON column feature?

The JSON column feature supports the following event types:

  * [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>)
  * [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>)
  * [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>)
  * [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>)
  * [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>)


#### Which data types are supported in the JSON column feature?

The JSON data type includes String, Integers, Float, Arrays, Booleans, and Maps.

#### How can I use the JSON column feature in BigQuery?

BigQuery stores JSON as strings. You can query this data using BigQuery’s JSON functions.

See the [BigQuery documentation](<https://cloud.google.com/bigquery/docs/reference/standard-sql/json_functions>) for more information.

#### How does RudderStack determine a column’s data type?

RudderStack determines a column’s data type based on the first event value during the first sync.

#### Why aren’t my existing columns converted to JSON after enabling this feature?

The JSON column feature only applies to **new** columns. It does not alter or convert columns that already exist in your warehouse schema. RudderStack treats the warehouse schema as the source of truth and does not modify existing column types automatically to avoid any unintended impact on your data pipeline.

For example, if a column like `cart_viewed` already exists in your table, enabling the JSON column feature does not change its data type — it remains as-is.

#### Can I use the JSON column feature to add event properties to the `tracks` table?

No — the `tracks` table only stores contextual information (contextual fields, IDs, timestamps, etc.). Event-specific properties set via the `properties` key are stored in their dedicated event name tables (for example, if your `track` event is called `button_clicked`, the properties are stored in the `button_clicked` table). The JSON column feature **does not change** this behavior.

If you need specific event properties available in the `tracks` table for cross-event analysis, consider the following alternatives:

  * Use a [transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to move the required properties into the `context` object of your events
  * Create a SQL view in your warehouse that joins the `tracks` table with your event-specific tables on the relevant keys.