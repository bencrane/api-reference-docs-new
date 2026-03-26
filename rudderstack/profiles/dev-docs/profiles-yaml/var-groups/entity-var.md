# Entity Var

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Entity Var

Learn how to create and use `entity_var` in your Profiles project.

* * *

  * __4 minute read

  * 


An `entity_var` adds a calculated (aggregated) column to the entity var tables and downstream feature views. It calculates a single value for each member of the entity (for example, each user).

`entity_vars` can be features for a feature view or an input to another `entity_var`.
    
    
    - entity_var:
        name: entity_var_name
        select: SQL statement
        default_value: value
        from: inputs/table
        where: condition
        window:
            order_by:
                - orderby_column
        description: Days when the user visited the website along with the number of pages visited per date stamp.
    

Field| Description  
---|---  
`name`| Name of the `entity_var`.  
`select`| SQL state, equivalent to `SELECT` statement.  
`from`| Path of the input table, equivalent to `FROM` statement.  
`merge`| SQL expression defining how to combine previous feature values with new calculations for [incremental features](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>). Use `{{rowset.feature_name}}` to reference the previous value from the checkpoint.  
`merge_where`| Optional SQL condition that filters which rows participate in the merge operation. Use `{{rowset.column}}` for previous values from the checkpoint and `{{this.column}}` for new values.  
`default_value`| Default value for `null` values.  
`where`| Filtering condition, equivalent to `WHERE` statement.  
[`window`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/var-groups/window-functions/>)| Adds `order_by` key for window functions. Rows are automatically partitioned by `rudder_id`.  
`description`| Description of the `entity_var`.  
  
## Example
    
    
    # Basic entity
    - entity_var:
        name: first_order_date
        select: min(order_date)
        from: inputs/orders
        description: First order date
    
    # Entity that is not a feature
    - entity_var:
        name: last_order_date
        select: max(order_date)
        from: inputs/orders
        is_feature: false
    
    # Using an entity_var as an input
    - entity_var:
        name: days_since_last_order
        select: "date_diff({{ end_time_sql }}, date({{user.last_order_date}}), day)"
        description: Days since user last completed an order
    
    # Using a window function
    - entity_var:
        name: campaign_source_first_touch
        select: first_value(context_campaign_source)
        from: inputs/rsIdentifies
        where: context_campaign_source is not null and context_campaign_source != ''
        window:
            order_by:
                - timestamp
    
    # Entity var referencing an input var
    - input_var:
        name: last_order
        select: last_value(order)
        from: inputs/rsTracks
        window:
            partition_by:
                - user_id
            order_by:
                - timestamp
    - entity_var:
        name: is_last_order
        select: boolor_agg({{rsTracks.Var("last_order")}})
        from: inputs/rsTracks
    
    # Incremental entity var with merge clause
    - entity_var:
        name: total_purchases
        select: SUM({{orders.value}})
        merge: SUM({{rowset.total_purchases}})
        from: inputs/orders
        description: Total purchase value
    

## Control update frequency

Entity vars inherit their update frequency from the parent `var_group`. To control how often a feature is computed, set `time_grain` on the var_group:
    
    
    var_groups:
      - name: weekly_features
        entity_key: user
        time_grain: week  # Features in this group update weekly
        vars:
          - entity_var:
              name: favorite_category
              select: mode(category)
              from: inputs/orders
    

This is useful for:

  * **Reducing compute costs** : Features that don’t need real-time updates (like monthly aggregates) can be computed less frequently.
  * **Organizing features by freshness** : Group real-time signals separately from slow-changing attributes.


See [Timegrains](<https://www.rudderstack.com/docs/profiles/concepts/timegrains/>) for available options and detailed configuration.

## Incremental features

You can make `entity_vars` incremental by adding a `merge:` clause. Incremental features update existing feature values with newly arrived data instead of recalculating from the entire historical dataset, significantly improving performance for large datasets.

For detailed information about incremental features, see the following guides:

Guide| Description  
---|---  
[Incremental Features Overview](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/>)| Overview of incremental features in Profiles  
[Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>)| Step-by-step guide to convert features to incremental  
[Simple Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/simple-aggregations/>)| Direct aggregations with merge clauses (SUM, MIN, MAX, COUNT)  
[Compound Aggregations](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/>)| Complex aggregations (AVG, MIN_BY/MAX_BY, arrays, Booleans)  
  
## Avoid `CURRENT_TIMESTAMP()` and `CURRENT_DATE` in entity vars

> ![warning](/docs/images/warning.svg)
> 
> **Do not use** warehouse date/time functions like `CURRENT_TIMESTAMP()`, `CURRENT_DATE`, `GETDATE()`, `NOW()`, or `SYSDATE()` in entity var `select` or `where` clauses.
> 
> These functions return the wall-clock time at query execution, which makes results **non-deterministic** across re-runs and `rebase_incremental` operations. Use `end_time_sql` instead.

`end_time_sql` is a **built-in macro** automatically available in every Profiles project. It produces a warehouse-specific formatted timestamp of the current run’s logical end time. No `macros.yaml` definition needed — just use `{{ end_time_sql }}` directly in entity var `where` and `select` clauses:

**In`where` clauses**:
    
    
    - entity_var:
        name: active_days_in_past_7_days
        select: count(distinct active_day)
        from: models/active_days
        where: active_day >= DATEADD(day, -7, {{ end_time_sql }})
    

**In`select` clauses**:
    
    
    - entity_var:
        name: days_since_last_order
        select: "DATEDIFF(day, MAX({{orders.order_date}}), {{ end_time_sql }})"
        from: inputs/orders
    

> ![info](/docs/images/info.svg)
> 
> You can define custom time-formatting macros in `macros.yaml` that build on `end_time_sql`. Pass `this` as an input so the macro can access the material’s temporal context via `mat.WhtCtx.TimeInfo.EndTime`.
> 
> **Example** : Define a macro that truncates the context end time to the nearest hour:
>     
>     
>     # In macros.yaml
>     macros:
>       - name: round_ctx_to_hour
>         inputs:
>           - mat
>         value: "{% if !(mat.WhtCtx|isnil) %}DATE_TRUNC('hour', {{ warehouse.Timestamp(mat.WhtCtx.TimeInfo.EndTime) }}){% else %}NULL{% endif %}"
>     
> 
> Then call it with `this` in an entity var:
>     
>     
>     - entity_var:
>         name: events_in_current_hour
>         select: count(*)
>         from: inputs/events
>         where: DATE_TRUNC('hour', {{events.timestamp}}) = {{ round_ctx_to_hour(this) }}
>     

  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/profiles-yaml/var-groups/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/profiles-yaml/var-groups/input-var/>)