# Feature Development

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Feature Development

Enrich unified profiles with the required features/traits to drive targeted campaigns.

* * *

  * __3 minute read

  * 


Once you have [performed identity stitching](<https://www.rudderstack.com/docs/archive/profiles/0.14/core-concepts/identity-stitching/#how-to-perform-identity-stitching>) to map the individual entities to known identifiers, you can use its output to enhance the unified profiles with additional data points and features.

You can define the features/traits in your warehouse tables and further perform calculations over this data to devise meaningful outcomes, which can help marketing teams to run effective campaigns.

## Define features

You can use `var_group` to define features. Each `var_group` can have multiple entity vars which can be considered as features for that entity. The Profiles project generates and runs SQL in the background and automatically adds the resulting features to a [feature view](<https://www.rudderstack.com/docs/archive/profiles/0.14/example/feature-views/>).

You can produce a customer [feature view](<https://www.rudderstack.com/docs/archive/profiles/0.14/example/feature-views/>) or a feature view for specific projects like personalization, recommendations, or analytics.

You can combine the features to create even more features. You can also use [custom SQL queries](<https://www.rudderstack.com/docs/archive/profiles/0.14/example/sql-model/>) to enrich unified user profiles for advanced use cases.

A sample `pb_project.yaml` file with a definition of a feature_view::
    
    
    ...
    entities:
      - name: user
        id_types:
          - main_id
          - user_id
        feature_views:
          using_ids:
            - id: user_id
    

A sample configuration file to create `var_groups`:
    
    
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
    

## Benefits

  * You can use the output of the identity graph to define or compute features based on given ID types. Feature views creates a view which will have all or a specified set of features on that entity from across the project based on the identifier column provided.
  * As the number of features/traits increases, Profiles makes the maintenance process much easier by using a configuration file (as opposed to large and complex SQL queries).
  * Profiles generates highly performant SQL to build feature views, which helps mitigate computing costs and engineering resources when the data sets become large, dependencies become complex, and features require data from multiple sources.


### Use-cases

  * Create analytics queries like demographic views, user activity views, etc.
  * Send data using a [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) pipeline to various cloud destinations.
  * Use RudderStack Audiences to send customer profiles to marketing tools (available for beta customers).
  * Define traits/features using `entity_vars` and ML models and unify them using the Feature Views model.


#### See also

  * [Sample feature views project](<https://www.rudderstack.com/docs/archive/profiles/0.14/example/feature-views/>)
  * [Sample SQL model project](<https://www.rudderstack.com/docs/archive/profiles/0.14/example/sql-model/>)


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.14/core-concepts/identity-stitching/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.14/permissions/>)