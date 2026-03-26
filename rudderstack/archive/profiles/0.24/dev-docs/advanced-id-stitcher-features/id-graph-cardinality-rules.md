# ID Graph Cardinality Rules

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# ID Graph Cardinality Rules

Define maximum connection limits between different ID types to provide fine-grained control over identity stitching.

* * *

  * __7 minute read

  * 


This guide explains how to use cardinality rules to limit the maximum number of connections between different ID types in your identity graph.

> ![info](/docs/images/info.svg)
> 
> This feature is only available for **Snowflake** currently — support for other warehouses is coming soon.

## Overview

ID Graph cardinality rules let you define maximum connection limits between different ID types in your identity graph, providing fine-grained control over how identities are stitched together.

> ![info](/docs/images/info.svg)
> 
> Cardinality rules help prevent identity explosion and maintain data quality by limiting how many connections a node of one type can have to nodes of another type.
> 
> This is particularly useful for maintaining data quality when dealing with shared identifiers like email addresses, device IDs, or anonymous IDs that might be used across multiple users.

Cardinality rules work seamlessly with other Profiles features:

  * Input [filters](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/pb-project-yaml/id-types/>) reduce data volume before graph processing. The cardinality enforcement step comes after this in the pipeline, so if expected nodes are missing from your graph, input filters can be the reason.
  * Manual [exclusion/inclusion rules](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/advanced-id-stitcher-features/id-graph-rules/>) provide explicit control over specific connections and happen after the cardinality enforcement step in the pipeline. If you find identity clusters that violate cardinality rules despite having the rules configured, those extra edges might be coming from manual inclusion overrides.


### Key features

  * **Data quality** : You can prevent identity graphs from becoming overly connected due to shared or recycled identifiers.
  * **Performance** : Maintain optimal graph size by controlling edge proliferation.
  * **Compliance** : Enforce business rules about identity relationships.
  * **Transparency** : Get full audit trail of which edges were filtered and why.
  * **Incremental consistency** : Historical violations persist across runs for reliable behavior.


### Performance considerations

Consider the following when implementing cardinality rules:

  * **Initial runs** may experience increased runtime as the system processes and enforces the new rules across your entire dataset.
  * **Incremental runs** should see minimal performance impact once the rules are established.
  * **Trade-off evaluation** : The increased runtime in initial runs delivers more precise ID stitching and better data quality. Evaluate whether the improved accuracy justifies the additional processing time for your use case.


## How cardinality rules work

### Directional rules

Cardinality rules are **directional** — they apply from a source ID type to a target ID type. For example:

  * `user_id → email: max_edges = 2` means each `user_id` can connect to at most 2 `email`.
  * Note that this does not limit how many `user_id` an `email` can connect to (unless you add a separate rule)


### Rule enforcement

When a rule is violated:

  1. **All edges** from the violating source are removed (not just the excess ones)
  2. **Nodes are preserved** as isolated stubs to maintain graph integrity
  3. **Violations are audited** with full details about what was removed and why
  4. **Historical context** is maintained across incremental runs


### Incremental behavior

The feature works seamlessly with incremental runs:

  * **Historical violations persist** : If a node violated a rule previously, new edges to that node type are automatically blocked.
  * **New violations break all edges** : If a new edge causes a violation, all current edges from that source are removed.
  * **Rule removal** : If you remove a rule from your configuration, the entire id graph is built from scratch, so historical violations for that rule are no longer enforced.


## Configuration

You can add cardinality rules to your `pb_project.yaml` under the `id_types` section, as shown:
    
    
    entities:
      - name: user
        id_stitcher: models/customer_id_graph
        id_types:
          - user_id
          - email
          - anonymous_id
    
    id_types:
      - name: user_id
        maximum_edges:
          - email: 2
          - anonymous_id: 1
      - name: email
        maximum_edges:
          - user_id: 1
      - name: anonymous_id
        maximum_edges:
          - email: 1
          - user_id: 1
    

### Configuration limits

The following limits ensure optimal performance for incremental runs:

  * **Maximum edges per rule** : 10 (The `maximum_edges` value for each rule cannot exceed 10)
  * **Maximum target types per source** : 5 (The `maximum_edges` list for each source ID type cannot have more than 5 entries)


> ![info](/docs/images/info.svg)
> 
> The above limits only apply when using cardinality rules. Without these rules, the regular ID stitcher can connect unlimited edges, as usual.

### Examples

This section provides examples of how to configure cardinality rules for different use cases:
    
    
    id_types:
      - name: user_id
        maximum_edges:
          - email: 2          # Users can have up to 2 emails
          - device_id: 5       # Users can have up to 5 devices
      - name: email
        maximum_edges:
          - user_id: 1         # Each email belongs to only 1 user
      - name: device_id
        maximum_edges:
          - user_id: 2         # Shared devices (family tablets)
    
    
    
    id_types:
      - name: anonymous_id
        maximum_edges:
          - email: 1           # Anonymous sessions link to 1 email
      - name: email
        maximum_edges:
          - user_id: 1         # Emails don't get shared between users
    

