# Incremental FeaturesBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Incremental Features Beta

Learn how to create and use incremental features in your Profiles project.

* * *

  * __3 minute read

  * 


Making a feature incremental improves performance and reduces costs by processing only new data instead of recomputing everything from scratch.

See [Incremental Features Overview](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/>) for more information.

## Quick decision guide

Can you express your logic as…| Use this approach| Read more  
---|---|---  
A single composable function (`SUM`, `MIN`, `MAX`, `COUNT`)| **Single Incremental Entity Var**| [Implementation Guide](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>)  
Combine multiple composable aggregations (for example, `AVG()`=`SUM()`/`COUNT()`)| **Express goal entity var as a composition of multiple Incremental Entity Vars**| [Implementation Guide](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>)  
Window functions, PIVOTs, or advanced logic| **Define an incremental SQL model and define entity vars (without merge) on top**| [Implementation Guide](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)  
  
Follow this decision tree if you’re unsure which approach to use:

[![Incremental features decision tree](/docs/images/profiles/incremental-features/incremental-patterns-decision-tree.webp)](</docs/images/profiles/incremental-features/incremental-patterns-decision-tree.webp>)

### Understand composable functions

**Composable functions** can be computed incrementally by combining results from different time periods:

  * `SUM`, `MIN`, `MAX`, `COUNT` are composable - they can merge results across checkpoints
  * `AVG` is **NOT** composable (you cannot average two averages correctly without knowing the counts)


**Compound composable functions** can be expressed as combinations of simple composable functions:

  * `AVG(x) = SUM(x) / COUNT(x)` \- requires two composable components
  * `WEIGHTED_AVG(x, w) = SUM(x * w) / SUM(w)` \- requires two composable components


This distinction matters because composable functions can use simple merge logic, while non-composable functions like `AVG` require compound aggregations.

## Simple aggregations

**Best for:** Direct aggregations using a single composable `merge` function

### When to use

  * Computing totals, counts, min/max values
  * Using `SUM`, `MIN`, `MAX`, or `COUNT`
  * Straightforward merge operations (for example, sum of previous + new, min/max of previous and new)


### Why start here

  * Minimal configuration (just add a `merge` property)
  * Predictable behavior
  * Best performance
  * Works across all warehouses


### Use cases

Use Case| Function  
---|---  
Total lifetime value| `SUM`  
First purchase date| `MIN`  
Last login time| `MAX`  
Total event count| `COUNT`  
  
### Quick example
    
    
    - entity_var:
        name: total_purchases
        select: SUM({{orders.value}})
        merge: SUM({{rowset.total_purchases}})  # ← Key: merge mirrors select
        from: inputs/orders
    

### Detailed reference

See [Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>) for implementation and detailed examples.

## Compound aggregations

**Best for:** Metrics combining multiple simple aggregations

### When to use

  * Need to calculate averages (sum ÷ count)
  * Combining multiple aggregations
  * Array operations (union, distinct, sort)


### How it works

This approach breaks down complex metrics into simple components, then combines them:
    
    
    # Components
    - entity_var:
        name: order_value_sum
        select: SUM({{orders.value}})
        merge: SUM({{rowset.order_value_sum}})
    
    - entity_var:
        name: order_count
        select: COUNT(*)
        merge: SUM({{rowset.order_count}})
    
    # Combination
    - entity_var:
        name: avg_order_value
        select: "{{user.order_value_sum}} / NULLIF({{user.order_count}}, 0)"
    

### Use cases

Use case| Components  
---|---  
Average order value| sum + count  
Conversion rate| purchase_count + session_count  
List of visited countries| array aggregation + distinct + sort  
  
### Detailed reference

See [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>) for detailed examples and implementation.

## Incremental SQL models

**Best for:** Stateful processing and advanced transformations

### When to use

Use this approach only when entity vars cannot express your logic. For example:

  * Tracking activity windows (MAU/DAU with rolling dates)
  * Maintaining running balances or state
  * Multi-step transformations with conditional logic
  * Complex business rules requiring temporary tables


### How it works

Reference previous model state and merge with new data:
    
    
    -- Previous state
    {{#with this.DeRef()}}
      SELECT * FROM {{this}}
    {{/with}}
    
    UNION ALL
    
    -- New incremental data
    SELECT * FROM new_data
    

### Use cases

Use case| Description  
---|---  
Monthly Active Users (MAU)| Rolling 30-day window with date-based filtering  
Wallet balances| Running balance with credits/debits  
Multi-step ETL| Conditional logic with intermediate calculations  
  
### Detailed reference

See [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>) for detailed examples and implementation.

## Quick reference

Pattern| Complexity| Use when  
---|---|---  
[Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>)| ⭐ Easiest| Single aggregation function  
[Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>)| ⭐⭐ Moderate| Multiple aggregations combined  
[Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)| ⭐⭐⭐ Advanced| Stateful or complex logic  
  
> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Start with simple aggregations first. If your use case doesn’t fit, move to compound aggregations. Use incremental SQL models only when simple and compound aggregations cannot express your requirements.

## See more

  * [How to Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>): Feature-level migration guide
  * [Entity Vars](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/var-groups/entity-var/>)
  * [Features](<https://www.rudderstack.com/docs/profiles/concepts/features/>)
  * [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>)


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/macros-yaml/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/incremental-features/simple-aggregations/>)