# Event Deduplication in RudderStack

Learn how RudderStack deduplicates events during processing.

* * *

  * __3 minute read

  * 


This guide details how RudderStack deduplicates events during processing.

## What is deduplication?

Rudderstack’s [SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) ensure at least once delivery of events. However, there can be cases where an event is sent multiple times due to retries (as a result of network issues, etc.)

With deduplication, RudderStack ensures an event is not processed multiple times, with a goal of **exactly once delivery**.

## How deduplication works

RudderStack SDKs assign a immutable UUID for every event called `messageId` and it is included in every event. This `messageId` is unchanged even during event retries and has the same value as assigned initially.

When RudderStack processes an event, it checks if a particular `messageId` is already processed and if yes, drops it. If it’s not processed already, RudderStack processes the event and stores the `messageId` for future lookups.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack recommends using the SDKs’ default `messageId` behavior to avoid any deduplication issues and data loss.
> 
> However, if you want to customize the `messageId` behavior, make sure that different events do not end up with the same `messageId`. Otherwise, RudderStack treats them as duplicates — it processes the first event and drops the subsequent events.
> 
> For example, if two separate users send two events with the same `messageId`, only one of the two events is processed.

### Does deduplication promise exactly once delivery?

While our system is designed with the goal of exactly once delivery, there are certain conditions under which exactly once delivery cannot be guaranteed. RudderStack cannot guarantee event deduplication in the following cases:

  * If the event is received outside the dedup window of 7 days.
  * Technical issues (like network interruption, etc.) that prohibit a a `messageId` from being stored after processing an event. This is a rare exception and is **very unlikely** to happen.
  * When a customer’s server nodes are scaled up or down as per their requirement (to handle peak traffic, for example). In such cases, the data in the existing nodes isn’t copied over to the new nodes and event duplication is possible.


## Deduplication time window

RudderStack’s deduplication time window is **7 days** \- this means that it stores a `messageId` for 7 days. If an event that RudderStack processed 8 days back reappears, it is processed again.

## Identify duplicates in your data store

A sample SQL query to get duplicate IDs (`messageId`) in [Snowflake](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>) is shown below:
    
    
    SELECT id, COUNT(*)
    FROM your_table 
    GROUP BY id
    HAVING COUNT(*) > 1
    

A sample SQL query to get the duplicate IDs along with their columns in Snowflake is shown below:
    
    
    WITH duplicate_ids AS (
        SELECT id
        FROM your_table
        GROUP BY id
        HAVING COUNT(*) > 1
    )
    SELECT yt.*
    FROM your_table
    JOIN duplicate_ids d ON yt.id = d.id
    ORDER BY yt.id ASC;