# Compound AggregationsBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Compound Aggregations Beta

Learn how to implement compound incremental aggregations like averages and arrays.

* * *

  * __10 minute read

  * 


This guide explains compound aggregations and how to implement them as incremental features in Profiles.

## Overview

Compound aggregations require intermediate calculations or multiple steps, each implemented as a simple composable aggregation. They break complex aggregations into component parts that can be maintained incrementally.

## Motivation: When and why to use compound aggregations

Use compound aggregations when:

  * You need to compute averages (`AVG`, `WEIGHTED_AVG`), which cannot be computed directly incrementally
  * You need to select values based on min/max of another column (`MIN_BY`, `MAX_BY`)
  * You need to replace window functions (`LAST_VALUE`, `FIRST_VALUE`) with incremental alternatives
  * You need to aggregate arrays or lists that require union and sorting operations
  * You need boolean aggregations (`BOOLOR_AGG`, `BOOLAND_AGG`)
  * Your aggregation requires multiple intermediate calculations


Compound aggregations use:

  * Component parts (like sum and count for averages)
  * Intermediate entity vars maintained incrementally
  * Final calculations that combine components


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** If compound aggregations don’t fit your use case, consider [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>) for stateful processing or complex transformations.

## Real-world examples

Here are common use cases that map to compound aggregations:

Use case| Pattern| Example  
---|---|---  
**Average order value**|  AVG using sum/count| Average purchase amount across all orders  
**Average session duration**|  AVG using sum/count| Average time spent per session  
**Weighted average rating**|  WEIGHTED_AVG using weighted sum/weight sum| Average product rating weighted by number of reviews  
**List of countries visited**|  Array aggregation| Sorted list of unique countries a user has visited  
**Array of product IDs**|  Array aggregation| List of all product IDs a user has purchased  
**Most recent login platform**|  MIN_BY/MAX_BY with helper| Platform of the most recent login event  
**First campaign source**|  MIN_BY/MAX_BY with helper| Campaign source from the earliest identification  
**Has ever enabled push**|  Boolean aggregation| Whether a user has ever enabled push notifications  
  
## Average (AVG) using component features

`AVG` cannot be computed directly incrementally. Express it using sum and count components:

  * **Sum component** : Maintain sum incrementally using `SUM` with `SUM` merge
  * **Count component** : Maintain count incrementally using `COUNT` with `SUM` merge (counts from previous checkpoints are summed together)
  * **Average calculation** : Divide sum by count in a final entity var with division by zero protection


### Example: Average order value
    
    
    - entity_var:
        name: sum_of_order_values
        select: SUM({{orders.amount}})
        merge: SUM({{rowset.sum_of_order_values}})
        from: inputs/orders
        is_feature: false
        description: Sum of order values (used for average calculation)
    
    - entity_var:
        name: count_of_orders
        select: COUNT({{orders.order_id}})
        merge: SUM({{rowset.count_of_orders}})
        from: inputs/orders
        is_feature: false
        description: Count of orders (used for average calculation)
    
    - entity_var:
        name: avg_order_value
        select: "CASE WHEN {{user.count_of_orders}} > 0 THEN {{user.sum_of_order_values}} / {{user.count_of_orders}} ELSE 0 END"
        description: Average order value across all orders
    

**How it works** :

  1. **Sum component** : Maintains total sum incrementally using `SUM` with `SUM` merge
  2. **Count component** : Maintains total count incrementally using `COUNT` with `SUM` merge (counts from previous checkpoints are summed together)
  3. **Average calculation** : Divides sum by count using `{{user.var_name}}` syntax, with division by zero protection


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Mark sum and count components with `is_feature: false` since they’re intermediate calculations. The average is computed on-the-fly from the incrementally maintained components.

### Workflow
    
    
    Input Data → [Sum Component (Incremental)] → Final Calculation
               → [Count Component (Incremental)] ↗
    

  1. Profiles creates intermediate tables for sum and count components
  2. Both components are maintained incrementally using simple aggregation patterns
  3. The average is computed by dividing sum by count (with division by zero protection)


## Weighted Average (WEIGHTED_AVG) using component features

`WEIGHTED_AVG` cannot be computed directly incrementally. You can express it using weighted sum and sum of weights components:

  * **Weighted sum component** : Maintain sum of (value × weight) incrementally using `SUM` with `SUM` merge
  * **Sum of weights component** : Maintain sum of weights incrementally using `SUM` with `SUM` merge
  * **Weighted average calculation** : Divide weighted sum by sum of weights in a final entity var with division by zero protection


