# SQL Models

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# SQL Models

Use custom SQL queries to enrich unified profiles for some advanced use-cases.

* * *

  * __less than a minute

  * 


In [feature development](<https://www.rudderstack.com/docs/archive/profiles/0.11/feature-development/>), you can define and use features to deliver meaningful business outcomes. However, there might be cases where you want to implement some complex use cases that are difficult to achieve by defining only a few features.

With Profiles, you can use **SQL models** to write custom SQL queries to define specific user features.

## How to use SQL Models?

You can use the RudderStack’s [SQL models](<https://www.rudderstack.com/docs/archive/profiles/0.11/example/sql-model/>) to write custom SQL queries defining the required features/traits.

A sample configuration file to create a SQL model:
    
    
    models:
    - name: test_sql
      model_type: sql_template
      model_spec:
        validity_time: 24h# 1 day
        materialization:                 // optional
          run_type: discrete             // optional [discrete, incremental]
        single_sql: |
            {%- with input1 = this.DeRef("inputs/tbl_a") -%}
              select id1 as new_id1, id2 as new_id2, {{input1}}.* 
                from {{input1}}
            {%- endwith -%}        
        occurred_at_col: insert_ts        // optional
        ids:
          - select: "new_id1"
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "new_id2"
            type: test_id
            entity: user
            to_default_stitcher: true
          - select: "id3"
            type: test_id
            entity: user
            to_default_stitcher: true
    

## Use-cases

  * Track first-touch attribution to extract the first-touch channel across customer activity.
  * Extract the last seen attribute for users by extracting the max timestamp across all the sources.


#### See also

  * [Sample SQL model project](<https://www.rudderstack.com/docs/archive/profiles/0.11/example/sql-model/>)


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/feature-development/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/predictions/>)