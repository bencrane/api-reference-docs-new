# Profiles OptimizationsBeta

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles Optimizations Beta

Learn about the different optimization options in Profiles.

* * *

  * __2 minute read

  * 


This guide introduces the available optimizations in Profiles and explains how to use them in your Profiles project to enhance execution efficiency.

## Optimization options

Profiles provides the following optimizations to reduce the execution time of a `pb run`:

### Input variable table optimization

Instead of copying the entire input table, Profiles automatically identifies and copies only the necessary columns, reducing data transfer and improving performance. PB identifies the necessary columns by parsing the SQL fragments provided in `input_vars` and `entity_vars`.

Set `enable_input_columns_filtering` to `true` in your `optimizations.yaml` file to enable this optimization.

**Limitation**

If Profiles fails to identify the necessary columns and the run fails, you need to specify the unidentified columns in the input model’s contract - this workaround should help you bypass the run failure. An example is shown below:
    
    
    - name: rsIdentifies
       contract: 
            is_optional: false 
            is_event_stream: true 
            with_entity_ids: 
                - users
            with_columns: 
                - name: missed_column # PB was not able to identify this column, it is added to the contract.
        app_defaults: 
            table: identifies 
            occurred_at_col: timestamp 
            ids: 
                - select: user_id 
                type: user_id 
                entity: users
    

### Efficient main ID column addition

Instead of performing multiple joins between the input variable table and the ID stitcher, a case-based approach is used to add the main ID column. This method is particularly effective for large input tables.

Set `main_id_addition_approach` to `case_based_join` in your `optimizations.yaml` file to enable this optimization.

### Input vars bundling

Profiles automatically groups the execution of related `input_vars` based on their definitions to optimize runtime performance.

Set `bundle_input_vars` to `true` in your `optimizations.yaml` file to enable this optimization.

### Entity vars bundling

Similar to input variable bundling, this optimization groups the execution of `entity_vars` based on their definitions to improve efficiency.

Set `bundle_entity_vars` to `true` in your `optimizations.yaml` file to enable this optimization.

There are two bundling strategies - `normal` and `aggressive`, with `normal` as the default strategy.

  * In the `normal` strategy, PB groups similar bundles with inter-dependencies and with or without a window together.
  * In the `aggressive` strategy, PB groups regardless of similarity.


#### Optimization options summary

The following table summarizes the available optimizations:

Optimization| Allowed values| Default value  
---|---|---  
`enable_input_columns_filtering`| `true`, `false`| `false`  
`main_id_addition_approach`| `plain_join`, `case_based_join`| `plain_join`  
`bundle_input_vars`| `true`, `false`| `false`  
`bundle_entity_vars`| `true`, `false`| `false`  
`bundle_entity_vars_strategy`| `normal`, `aggressive`| `normal`  
  
## Usage

Specify the optimizations in the `optimizations.yaml` file.

### Example configuration
    
    
    optimizations:
        main_id_addition_approach: case_based_join
        enable_input_columns_filtering: true
        bundle_entity_vars: true
        bundle_input_vars: true
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to place the `optimizations.yaml` file in the appropriate configuration directory of your Profiles project (within the `models` folder). Also, make sure that there is only one `optimizations.yaml` file in your project.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.21/dev-docs/macros-yaml/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.21/dev-docs/run-project/>)