### Example: Weighted average product rating
    
    
    - entity_var:
        name: weighted_sum_of_ratings
        select: SUM({{reviews.rating}} * {{reviews.review_count}})
        merge: SUM({{rowset.weighted_sum_of_ratings}})
        from: inputs/reviews
        is_feature: false
        description: Sum of (rating × review_count) for weighted average calculation
    
    - entity_var:
        name: sum_of_review_counts
        select: SUM({{reviews.review_count}})
        merge: SUM({{rowset.sum_of_review_counts}})
        from: inputs/reviews
        is_feature: false
        description: Sum of review counts (weights) for weighted average calculation
    
    - entity_var:
        name: weighted_avg_rating
        select: "CASE WHEN {{user.sum_of_review_counts}} > 0 THEN {{user.weighted_sum_of_ratings}} / {{user.sum_of_review_counts}} ELSE 0 END"
        description: Weighted average product rating across all reviews
    

**How it works** :

  * **Weighted sum component** : Maintains sum of (value × weight) incrementally using `SUM` with `SUM` merge -**Sum of weights component** : Maintains total sum of weights incrementally using `SUM` with `SUM` merge
  * **Weighted average calculation** : Divides weighted sum by sum of weights using `{{user.var_name}}` syntax, with division by zero protection


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Mark weighted sum and sum of weights components with `is_feature: false` since they’re intermediate calculations. The weighted average is computed on-the-fly from the incrementally maintained components.

### Workflow
    
    
    Input Data → [Weighted Sum Component (Incremental)] → Final Calculation
               → [Sum of Weights Component (Incremental)] ↗
    

  1. Profiles creates intermediate tables for weighted sum and sum of weights components
  2. Both components are maintained incrementally using simple aggregation patterns
  3. The weighted average is computed by dividing weighted sum by sum of weights (with division by zero protection)


## Array aggregations

For array aggregations, use `ARRAY_UNION_AGG` or `ARRAY_SORT` in the `merge` property to combine arrays from previous checkpoints with new arrays.

> ![warning](/docs/images/warning.svg)
> 
> **Warehouse-specific syntax** : Array aggregation syntax varies by warehouse. The examples in this section are specific to Snowflake. Adjust syntax for your warehouse.

### Example: List of countries visited
    
    
    - entity_var:
        name: countries_list
        select: ARRAY_AGG(DISTINCT {{tracks.country}}) WITHIN GROUP (ORDER BY {{tracks.country}})
        merge: ARRAY_SORT(ARRAY_UNION_AGG({{rowset.countries_list}}))
        from: models/tracks
        where: country IS NOT NULL
        description: Sorted list of unique countries
    

**How it works** :

  1. **Select clause** : Creates an array of distinct countries from new data, sorted

  2. **Merge property** :

     * `ARRAY_UNION_AGG({{rowset.countries_list}})`: Unions previous and new arrays, removing duplicates
     * `ARRAY_SORT(...)`: Sorts the final array


### Array merge functions

Select function| Merge function| Notes  
---|---|---  
`ARRAY_AGG(...)`| `ARRAY_UNION_AGG({{rowset.feature_name}})`| Unions arrays, removing duplicates  
`ARRAY_AGG(...)`| `ARRAY_SORT(ARRAY_UNION_AGG({{rowset.feature_name}}))`| Unions and sorts arrays  
  
## MIN_BY / MAX_BY with ordering helper

`MIN_BY` and `MAX_BY` select a value from the row with the minimum or maximum of another column. These are common replacements for window functions like `FIRST_VALUE` and `LAST_VALUE`.

> ![warning](/docs/images/warning.svg)
> 
> **Required:`_by_param` helper var.**
> 
> When using `MIN_BY` or `MAX_BY` in a `merge` clause, you **must** define a companion entity var (conventionally suffixed `_by_param`) that tracks the ordering column. Omitting this helper breaks incremental runs because the merge has no ordering context from previous checkpoints.

### Example: Most recent login platform
    
    
    - entity_var:
        name: last_login_platform
        select: MAX_BY({{logins.platform}}, {{logins.timestamp}})
        merge: MAX_BY({{rowset.last_login_platform}}, {{rowset.last_login_platform_by_param}})
        from: inputs/logins
        description: Platform of the most recent login
    
    - entity_var:
        name: last_login_platform_by_param
        select: MAX({{logins.timestamp}})
        merge: MAX({{rowset.last_login_platform_by_param}})
        from: inputs/logins
        is_feature: false
        description: Ordering helper for last_login_platform
    

