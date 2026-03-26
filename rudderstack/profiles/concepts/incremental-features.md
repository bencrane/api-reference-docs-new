# Incremental FeaturesBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Incremental Features Beta

Learn about incremental features in Profiles and how they improve performance for large datasets.

* * *

  * __3 minute read

  * 


This guide introduces you to the concept of incremental features in Profiles and explains how they improve performance when processing large datasets.

## Overview

Incremental features update existing feature values with newly arrived event data instead of recalculating from the entire historical dataset.

> ![info](/docs/images/info.svg)
> 
> Instead of scanning billions of rows on every run, incremental features reuse previously computed results and only process new data that has arrived since the last run.

## How incremental features work

When you define an incremental feature, Profiles stores previous results in a [checkpoint](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>), identifies new data since the last checkpoint, merges previous values with new calculations using your merge logic, and produces updated feature values.

> ![warning](/docs/images/warning.svg)
> 
> **Mandatory requirement** :
> 
> Inputs used by incremental features require `contract.is_append_only: true` to be configured. Without this configuration, the project may throw an error.
> 
> See [Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>) for configuration details.

> ![warning](/docs/images/warning.svg)
> 
> Features built incrementally may drift slightly with every run due to late-landing data.

## When to use incremental features

Use incremental features when:

  * You want to reduce warehouse costs when processing large historical datasets (millions or billions of rows)
  * New data arrives regularly (daily, hourly, or more frequently)
  * The volume of new data is significantly smaller than your total dataset
  * Your features can be expressed using supported incremental patterns


> ![warning](/docs/images/warning.svg)
> 
> **Not all features can be computed incrementally.**
> 
> Features that require scanning all historical data (such as median or percentile calculations) **cannot** use incremental computation. For such cases, consider using [Timegrains](<https://www.rudderstack.com/docs/profiles/concepts/timegrains/>) and [bundling](<https://www.rudderstack.com/docs/profiles/dev-docs/optimizations/>).

## Relationship to other Profiles features

Incremental features work alongside other Profiles capabilities:

  * **Incremental ID stitching** : The identity graph can also run incrementally, processing only new identity relationships.
  * **Timegrains** : For features that cannot be incremental, timegrains control how frequently they recompute.
  * **Entity Var Bundling** : Groups the execution of `entity_vars` based on their definitions to improve efficiency. This optimization complements incremental features and can help optimize performance for features that cannot be incremental.


> ![info](/docs/images/info.svg)
> 
> Incremental entity vars do not support entity var bundling yet. The bundling algorithm will only bundle non incremental entity vars. Incremental entity vars will run one at a time.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Input vars are generally discouraged due to performance considerations. For incremental processing, consider using entity_vars with `merge` property or incremental SQL models.
> 
> Contact [RudderStack Support](<mailto:support@rudderstack.com>) to discuss specific use cases that may require input vars.

## Understanding composable functions

**Composable functions** are functions that can be merged incrementally by combining results from different time periods:

  * **Simple composable** : `SUM`, `MIN`, `MAX`, `COUNT` \- can be merged directly (e.g., `SUM(period1) + SUM(period2) = SUM(all)`)
  * **Compound composable** : `AVG`, `WEIGHTED_AVG` \- require breaking into multiple simple composable functions (e.g., `AVG = SUM / COUNT`)


Note that **non-composable** functions (e.g., Median, percentiles, `DISTINCT COUNT` (in most warehouses)) cannot be computed incrementally and require full scans.

> ![info](/docs/images/info.svg)
> 
> **AVG is not composable directly** : You cannot average two averages correctly without knowing the counts. For example, averaging 10 (from 5 values) and 20 (from 3 values) doesn’t give you the correct overall average. You need: `(SUM1 + SUM2) / (COUNT1 + COUNT2)`.

## Supported patterns

Profiles supports incremental computation through three main pattern categories:

Pattern| Description  
---|---  
[Simple aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>)| Direct composable aggregations using `SUM`, `MIN`, `MAX`, `COUNT` with merge property  
[Compound aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>)| Aggregations requiring multiple intermediate simple composable aggregations, such as:  
  


  * `AVG(=SUM/COUNT)`
  * `WEIGHTED_AVG(=SUM_OF_WEIGHTED_VALUES/SUM_OF_WEIGHTS)`
  * `LAST_KNOWN_LOCATION(=MAX_BY(location update, update timestamp))`
  * arrays(e.g. `LAST_10_TOUCHPOINTS`)

  
[Patterns requiring input pre-processing before aggregation](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)| An incremental SQL model maintains a running snapshot of input dataset. Non-incremental entity vars are then defined on top of this processed input.  
  
For example, window function cases can be made incremental using an intermediate incremental input window model, like `user_touchpoints_in_last_30_days`, to subsequently define `is_daily_active_user` and `is_monthly_active_user` over it  
  
## See also

  * [Incremental Features Developer Documentation](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/>)
  * [Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>)
  * [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>): Point-in-time snapshots that enable incremental computation


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/concepts/features/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>)