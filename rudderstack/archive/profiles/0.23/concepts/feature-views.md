# Feature Views

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Feature Views

Learn about feature views in Profiles.

* * *

  * __2 minute read

  * 


This guide introduces you to the concept of feature views in Profiles and shows how to use them in your Profiles project.

## Video walkthrough

## Overview

Profiles adds a unique ID when you create a Customer360 (C360) table. But for most activation use cases, you need to use a specific ID from your data warehouse, like user_name, email, or anonymous ID. You can achieve this using SQL, the ID graph table, and the C360 table, but it is complicated and can be difficult to maintain.

Profiles can create these pivots automatically with `feature views`. They include the same [`entity_vars`](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/profiles-yaml/var-groups/entity-var/>) as the C360 table but with the chosen ID as the primary key.

**SQL Keyword** : `VIEW`

## Requirements

  * `entity_vars` where `is_feature` is set to `true`.
  * View primary ID is included in ID graph.


## Usage

Feature views (`feature_views`) are in the [`pb_project.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.23/dev-docs/pb-project-yaml/>) file within the `entities` block, as shown:
    
    
    name: llm_sdr_email_content_generation
    schema_version: 85
    connection: llm-recommend-dev
    model_folders:
      - models
    entities:
      - name: user
        id_stitcher: models/user_id_stitcher
        id_types:
          - user_id
          - anonymous_id**
    ###########################################
        feature_views:
          using_ids:
            - id: anonymous_id
              name: anonymous_id_360
    ###########################################
    id_types:
      - name: user_id
      - name: anonymous_id
        filters:                      # Optional
          - type: exclude
            value: ""
    python_requirements:              # Optional
      - profiles_mlcorelib==0.7.2
    

## Best practices

  * Profiles automatically creates a feature view where the `main_id` is the primary key, called `{entity_name}_feature_view`. It is a best practice to create another `feature view` using a desired ID type as the primary key for data activation.
  * All features will be included in all feature views for an entity, unless you set `is_feature` to `false` for a specific `entity_var`.
  * Feature views are defined in `pb_project.yaml` for the `user/all` [cohort](<https://www.rudderstack.com/docs/archive/profiles/0.23/concepts/cohort/>). For individual cohorts, they are defined in the cohort definition in `profiles.yaml`.
  * [`Cohorts`](<https://www.rudderstack.com/docs/archive/profiles/0.23/concepts/cohort/>) inherit the features from their parent, so you do not need to define them at the cohort level.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.23/concepts/features/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.23/concepts/cohort/>)