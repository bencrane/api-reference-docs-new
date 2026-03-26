# Macros and Window Functions

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Macros and Window Functions

Easily compute complex features using macros and window functions.

* * *

  * __4 minute read

  * 


## Macros

If you need to re-use complex SQL expressions, you can use a macro instead of re-writing the SQL every time with minor modifications.

Macros are the reusable functions that encapsulate complex processing logic directly within the SQL expression. Once created, you can use the macro to perform computations and use them in multiple models.

For example, if you are building traits that require a `dateadd()` or `datediff()` calculation, you can create a macro and call it within the `select` or `where` function.

Within Macros, you can define the column names in the `inputs` key and the operation to be performed in the `value` key:
    
    
    macros:
      - name: macro_datediff
        inputs:
          - column
        value: "{% if !(end_time|isnil) %} datediff(day, date({{column}}), date('{{end_time.Format(\"2006-01-02 15:04:05\")}}')) {% else %} datediff(day, date({{column}}), GETDATE()) {% endif %}"
      - name: macro_datediff_n
        inputs:
          - column
          - number_of_days
        value: "{% if !(end_time|isnil) %} datediff(day, date({{column}}), date('{{end_time.Format(\"2006-01-02 15:04:05\")}}')) <={{number_of_days}} {% else %} datediff(day, date({{column}}), GETDATE()) <= {{number_of_days}} {% endif %}"
      - name: array_agg
        inputs:
          - column_name
        value: "array_agg( distinct {{column_name}})"
      - name: array_size
        inputs:
          - column_name
        value: "array_size( parse_json({{column_name}}) )"
      - name: frame_clause
        value: "frame_condition = 'rows between unbounded preceding and unbounded following'"
      - name: macro_listagg
        inputs:
          - column
          - timestamp
        value: "{% if warehouse.DatabaseType() == \"bigquery\" %} STRING_AGG({{column}}, ',' ORDER BY {{timestamp}} ASC) {% else %} LISTAGG({{column}}, ',') WITHIN group (order by {{timestamp}} ASC) {% endif %}"
    

You can create a file for macros (say `macros.yaml`) under the `models` folder. Further, refer the macro in the `entity_var` definition in the `profiles.yaml` file by passing it as a value to the `select` or `where` key:
    
    
    - entity_var:
        name: date difference
        select: "{{ macro_datediff('{{user.Var(\"first_sale_time\")}}') }}"
    

Field| Data type| Description  
---|---|---  
`name`| String| Name to uniquely identify the macro.  
`inputs`| List| Defines the input variables to be used by the macro function.  
`value`| String| Contains the reusable function in the form of a SQL expression. Any reference to the inputs must be encapsulated within double curly brackets.  
  
See a sample [Profiles library project](<https://github.com/rudderlabs/profiles-stripe-features>) that creates user features from Stripe tables using Macros.

## Window functions

A window function operates on a window (group) of related rows. It performs calculation on a subset of table rows that are connected to the current row in some way. The window function has the ability to access more than just the current row in the query result.

The window function returns one output row for each input row. The values returned are calculated by using values from the sets of rows in that window. A window is defined using a window specification, and is based on three main concepts:

  * Window partitioning, which forms the groups of rows (`PARTITION BY` clause)
  * Window ordering, which defines an order or sequence of rows within each partition (`ORDER BY` clause)
  * Window frames, which are defined relative to each row to further restrict the set of rows (`ROWS` specification). It is also known as the frame clause.


**Snowflake** does not enforces users to define the cumulative or sliding frames, and considers `ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING` as the default cumulative window frame. However, you can override this by defining the frame manually.

On the **Redshift** aggregate window function list given below, specify the `frame_clause` while using any function from the list:

  * `AVG`
  * `COUNT`
  * `CUME_DIST`
  * `DENSE_RANK`
  * `FIRST_VALUE`
  * `LAG`
  * `LAST_VALUE`
  * `LEAD`
  * `LISTAGG`
  * `MAX`
  * `MEDIAN`
  * `MIN`
  * `NTH_VALUE`
  * `PERCENTILE_CONT`
  * `PERCENTILE_DISC`
  * `RATIO_TO_REPORT`
  * `STDDEV_POP`
  * `STDDEV_SAMP` (synonym for `STDDEV`)
  * `SUM`
  * `VAR_POP`
  * `VAR_SAMP` (synonym for `VARIANCE`)


In the Redshift ranking window functions given below, **do not** specify the `frame_clause` while using any function from the list:

  * `DENSE_RANK`
  * `NTILE`
  * `PERCENT_RANK`
  * `RANK`
  * `ROW_NUMBER`


> ![warning](/docs/images/warning.svg)
> 
> Use `frame_clause` carefully when using a window function. While It is not very critical for Snowflake, using it incorrectly in Redshift can lead to errors.

Example of using `frame_clause`:
    
    
    - entity_var:
        name: first_num_b_order_num_b
        select: first_value(tbl_c.num_b) # Specify frame clause as aggregate window function is used
        from: inputs/tbl_c
        default: -1
        where: tbl_c.num_b >= 10
        window:
            order_by:
            - tbl_c.num_b desc
            frame_clause: ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    - entity_var:
        name: first_num_b_order_num_b_rank
        select: rank() # DO NOT specify frame clause as ranking window function is used
        window:
            order_by:
            - first_num_b_order_num_b asc
    

Note how `frame_clause` is specified in first `entity_var` and not in the second one.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.15/additional-concepts/multi-version/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.15/additional-concepts/input-sources/>)