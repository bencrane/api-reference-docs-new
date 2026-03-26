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


Once you have [performed identity stitching](<https://www.rudderstack.com/docs/archive/profiles/0.18/core-concepts/identity-stitching/#how-to-perform-identity-stitching>) to map the individual entities to known identifiers, you can use its output to enhance the unified profiles with additional data points and features.

You can define the features/traits in your warehouse tables and further perform calculations over this data to devise meaningful outcomes, which can help marketing teams to run effective campaigns.

## Define features

You can use `var_groups` to define features. Each `var_group` can have multiple entity vars which can be considered as features for that entity. The Profiles project generates and runs SQL in the background and automatically adds the resulting features to a [feature view](<https://www.rudderstack.com/docs/archive/profiles/0.18/example/feature-views/>).

You can produce a customer feature view or a feature view for specific projects like personalization, recommendations, or analytics.

Further, you can combine the features to create even more features or use [custom SQL queries](<https://www.rudderstack.com/docs/archive/profiles/0.18/example/sql-model/>) to enrich unified user profiles for advanced use cases.

A sample `pb_project.yaml` file with the `feature_view` definition:
    
    
    ...
    entities:
      - name: user
        id_types:
          - main_id
          - user_id
        feature_views:
          using_ids:
            - id: user_id
    

A sample `profiles.yaml` file with `var_groups`:
    
    
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
              select: '{{user.last_seen}} - {{user.first_seen}}'
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
          entity_key: user
          materialization:
            run_type: incremental
          edge_sources:
            - from: inputs/rsIdentifies
            - from: inputs/rsTracks
    

## Feature creation models

To create features for your entity, you must define the following in your Profiles project:

  * An entity
  * A `var_group` for the entity
  * `entity_vars` within that group, which represent the individual variables (attributes or traits) for your entity


Once you define the above, RudderStack creates the following model types by default:

  * Input var table
  * Entity var table
  * Default cohort (view named **ALL**)


These models act as the base models to create and store the features and are not meant to be activated to the downstream systems. To activate these features, you can create the [feature view model](<https://www.rudderstack.com/docs/archive/profiles/0.18/example/feature-views/>). All the features (which are not explicitly excluded) will automatically propagate to the feature view model from where you can activate them against any ID type.

## Benefits

  * You can use the output of the identity graph to define or compute features based on given ID types. Feature view creates a view which will have all or a specified set of features on that entity from across the project based on the identifier column provided.
  * As the number of features/traits increases, Profiles makes the maintenance process much easier by using a configuration file (as opposed to large and complex SQL queries).
  * Profiles generates highly performant SQL to build feature views, which helps mitigate computing costs and engineering resources when the data sets become large, dependencies become complex, and features require data from multiple sources.


### Use-cases

  * Create analytics queries like demographic views, user activity views, etc.
  * Send data using a [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) pipeline to various cloud destinations.
  * Use RudderStack Audiences to send customer profiles to marketing tools (available for beta customers).
  * Define traits/features using `entity_vars` and ML models and unify them using the feature view model.


#### See also

  * [Sample feature view project](<https://www.rudderstack.com/docs/archive/profiles/0.18/example/feature-views/>)
  * [Sample SQL model project](<https://www.rudderstack.com/docs/archive/profiles/0.18/example/sql-model/>)


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.18/core-concepts/identity-stitching/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.18/permissions/>)