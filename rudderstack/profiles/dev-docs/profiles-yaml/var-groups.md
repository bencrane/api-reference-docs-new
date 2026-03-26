# Var Groups (Features)

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Var Groups (Features)

Use `var_groups` to define features for your Profiles entities.

* * *

  * __2 minute read

  * 


`var_groups` define and organize features for entities and cohorts, and they consist of `input_vars` and `entity_vars`.

You can `var_groups` in the [`profiles.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/>) file:
    
    
    var_groups:
        name: var_groups_name
        entity_key: entity_name
        time_grain: day
        vars:
            - input_var:
              <input-var-config>
            - entity_var:
              <entity-var-config>
    

Key| Description  
---|---  
`name`| Name of the `var_groups`.  
`entity_key`| `entity` for the defined vars.  
[`time_grain`](<https://www.rudderstack.com/docs/profiles/concepts/timegrains/>)| Controls how often features in this group are computed. This parameter accepts the following values: `tick`, `tenminutes`, `hour`, `day`, `week`, `month`, `year`.  
  
See [Timegrains](<https://www.rudderstack.com/docs/profiles/concepts/timegrains/>) for details.  
`vars`| Definition of entity and input vars.  
[`entity_var`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/var-groups/entity-var/>)| Entity variable configuration.  
[`input_var`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/var-groups/input-var/>)| Input variable configuration. See warning below.  
  
> ![warning](/docs/images/warning.svg)
> 
> **Input vars scan all input data on every run, which can be expensive for large datasets.**
> 
> Consider using [`entity_var` with Incremental Features](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>) or [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>) instead for better performance.
> 
> Use `input_var` only when you need to add a calculated column to the input table itself (for example, window functions that must be computed before entity-level aggregation).

## Example
    
    
    var_groups:
        name: user_var_group
        entity_key: user
        time_grain: day  # Features in this group are computed daily
        vars:
            - input_var:
              name: page_count
              select: count(distinct url)
              from: inputs/rsPages
              window:
                partition_by:
                  - profile_id
                  - date
              description: Add column to rsPages SQL model to get a page count per date
            - entity_var:
              name: web_dates_visited_365_days
              select: array_agg(distinct object_construct('date', date, 'page_count',{{pages_orderby_table.page_count}}))
              from: inputs/rsPages
              description: rolling 365 days array of json objects with the UTC timestamps the user visited the website along with the number of pages visited per date stamp
            - entity_var:
              name: first_order_date
              select: min(order_date)
              from: inputs/orders
              description: First order date
            - entity_var:
              name: last_order_date
              select: max(order_date)
              from: inputs/orders
              is_feature: false
            - entity_var:
              name: days_since_la`st_order
              select: "date_diff(CURRENT_DATE(), date({{user.last_order_date}}), day)"
              description: Days since user last completed an order
    

  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/profiles-yaml/id-stitcher/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/profiles-yaml/var-groups/entity-var/>)