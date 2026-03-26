# Entity Var

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Entity Var

Learn how to create and use `entity_var` in your Profiles project.

* * *

  * __2 minute read

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
`default_value`| Default value for `null` values.  
`where`| Filtering condition, equivalent to `WHERE` statement.  
[`window`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/window-functions/>)| Adds `order_by` key for window functions. Rows are automatically partitioned by `rudder_id`.  
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
        select: "date_diff(CURRENT_DATE(), date({{user.last_order_date}}), day)"
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
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/input-var/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/window-functions/>)