# Simple AggregationsBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Simple Aggregations Beta

Learn how to implement simple incremental aggregations using direct merge functions.

* * *

  * __5 minute read

  * 


This guide explains simple aggregations and how to implement them as incremental features in Profiles.

## Overview

Simple aggregations are direct composable aggregations that combine previous values with new data using straightforward merge functions.

> ![warning](/docs/images/warning.svg)
> 
> **Only composable functions work** : `SUM`, `MIN`, `MAX`, `COUNT` are composable because results from different time periods can be merged correctly. `AVG` is **NOT** composable - you cannot average two averages correctly. For example, averaging 10 (from 5 values) and 20 (from 3 values) doesn’t give the correct overall average of 13.75. Use [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>) for `AVG`.

## Motivation: When and why to use simple aggregations

Use simple aggregations when:

  * You need to compute totals, counts, or min/max values
  * Your aggregation uses composable functions: `SUM`, `MIN`, `MAX`, or `COUNT`
  * The merge operation is straightforward (sum previous + new, take min/max of previous and new)


Simple aggregations are the first pattern to try because they:

  * Require minimal configuration (just add a `merge:` clause)
  * Have predictable behavior
  * Are the most performant incremental pattern
  * Work across all data warehouses


> ![info](/docs/images/info.svg)
> 
> If your use case doesn’t fit simple aggregations, consider [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>) or [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>).

## Real-world examples

Here are common use cases that map to simple aggregations:

Use case| Aggregation| Example  
---|---|---  
**Total lifetime value**| `SUM`| Sum of all purchases across a customer’s lifetime  
**First purchase date**| `MIN`| Earliest timestamp when a customer made their first purchase  
**Last login time**| `MAX`| Most recent timestamp when a user logged in  
**Total event count**| `COUNT`| Total number of events a user has generated  
  
## Supported simple aggregators

Profiles supports the following simple aggregators for incremental features:

### SUM

Use `SUM` for totals and cumulative values.

**Example: Total lifetime value**
    
    
     - entity_var:
        name: total_purchases
        select: SUM({{orders.value}})
        merge: SUM({{rowset.total_purchases}})
        from: inputs/orders
        description: Total purchase value across all orders
    

**How it works** : The `merge` property adds the previous total to the new sum.

### MIN

Use `MIN` for earliest values or minimum values.

**Example: First purchase date**
    
    
     - entity_var:
        name: first_purchase_date
        select: MIN({{orders.order_date}})
        merge: MIN({{rowset.first_purchase_date}})
        from: inputs/orders
        where: {{orders.status}} = "completed"
        description: Date of first completed purchase
    

**How it works** : The `merge` property takes the minimum of the previous and new values.

### MAX

Use `MAX` for latest values or maximum values.

**Example: Last login time**
    
    
     - entity_var:
        name: last_purchase_date
        select: MAX({{orders.order_date}})
        merge: MAX({{rowset.last_purchase_date}})
        from: inputs/orders
        description: Most recent purchase date
    

**How it works** : The `merge` property takes the maximum of the previous and new values.

### COUNT

Use `COUNT` for counting events or rows.

**Example: Total event count**
    
    
     - entity_var:
        name: event_count
        select: COUNT(*)
        merge: SUM({{rowset.event_count}})
        from: inputs/events
        description: Total number of events
    

> ![info](/docs/images/info.svg)
> 
> **Important** : For `COUNT` aggregations, always use `SUM` in the `merge` property, not `COUNT`. You’re summing the counts from previous runs and new data, not counting counts.

**How it works** : The `merge` property adds the previous count to the new count.

## `merge` property syntax

The `merge` property defines how to combine previous feature values (from the checkpoint) with new calculations.

### Basic syntax
    
    
    - entity_var:
        name: feature_name
        select: AGGREGATION_FUNCTION(...)
        merge: MERGE_FUNCTION({{rowset.feature_name}})
        from: inputs/table_name
    

### Merge function reference

Select function| Merge function| Notes  
---|---|---  
`MIN(...)`| `MIN({{rowset.feature_name}})`| Takes minimum of previous and new values  
`MAX(...)`| `MAX({{rowset.feature_name}})`| Takes maximum of previous and new values  
`SUM(...)`| `SUM({{rowset.feature_name}})`| Sums previous and new values  
`COUNT(...)`| `SUM({{rowset.feature_name}})`| Sums counts (not COUNT of counts)  
  
