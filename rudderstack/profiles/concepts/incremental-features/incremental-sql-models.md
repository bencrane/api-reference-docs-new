# Incremental SQL ModelsBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Incremental SQL Models Beta

Learn about incremental SQL models and how they enable incremental processing for complex stateful patterns.

* * *

  * __3 minute read

  * 


This guide explains incremental SQL models and how they enable incremental processing for complex stateful patterns.

## Overview

Incremental SQL models are [SQL models](<https://www.rudderstack.com/docs/profiles/concepts/sql-models/>) that dereference their own previous materialization to enable incremental processing. Incremental SQL models are the raw foundation of incremental features. They are general-purpose and enable any incremental SQL pattern, including advanced use cases like windowed incremental features that require complex stateful processing beyond what simple incremental entity vars can express.

> ![info](/docs/images/info.svg)
> 
> Instead of recalculating from all historical data on every run, incremental SQL models reuse previously computed results and only process new data that has arrived since the last checkpoint.

## What are incremental SQL models?

An incremental SQL model is a SQL-template model that:

  * Uses `this.DeRef()` with `pre_existing=true` to reference a previous materialization of itself
  * Merges previous state with new data instead of recalculating from scratch
  * Handles both incremental processing (when baseline exists) and full refresh (when no baseline exists)


> ![info](/docs/images/info.svg)
> 
> Unlike regular SQL models that process all data on each run, incremental SQL models process only new data that arrived since the last checkpoint and merge it with previous state.

## How incremental SQL models work

When you define an incremental SQL model, Profiles stores previous materializations as checkpoints, identifies new data that has arrived since the baseline checkpoint, merges the previous state with new data using your SQL logic, and produces updated results that become the new checkpoint.

> ![warning](/docs/images/warning.svg)
> 
> **Mandatory requirement** :
> 
> All inputs used by incremental SQL models must have `contract: is_append_only: true` configured in the input’s `contract`. Without this configuration, delta models cannot be generated and incremental processing will not work.
> 
> See [Incremental SQL Models Developer Documentation](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>) for configuration details.

## When to use incremental SQL models

Use incremental SQL models when:

  * You want to reduce warehouse costs when processing large historical datasets (millions or billions of rows)
  * New data arrives regularly (daily, hourly, or more frequently)
  * The volume of new data is significantly smaller than your total dataset
  * Your use case requires stateful processing that cannot be expressed with simple aggregations


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** For simple aggregations like `SUM`, `MIN`, `MAX`, `COUNT`, prefer using [Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>) with `merge` property. For averages and arrays, use [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>).
> 
> Incremental SQL models are best for complex scenarios requiring stateful processing.

## Relationship to other Profiles features

Incremental SQL models work alongside other Profiles capabilities:

  * **SQL Models** : Incremental SQL models are specialized [SQL models](<https://www.rudderstack.com/docs/profiles/concepts/sql-models/>) that dereference their own past, using the same `sql_models.yaml` structure and `model_spec` configuration as regular SQL models. Both regular and incremental SQL models can be materialized as tables, views, or ephemeral sources.
  * **Incremental Features** : Incremental SQL models enable incremental processing for complex patterns that cannot be expressed using simple incremental entity vars.
  * **Checkpoints** : Incremental SQL models rely on [checkpoints](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>) to reference previous materializations and enable incremental processing.


## Supported patterns

Incremental SQL models support two main pattern categories:

Pattern| Description  
---|---  
[Incremental input window models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/#incremental-input-window-models>)| Tracking recent activity or maintaining rolling windows of data (e.g., MAU/DAU)  
[Composite key models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/#composite-key-models>)| Per-dimension aggregations where you need one value per (entity_id, dimension_id) composite key pair  
  
## See also

  * [Incremental SQL Models Developer Documentation](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>): Implementation guide with examples
  * [SQL Models](<https://www.rudderstack.com/docs/profiles/concepts/sql-models/>): Overview of SQL models in Profiles
  * [Incremental Features](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/>): Introduction to incremental features
  * [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>): Understanding checkpoints and how they enable incremental computation


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/concepts/feature-views/>)