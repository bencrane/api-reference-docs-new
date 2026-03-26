# Feature Development

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Feature Development

Use unified profiles and enrich them with the required features/traits to drive targeted campaigns.

* * *

  * __2 minute read

  * 


Once you have [performed identity stitching](<https://www.rudderstack.com/docs/archive/profiles/0.11/identity-stitching/#how-to-perform-identity-stitching>) to map the individual entities to known identifiers, you can enhance the unified profiles with additional data points and features.

To develop user features, you can use a **feature table** to define the features/traits in your warehouse tables. You can perform calculations over this data to devise meaningful outcomes, which can help marketing teams to run effective campaigns.

## How to define features?

You can use RudderStack’s [Feature Table model](<https://www.rudderstack.com/docs/archive/profiles/0.11/example/feature-table/>) to write feature definitions. The Profiles project generates and runs SQL in the background and automatically adds the resulting features to a feature table.

You can produce a customer feature table or a feature table for specific projects like personalization, recommendations, or analytics.

> ![success](/docs/images/tick.svg)
> 
> You can combine the features to create even more features. You can also use [custom SQL queries](<https://www.rudderstack.com/docs/archive/profiles/0.11/feature-development/sql-models/>) to enrich unified user profiles for advanced use cases.

A sample configuration file to create a feature table:
    
    
    var_groups:
      - name: user_vars
        entity_key: user
        vars:
          - entity_var:
              name: first_seen
              select: min(timestamp::date)
              from: inputs/rsTracks
              is_feature: false
          - entity_var:
              name: last_seen
              select: max(timestamp::date)
              from: inputs/rsTracks
              is_feature: false
          - entity_var:
              name: user_lifespan
              select: '{{user.Var("last_seen")}} - {{user.Var("first_seen")}}'
              description: Life Time Value of a customer
          - entity_var:
              name: days_active
              select: count(distinct timestamp::date)
              from: inputs/rsTracks
              description: No. of days a customer was active
    # ID stitcher
    models:
      - name: domain_profile_id_stitcher
        model_type: id_stitcher
        model_spec:
          validity_time: 24h # 1 day
          entity_key: user
          materialization:
            run_type: incremental
          edge_sources:
            - from: inputs/rsIdentifies
            - from: inputs/rsTracks
    # Feature table
      - name: domain_profile
        model_type: feature_table_model
        model_spec:
          validity_time: 24h # 1 day
          entity_key: user
        features:
            - user_lifespan
            - days_active
    

## Benefits

  * You can use the output of the identity graph to define or compute features across multiple feature tables.
  * As the number of features/traits increases, Profiles makes the maintenance process much easier by using a configuration file (as opposed to large and complex SQL queries).
  * Profiles generates highly performant SQL to build feature tables, which helps mitigate computing costs and engineering resources when the data sets become large, dependencies become complex, and features require data from multiple sources.


## Use-cases

  * Create analytics queries like demographic views, user activity views, etc.
  * Send data using a [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) pipeline to various cloud destinations.
  * Use RudderStack Audiences to send customer profiles to marketing tools (available for beta customers).


#### See also

  * [Sample feature table project](<https://www.rudderstack.com/docs/archive/profiles/0.11/example/feature-table/>)


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/identity-stitching/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/feature-development/sql-models/>)