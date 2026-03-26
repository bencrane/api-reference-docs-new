# Entities

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Entities

Learn about entities in Profiles.

* * *

  * __2 minute read

  * 


This guide introduces you to the concept of entities in Profiles and shows how to define `entities` in your Profiles project.

## Overview

Every business has artifacts that are tracked across systems for creating a complete data picture of that artifact. In Profiles, these are called `Entities`.

`Entities` can be as common as users, accounts, etc. It can also expand to be anything that you can track across systems and want a complete picture of, like campaigns, devices, or even month of the year.

`Entities` are the central concept that a Profiles project is built around. It is where you define what your identity graphs and C360 tables are built around.

**SQL Keyword** : `GROUP BY`

## Requirements

  * An entity must have multiple IDs in the data sources, also called as [`inputs`](<https://www.rudderstack.com/docs/archive/profiles/0.21/concepts/inputs/>).
  * Each input must have at least one ID that is shared with another input.
  * No ID can be shared across any member of an entity (that is, an ID cannot shared by multiple users).


## Usage

You can use`entities` in the [`pb_project.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.21/dev-docs/pb-project-yaml/>) file present in the top level of every Profiles project, as shown:
    
    
    name: profiles_project
    schema_version: 85
    connection: wh_connection_dev
    model_folders:
      - models
    ##########################################
    entities:
      - name: user
        id_stitcher: models/user_id_stitcher
        id_types:
          - user_id
          - anonymous_id
        feature_views:                # Optional
          using_ids:
            - id: anonymous_id
              name: anonymous_id_360
    ##########################################
    id_types:
      - name: user_id
      - name: anonymous_id
        filters:                      # Optional
          - type: exclude
            value: ""
    python_requirements:              # Optional
      - profiles_mlcorelib==0.7.2
    

## Best practices

  * As `entities` are the central building block of a Profiles project, you should define them **before** building the rest of the project.
  * Most common `entities` include user, account, organization, and prospect. But you can define an entity for anything that you want to group and aggregate your data around, including marketing campaigns, business units, or even months of the year (for monthly reporting).
  * When picking [`id_types`](<https://www.rudderstack.com/docs/archive/profiles/0.21/dev-docs/pb-project-yaml/id-types/>), consider the granularity of the entity. At the user grain, you will want to pick unique `id_types` of the same grain. For higher level grains like organization or account, you can include user level grain `id_types` as well as org level `id_types` as long each user only belongs to one org or account.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.21/concepts/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.21/concepts/id/>)