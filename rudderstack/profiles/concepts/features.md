# Features

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Features

Learn about features in Profiles.

* * *

  * __2 minute read

  * 


This guide introduces you to the concept of features in Profiles and explains how to define them in your Profiles project.

## Overview

A Customer360 (C360) table contains various customer features. In Profiles, you can create these features using [`entity_vars`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/var-groups/entity-var/>) which, in turn, can be created using an [`input`](<https://www.rudderstack.com/docs/profiles/concepts/inputs/>), `model` or other `entity_vars`.

## Usage

You can define features in the [`profiles.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/>) file, as shown:
    
    
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
    

## Incremental features

> ![announcement](/docs/images/announcement.svg)
> 
> This is a beta feature.

Profiles also supports [Incremental Features](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/>) to help reduce warehouse costs, especially in case of large datasets.

By adding a `merge:` clause to your `entity_var` definitions and marking the input model as `is_append_only: true`, you enable Profiles to process only new data and merge it with previously computed values — improving performance and reducing costs considerably.

## Controlling update frequency

Not all features need to be computed on every run — use [Timegrains](<https://www.rudderstack.com/docs/profiles/concepts/timegrains/>) to control how often features are updated:
    
    
    var_groups:
      - name: realtime_signals
        entity_key: user
        time_grain: day       # Computed daily
        vars:
          - entity_var:
              name: last_active_date
              select: max(timestamp::date)
              from: inputs/rsPages
    
      - name: monthly_aggregates
        entity_key: user
        time_grain: month     # Computed monthly
        vars:
          - entity_var:
              name: favorite_category
              select: mode(category)
              from: inputs/orders
    

This helps reduce compute costs for features that don’t need frequent updates.

## Best practices

  * An `entity_var` will automatically group records from a source `input` or `model` by customer, so you need only to specify an aggregate function in the `select` field.
  * Every `entity_var` is included in [`feature_views`](<https://www.rudderstack.com/docs/profiles/concepts/feature-views/>) by default.
  * To use an `entity_var` to create another `entity_var` but **not include** it as a feature, add `is_feature: false` to the `entity_var` definition.
  * For large datasets, consider making features incremental to improve performance.
  * Group features by update frequency using `time_grain` on `var_group` to optimize compute costs.

  


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/concepts/inputs/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/concepts/incremental-features/>)