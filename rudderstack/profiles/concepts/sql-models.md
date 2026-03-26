# SQL Models

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# SQL Models

Learn about SQL models in Profiles.

* * *

  * __2 minute read

  * 


This guide introduces you to the concept of SQL models in Profiles and shows how to use them in your Profiles project.

## Overview

Profiles projects allows for the importing and transformation of almost any source. However, there are edge cases that cannot be completed, or are overly onerous in case of Profiles. You can use SQL models in such cases.

SQL models allow you to model data using plain or templated SQL. This is useful for complex use cases where you need to join, union, or intermediately transform data.

You can use a SQL model as an ephemeral source for ID stitcher and feature creation models, materialize it as a table or view.

## Usage

You can define SQL models in the [`sql_model.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/sql-model-yaml/>) file, as shown:
    
    
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
    

## Relationship to other Profiles features

SQL models integrate with other Profiles capabilities:

  * **Incremental SQL Models** : Regular SQL models can be made incremental by dereferencing their own previous materialization. See [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/incremental-sql-models/>) for details on enabling incremental processing for complex stateful patterns.
  * **ID Stitcher** : SQL models can serve as ephemeral sources for ID stitcher, providing transformed data for identity resolution.
  * **Feature Creation** : SQL models can be used as intermediate data sources for entity vars and feature creation, enabling complex data transformations before aggregation.
  * **Materialization Options** : SQL models can be materialized as tables (persistent storage), views (virtual tables), or ephemeral sources (temporary computation).


## Best practices

  * Verify the outputs of any SQL model in your warehouse before adding to a Profiles project.

  


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/concepts/timegrains/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/concepts/cleanup/>)