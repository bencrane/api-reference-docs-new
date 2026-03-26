# Var Groups (Features)

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Var Groups (Features)

Use `var_groups` to define features for your Profiles entities.

* * *

  * __less than a minute

  * 


`var_groups` define and organize features for entities and cohorts, and they consist of `input_vars` and `entity_vars`.

You can `var_groups` in the [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/profiles-yaml/>) file:
    
    
    var_groups:
        name: var_groups_name
        entity_key: entity_name
        vars:
            - input_var:
              <input-var-config>
            - entity_var:
              <entity-var-config>
    

Key| Description  
---|---  
`name`| Name of the `var_groups`.  
`entity_key`| `entity` for the defined vars.  
`vars`| Definition of input and entity vars.  
[`input_var`](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/profiles-yaml/var-groups/input-var/>)| Input variable configuration.  
[`entity_var`](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/profiles-yaml/var-groups/entity-var/>)| Entity variable configuration.  
  
## Example
    
    
    var_groups:
        name: user_var_group
        entity_key: user
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
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.20/dev-docs/profiles-yaml/id-stitcher/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.20/dev-docs/profiles-yaml/var-groups/entity-var/>)