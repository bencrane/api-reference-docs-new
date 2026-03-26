# Warehouse Schema

Understand the RudderStack schema for warehouse destinations.

* * *

  * __16 minute read

  * 


When sending your events to a data warehouse via RudderStack, you don’t need to define a schema for your event data. RudderStack automatically does that for you by following a predefined warehouse schema.

This guide details the structure of this warehouse schema and the columns created in various tables based on different event types.

## Schema

RudderStack uses the source name (written in snake case, for example, `source_name`) to create a schema in your data warehouse.

> ![success](/docs/images/tick.svg)
> 
> RudderStack treats the warehouse schema as the source of truth. If you manually make any changes to the schema, for example, add or modify a column, or update a column’s data type, RudderStack honors the modified schema and sends the data to the warehouse accordingly.

The following tables are created in your data warehouse for each RudderStack source connected to it:

Name| Description  
---|---  
`<source_name>.identifies`| Every `identify` call sent from the source is stored in this table, including the properties passed as `traits`.  
`<source_name>.users`| RudderStack stores all unique users in this table. Only the latest properties used to identify a user are stored, including the latest `anonymousId`.  
`<source_name>.tracks`| Every `track` call sent from the source is stored in this table. It **does not include** the custom properties present in the event’s `properties` but has some standard properties listed in the Standard properties section below such as `received_at`, `anonymous_id`, `context_device_info`, etc.  
`<source_name>.<track_event_name>`| All the standard properties and the custom properties for a `track` event are stored in this table. The table name is the event name specified in the `track` call, e.g., `Added to Cart`.  
`<source_name>.pages`| Every `page` call sent from the source is stored in this table, including the associated event properties.  
`<source_name>.screens`| Every `screen` call sent from the source is stored in this table, including the associated event properties.  
`<source_name>.groups`| Every `group` call sent from the source is stored in this table, including the associated event properties.  
`<source_name>.aliases`| Every `alias` call sent from the source is stored in this table, including the associated event properties.  
  
The following image highlights the warehouse schema and the relationships between the tables:

[![RudderStack warehouse schema](/docs/images/warehouse-destinations/warehouse-schema.svg)](</docs/images/warehouse-destinations/warehouse-schema.svg>)

> ![info](/docs/images/info.svg)
> 
> All the event properties are stored as top-level columns in the corresponding table. The nested properties are prefixed with the parent key. For example, an event with properties `{ product: { name: iPhone, version: 11 }}` will result in RudderStack creating the columns `product_name` and `product_version`.

## Standard RudderStack properties

RudderStack sets the following standard properties on all above-mentioned tables:

