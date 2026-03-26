# ID Collator

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# ID Collator

Step-by-step tutorial stitching different user identities together.

* * *

  * __3 minute read

  * 


ID Stitching is one of the most important features of Profiles. Being able to perform ID stitching to determine the accounts belonging to the same customer/user is very important to get a 360-degree view of that user.

However many a times, we may not require ID stitching for a particular entity, especially if there are no edges in the ID graph of an entity. To build a feature view on such an entity, you will still need to perform ID stitching. Although this approach is not wrong, it is computationally redundant.

Profiles provides the ID Collator is to get all IDs of that particular entity from various input tables and create one collated list of IDs.

## Sample project

Let’s take a case where we have defined two entities in our project - one is `user` and the other is `session`.

If `user` entity has multiple IDs defined, there are basically edges which make the use of an ID stitcher logical. On the other hand, `session` may have only one ID, `ssn_id`, there won’t be any possibility of edges. In such a case, all we need is a complete list of `ssn_id`.

Here is the corresponding inputs and entities definition.
    
    
    entities:
      - name: user
        id_column_name: user_rud_id
        id_types:
          - user_id
          - anonymous_id
      - name: session
        id_column_name: session_id
        id_types:
          - ssn_id
    

Project file:
    
    
    inputs:
      - name: user_accounts
        table: tbl_user_accounts
        occurred_at_col: insert_ts
        ids:
          - select: "user_id"
            type: user_id
            entity: user
      - name: sign_in
        table: tbl_sign_in
        occurred_at_col: insert_ts
        ids:
          - select: "user_id"
            type: user_id
            entity: user
          - select: "ssn_id"
            type: ssn_id
            entity: session
          - select: "anonymous_id"
            type: anonymous_id
            entity: user
      - name: sign_up
        table: tbl_sign_up
        occurred_at_col: insert_ts
        ids:
          - select: "user_id"
            type: user_id
            entity: user
          - select: "ssn_id"
            type: ssn_id
            entity: session
          - select: "anonymous_id"
            type: anonymous_id
            entity: user
    

Here, the `entity: session` has only one ID type. Creating an ID stitcher for such an entity is possible but unnecessary.

Using all the models having `ssn_id`, we can just make a union of all `ssn_id` and get all distinct values of it and obtain the final list of sessions.

The underlying SQL will look as follows:
    
    
    SELECT ssn_id AS session_id FROM sign_in
    UNION
    SELECT ssn_id AS session_id FROM sign_up;
    

## YAML Changes

The YAML writer cannot define a custom ID collator the way they define a custom ID stitcher. If an entity has no edges, the PB project will automatically figure out if an ID collator is needed. To exclude certain inputs (having the required ID) from being used in the collation, we can just set `to_id_stitcher: false` in the input.
    
    
    entities:
      - name: session
        id_column_name: session_id
        id_types:
          - ssn_id
    

The `id_column_name` is a new field added in the entity definition which will be the name of the ID column and it applies to both ID stitcher and ID collator.

> ![info](/docs/images/info.svg)
> 
> In the ID collator, you won’t generate a UUID like in ID stitcher.

## Comparing ID Collator and ID Stitcher

ID Stitcher| ID Collator  
---|---  
Uses edges to converge the ID graph.| Collates all distinct IDs as there is only one ID Type and no edges are present.  
Higher cost of computation.| Lower cost of computation.  
A UUID is generated and used as the unique identifier for the entity.| Collates the existing IDs only.  
The generated ID is always of the type: `rudder_id`| The ID column of the generated ID collator table/view will be of the ID type of the corresponding ID.  
User may override the default ID stitcher with custom one.| You cannot override the default ID collator, though you can define a custom ID stitcher to override default ID collator.  
  
  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.15/example/id-stitcher/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.15/example/feature-table/>)