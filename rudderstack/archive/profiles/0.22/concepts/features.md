# Features

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Features

Learn about features in Profiles.

* * *

  * __less than a minute

  * 


This guide introduces you to the concept of features in Profiles and explains how to define them in your Profiles project.

## Overview

A Customer360 (C360) table contains various customer features. In Profiles, you can create these features using [`entity_vars`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/var-groups/entity-var/>) which, in turn, can be created using an [`input`](<https://www.rudderstack.com/docs/archive/profiles/0.22/concepts/inputs/>), `model` or other `entity_vars`.

## Usage

You can define features in the [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.22/dev-docs/profiles-yaml/>) file, as shown:
    
    
    var_groups:
      - name: user_features
        entity_key: user
        vars:
          - entity_var:
              name: first_seen
              select: min(cast(timestamp as date))
              from: inputs/rsPages
              is_feature: false
              description: First seen date
          - entity_var:
              name: last_seen
              select: max(cast(timestamp as date))
              from: inputs/rsPages
              description: Last seen date
          - entity_var:
              name: user_lifespan
              select: '{{ user.last_seen }} - {{ user.first_seen }}'
              description: User lifespan
    

## Best practices

  * An `entity_var` will automatically group records from a source `input` or `model` by customer, so you need only to specify an aggregate function in the `select` field.
  * Every `entity_var` is included in [`feature_views`](<https://www.rudderstack.com/docs/archive/profiles/0.22/concepts/feature-views/>) by default.
  * To use an `entity_var` to create another `entity_var` but **not include** it as a feature, add `is_feature: false` to the `entity_var` definition.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.22/concepts/inputs/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.22/concepts/feature-views/>)