Name| Description  
---|---  
`anonymous_id`| The user’s anonymous ID.  
`context_<prop>`| The context properties set in the event.  
`id`| The unique message ID of the event. Not applicable for the `users` table, as the field be set to the user ID in that case.  
`sent_at`| Captures the time when the event was sent from the client to RudderStack. Conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`.  
`received_at`| Timestamp registered by RudderStack when the event was ingested (received). Conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`.  
`original_timestamp`| Timestamp registered by the RudderStack SDK when the event call was invoked (event was emitted in the SDK).  
`timestamp`| **If not already specified in the payload** , RudderStack calculates this field to account for the client clock skew. The formula used is `timestamp` = `received_at` \- (`sent_at` -`original_timestamp`). Make sure it conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`. For e.g., `2022-02-01T19:14:18.381Z`.  
`event_text`| The name of the event mapped from the `event` key in the `track` event payload.  
`event`| The name of the event table in case of the `track` calls.  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack automatically converts the property names from camel case to snake case. For more information on the properties captured at the API level, refer to the [RudderStack Event Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>) guide.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack reserves the above-mentioned standard properties. In case of any conflict, RudderStack automatically discards the properties set by the user.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack drops any non-standard properties declared at the top level of an event.

## Identify

For every [Identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call, RudderStack creates a record in the `identifies` table and upserts the records in the `users` table based on the `userId`.

> ![success](/docs/images/tick.svg)
> 
> In case of Google BigQuery, you can use the views created over the tables to query for unique users in the dataset. Refer to the [BigQuery documentation](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/#schema-partitioned-tables-views-and-deduplication>) for more details.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify(
      "userId",
      {
        email: "alex@company.com",
        first_name: "Alex",
        last_name: "Keener",
        age: 35,
      },
      {
        context: {
          ip: "0.0.0.0",
        },
        anonymousId: "59b703e3-467a-4a1d-9fe6-da27ed319619",
      }
    )
    

The corresponding schemas created for the `identifies` and `users` tables are shown in the following sections:

#### Table: `identifies`

Column| Type| Example value| Note  
---|---|---|---  
`id`| String| `4d5a7681-e596-40ea-a81c-bf69f9b297f1`| Unique `messageId` generated by RudderStack.  
`user_id`| String| `userId`| The `userId` in the `identify` call.  
`anonymous_id`| String| `59b703e3-467a-4a1d-9fe6-da27ed319619`| -  
`received_at`| Timestamp| `2020-04-26 07:00:45.558`| -  
`sent_at`| Timestamp| `2020-04-26 07:00:45.124`| -  
`original_timestamp`| Timestamp| `2020-04-26 07:00:43.400`| -  
`timestamp`| Timestamp| `2020-04-26 07:00:44.834`| -  
`context_ip`| String| `0.0.0.0`| -  
`context_<prop>`| String, Int| `context_app_version: 1.2.3`, `context_screen_density: 2`| -  
`email`| String| `alex@company.com`| -  
`first_name`| String| `Alex`| -  
`last_name`| String| `Keener`| -  
`age`| Int| `35`| -  
`uuid_ts`| Timestamp| `2020-04-26 07:31:54:735`| Added by RudderStack for debugging purposes. Can be ignored for analytics.  
  
#### Table: `users`

Column| Type| Value| Note  
---|---|---|---  
`id`| String| `userId`| The unique user ID.  
`received_at`| Timestamp| `2020-04-26 07:00:45.558`| -  
`context_ip`| String| `0.0.0.0`| -  
`context_<prop>`| String, Integer| `context_app_version: 1.2.3`, `context_screen_density: 2`| -  
`email`| String| `alex@company.com`| -  
`first_name`| String| `Alex`| -  
`last_name`| String| `Keener`| -  
`age`| Int| `35`| -  
`uuid_ts`| Timestamp| `2020-04-26 07:31:54:735`| Added by RudderStack for debugging purposes. Can be ignored for analytics.  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The `users` table contains the properties from the latest `identify` call made for an user. It only has the `id` column (same as `user_id` in the `identifies` table) and does not have the `anonymous_id` column.
>   * To obtain a user’s `anonymous_id`, you can query the `identifies` table by grouping on the `user_id` column.
> 


#### Skip sending data to `users` table

You can skip sending the event data to the `users` table by setting the `skipUsersTable` option to `true`.

For example, you can add the following transformation that adds an `integrations` object to your event and skips sending the event data to the `users` table:
    
    
    event.integrations = {
        "DELTALAKE": {
            options: {
                skipUsersTable: true
            }
        }
    }
    

Use the following names for your preferred warehouse destination in the above snippet:

Warehouse destination| Name  
---|---  
PostgreSQL| `POSTGRES`  
Snowflake| `SNOWFLAKE`  
Google BigQuery| `BQ`  
Microsoft SQL Server| `MSSQL`  
Databricks Delta Lake| `DELTALAKE`  
ClickHouse| `CLICKHOUSE`  
Amazon S3 Data Lake| `S3_DATALAKE`  
Google Cloud Storage Data Lake| `GCS_DATALAKE`  
Azure Data Lake| `AZURE_DATALAKE`  
Amazon Redshift| `RS`  
Azure Synapse| `AZURE_SYNAPSE`  
  
## Track

For every [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call, RudderStack creates a record in the `tracks` and `<event_name>` table. In addition to the `tracks` table columns, the `<event_name>` table includes the properties set by the user via the `properties` key.

You can also skip sending the event data to `tracks` table by setting the `skipTracksTable` option to `true`.

A sample `track` event named `Add to Cart` is shown below:
    
    
    rudderanalytics.track(
      "Add to Cart", {
        price: 5,
        currency: "USD",
        product_id: "P12345",
        product_name: "N95 Mask",
      }, {
        context: {
          ip: "0.0.0.0",
        },
        anonymousId: "59b703e3-467a-4a1d-9fe6-da27ed319619",
      }
    )
    

The corresponding schemas created for the `tracks` and `add_to_cart` tables are as shown:

#### Table: `tracks`

The `tracks` table stores contextual information like `ip`, `device`, etc. which helps you to perform analytics-related operations on top of it.

Column| Type| Example value| Description  
---|---|---|---  
`id`| String| `4d5a7681-e596-40ea-a81c-bf69f9b297f1`| Unique `messageId` generated by RudderStack.  
`anonymous_id`| String| `59b703e3-467a-4a1d-9fe6-da27ed319619`| The anonymous ID of the user.  
`received_at`| Timestamp| `2020-04-26 07:00:45.558`| Timestamp registered by RudderStack when the event was ingested (received).  
`sent_at`| Timestamp| `2020-04-26 07:00:45.124`| Timestamp set by the SDK when the event was sent from the client to RudderStack.  
`original_timestamp`| Timestamp| `2020-04-26 07:00:43.400`| Timestamp registered by the SDK when the event was invoked (event was emitted in the SDK).  
`timestamp`| Timestamp| `2020-04-26 07:00:44.834`| Calculated by RudderStack to account for the client clock skew. The formula used is: `timestamp` = `received_at` \- (`sent_at` \- `original_timestamp`).  
`context_ip`| String| `0.0.0.0`| -  
`context_<prop>`| String, Integer| `context_app_version: 1.2.3, context_screen_density: 2`| -  
`event`| String| `add_to_cart`| The name of the corresponding event table.  
`event_text`| String| `Add to Cart`| The name of the event.  
`uuid_ts`| Timestamp| `2020-04-26 07:31:54:735`| Added by RudderStack for debugging purposes. Can be ignored for analytics.  
  
#### Skip sending data to `tracks` table

Similar to `users` table, you can skip sending the event data to the `tracks` table by setting `skipTracksTable` to `true`.

The transformation that adds the `integrations` object to your event and skips sending the event data to the `tracks` table:
    
    
    event.integrations = {
        "DELTALAKE": {
            options: {
                skipTracksTable: true
            }
        }
    }
    

Use the following names for your preferred warehouse destination in the above snippet:

Warehouse destination| Name  
---|---  
PostgreSQL| `POSTGRES`  
Snowflake| `SNOWFLAKE`  
Google BigQuery| `BQ`  
Microsoft SQL Server| `MSSQL`  
Databricks Delta Lake| `DELTALAKE`  
ClickHouse| `CLICKHOUSE`  
Amazon S3 Data Lake| `S3_DATALAKE`  
Google Cloud Storage Data Lake| `GCS_DATALAKE`  
Azure Data Lake| `AZURE_DATALAKE`  
Amazon Redshift| `RS`  
Azure Synapse| `AZURE_SYNAPSE`  
  
#### Table: `add_to_cart`

The `add_to_cart` table has the same columns as the `tracks` table. Additionally, it includes the properties set by the user via the `properties` key.

Column| Type| Example value| Note  
---|---|---|---  
`id`| String| `4d5a7681-e596-40ea-a81c-bf69f9b297f1`| Unique `messageId`generated by RudderStack.  
`anonymous_id`| String| `59b703e3-467a-4a1d-9fe6-da27ed319619`| -  
`received_at`| Timestamp| `2020-04-26 07:00:45.558`| -  
`sent_at`| Timestamp| `2020-04-26 07:00:45.124`| -  
`original_timestamp`| Timestamp| `2020-04-26 07:00:43.400`| -  
`timestamp`| Timestamp| `2020-04-26 07:00:44.834`| -  
`context_ip`| String| `0.0.0.0`| -  
`context_<prop>`| String, Int| `context_app_version: 1.2.3, context_screen_density: 2`| -  
`event`| String| `add_to_cart`| The name of the event table.  
`event_text`| String| `Add to Cart`| The name of the event.  
`price`| Int| `5`| -  
`currency`| String| `USD`| -  
`product_id`| String| `P12345`| -  
`product_name`| String| `N95 Mask`| -  
`uuid_ts`| Timestamp| `2020-04-26 07:31:54:735`| Added by RudderStack for debugging purposes. Can be ignored for analytics.  
  
## Page/Screen

For every [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>)/[`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call, RudderStack creates a record in the corresponding `pages` or `screens` table.

