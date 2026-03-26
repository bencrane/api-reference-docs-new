# How to Make Features IncrementalBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# How to Make Features Incremental Beta

Learn how to convert features to incremental mode in your Profiles project.

* * *

  * __7 minute read

  * 


This guide walks you through converting features to incremental mode in Profiles.

## Prerequisites

Before making a feature incremental, make sure that:

  * Your input sources are append-only and have reliable `occurred_at_col` timestamps
  * The feature can be expressed using [supported incremental patterns](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/>)
  * You understand how [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>) work in Profiles


> ![warning](/docs/images/warning.svg)
> 
> **Not all features can be incremental.**
> 
> Features that require scanning all historical data (such as median or percentile calculations) **cannot** use incremental computation. For such cases, consider using [Timegrains](<https://www.rudderstack.com/docs/profiles/concepts/timegrains/>) and [bundling](<https://www.rudderstack.com/docs/profiles/dev-docs/optimizations/>).

## Step 1: Configure input contracts

Before making features incremental, you must configure all input sources and SQL models with the `is_append_only` contract. This applies to inputs and SQL models (which can also be ephemeral).

### Verify append-only behavior

Before marking an input as append-only, verify that it truly only appends new rows and never updates or deletes existing ones:

  1. **Check business semantics** : Event/fact tables (page views, purchases, clicks) are typically append-only. Dimension tables (user profiles, account settings) that update rows in place are **not** append-only.

  2. **Run a warehouse query** : Check for duplicate primary keys that would indicate updates:
         
         SELECT entity_id_column, COUNT(*)
         FROM your_input_table
         GROUP BY entity_id_column
         HAVING COUNT(*) > 1;
         


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Inspect results to distinguish genuine duplicate events from row updates.

  3. **Check downstream usage** : If a downstream model selects the latest attribute value (like current subscription status), the input likely receives updates and should **not** be marked append-only.


> ![warning](/docs/images/warning.svg)
> 
> **When in doubt, treat an input as not append-only.**
> 
> Incorrectly marking a mutable input as `is_append_only: true` leads to incorrect incremental results that are difficult to diagnose.

### Input example

Add the following to each verified append-only input in your `inputs.yaml`:
    
    
    inputs:
      - name: orders
        table: PROD.ANALYTICS.ORDERS
        contract:
          is_append_only: true
          is_event_stream: true
        occurred_at_col: order_timestamp
    

### SQL model example

You can also create append-only SQL models that filter or transform inputs. Add this to your `sql_models.yaml`:
    
    
    models:
      - name: purchase_events
        model_type: sql_template
        model_spec:
          occurred_at_col: timestamp
          materialization:
            output_type: table
          single_sql: |
            {% with events = this.DeRef("inputs/events") %}
              SELECT * FROM {{ events }}
              WHERE event_name = 'purchase'
            {% endwith %}        
          contract:
            is_append_only: true
            is_event_stream: true
    

This SQL model filters events to only purchases and is marked as `is_append_only: true`, making it usable as an incremental source.

### Ephemeral SQL models

Ephemeral SQL models (`output_type: ephemeral`) that sit on top of append-only inputs can also be marked as `is_append_only: true`. This is useful for filtering or transforming inputs without materializing intermediate tables.

Only mark an ephemeral model as append-only if:

  * All upstream inputs are append-only
  * The model only filters, renames, or transforms columns (no joins with mutable dimension tables)
  * The output is itself append-only (no aggregations that change with updates)


> ![warning](/docs/images/warning.svg)
> 
> All inputs and SQL models used by incremental features must have `contract: is_append_only: true`. SQL models can also be ephemeral. Without this configuration, the project will throw an error when you try to run incremental features.

### Complete example: Simple incremental feature

The following example shows a complete setup for a simple incremental feature that tracks total purchase value:

**Input configuration** (`inputs.yaml`):
    
    
    inputs:
      - name: orders
        table: PROD.ANALYTICS.ORDERS
        contract:
          is_append_only: true
          is_event_stream: true
        occurred_at_col: order_timestamp
    

**Entity var** (`profiles.yaml`):
    
    
    - entity_var:
        name: total_purchases
        select: SUM({{orders.value}})
        merge: SUM({{rowset.total_purchases}})
        from: inputs/orders
        description: Total purchase value across all orders
    

This example shows:

  * Input configured with `contract: is_append_only: true`
  * Entity var using `SUM` aggregation with `merge: SUM({{rowset.total_purchases}})`
  * Profiles automatically handles incremental computation


## Step 2: Identify the feature pattern

Determine which incremental pattern your feature matches:

  * **Simple aggregations** : `MIN`, `MAX`, `SUM`, `COUNT` \- See [Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>)
  * **Compound aggregations** : `AVG`, `MIN_BY`/`MAX_BY`, arrays, booleans - See [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>)
  * **Window function replacements** : `LAST_VALUE` -> `MAX_BY`, `FIRST_VALUE` -> `MIN_BY` \- See [Replacing window functions](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/#replacing-window-functions>)
  * **Complex patterns** : Stateful processing, running totals, activity windows - See [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)


See [Incremental Features](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/>) for a pattern selection guide and detailed examples.

## Step 3: Add the `merge` property

Add a `merge:` property to your `entity_var` definition in your `profiles.yaml` file. This property defines how to combine previous feature values with new data.

### Simple aggregators

For `MIN`, `MAX`, `SUM`, `COUNT`, and similar functions:
    
    
    - entity_var:
        name: first_event_time
        select: MIN({{events.timestamp}})
        merge: MIN({{rowset.first_event_time}})
        from: inputs/events
        description: Earliest timestamp of any event
    

### Average using component features

For `AVG`, break it into sum and count components. Define three separate `entity_var` entries at the same level in your `profiles.yaml`:
    
    
    - entity_var:
        name: sum_of_scores
        select: SUM({{game_events.score}})
        merge: SUM({{rowset.sum_of_scores}})
        from: inputs/game_events
        is_feature: false
        description: Sum of scores (used for average calculation)
    
    - entity_var:
        name: count_of_scores
        select: COUNT({{game_events.score}})
        merge: SUM({{rowset.count_of_scores}})
        from: inputs/game_events
        is_feature: false
        description: Count of scores (used for average calculation)
    
    - entity_var:
        name: avg_score
        select: "CASE WHEN {{user.count_of_scores}} > 0 THEN {{user.sum_of_scores}} / {{user.count_of_scores}} ELSE 0 END"
        description: Average score across all games
    

> ![info](/docs/images/info.svg)
> 
> **Features referencing other features**
> 
> When a feature references another feature (like `{{user.sum_of_scores}}`), it doesn’t need a `merge:` clause if it’s just performing a calculation on incrementally maintained features. The referenced features (`sum_of_scores` and `count_of_scores`) maintain their incremental state, and the calculation (`avg_score`) is computed on-the-fly from those values.

### Use incremental sources

You can also make features incremental by pointing to an incremental source (such as a [delta model](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/use-checkpoints/#delta-models>) or incremental input window). Even if the `entity_var` SQL runs a full aggregation, the scan volume stays small because the source is already delta-restricted:
    
    
    - entity_var:
        name: recent_purchases
        select: SUM({{recent_orders.value}})
        from: inputs/orders/incr_delta_tbl
        description: Purchases from recent data only
    

## Step 4: Define merge logic

The `merge:` clause must match the aggregation function in `select:`. Common patterns:

Select function| Merge function  
---|---  
`MIN(...)`| `MIN({{rowset.feature_name}})`  
`MAX(...)`| `MAX({{rowset.feature_name}})`  
`SUM(...)`| `SUM({{rowset.feature_name}})`  
`COUNT(...)`| `SUM({{rowset.feature_name}})`  
`MAX_BY(val, ord)`| `MAX_BY({{rowset.feature}}, {{rowset.feature_by_param}})` \+ [helper var](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/#min_by--max_by-with-ordering-helper>)  
`MIN_BY(val, ord)`| `MIN_BY({{rowset.feature}}, {{rowset.feature_by_param}})` \+ [helper var](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/#min_by--max_by-with-ordering-helper>)  
`ARRAY_AGG(...)`| `ARRAY_UNION_AGG({{rowset.feature_name}})`  
`BOOLOR_AGG(...)`| `BOOLOR_AGG({{rowset.feature_name}})`  
  
For complete `merge` syntax, see [Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>) and [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>).

### Which `merge` function should I use?

The `merge` function must match your aggregation type. For `COUNT`, always use `SUM` in the `merge` property (summing counts, not counting counts). See the table above for the correct merge function for each aggregation type.

## Step 5: Use `merge_where` when needed

For complex merges, use `merge_where:` to restrict merging to only changed rows. Define separate `entity_var` entries at the same level in your `profiles.yaml`:
    
    
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
    

The `timestamp` entity var is marked with `is_feature: false` since it’s an intermediate calculation used by `score_at_last_break`.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Mark helper entity vars with `is_feature: false` when they’re intermediate calculations used by other features. This prevents them from appearing as features in your output while still allowing them to be referenced by other entity vars.

## When merge is not needed

Not every entity var requires a `merge` clause to participate in an incremental project:

  * **Derived-only vars** (no `from` clause) that reference other entity vars are recomputed from their incrementally maintained dependencies. Since they don’t read from input sources directly, they don’t need their own merge logic:
        
        - entity_var:
            name: days_since_last_seen
            select: "DATEDIFF(day, {{user.last_seen}}, {{ end_time_sql }})"
            description: Days since the user was last seen
        

  * **Vars from window-bounded incremental tables** that read from an [Incremental SQL Model](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>) maintaining a sliding window. The SQL model handles state incrementally, and the entity var recomputes from the bounded window each run:
        
        - entity_var:
            name: active_days_in_past_7_days
            select: count(distinct active_day)
            from: models/recent_active_days
            where: active_day >= DATEADD(day, -7, {{ end_time_sql }})
            description: Days active in the last 7 days
        


## Step 6: Test your implementation

  1. Run `pb run` to verify the feature computes correctly
  2. Compare incremental results with a full refresh to ensure accuracy
  3. Monitor run times to verify improvement


> ![warning](/docs/images/warning.svg)
> 
> The first run performs a full refresh to establish the baseline checkpoint. Subsequent runs use incremental computation.

### Verifying incremental behavior

To verify your feature is running incrementally:

  * **Check run times** : Incremental runs should be faster than full refresh runs (after the first run)
  * **Compare results** : Run with incremental mode and compare results with a full refresh to ensure they match
  * **Monitor checkpoint usage** : Verify that checkpoints are being created and used in subsequent runs


## Troubleshooting

Issue| Solution  
---|---  
Feature values are incorrect| 

  * Verify that your `merge:` clause correctly matches the aggregation logic
  * Ensure that your input sources are append-only or have reliable timestamps
  * Check that you are not missing edge cases in merge logic
  * Compare incremental results with a full refresh to identify discrepancies

  
Performance not improving| 

  * Verify that your input sources are properly configured for incremental processing
  * Check that delta models are being used correctly
  * Ensure your data warehouse supports efficient timestamp filtering
  * Monitor checkpoint creation and usage

  
Merge errors| 

  * Verify that all aggregators in `select:` have corresponding merge logic
  * Check that merge functions match the aggregation type
  * Ensure `merge_where:` conditions are correct if used
  * Review [Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>) and [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>) for correct syntax

  
The first run is slow| This is expected. The first run always performs a full refresh to establish the baseline checkpoint. Subsequent runs use incremental computation and should be faster.  
  
## See more

  * Explore [Incremental Features](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/>) for pattern selection guide
  * Learn about [Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>)
  * Learn about [Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>)
  * Learn about [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)
  * Learn about [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>)


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/incremental-features/incremental-sql-models/deref-reference/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/incremental-features/migrate-project-to-incremental/>)