**How it works** :

  1. **Main var** : `MAX_BY(platform, timestamp)` selects the platform from the row with the latest timestamp
  2. **Helper var** : `MAX(timestamp)` tracks the latest timestamp across checkpoints
  3. **Merge** : `MAX_BY({{rowset.last_login_platform}}, {{rowset.last_login_platform_by_param}})` compares the previous value’s timestamp with the new value’s timestamp and keeps the one with the later timestamp


### Example: First purchase store
    
    
    - entity_var:
        name: first_purchase_store
        select: MIN_BY({{orders.store_name}}, {{orders.order_date}})
        merge: MIN_BY({{rowset.first_purchase_store}}, {{rowset.first_purchase_store_by_param}})
        from: inputs/orders
        description: Store where the user made their first purchase
    
    - entity_var:
        name: first_purchase_store_by_param
        select: MIN({{orders.order_date}})
        merge: MIN({{rowset.first_purchase_store_by_param}})
        from: inputs/orders
        is_feature: false
        description: Ordering helper for first_purchase_store
    

### MIN_BY / MAX_BY merge reference

Select function| Merge function| Helper var  
---|---|---  
`MIN_BY(value_col, order_col)`| `MIN_BY({{rowset.feature}}, {{rowset.feature_by_param}})`| `MIN(order_col)` with `MIN` merge  
`MAX_BY(value_col, order_col)`| `MAX_BY({{rowset.feature}}, {{rowset.feature_by_param}})`| `MAX(order_col)` with `MAX` merge  
  
### When you can skip the `_by_param` helper

You can skip the helper only when the ordering column is irrelevant to the merge. For example, when you always want the latest value and don’t need to track when it changed. In practice, this is rare — however when in doubt, include the helper.

## Boolean aggregations

For boolean OR aggregations, use `BOOLOR_AGG` in both `select` and `merge`:

### Example: Has user ever enabled push notifications
    
    
    - entity_var:
        name: has_ever_enabled_push
        select: BOOLOR_AGG(COALESCE({{settings.push_enabled}}, false))
        merge: BOOLOR_AGG({{rowset.has_ever_enabled_push}})
        from: inputs/settings
        description: Whether the user has ever enabled push notifications
    

**How it works** : `BOOLOR_AGG` returns `true` if any value in the group is `true`. Since boolean OR is composable (once `true`, always `true`), previous and new results can be merged directly.

### Boolean merge reference

Select function| Merge function| Notes  
---|---|---  
`BOOLOR_AGG(...)`| `BOOLOR_AGG({{rowset.feature_name}})`| Boolean OR: true if any value is true  
`BOOLAND_AGG(...)`| `BOOLAND_AGG({{rowset.feature_name}})`| Boolean AND: true only if all values are true  
  
> ![warning](/docs/images/warning.svg)
> 
> **Warehouse-specific syntax** : `BOOLOR_AGG` and `BOOLAND_AGG` are Snowflake functions.
> 
> For other warehouses, use equivalent functions (for example, `LOGICAL_OR` / `LOGICAL_AND` in BigQuery, `BOOL_OR` / `BOOL_AND` in Redshift and Databricks).

## Replace window functions

Window functions like `LAST_VALUE`, `FIRST_VALUE`, `LAG`, and `LEAD` cannot be used in incremental entity vars because they require scanning all data to determine row ordering. Replace them with composable alternatives.

### Common replacements

Window function| Incremental replacement| Pattern  
---|---|---  
`LAST_VALUE(col) OVER (ORDER BY ts)`| `MAX_BY(col, ts)`| MIN_BY/MAX_BY with helper  
`FIRST_VALUE(col) OVER (ORDER BY ts)`| `MIN_BY(col, ts)`| MIN_BY/MAX_BY with helper  
`ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`| Not directly replaceable| Use [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)  
`LAG()`, `LEAD()`| Not directly replaceable| Use [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)  
  
### Example: Replace LAST_VALUE with MAX_BY
    
    
    # Before (non-incremental, uses window function)
    - entity_var:
        name: last_known_city
        select: last_value(city)
        from: inputs/events
        window:
          order_by:
            - timestamp
        where: city IS NOT NULL
    
    # After (incremental, uses MAX_BY with helper)
    - entity_var:
        name: last_known_city
        select: MAX_BY({{events.city}}, {{events.timestamp}})
        merge: MAX_BY({{rowset.last_known_city}}, {{rowset.last_known_city_by_param}})
        from: inputs/events
        where: {{events.city}} IS NOT NULL
        description: Most recent city from events
    
    - entity_var:
        name: last_known_city_by_param
        select: MAX({{events.timestamp}})
        merge: MAX({{rowset.last_known_city_by_param}})
        from: inputs/events
        where: {{events.city}} IS NOT NULL
        is_feature: false
        description: Ordering helper for last_known_city
    

