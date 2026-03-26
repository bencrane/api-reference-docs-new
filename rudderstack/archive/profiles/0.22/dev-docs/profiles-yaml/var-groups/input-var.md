# Input Var

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Input Var

Learn how to create and use `input_var` in your Profiles project.

* * *

  * __less than a minute

  * 


An `input_var` adds a calculated column to an [input](<https://www.rudderstack.com/docs/archive/profiles/0.22/concepts/inputs/>) table. It calculates a single value per row of the input table which can be used as an input for [`entity_vars`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/entity-var/>).
    
    
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
[`window`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/window-functions/>)| Adds `partition_by` and/or `order_by` keys for window functions  
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
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/entity-var/>)