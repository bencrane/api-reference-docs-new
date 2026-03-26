# Input Var

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Input Var

Learn how to create and use `input_var` in your Profiles project.

* * *

  * __3 minute read

  * 


An `input_var` adds a calculated column to an [input](<https://www.rudderstack.com/docs/profiles/concepts/inputs/>) table. It calculates a single value per row of the input table which can be used as an input for [`entity_vars`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/var-groups/entity-var/>).

> ![warning](/docs/images/warning.svg)
> 
> **Performance consideration** : Input vars scan all input data on every run, which can be expensive for large datasets.
> 
> Consider using the following approaches for better performance:
> 
>   * [`entity_var` with Incremental Features](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>) for aggregations like `SUM`, `COUNT`, `MIN`, `MAX`
>   * [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>) for complex transformations
> 

> 
> Use `input_var` only when you need row-level calculations on the input table before entity-level aggregation (for example, window functions like `ROW_NUMBER()` or `LAG()`).
    
    
    - input_var:
        name: input_var_name
        select: SQL statement
        from: inputs/table
        window:
            partition_by:
                - partition_column
        description: description
    

Field| Description  
---|---  
`name`| Name of the `input_var`.  
`select`| SQL state, equivalent to `SELECT` statement.  
`from`| Path of the input table, equivalent to `FROM` statement.  
`where`| Filtering condition, equivalent to `WHERE` statement.  
[`window`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/var-groups/window-functions/>)| Adds `partition_by` and/or `order_by` keys for window functions  
`description`| Description of the `input_var`.  
  
## Example
    
    
    - input_var:
        name: page_count
        description: Adds column to a SQL model to get a page count per date.
        select: count(distinct url)
        from: models/pages_orderby_table
        window:
            partition_by:
                - profile_id
                - date
    

## Migrate input vars to incremental alternatives

Input vars scan all input data on every run and **block incremental processing** for any entity var that depends on them. When migrating a project to incremental mode, you must convert or replace every input var.

### Decision tree

For each input var, follow this decision tree to choose the best replacement:
    
    
    Input Var
    +-- Uses LAST_VALUE / FIRST_VALUE window function?
    |   +-- Yes: Convert to entity_var using MAX_BY / MIN_BY
    |
    +-- Uses a simple aggregation with partition_by?
    |   +-- Yes: Convert to entity_var with merge clause
    |
    +-- Requires complex multi-step logic?
        +-- Yes: Create an incremental SQL model and
            reference it from entity vars
    

### Option 1: Convert to entity var (most common)

You can replace window functions like `LAST_VALUE` and `FIRST_VALUE` with `MAX_BY` and `MIN_BY`:
    
    
    # Before (input var with LAST_VALUE)
    - input_var:
        name: last_known_city
        select: last_value(city)
        from: inputs/events
        window:
          partition_by:
            - user_id
          order_by:
            - timestamp
        where: city IS NOT NULL
    
    # After (entity var with MAX_BY + ordering helper)
    - entity_var:
        name: last_known_city
        select: MAX_BY({{events.city}}, {{events.timestamp}})
        merge: MAX_BY({{rowset.last_known_city}}, {{rowset.last_known_city_by_param}})
        from: inputs/events
        where: {{events.city}} IS NOT NULL
    
    - entity_var:
        name: last_known_city_by_param
        select: MAX({{events.timestamp}})
        merge: MAX({{rowset.last_known_city_by_param}})
        from: inputs/events
        where: {{events.city}} IS NOT NULL
        is_feature: false
    

For detailed patterns, see the following sections:

  * [MIN_BY/MAX_BY with ordering helper](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/#min_by--max_by-with-ordering-helper>)
  * [Replace window functions](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/compound-aggregations/#replace-window-functions>)


### Option 2: Create an incremental SQL model

When the input var logic is too complex for an entity var (multi-step transformations, complex joins, or logic that truly requires row-level windowing), create an [Incremental SQL Model](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>) that handles the computation incrementally, then reference it from entity vars.

  


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/profiles-yaml/var-groups/entity-var/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/profiles-yaml/var-groups/window-functions/>)