# Incremental SQL ModelsBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Incremental SQL Models Beta

Learn about incremental SQL models and how to use them for complex stateful processing in Profiles.

* * *

  * __10 minute read

  * 


This guide explains incremental SQL models and how they enable complex stateful processing in Profiles.

## Overview

Incremental SQL models are [SQL models](<https://www.rudderstack.com/docs/profiles/concepts/sql-models/>) that dereference their own previous materialization to enable incremental processing. They enable complex patterns requiring stateful processing, running totals, or multi-step transformations that cannot be expressed using simple incremental entity vars.

See [Incremental SQL Models Overview](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/incremental-sql-models/>) for conceptual information.

## What are incremental SQL models?

An incremental SQL model is a SQL-template model that:

  * Dereferences a previous materialization of itself using `this.DeRef()` with `pre_existing=true`

  * Produces the same final result whether the previous state is available or not (idempotence)

  * Operates with two checkpoints:

    * Current checkpoint: The checkpoint being produced now
    * Baseline checkpoint: A previous checkpoint represented by the previous materialization


When the previous state is present, the model merges its prior state with new/changed inputs; otherwise it runs a full scan.

## When and why to use incremental SQL models

Use incremental SQL models when:

  * **Simple aggregations don’t work** : Your use case requires stateful processing that cannot be expressed with `SUM`, `MIN`, `MAX`, or `COUNT` in your `merge` property
  * **Compound aggregations don’t work** : Your use case requires complex transformations beyond averages or arrays
  * **You need activity windows** : Tracking recent activity over time windows (like MAU/DAU)
  * **You need window functions or composite key aggregations** : Per-dimension aggregations or window-based calculations
  * **You need multi-step transformations** : Complex business logic that requires multiple steps or conditional processing


Incremental SQL models let you:

  * Reference previous computation results using `this.DeRef()`
  * Maintain stateful aggregations across runs
  * Implement complex business logic with full SQL control
  * Handle both incremental and full refresh modes


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** For simple aggregations like `SUM`, `MIN`, `MAX`, `COUNT`, prefer using [Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>) with `merge` property. For averages and arrays, use [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>).
> 
> Incremental SQL models are best for complex scenarios.

## Real-world examples

Some common use cases that map to incremental SQL models are listed below:

Use case| Pattern| Example  
---|---|---  
**Monthly Active Users (MAU)**|  Incremental Input Window Models| Count of users active in the past 30 days  
**Daily Active Users (DAU)**|  Incremental Input Window Models| Count of users active today  
**Account balances by wallet**|  Composite Key Models| Account balance per (user_id, wallet_id) composite key maintained across transactions - each user has multiple wallets with individual balances  
**Recent activity tracking**|  Incremental Input Window Models| Tracking recent interactions within a time window  
  
## Incremental SQL models subcategories

Incremental SQL models can be categorized into two main patterns:

### Incremental input window models

**When to use** : Tracking recent activity or maintaining rolling windows of data.

**Characteristics**

  * Maintain a rolling window of recent interactions (e.g., last 90 days of activity)
  * Track activity over time windows (MAU, DAU, weekly active users)
  * Filter and maintain only recent data incrementally


**Example** : Monthly Active Users (MAU) or Daily Active Users (DAU) where you need to track which users were active in a recent time window.

### Composite key models

**When to use** : Per-dimension aggregations where you need one value per (entity_id, dimension_id) composite key pair.

**Characteristics**

  * Maintain aggregations per (entity_id, dimension_id) composite key instead of just per entity_id
  * Handle multi-dimensional state with composite key granularity
  * Support complex logic where each entity has multiple related objects to track


**Example** : Account balances by wallet where each user (entity_id) has multiple wallets (dimension_id), and you need to maintain a separate balance for each wallet. This is a composite key pattern common in financial applications.

## How incremental SQL models work

Incremental SQL models follow this workflow:

  1. Reference previous state using `this.DeRef()` with `pre_existing=true`
  2. Reference delta models that represent changes since the baseline checkpoint
  3. Collect new rows from upstream sources that arrived since the baseline checkpoint
  4. If previous state exists, merge it with new data; otherwise perform a full scan
  5. Materialize the result as a table, view, or ephemeral model


### Key advantages

Profiles handles the complexity for you:

  * **Automatic creation** : Delta models are automatically generated for append-only inputs
  * **Automatic cleanup** : Old materials are cleaned up based on retention periods
  * **Automatic build order** : Dependency resolution ensures correct execution order
  * **No manual backfill required** : Full refresh mode handles first run automatically
  * **Per-model incremental base** : If one entity var changes, others can still run incrementally
  * **Efficient time management** : Large changes may take longer, but subsequent runs remain fast


## Basic template structure
    
    
    models:
        - name: example_incremental_model
            model_type: sql_template
            model_spec:
                occurred_at_col: timestamp
                materialization:
                    output_type: table
                single_sql: |
                    {%- set lastThis = this.DeRef(pre_existing=true, dependency="optional", checkpoint_name="baseline") -%}
                    
                    {% set events_delta = this.DeRef("inputs/events/incr_delta_tbl", dependency="coercive", baseline_name="baseline", prereqs=[lastThis]) %}
                    
                    {% set events_full = this.DeRef("inputs/events", prereqs=[events_delta.Except()]) %}
                    
                    {# All DeRef before this line. Note that DeRef should not be put in conditionals. DeRef mark dependencies — use prereqs for conditional dependencies #}
    
                     {% if lastThis.IsEnabled() && events_delta.IsEnabled() %}
                        -- Incremental mode: merge with baseline
                        SELECT * FROM {{ lastThis }}
                        UNION ALL
                        SELECT * FROM {{ events_delta }}
                    {% else %}
                        -- Full refresh mode: process all data
                        SELECT * FROM {{ events_full }}
                    {% endif %}                
            contract:
                is_append_only: false
    

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Note the following:
> 
>   * **Incremental SQL models work on append-only inputs** : The upstream inputs must have `contract: is_append_only: true` to enable delta model generation.
>   * **Also works on append-only SQL models** : Incremental SQL models can build on other append-only SQL models, even ephemeral ones.
>   * Set `is_append_only: false` for incremental SQL models that merge or update data.
>   * Set `is_append_only: true` only if your model truly only appends new rows without modifying existing ones.
>   * Profiles also supports keeping the SQL template in another file and referencing it using `{% exec %} {{ this.ReadFile("file/path") }} {% endexec %}`.
> 


## Key concepts

This section explains the key concepts of incremental SQL models.

### Previous state reference

Use `this.DeRef()` with `pre_existing=true` to reference the previous materialization of the current model:
    
    
    {%- set lastThis = this.DeRef(
          pre_existing=true,
          dependency="optional",
          checkpoint_name="baseline") -%}
    

This looks for a previous materialization, uses it as a baseline checkpoint, and returns `nil` if no baseline exists (enabling full refresh mode).

See [DeRef Reference](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/deref-reference/>) for complete syntax and usage.

### Collecting new data

When running incrementally, collect only new data that arrived since the baseline checkpoint. Profiles automatically handles this for append-only inputs when you reference them with the appropriate baseline context using `baseline_name` that matches the `checkpoint_name` used for `lastThis`.

### Incremental vs. full refresh modes

  * **Incremental mode** (when baseline exists): Merges previous state with new data, processing only changes since the last checkpoint.
  * **Full refresh mode** (when no baseline exists): Processes all historical data, used on first run or when baseline is unavailable.


See the [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/#incremental-vs-full-refresh>) guide for more information on these modes.

## Example: Monthly Active Users (MAU)

This example demonstrates an incremental input window model pattern for tracking monthly active users, where an incremental SQL model maintains a rolling window of active days, and an entity var references it to compute MAU.

**Input configuration** (`inputs.yaml`):
    
    
    inputs:
      - name: events
        table: PROD.ANALYTICS.EVENTS
        contract:
          is_append_only: true
          is_event_stream: true
        occurred_at_col: timestamp
    

**Incremental SQL model** (`sql_models.yaml`):
    
    
    models:
      - name: recent_user_activity
        model_type: sql_template
        model_spec:
          occurred_at_col: timestamp
          materialization:
            output_type: table
          single_sql: |
            {%- set lastThis = this.DeRef(pre_existing=true, dependency="optional", checkpoint_name="baseline") -%}
            
            {% set events_delta = this.DeRef("inputs/events/incr_delta_tbl", dependency="coercive", baseline_name="baseline", prereqs=[lastThis]) %}
            
            {% set events_full = this.DeRef("inputs/events", prereqs=[events_delta.Except()]) %}
            
            {# All DeRef before this line. Note that DeRef should not be put in conditionals. DeRef mark dependencies — use prereqs for conditional dependencies #}
    
            SELECT user_id, active_day
              FROM (
                {%- if lastThis.IsEnabled() %}
                  -- Incremental mode: merge previous active days with new events
                  SELECT DISTINCT user_id, CAST(timestamp AS DATE) AS active_day
                  FROM (
                    SELECT user_id, timestamp FROM {{ events_delta }}
                    UNION ALL
                    SELECT user_id, active_day AS timestamp FROM {{ lastThis }}
                  )
                {%- else %}
                  -- Full refresh mode: process all events
                  SELECT DISTINCT user_id, CAST(timestamp AS DATE) AS active_day
                  FROM {{ events_full }}
                {%- endif %}
              )
              WHERE active_day >= DATEADD('day', -365, COALESCE({{end_time.Format(\"2006-01-02 15:04:05\"}}, CURRENT_DATE()))        
          ids:
            - select: user_id
              type: user_id
              entity: user
          contract:
              is_append_only: false
    

This incremental SQL model has `is_append_only: false` because it maintains a rolling window that removes old data (older than 365 days). Incremental SQL models that merge or update data should set `is_append_only: false` — only set `is_append_only: true` if your model truly only appends new rows without modifying existing ones.

**Entity variable** (`profiles.yaml`):
    
    
    - entity_var:
        name: monthly_active_users
        select: COUNT(DISTINCT user_id)
        from: models/recent_user_activity
        where: active_day >= DATEADD('day', -30, {{end_time.Format(\"2006-01-02 15:04:05\"}})
        description: Number of distinct users active in the past 30 days
    

### How it works

  1. **Input configuration** : The `events` input has `contract: is_append_only: true`, enabling incremental processing.

  2. **Incremental SQL model** : The `recent_user_activity` model:

     * References its previous materialization using `lastThis` with `pre_existing=true`
     * Collects new events from `events_delta` when running incrementally
     * Merges previous active days with new event dates using `UNION ALL` and `DISTINCT`
     * Filters to maintain only the last 365 days of activity
     * Handles full refresh mode when no baseline exists
  3. **Entity var reference** : The `monthly_active_users` entity var references the incremental SQL model and filters to the past 30 days, counting distinct users from the pre-computed model.


This pattern is efficient because the SQL model maintains state incrementally (only processing new events), and the entity var performs a simple aggregation on the pre-computed model.

## Troubleshooting

Issue| Solution  
---|---  
Model fails on first run| Ensure your model handles cases when `lastThis.IsEnabled()` is both false and true. Use `events_full` with `prereqs=[events_delta.Except()]` to ensure proper fallback when baseline doesn’t exist  
New data not being processed| Verify that upstream inputs have `contract: is_append_only: true` configured and that your `baseline_name` matches the `checkpoint_name` used for `lastThis`  
Incorrect merge results| Check that your merge logic correctly handles both existing and new entities. Use appropriate SQL joins, UNION ALL patterns, or ordering/de-duplication functions based on your use case  
Performance not improving| Ensure your filtering logic correctly identifies only new data and that your merge logic is efficient. Verify that delta models are being used instead of full inputs  
`DeRef` errors| See [DeRef Reference](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/deref-reference/>) for syntax and troubleshooting  
SQL syntax errors| Note that SQL syntax varies by warehouse. `DATEADD` is Snowflake/Redshift syntax. For BigQuery, use `DATE_SUB`; for Databricks, use `date_sub`  
  
### Avoiding cycles and infinite regress

> ![warning](/docs/images/warning.svg)
> 
> Incremental features are powerful but need to be used carefully to avoid cycles and infinite regress.

**Important: All DeRef before conditionals**

All `DeRef` calls must be placed before any conditional logic (`if` statements). Profiles needs to discover all dependencies during the dependency discovery phase, which happens before SQL execution. If `DeRef` is inside a conditional, Profiles cannot determine dependencies correctly.
    
    
    {# CORRECT: All DeRef at the top #}
    {% set lastThis = this.DeRef(pre_existing=true, dependency="optional") %}
    {% set events_delta = this.DeRef("inputs/events/incr_delta_tbl", prereqs=[lastThis]) %}
    
    {% if lastThis.IsEnabled() %}
      {# Use materials here #}
    {% endif %}
    
    {# WRONG: DeRef inside conditional - breaks dependency discovery #}
    {% if some_condition %}
      {% set material = this.DeRef("some/model") %}  {# ERROR! #}
    {% endif %}
    

**Common mistakes and how to avoid them:**

  1. **Infinite regress: Self pre-existing DeRef must be optional**
         
         {# WRONG: mandatory self-reference creates infinite regress #}
         {% set lastThis = this.DeRef(pre_existing=true, dependency="normal") %}
         
         {# CORRECT: self-reference must be optional #}
         {% set lastThis = this.DeRef(pre_existing=true, dependency="optional", checkpoint_name="baseline") %}
         

**Why** : Without `dependency="optional"`, Profiles tries to create infinite historical chain of materials.

  2. **Cycle: Missing pre_existing=true flag**
         
         {# WRONG: missing pre_existing creates cycle #}
         {% set lastThis = this.DeRef(checkpoint_name="baseline") %}
         
         {# CORRECT: must specify pre_existing=true #}
         {% set lastThis = this.DeRef(pre_existing=true, dependency="optional", checkpoint_name="baseline") %}
         

**Why** : Without `pre_existing=true`, the model depends on itself in the same time context, creating a cycle.

  3. **Inefficient: Delta derefs must be conditional**
         
         {# INEFFICIENT: delta runs even in full refresh mode #}
         {% set events_delta = this.DeRef("inputs/events/incr_delta_tbl", baseline_name="baseline") %}
         
         {# CORRECT: delta only runs when baseline exists #}
         {% set lastThis = this.DeRef(pre_existing=true, dependency="optional", checkpoint_name="baseline") %}
         {% set events_delta = this.DeRef("inputs/events/incr_delta_tbl", dependency="coercive", baseline_name="baseline", prereqs=[lastThis]) %}
         

**Why** : Without `prereqs=[lastThis]`, delta model runs even during full refresh, wasting compute. Var tables may also run unnecessarily.


**Profiles protections:**

Profiles has built-in protections to catch these issues:

  * **Cycle detection** : Graph validation catches same-time-context cycles during dependency resolution
  * **Infinite regress detection** : If >10,000 temporary sequence numbers are created, Profiles throws an error with diagnostic information
  * **Helpful error messages** : Errors include the call chain, recent material allocations, and suggestions for fixing the issue


**Debug tips:**

  * Check that all self-referencing DeRefs have `dependency="optional"`
  * Verify all pre-existing references include `pre_existing=true`
  * Ensure delta model DeRefs include `prereqs=[lastThis]` to make them conditional
  * Use `baseline_name` matching the `checkpoint_name` for consistency


## See more

  * [Incremental SQL Models Overview](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/incremental-sql-models/>): Conceptual introduction to incremental SQL models
  * [How to Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>): Step-by-step guide to convert features to incremental
  * [DeRef Reference](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/deref-reference/>): Complete reference for `this.DeRef()` syntax and usage
  * [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>): Understanding checkpoints and how they enable incremental computation


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/incremental-features/compound-aggregations/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/incremental-features/incremental-sql-models/deref-reference/>)