# Cohorts

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Cohorts

Learn about user cohorts in Profiles.

* * *

  * __2 minute read

  * 


This guide introduces you to the concept of cohorts in Profiles and shows how to use them in your Profiles project.

## Overview

All businesses have core entities like customers. Within those entities, there are core segments that are tracked and interacted with across the business, for example, high value customers, brands, business segments, regions, etc.

In Profiles, you can create these enduring subsets by leveraging **cohorts**. You use the [features](<https://www.rudderstack.com/docs/archive/profiles/0.23/concepts/features/>) of your Customer360 (C360) to filter [entities](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/profiles-yaml/var-groups/entity-var/>) into these cohorts. This gives you a stable definition for these important segments within the warehouse that you can leverage across the business.

## Requirements

  * Features used for filtering must be defined in the `entity/all` `cohort` or other parent `cohort` `var_group`.


## Usage

You can define cohorts in the [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/profiles-yaml/>) file, as shown:
    
    
    # Cohort definition
    models:
      - name: credit_card_user
        model_type: entity_cohort
        model_spec:
          extends: customers/all
          materialization:
            output_type: view
          filter_expression:
            AND:
              - "{{ customers.has_credit_card }} = 1"
          feature_views:
            - id: email
              name: credit_card_user_by_email
    
    # Cohort Feature Definition
    var_groups:
      - name: credit_card_user_vars
        entity_cohort: models/credit_card_user
        vars:
          - entity_var:
              name: total_sales
              select: sum(total)
              from: inputs/orders
          - entity_var:
              name: total_orders
              select: count(order_id)
              from: inputs/orders
    

## Best practices

  * Use cohorts as sub-groups that require a standard definition, can be used across teams, and are needed to exist for a long period of time. For example, key customer segments, brands, or business units, but not a campaign audience.
  * Cohorts can also be a subset of another cohort. For example, you can create a cohort named `known_mobile_users` by filtering the `known_users` cohort.
  * A child cohort inherits all the features from their parent and can have features and [feature views](<https://www.rudderstack.com/docs/archive/profiles/0.23/concepts/feature-views/>) defined at the individual cohort level.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.23/concepts/feature-views/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.23/concepts/timegrains/>)