## How rule application works

This section explains how cardinality rules are applied to your identity graph.

### Fresh and incremental runs

Cardinality rules behave differently depending on whether you’re running a fresh or incremental run:

  * **Fresh runs** : Rules are applied to all incoming data. If a node stays within its limits, all edges are preserved.
  * **Incremental runs** : Rules consider historical violations. If a node previously violated a rule or if new data causes a violation, all edges from that source are removed, including previously valid ones.


#### Fresh run
    
    
    # Input data
    user_1 → email_a
    user_1 → email_b  # Valid: within limit of 2
    
    # Result: Both edges allowed
    

#### Incremental run
    
    
    # Previous run: user_1 had 2 emails (at limit)
    # New data: 
    user_1 → email_c  # This causes violation
    
    # Result: ALL edges from user_1 are broken (including previous ones)
    

### Example

Given these rules:
    
    
    id_types:
      - name: user_id
        maximum_edges:
          - email: 2
      - name: email  
        maximum_edges:
          - user_id: 1
    

And the following data:
    
    
    user_1 ↔ email@example.com
    user_2 ↔ email@example.com  
    user_3 ↔ email@example.com
    

**What happens**

  1. `email@example.com` connects to 3 user_ids, violating the `email → user_id: 1` rule
  2. **All three connections** are broken, not just the excess ones.
  3. All nodes are preserved as isolated stubs.
  4. Three audit entries are created documenting the violation.


## Monitoring and debugging

This section explains how to monitor and debug cardinality rules.

### Cardinality Audit table

Each violation is logged in the cardinality audit table, which resides in the same schema as the ID Stitcher output tables. The table name is derived by appending the suffix `_CARDINALITY_AUDIT` to the name of the ID Stitcher model and contains the following columns:

Column| Description  
---|---  
`run_id`| ID of the run when the violation occurred  
`model_hash`| Hash of the model configuration  
`id1`| Source ID value  
`id1_type`| Source ID type  
`id2`| Target ID value  
`id2_type`| Target ID type  
`reason`| Always `"CARDINALITY_VIOLATION"`  
`rule_details`| JSON with `max_edges` and `current_count`  
  
## Best practices

This section provides best practices for configuring the cardinality rules correctly in your Profiles project.

#### 1\. Start conservatively

Begin with lower limits and gradually increase based on your data patterns:
    
    
    # Start here
    id_types:
      - name: email
        maximum_edges:
          - user_id: 1
    
    # Adjust based on audit results
    id_types:
      - name: email
        maximum_edges: 
          - user_id: 2  # If you see legitimate shared emails
    

#### 2\. Monitor audit tables

Make sure to review the Cardinality Audit table regularly to understand:

  * Which rules are triggering most often
  * Whether legitimate connections are being blocked
  * If limits need adjustment


#### 3\. Test with historical data

Before deploying rules to production:

  * Run rules against historical data in a test environment.
  * Analyze the audit results.
  * Adjust limits based on findings.


#### 4\. Consider bidirectional rules

Make sure to consider both directions of a relationship:
    
    
    # Often you want both directions
    id_types:
      - name: user_id
        maximum_edges:
          - email: 2        # Users can have multiple emails
      - name: email
        maximum_edges:
          - user_id: 1      # But emails belong to one user
    

## Troubleshooting

Issue| Solution  
---|---  
Legitimate connections being blocked| Review audit table and increase limits if needed.  
Identity graph still too connected| Add more restrictive rules or lower existing limits.  
  
### Debugging

  * **Check rule configuration** in `pb_project.yaml`.
  * **Query audit table** to see what is blocked.
  * **Review stub metadata** in the final ID graph.
  * Compare **fresh vs. incremental** run results.


## Migration guide

This section provides tips on managing cardinality rules in your Profiles models.

### Enable rules on existing models

  1. **Add rules gradually** : Start with one rule and observe effects
  2. **Test in development** : Use a copy of production data to validate
  3. **Monitor after deployment** : Watch audit tables and graph metrics
  4. **Adjust as needed** : Fine-tune limits based on real-world results


### Disable rules

To stop enforcing a rule, simply remove it from your configuration:
    
    
    # Before
    id_types:
      - name: email
        maximum_edges:
          - user_id: 1
    
    # After (rule removed)
    id_types:
      - name: email
        # maximum_edges section removed
    

> ![info](/docs/images/info.svg)
> 
> This triggers a complete fresh run of the model. Historical violations are no longer enforced, but previous audit records remain for reference.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.24/dev-docs/advanced-id-stitcher-features/id-graph-rules/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.24/dev-docs/run-project/>)