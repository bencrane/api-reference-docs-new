# Define Cohorts in Profiles

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Define Cohorts in Profiles

Create core customer segments in your warehouse.

* * *

  * __2 minute read

  * 


You can define [cohorts](<https://www.rudderstack.com/docs/archive/profiles/0.22/concepts/cohort/>) along with any associated features and feature views in the [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/>) file.
    
    
    models:
        - name: cohort_name
            model_type: entity_cohort
            model_spec:
                extends: cohort/path    # Optional
                materialization:        # Optional
                    output_type: table\view  
                filter_expression:        # Optional
                  AND/OR:
                    - filter_condition
                feature_views:          # Optional
                    - id: column
                      name: feature_view_name
    

Key| Description  
---|---  
`name`  
Required| Model name.  
`model_type`  
Required| Model type - set this parameter to `entity_cohort`.  
`model_spec`  
Required| Model configuration.  
`extends`| Path to the parent cohort. `users/all` is used for all members of an entity.  
`output_type`| Warehouse output, either `table` or `view`.  
`filter_expression`| Defines the filters.  
`type`| Filter type - accepted values are `include` or `exclude`.  
`value`| SQL statement of rows to filter (similar to a `where` clause).  
`feature_view`| Defines the `id` and `name` of any views.  
  
## Example
    
    
    # Basic cohort
    
    models:
        - name: knownUsers
          model_type: entity_cohort
          model_spec:
              extends: user/all
              materialization:
                 output_type: table
              filter_expression: "{{ user.id_type_email_count }} > 0"
    
    # A cohort of a cohort
    
    models:
        - name: knownUsersOrderWithCC
          model_type: entity_cohort
          model_spec:
              extends: models/knownUsers
              materialization:
                  output_type: view
             filter_expression:
                AND:
                  - "{{ knownUsers.has_credit_card }} = 1"
                  - "{{ knownUsers.order_total }} > 0"
    
    # Adding a feature view to a cohort
    
    models:
        - name: knownUsers
          model_type: entity_cohort
          model_spec:
              extends: user/all
              materialization:
                  output_type: table
              filter_expression: "{{ user.id_type_email_count }} > 1"
              feature_views:
                name: known_users_feature_view
                  - id: email
                    name: known_users_by_email
    
    # Combining two cohorts into a new cohort
    
    models:
      - name: americanUsers
        model_type: entity_cohort
        model_spec:
           extends: user/all
           filter_expression:
            OR:
              - "{{ warehouse.EntityCohortCondition('models/north_american_users', 'in') }}"
              - "{{ warehouse.EntityCohortCondition('models/south_american_users', 'in') }}"
    
    # Create var_group for a cohort
    
    var_groups:
        - name: known_users_vars
          entity_cohort: models/knownUsers
          vars:
              - entity_var:
                name: last_transaction
                select: max(order_date)
                from: inputs/orders
    

## View cohorts in RudderStack dashboard

You can view the output for cohorts in the **Entities** tab of the UI once you [import a Profiles project from Git](<https://www.rudderstack.com/docs/archive/profiles/0.22/management/import-from-git/>) and run it.

[![Entities Tab - Cohorts](/docs/images/profiles/cohorts-view-ui.webp)](</docs/images/profiles/cohorts-view-ui.webp>)

> ![info](/docs/images/info.svg)
> 
> Contact the Profiles support team in RudderStack’s [Community Slack](<https://rudderstack.com/join-rudderstack-slack-community>) if you are unable to see the **Entities** tab.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/window-functions/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.22/dev-docs/inputs-yaml/>)