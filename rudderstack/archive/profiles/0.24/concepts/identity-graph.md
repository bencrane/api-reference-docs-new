# Identity Graph

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Identity Graph

Learn about identity graphs in Profiles.

* * *

  * __3 minute read

  * 


This guide introduces you to the concept of identity graphs in Profiles and shows how to use them in your Profiles project.

## Overview

Multiple identities is the biggest obstacle to getting a full picture of your customers, user, or any other [`entity`](<https://www.rudderstack.com/docs/archive/profiles/0.24/concepts/entities/>).

Companies gather user data across digital touchpoints like websites, mobile apps, enterprise systems like CRMs, marketing platforms, etc. During this process, a single user is identified with multiple identifiers across your systems, like email address, phone number, device ID, anonymous ID, user name, etc. To create a unified user profile, it is vital to collect and stitch all of those different identifiers into one canonical identifier.

You can leverage Profiles’ `id_stitcher` model to take your inputs and stitch all the identifiers together into an identity graph.

An identity graph consists of two main components:

  * **Nodes** : Represent individual identifiers that belong to an entity.
  * **Edges** : Represent the relationships observed between these identifiers in your input data.


## Requirements

  * Defined [`id_types`](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/pb-project-yaml/id-types/>) for your entity and mapped to your input sources.
  * Identifiers from your inputs must be of the string data type. If the columns in your input sources are not of string types already, you must cast them explicitly.


## Usage

The identity graph is located in the [`profiles.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/profiles-yaml/>) file as an `id_stitcher` model.
    
    
    models:
      - name: user_id_stitcher
        model_type: id_stitcher
        model_spec:
          entity_key: user
          edge_sources:
            - from: inputs/rsIdentifies
            - from: inputs/rsPages
    

## Metadata and observability

To provide transparency into the stitching process, you can enable metadata logging using the following flags in your `id_stitcher` model specification. These flags control what metadata is logged for the identity graph components:

Flag| Description  
---|---  
`log_direct_edge_info`| Logs metadata about the direct relationships (edges) between identifiers.  
`log_node_metadata`| Logs metadata for each individual identifier (node).  
  
An example of how to enable these flags is shown below:
    
    
    models:
      - name: user_id_stitcher
        model_type: id_stitcher
        model_spec:
          entity_key: user
          log_direct_edge_info: true
          log_node_metadata: true
          edge_sources:
            - from: inputs/rsIdentifies
            - from: inputs/rsPages
    

This metadata helps you understand how identifiers are connected and trace the lineage of your identity graph.

### Metadata structure

The generated metadata contains two main objects:

Object| Details  
---|---  
`node_info`| Array of objects containing aggregated metadata for the node (identifier) itself. It includes the `source_model` where the identifier was first seen and the `first_seen_at` timestamp.  
`direct_edge_info`| Object containing details about the direct relationships (edges) of a node. It is broken down by the identifier type (`edges_by_type`) and includes a `count` of edges and an array of the connected nodes, including when and where the connection was first observed.  
  
Here is an example of the metadata structure:
    
    
    {
      "direct_edge_info": {
        "edges_by_type": {
          "email": {
            "count": 1,
            "edges": [
              {
                "first_seen_at": "2001-06-01 00:00:01.000",
                "first_seen_source_model": ["tbl_identifies"],
                "id": "self_user"
              }
            ]
          }
        }
      },
      "node_info": [
        {
          "first_seen_at": "2001-06-01 00:00:01.000",
          "source_model": [
            "tbl_identifies"
          ]
        }
      ]
    }
    

## Best practices

  * For the `identity_stitcher` model, use **only** the `id_types` and `inputs` necessary to stitch the identifiers relevant to an `entity`. For example, if you don’t care about anonymous traffic, do not add `anonymous_id` as an `id_type` or any `inputs` related to anonymous traffic.
  * Conceptually, you can think of your `identity_graph` table as a kind of fact table in star or Snowflake schema. All of your core identifiers are in the center table and are used to connect to your `inputs`.
  * Only include `inputs` as edge sources that include `id_types` directly related to the entity (the first level out from the fact table in a Snowflake schema). For example, you may need to include an `id_type` for product names because they are in a separate table but you do not want to include them in the `identity_graph`.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.24/concepts/id/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.24/concepts/inputs/>)