# IDs

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# IDs

Learn about IDs and ID types in Profiles.

* * *

  * __3 minute read

  * 


This guide introduces you to the concept of IDs in Profiles and shows how to define `id_types` and `ids` in your Profiles project.

## Overview

Creating a Customer360 (C360) is primarily combining data from different sources, or [`inputs`](<https://www.rudderstack.com/docs/archive/profiles/0.24/concepts/inputs/>). ID fields define how those tables are connected.

You can create the [`features`](<https://www.rudderstack.com/docs/archive/profiles/0.24/concepts/features/>) of a C360 by chaining these IDs from different inputs together. Note that IDs are not always consistent between `inputs` in name or format.

Profiles has two concepts related to IDs:

  * `id`: This is the field within `inputs` that is an identifier for a given [entity](<https://www.rudderstack.com/docs/archive/profiles/0.24/concepts/entities/>). For example a user name, an email, or an anonymous ID.
  * `id_type`: These are the categories of an ID. ID fields that have the same `id_type` mean those `inputs` can be joined on those `id`.


**SQL Keyword** : `JOIN ON`

## Requirements

  * ID must be unique for the members of an entity.
  * ID must exist in multiple `inputs`.
  * IDs must be strings.


## Usage

You can define `id_types` in the [`pb_project.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/pb-project-yaml/>) file present in the top level of every Profiles project, as shown:
    
    
    name: llm_sdr_email_content_generation
    schema_version: 85
    connection: llm-recommend-dev
    model_folders:
      - models
    entities:
      - name: user
        id_stitcher: models/user_id_stitcher
    ############### ID Types #################
        id_types:
          - user_id
          - anonymous_id
    ##########################################
        feature_views:                # Optional
          using_ids:
            - id: anonymous_id
              name: anonymous_id_360
              
    ############## ID Type Definitions #######
    id_types:
      - name: user_id
      - name: anonymous_id
        filters:                      # Optional
          - type: exclude
            value: ""
    ##########################################
    python_requirements:              # Optional
      - profiles_mlcorelib==0.7.2
    

You can then define `ids` with the ID types in the [`inputs.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/inputs-yaml/>) file. Each `inputs` ID is labeled with one of the `id_type` defined in [`pb_project.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/pb-project-yaml/>).
    
    
    inputs:
      - name: rsIdentifies
        app_defaults:
          table: rudder_autotrack_data.autotrack.identifies
          occurred_at_col: timestamp
    ########## Map ID to ID Type #############
          ids:
            - select: "anonymous_id"
              type: anonymous_id
              entity: user
            - select: "CAST(user_id AS VARCHAR)" # If data type of user_id column is not a string, you need to cast it to VARCHAR, STRING, or TEXT type depending on your warehouse syntax.
              type: user_id
              entity: user
            - select: "lower(email)"
              type: email
              entity: user
    ##########################################
    

## Best practices

  * You can define `id_types` for the [`id_graph`](<https://www.rudderstack.com/docs/archive/profiles/0.24/concepts/identity-graph/>) or to connect additional tables for `features`.
  * `id_types` should only be identifiers that are relevant to your entities and the features you are going to create. For example, if you are looking at customer support tickets, you do not need to include IDs related to your Customer Success systems.
  * To use email address as an `id_type`, remove the test and internal domains.
  * Ensure the `id_types` you choose are unique. For example, `first_name`, `last_name`, or `cat(first_name, last_name)` would not reasonably be expected to be unique across all users, making them an unsuitable identifier for a user entity. But `user_id` or `email`could be depending on your product.
  * When picking `id_types`, consider the granularity of the `entity`. At the user grain, you will want to pick unique `id_types` of the same grain. For higher level grains like organization or account, you can include user level grain `id_types` as well as org level `id_types` as long each user only belongs to one org or account.
  * If any of your ID columns are not of the string data type, then you must cast the columns to string in the `select` statement.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.24/concepts/entities/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.24/concepts/identity-graph/>)