### Rowset reference

In `merge` property, use `{{rowset.feature_name}}` to reference one or more base aggregations from the baseline checkpoint, and the delta aggregation from current checkpoint.

For example, if baseline `ID1`, `ID2` and `ID3` merge into current checkpoint `ID2`, then you would be merging the following rowsets:

  1. All input rows associated with `ID1` and part of baseline.
  2. All input rows associated with `ID2` and part of baseline.
  3. All input rows associated with `ID3` and part of baseline.
  4. All input rows landing between baseline and current checkpoint, and mapped to the merged `ID2`.


**Key points** :

  * `{{rowset.feature_name}}`: References the previous value of `feature_name` from the checkpoint
  * `{{rowset.column_name}}`: References any column from the previous checkpoint
  * `{{this.feature_name}}`: References the new value being computed (used in `merge_where` clauses)


## When simple aggregations don’t work

Simple aggregations may not be sufficient when:

  * **Your aggregation isn’t directly composable** : `AVG`(`WEIGHTED_AVG`) cannot be computed directly. Use [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>) and combine helper aggregations like `SUM(weighted sum)` and `COUNT(sum_of_weights)`.
  * **You need MIN_BY/MAX_BY aggregations** : Selecting a value based on the min/max of another column (for example, `LAST_KNOWN_LOCATION` using `MAX_BY(location, timestamp)` or `FIRST_PURCHASE_STORE` using `MIN_BY(store, purchase_date)`) requires a `_by_param` helper var. See [MIN_BY/MAX_BY with ordering helper](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/#min_by--max_by-with-ordering-helper>).
  * **You need to replace window functions** : `LAST_VALUE`, `FIRST_VALUE`, and other window functions are not composable — replace them with `MAX_BY`/`MIN_BY`. See [Replace window functions](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/#replace-window-functions>).
  * **You need array aggregations** : Lists and arrays require union operations. Use [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>).
  * **You need time window aggregations** : When you need to aggregate running totals, balances including or multi-step aggregations within a time window, you can create an incremental input window using [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>).
  * **You need PIVOT operations** : When you need to transform rows into columns (for example, `last_login_by_device_id` to track the last login time for each device separately). You can use [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>) to achieve this.


## `merge_where` for conditional merging

You can use the `merge_where:` clause to restrict merging to only those **rowsets** that meet specific conditions:
    
    
    - entity_var:
        name: timestamp
        select: MAX({{game_events.timestamp}})
        merge: MAX({{rowset.timestamp}})
        from: inputs/game_events
        where: {{game_events.event_type}} = "BREAK"
        is_feature: false
        description: Timestamp of the most recent break event (used for score lookup)
    
    - entity_var:
        name: score_at_last_break
        select: any_value({{game_events.score}})
        where: {{game_events.timestamp}} = {{user.timestamp}}
        merge: any_value({{game_events.score}})
        merge_where: {{rowset.timestamp}} = {{user.timestamp}}
        from: inputs/game_events
        description: Score at the most recent break event
    

Use `{{rowset.column}}` for previous values and `{{this.column}}` for new values in the condition.

## Best practices

  * Start with simple aggregations before moving to more complex patterns
  * Ensure `merge` property matches the aggregation function
  * For `COUNT`, always use `SUM` in the `merge` property
  * Use `merge_where:` only when you need conditional merging logic
  * Verify incremental results match full refresh results


## Troubleshooting

Issue| Solution  
---|---  
`merge` function does not match aggregation type| Ensure `merge` function matches select aggregation (`SUM` for `SUM`, `MIN` for `MIN`, etc.)  
Missing rowset reference| Use `{{rowset.feature_name}}` to reference previous values from checkpoint  
`COUNT` merge using `COUNT` instead of `SUM`| Use `SUM({{rowset.feature_name}})` for COUNT aggregations  
Incorrect merge results| Verify `merge_where:` conditions are logically correct, if used  
  
## See more

  * [How to Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>)
  * [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>)
  * [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)
  * [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>)
  * [Entity Vars](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/var-groups/entity-var/>)


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/incremental-features/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/incremental-features/compound-aggregations/>)