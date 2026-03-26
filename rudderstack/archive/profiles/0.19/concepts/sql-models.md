# SQL Models

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# SQL Models

Learn about SQL models in Profiles.

* * *

  * __less than a minute

  * 


This guide introduces you to the concept of SQL models in Profiles and shows how to use them in your Profiles project.

## Overview

Profiles projects allows for the importing and transformation of almost any source. However, there are edge cases that cannot be completed, or are overly onerous in case of Profiles. You can use SQL models in such cases.

SQL models allow you to model data using plain or templated SQL. This is useful for complex use cases where you need to join, union, or intermediately transform data.

You can use a SQL model as an ephemeral source for ID stitcher and feature creation models, materialize it as a table or view.

## Usage

You can define SQL models in the [`sql_model.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/sql-model-yaml/>) file, as shown:
    
    
    models:
      - name: tracks_union_pages
        model_type: sql_template
        model_spec:
          materialization:
            output_type: view
            run_type: discrete
          single_sql: |
            {% with tracks = this.DeRef("inputs/tracks") pages = this.DeRef("inputs/pages") %}
            SELECT
              anonymous_id,
              event,
              timestamp
            FROM {{ tracks }}
            UNION
            SELECT
              anonymous_id,
              'page_viewed' AS event,
              timestamp
            FROM {{ pages }}
            {% endwith %}        
    

## Best practices

  * Verify the outputs of any SQL model in your warehouse before adding to a Profiles project.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.19/concepts/cohort/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.19/dev-docs/>)