A sample `page` event is shown below:
    
    
    rudderanalytics.page(
      "Cart",
      "Cart Viewed",
      {
        path: "/cart",
        title: "Shopping Cart",
        url: "https://rudderstack.com",
      },
      {
        context: {
          ip: "0.0.0.0",
        },
        anonymousId: "59b703e3-467a-4a1d-9fe6-da27ed319619",
      }
    )
    

The corresponding schema created for the `pages`/`screens` table is as shown:

#### Table: `pages`/`screens`

Column| Type| Example value| Note  
---|---|---|---  
`id`| String| `4d5a7681-e596-40ea-a81c-bf69f9b297f1`| -  
`anonymous_id`| String| `59b703e3-467a-4a1d-9fe6-da27ed319619`| -  
`received_at`| Timestamp| `2020-04-26 07:00:45.558`| -  
`sent_at`| Timestamp| `2020-04-26 07:00:45.124`| -  
`original_timestamp`| Timestamp| `2020-04-26 07:00:43.400`| -  
`timestamp`| Timestamp| `2020-04-26 07:00:44.834`| -  
`context_ip`| String| `0.0.0.0`| -  
`context_<prop>`| String, Integer| `context_app_version: 1.2.3`, `context_screen_density: 2`| -  
`name`| String| `Cart Viewed`| The page name.  
  
