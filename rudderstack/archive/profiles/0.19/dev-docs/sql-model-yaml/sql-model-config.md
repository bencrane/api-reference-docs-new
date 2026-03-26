# SQL Model Spec

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# SQL Model Spec

Learn how to use `model_spec` for your Profiles project.

* * *

  * __2 minute read

  * 


`model_spec` defines SQL queries, how the table is created, and any [`ids`](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/inputs-yaml/identifiers/>) and [`entities`](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/pb-project-yaml/entities/>) for the table.
    
    
    model_spec:
        materialization:
            output_type: table or ephemeral     # Optional
            run_type: discrete or incremental       # Optional
        single_sql: sql_query       # single_sql or multi_sql required
        occurred_at_col: timestamp  # Optional
        ids:               # Optional
            - select: column
              type: id_type
              entity: entity
    

Key| Description  
---|---  
`output_type`| Output type - accepted values are `table` or `ephemeral`.  
`run_type`| Run type - accepted values are `discrete` or `incremental`.  
`single_sql`  
Required| Evaluates a single SQL statement.  
`multi_sql`  
Required| Evaluates multiple SQL statements. Requires one state to be a `CREATE` statement to materialize the model into a table.  
[`ids`](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/inputs-yaml/identifiers/>)| Define the ID fields, `select`, `id_types`, and related `entity` parameters.  
  
## Syntax

  * Begin `single_sql` or `multi_sql` with `|` to write SQL queries over multiple lines.
  * To import a SQL file, use `{% exec %} {{this.ReadFile("models/sql1.sql")}} {% endexec %}` with the `single_sql` key.
  * To include `inputs` defined in `inputs.yaml`, assign the inputs to a placeholder in a `{$ with %}` statement and using `this.DeRef("models/input_name")`. For example: `{% with input1 = this.DeRef("models/input_name") %}`
  * To reference in the SQL, surround with double curly brackets: `{{ input1 }}`.


## Example
    
    
    # basic example
    model_spec:
        single_sql: |
            select * from table        
    
    # import file saved in models folder
    model_spec:
        single_sql: |
            {% exec %} {{this.ReadFile("models/sql_file.sql")}} {% endexec %}        
    
    # multiple sql queries
    model_spec:
        multi_sql: |
            with ids (
            select distinct id from IDS)
    
            create table events as 
            select * from events where id not in (select * from ids)        
    
    # add ids
    model_spec:
        single_sql: |
            {% exec %} {{this.ReadFile("models/sql_file.sql")}} {% endexec %}        
        ids:
            - select: lower(email_address)
              type: email
              entity: user
    
    # use Profiles input source
    model_spec:
        single_sql: |
            {% with input_table = this.DeRef("inputs/rsIDS) %}
              select 
                id,
                first,
                last
              from
                {{input_table}}
              where
                id_type = 'email'
            {% endwith %}        
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.19/dev-docs/sql-model-yaml/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.19/dev-docs/macros-yaml/>)