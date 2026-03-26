# Identity Graph

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Identity Graph

Learn about identity graphs in Profiles.

* * *

  * __2 minute read

  * 


This guide introduces you to the concept of identity graphs in Profiles and shows how to use them in your Profiles project.

## Overview

Multiple identities is the biggest obstacle to getting a full picture of your customers, user, or any other [`entity`](<https://www.rudderstack.com/docs/archive/profiles/0.19/concepts/entities/>).

Companies gather user data across digital touchpoints like websites, mobile apps, enterprise systems like CRMs, marketing platforms, etc. During this process, a single user is identified with multiple identifiers across your systems, like email address, phone number, device ID, anonymous ID, user name, etc. To create a unified user profile, it is vital to collect and stitch all of those different identifiers into one canonical identifier.

You can leverage Profiles’ `id_stitcher` model to take your inputs and stitch all the identifiers together into an identity graph.

## Requirements

  * Defined [`id_types`](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/pb-project-yaml/id-types/>) for your entity and mapped to your input sources.


## Usage

The identity graph is located in the [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/profiles-yaml/>) file as an `id_stitcher` model.
    
    
    models:
      - name: user_id_stitcher
        model_type: id_stitcher
        model_spec:
          entity_key: user
          edge_sources:
            - from: inputs/rsIdentifies
            - from: inputs/rsPages
    

## Best practices

  * For the `identity_stitcher` model, use **only** the `id_types` and `inputs` necessary to stitch the identifiers relevant to an `entity`. For example, if you don’t care about anonymous traffic, do not add `anonymous_id` as an `id_type` or any `inputs` related to anonymous traffic.
  * Conceptually, you can think of your `identity_graph` table as a kind of fact table in star or Snowflake schema. All of your core identifiers are in the center table and are used to connect to your `inputs`.
  * Only include `inputs` as edge sources that include `id_types` directly related to the entity (the first level out from the fact table in a Snowflake schema). For example, you may need to include an `id_type` for product names because they are in a separate table but you do not want to include them in the `identity_graph`.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.19/concepts/id/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.19/concepts/inputs/>)