RudderStack sets the value of this field to `null` if you do not explicitly declare it in the `page` event.  
`category`| String| `Cart`| The page category.  
`path`| String| `/cart`| -  
`title`| String| `Shopping Cart`| -  
`url`| String| `https://rudderstack.com`| -  
`uuid_ts`| Timestamp| `2020-04-26 07:31:54:735`| Added by RudderStack for debugging purposes. Can be ignored for analytics.  
  
## Group

For every [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call, RudderStack creates a record in the corresponding `groups` table.

A sample `group` call is shown below:
    
    
    rudderanalytics.group(
      "groupId", {
        email: "alex@keener.com",
        first_name: "Alex",
        last_name: "Keener",
        age: 35,
      }, {
        context: {
          ip: "0.0.0.0",
        },
        anonymousId: "59b703e3-467a-4a1d-9fe6-da27ed319619",
      }
    )
    

The corresponding schema created for the `groups` table is as shown:

#### Table: `groups`

Column| Type| Example value| Note  
---|---|---|---  
`id`| String| `4d5a7681-e596-40ea-a81c-bf69f9b297f1`| The group ID associated with the current user.  
`anonymous_id`| String| `59b703e3-467a-4a1d-9fe6-da27ed319619`| -  
`group_id`| String| `groupId`| -  
`received_at`| Timestamp| `2020-04-26 07:00:45.558`| -  
`sent_at`| Timestamp| `2020-04-26 07:00:45.124`| -  
`original_timestamp`| Timestamp| `2020-04-26 07:00:43.400`| -  
`timestamp`| Timestamp| `2020-04-26 07:00:44.834`| -  
`context_ip`| String| `0.0.0.0`| -  
`context_<prop>`| String, Integer| `context_app_version: 1.2.3`, `context_screen_density: 2`| -  
`uuid_ts`| Timestamp| `2020-04-26 07:31:54:735`| Added by RudderStack for debugging purposes. Can be ignored for analytics.  
  
## Alias

For every [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call, RudderStack creates a record in the corresponding `aliases` table.

A sample `alias` call is shown below:
    
    
    rudderanalytics.alias("9bb5d4c2", "e6ab2c5e")
    

#### Table: `aliases`

Column| Type| Example value| Note  
---|---|---|---  
`user_id`| String| `9bb5d4c2`| The new ID associated with the user.  
`previous_id`| String| `e6ab2c5e`| The previous ID associated with the user.  
`received_at`| Timestamp| `2020-04-26 07:00:45.558`| -  
`sent_at`| Timestamp| `2020-04-26 07:00:45.124`| -  
`original_timestamp`| Timestamp| `2020-04-26 07:00:43.400`| -  
`timestamp`| Timestamp| `2020-04-26 07:00:44.834`| -  
`context_ip`| String| `0.0.0.0`| -  
`context_<prop>`| String, Integer| `context_app_version: 1.2.3`, `context_screen_density: 2`| -  
`uuid_ts`| Timestamp| `2020-04-26 07:31:54:735`| Added by RudderStack for debugging purposes. Can be ignored for analytics.  
  
## Clock skew considerations

RudderStack considers the time at its end to be absolute and assumes any difference on the client-side. Thus, the client clock skew is relative.

> ![info](/docs/images/info.svg)
> 
> If not specified in the payload explicitly, RudderStack calculates `timestamp` based on `originalTimestamp` and `sentAt` to account for the client clock skew.

As mentioned in the above section:

Field| Description  
---|---  
`original_timestamp`| Records the actual time when the event occurred at the source.  
`sent_at`| Captures the time when the event was sent from the client to RudderStack.  
`received_at`| The timestamp when the event is received(ingested) by the RudderStack server.  
`timestamp`| Calculated by RudderStack to account for the client clock skew, **IF** the user does not explicitly specify it in the payload.  
  
> ![info](/docs/images/info.svg)
> 
> `sent_at` > `original_timestamp` is **always true**. However, `timestamp` can be more or less than the `original_timestamp`. Refer to the cases below for more details.

### Case 1: `original_timestamp` < `received_at`

The following table demonstrates an example of `original_timestamp` < `received_at`(when the client-side time is less than the time registered by RudderStack):

original_timestamp| sent_at| received_at| timestamp = received_at - (sent_at - original_timestamp)  
---|---|---|---  
2020-04-26 07:00:43.400| 2020-04-26 07:00:45.124| 2020-04-26 07:00:45.558| 2020-04-26 07:00:44.834  
  
In this case, `timestamp` will be **greater** than `original_timestamp`.

### Case 2: `original_timestamp` > `received_at`

The following table demonstrates an example of `original_timestamp` > `received_at`(when the client-side time is more than the time registered by RudderStack):

original_timestamp| sent_at| received_at| timestamp = received_at - (sent_at - original_timestamp)  
---|---|---|---  
2020-04-26 07:00:45.558| 2020-04-26 07:00:46.124| 2020-04-26 07:00:43.400| 2020-04-26 07:00:42.834  
  
In this case, `timestamp` will be **less** than `original_timestamp`.

## Accepted timestamp formats

RudderStack recognizes only the following subsets of the ISO 8601 timestamp format:

  * `2019-09-26`
  * `2009-05-19 14:39:22`
  * `2019-09-26T06:30:12.984Z`
  * `2020-02-11 04:56:55.175116`
  * `2019-09-26T06:30:12.984+0530`
  * `2019-09-26T06:30:12.984+05:30`


> ![warning](/docs/images/warning.svg)
> 
> RudderStack **does not recognize** any other timestamp format apart from the ones mentioned above.

## Reserved keywords

There are some limitations when it comes to using the reserved words in a schema, table, or column names. If these words are used in the event names, traits or properties, RudderStack automatically prefixes an underscore(`_`) when creating the tables or columns for them in your schema.

> ![warning](/docs/images/warning.svg)
> 
> Integers are not allowed at the start of the schema or table name. Such schema, column, or table names will be prefixed with an underscore. For e.g., `25dollarpurchase` will be changed to `_25dollarpurchase`.

The following table lists the warehouse-specific documentation references for reserved keywords:

Warehouse| Reference  
---|---  
Amazon Redshift| [Link](<https://docs.aws.amazon.com/redshift/latest/dg/r_pg_keywords.html>)  
Google BigQuery| [Link](<https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical#reserved-keywords>)  
Snowflake| [Link](<https://docs.snowflake.net/manuals/sql-reference/reserved-keywords.html>)  
  
## How RudderStack determines column data types

RudderStack determines the column’s data type based on its value in the first event (during the first sync). For example, suppose `column_x` is received with the value as `1`. RudderStack then sets the data type of this column as **Integer** in the event table.

### Change an existing column’s data type

> ![info](/docs/images/info.svg)
> 
> You can change the column data type in the warehouse at any point. However, RudderStack applies the changes to the events only from the next sync.

To change a column’s data type:

  1. Create a column in the warehouse with a placeholder name and the required data type.
  2. Cast the data from the original column and load it into the placeholder column.
  3. Drop the original column.
  4. Rename the placeholder column to the original column name.


> ![warning](/docs/images/warning.svg)
> 
> **Important considerations**
> 
>   * The tables will be locked during steps 3 and 4, which may impact realtime data uploads/syncs.
>   * For lengthy operations, consider temporarily halting warehouse operations. See this [FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/#how-do-i-avoid-lags-in-data-syncs-while-heavy-loads-are-running-on-my-data-warehouse>) for more information.
> 


## How RudderStack handles data type mismatches

RudderStack automatically handles type conversion in some common scenarios depending on the warehouse column’s data type.

Incoming data type| Warehouse column data type| Notes  
---|---|---  
All data types **except** String, Text, or JSON| String| RudderStack automatically stringifies the incoming data.  
Integer  
BigInt| Float| RudderStack converts the incoming data to Float.  
Float| Integer  
BigInt| RudderStack converts the incoming data to Integer.  
Integer  
Float  
Boolean| JSON| RudderStack automatically stringifies the incoming data.  
  
In cases where RudderStack cannot typecast the incoming data into the warehouse column-specific data type, the data is sent to the `rudder_discards`table.

See the [rudder-server](<https://github.com/rudderlabs/rudder-server/blob/9e06351b921fb9e6d40878002b8b49efbada1e48/warehouse/schema.go#L25>) GitHub repository for more information and implementation details.

### `rudder_discards` table

Once RudderStack recognizes and sets a data type for a table column, it **does not** accept any values that cannot be cast to that column’s data type.

> ![info](/docs/images/info.svg)
> 
> The values which RudderStack cannot cast are set as `NULL` in the table and stored in the `rudder_discards` table.

The `rudder_discards` table schema is shown below:

Column| Description  
---|---  
`row_id`| The unique identifier (ID) associated with each record in the table. This corresponds to the event’s `messageId` for all tables except for `users` table, where it is `userId`.  
  


> ![info](/docs/images/info.svg)`row_id` is the column which users can use to join with original table and update it as required. As mentioned in the above table, it is set to `messageId` for all tables except the `users` table, where it corresponds to `userId`.  
  
`table_name`| The table name where the full record is inserted, like `tracks`, `add_to_cart`, `identifies` , etc.  
`column_name`| The column (property) name corresponding to the erroneous record value.  
`column_value`| The value that caused the data type mismatch and the record to be discarded.  
`reason`| Detailed reason for discarding the record.  
  
See Discard reasons for more information.  
  
The following snippet highlights a sample event whose properties are discarded due to a data type mismatch:
    
    
    // intial track call using the RudderStack JavaScript SDK
    
    rudderanalytics.track(
      "Add to Cart",
      {
        price: 5, // originally a int value
        currency: "USD",
        product_id: "P12345",
        product_name: "N95 Mask",
        added_at: "2020-05-19 14:39:22", // originally a datetime value
      },
      {
        context: {
          ip: "0.0.0.0",
        },
        anonymousId: "59b703e3-467a-4a1d-9fe6-da27ed319619",
      }
    )
    
    // subsequent track call using the RudderStack JavaScript SDK
    
    rudderanalytics.track(
      "Add to Cart",
      {
        price: "NA", // sent as a string in latest event
        currency: "USD",
        product_id: 789, // sent as int but can be casted into original string data type
        product_name: "N95 Mask",
        added_at: "4 December 2020", // sent as string
      },
      {
        context: {
          ip: "0.0.0.0",
        },
        anonymousId: "59b703e3-467a-4a1d-9fe6-da27ed319619",
      }
    )
    

The subsequent records created in the `rudder_discards` table for the discarded properties from the second event shown in the following table:

Row ID| Table name| Column name| Column value| Reason  
---|---|---|---|---  
`a21620be-6502-44d6-941d-78209a386d58`| `add_to_cart`| `price`| `NA`| `incompatible schema conversion from int to string`  
`1e42b2b3-8b6a-49da-8502-83a8db334375`| `add_to_cart`| `added_at`| `05/25/2020`| `incompatible schema conversion from datetime to string`  
  
#### Discard reasons

RudderStack provides observability into why the event was discarded with descriptive messages, especially in cases where there is a data type mismatch and the event data does not conform to the warehouse schema.

For example:

  * `incompatible schema conversion from string to boolean`
  * `incompatible schema conversion from string to int`
  * `incompatible schema conversion from datetime to string`
  * `incompatible schema conversion from bigint to float`


#### SQL query to analyze discard reasons

You can run the below SQL query on the `rudder_discards` table to analyze the discard reasons:
    
    
    SELECT reason,
           Count(*) AS TOTAL
    FROM   <DATABASE>.<SCHEMA>.rudder_discards -- Replace `<DATABASE>` and `<SCHEMA>` with the actual values.
    GROUP  BY reason
    ORDER  BY reason DESC;
    

The above query groups the records from the `rudder_discards` table by the `REASON` column and calculates the count of occurrences for each reason. Then, it orders the results in descending order of the `REASON` values.

A sample output table after running the above query is shown below:

Reason| Total  
---|---  
incompatible schema conversion from boolean to string| 100  
incompatible schema conversion from string to int| 75  
incompatible schema conversion from string to boolean| 50  
incompatible schema conversion from datetime to string| 25  
incompatible schema conversion from bigint to float| 10  
  
Note that the above table is just sample representation and **does not** include all the possible discard reasons.

## FAQ

#### Can I change the namespace (schema name) of my data warehouse in RudderStack?

Yes, you can. Although the default namespace will be the source name, RudderStack gives you the option to explicitly set the namespace while setting up your warehouse destination. For more information, refer to the [warehouse-specific destination settings](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>) for configuring the namespace in the RudderStack dashboard.

#### Why am I not able to see the properties added at the top level of an event in warehouse destination?

RudderStack drops any non-standard properties (properties apart from the standard properties) declared at the top level of an event. However, you can add such properties in the `context` or `properties` section of the event payload.

> ![info](/docs/images/info.svg)
> 
> For a more comprehensive FAQ list, refer to the [Warehouse FAQ](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/faq/>) guide.