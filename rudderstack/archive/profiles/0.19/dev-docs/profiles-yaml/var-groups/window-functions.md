# Window Functions

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Window Functions

Learn how to compute complex features using window functions.

* * *

  * __less than a minute

  * 


Window functions are SQL functions that you can use with [`input_vars`](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/profiles-yaml/var-groups/input-var/>) and [`entity_vars`](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/profiles-yaml/var-groups/entity-var/>).

SQL window functions perform calculations across rows related to the current row, enabling complex analytics like rankings, running totals, and running averages.
    
    
    window:
        order_by:
            - order_column (desc)
        frame_clause: ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
        partition_by:
            - partition_column
    

Field| Description  
---|---  
`order_by`| Column to order rows by, for example, add `desc` for descending order.  
`frame_clause`| Specify the set of rows (or window) the calculation is applied to, see the specific warehouse documentation for more details.  
`partition_by`| Column to partition the rows by.  
  
## Window function references

  * [Snowflake](<%22https://docs.snowflake.com/en/sql-reference/functions-window%27>)
  * [Redshift](<%22https://docs.aws.amazon.com/redshift/latest/dg/c_Window_functions.html%22>)
  * [BigQuery](<%22https://cloud.google.com/bigquery/docs/reference/standard-sql/window-function-calls%22>)
  * [Databricks](<%22https://docs.databricks.com/en/sql/language-manual/sql-ref-window-functions.html%22>)


## Example
    
    
    # Order by
    - entity_var:
        name: order_number
        select: rank() # DO NOT specify frame clause when a ranking window function is used
        window:
            order_by:
                - order_date
    
    # Partition by and Input var
    - input_var:
        name: session_start_time
        from: models/rsTracksUnionPages
        select: min(timestamp)
        window:
            partition_by:
                - context_session_id
                - rudder_id
        description: Describes the start time of session of a specific context_id
    
    # Using frame clause
    
    - entity_var:
        name: first_num_b_order_num_b
        select: first_value(tbl_c.num_b) # Specify frame clause as aggregate window function is used
        from: inputs/tbl_c
        default_value: -1
        where: tbl_c.num_b >= 10
        window:
            order_by:
                - tbl_c.num_b desc
            frame_clause: ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.19/dev-docs/profiles-yaml/var-groups/input-var/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.19/dev-docs/profiles-yaml/cohorts/>)