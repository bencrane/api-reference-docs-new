# macros.yaml

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# macros.yaml

Leverage macros to reuse code in your Profiles project.

* * *

  * __2 minute read

  * 


Macros are reusable blocks of code that can be used in a Profiles project as a form of templating. They operate similar to functions in that you can reuse them with different parameters, reducing repetition and making the code more modular.

## Define macros

You can define macros in the `macros.yaml` file in the model folder, and call them within any other [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/profiles-yaml/>) file.
    
    
    macros:
        - name: macro_name          # Required
          inputs:                   # Required
              - list_of_parameters
          value: "code as string" # Required
    

Key| Description  
---|---  
`name`  
Required| Name of the macro - you can use it to call the macro.  
`inputs`| Parameters for the macro.  
`value`  
Required| Macro code in a string format.  
  
## Syntax

The syntax for Profiles macros is largely based on [pongo2](<https://github.com/rudderlabs/pongo2/>). The basic principles of writing a macro are as follows:

  * Macros operate on the YAML code itself, generating new code before execution. The inputs are parameters for adding strings at compile-time, expanding the reusability of the macro.
  * Input parameters are surrounded by double curly brackets (e.g. `{{input}}`)
  * Control logic (`if`, `else`, `endif`) is defined within `{%` and `%}`.
  * Reserved inputs words are `this` and `warehouse`.


## Example
    
    
    # Macro with one input
      - name: array_agg
        inputs:
            - column_name
        value: "array_agg( distinct {{column_name}})"
    
    # Macro with two inputs
      - name: macro_listagg
        inputs:
            - column
            - timestamp
        value: "LISTAGG({{column}}, ',') WITHIN group (order by {{timestamp}} ASC)"
    
    # Macro with no inputs
      - name: frame_clause
        value: "frame_condition = 'rows between unbounded preceding and unbounded following'"
    
    # Define If/Else logic
      - name: macro_listagg
        inputs:
            - column
            - timestamp
        value: "{% if warehouse.DatabaseType() == \"bigquery\" %} STRING_AGG({{column}}, ',' ORDER BY {{timestamp}} ASC) {% else %} LISTAGG({{column}}, ',') WITHIN group (order by {{timestamp}} ASC) {% endif %}"
    
    # Define more complex logic
      - name: macro_datediff
        inputs:
            - column
        value: "
            {% if warehouse.DatabaseType() == \"bigquery\" %}
              {% if !(end_time|isnil) %} date_diff(date('{{end_time.Format(\"2006-01-02 15:04:05\")}}'), date({{column}}), day)
              {% else %} 
              date_diff(CURRENT_DATE(), date({{column}}), day){% endif %}
            {% else %}
              {% if !(end_time|isnil) %} datediff(day, date({{column}}), date('{{end_time.Format(\"2006-01-02 15:04:05\")}}'))
              {% else %} 
              datediff(day, date({{column}}), GETDATE()) {% endif %}
            (% endif %)"
    
    # Use macro in a feature definition in the profiles.yaml file
    - entity_var:
      name: all_anonymous_ids
      select: "{{ array_agg(anonymous_id) }}"
      from: inputs/rsIdentity
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.20/dev-docs/sql-model-yaml/sql-model-config/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.20/dev-docs/run-project/>)