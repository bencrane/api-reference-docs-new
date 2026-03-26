# sql_models.yaml

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# sql_models.yaml

Write SQL queries in a Profile project.

* * *

  * __less than a minute

  * 


You can write queries within the YAML file or in standalone `sql` files and reference them in the `sql_template` model. They have the same keys as an [`input` model](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/inputs-yaml/>).

This data is saved in the `model` folder of a Profiles project, along with any referenced `sql` files.
    
    
    models:
        - name: name_of_sql_model       
          model_type: sql_template      
          model_spec:
              <model-spec>
    

Key| Description  
---|---  
`name`  
Required| SQL model name.  
`model_type`  
Required| Model type - set it to `sql_template`.  
`model_spec`  
Required| Model configuration. See [SQL Model Spec](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/sql-model-yaml/sql-model-config/>) for more information.  
  
## Example
    
    
    models:
        - name: 
          model_type: sql_template
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
              ids:
                  select: "id"
                  type: user_id
                  entity: user
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.22/dev-docs/inputs-yaml/s3-bucket-input/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.22/dev-docs/sql-model-yaml/sql-model-config/>)