### Example: Replace FIRST_VALUE with MIN_BY
    
    
    # Before (non-incremental, uses window function)
    - entity_var:
        name: first_campaign_source
        select: first_value(campaign_source)
        from: inputs/identifies
        window:
          order_by:
            - timestamp
        where: campaign_source IS NOT NULL
    
    # After (incremental, uses MIN_BY with helper)
    - entity_var:
        name: first_campaign_source
        select: MIN_BY({{identifies.campaign_source}}, {{identifies.timestamp}})
        merge: MIN_BY({{rowset.first_campaign_source}}, {{rowset.first_campaign_source_by_param}})
        from: inputs/identifies
        where: {{identifies.campaign_source}} IS NOT NULL
        description: Campaign source from first identification
    
    - entity_var:
        name: first_campaign_source_by_param
        select: MIN({{identifies.timestamp}})
        merge: MIN({{rowset.first_campaign_source_by_param}})
        from: inputs/identifies
        where: {{identifies.campaign_source}} IS NOT NULL
        is_feature: false
        description: Ordering helper for first_campaign_source
    

## When compound aggregations don’t work

Compound aggregations may not be sufficient when:

  * **You need activity windows** : Tracking recent activity over time windows (like MAU/DAU) requires [Incremental SQL Models with Incremental Input Windows](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>).
  * **You need per-object aggregations** : Instead of one value per user, you need one value per (user_id, object_id) pair, where object_id could be product_id, location_id, or any other dimension. This requires [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>).
  * **You need complex business logic** : Multi-step transformations with conditional logic may require [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>).


> ![warning](/docs/images/warning.svg)
> 
> **Input-vars cannot be built incrementally**
> 
> An `entity_var` dependent on an `input_var` cannot be incremental. To enable incremental features, replace the `input_var` with an [Incremental SQL Model](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>) and reference the model from the `entity_var` instead.

## Best practices

  * Break `AVG` into sum and count components with separate `merge` properties
  * Break `WEIGHTED_AVG` into weighted sum (value × weight) and sum of weights components with separate `merge` properties
  * Always define a `_by_param` helper var when using `MIN_BY`/`MAX_BY` in merge clauses
  * Replace `LAST_VALUE` window functions with `MAX_BY`, and `FIRST_VALUE` with `MIN_BY`
  * Mark intermediate entity vars (helpers, components) with `is_feature: false` to avoid exposing them as features
  * Add division by zero protection when computing averages (use `CASE WHEN count > 0 THEN sum/count ELSE 0 END` for AVG, or `CASE WHEN sum_of_weights > 0 THEN weighted_sum / sum_of_weights ELSE 0 END` for WEIGHTED_AVG)
  * Use `ARRAY_UNION_AGG` for array aggregations to maintain deduplication
  * Be aware of warehouse-specific syntax differences for array and boolean operations
  * Verify incremental results match full refresh results


## Troubleshooting

Issue| Solution  
---|---  
Average calculation returns incorrect values| Verify that sum and count components are correctly maintained incrementally and include division by zero protection  
Weighted average calculation returns incorrect values| Verify that weighted sum (value × weight) and sum of weights components are correctly maintained incrementally and include division by zero protection  
Division by zero errors| Add `CASE WHEN count > 0 THEN sum/count ELSE 0 END` for AVG, or `CASE WHEN sum_of_weights > 0 THEN weighted_sum / sum_of_weights ELSE 0 END` for WEIGHTED_AVG  
Array aggregation syntax errors| Check warehouse-specific syntax requirements (Snowflake, BigQuery, etc.)  
Duplicate values in arrays| Ensure `ARRAY_UNION_AGG` is used in `merge` property to remove duplicates  
Intermediate features appearing in output| Mark intermediate entity vars with `is_feature: false`  
Missing `_by_param` helper for MIN_BY/MAX_BY| Define a companion entity var (suffixed `_by_param`) that tracks the ordering column with `is_feature: false`  
MIN_BY/MAX_BY merge returns wrong value| Verify the `_by_param` helper uses the same `from`, `where`, and ordering column as the main var  
Boolean aggregation syntax errors| Use warehouse-appropriate function: `BOOLOR_AGG` (Snowflake), `LOGICAL_OR` (BigQuery), `BOOL_OR` (Redshift/Databricks)  
  
## See more

  * [How to Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>)
  * [Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>)
  * [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)
  * [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>)
  * [Entity Vars](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/var-groups/entity-var/>)


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/incremental-features/simple-aggregations/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)