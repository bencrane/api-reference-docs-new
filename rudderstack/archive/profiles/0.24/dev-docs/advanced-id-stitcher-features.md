# Advanced ID Stitcher Features

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Advanced ID Stitcher Features

Advanced features for fine-grained control over identity stitching, including inclusion/exclusion rules and cardinality limits.

* * *

  * __2 minute read

  * 


The Profiles ID Stitcher provides advanced features that give you fine-grained control over how identities are connected in your graph, helping you maintain data quality, prevent identity explosion, and enforce business rules about identity relationships.

## Available features

This section describes the advanced features available in the Profiles ID Stitcher.

### Inclusion/exclusion rules

You can define specific rules to control which nodes and edges are included in your ID graph using a warehouse table. These rules provide the highest precedence over any other filtering mechanisms.

**Key capabilities**

  * Exclude or include specific identifiers (node control)
  * Define specific connections between identifiers (edge control)
  * Manage rules through CLI tools
  * Handle conflicting rules with configurable priority settings


See [ID Graph Inclusion/Exclusion Rules](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/advanced-id-stitcher-features/id-graph-rules/>) for more details.

### Cardinality rules

Set maximum connection limits between different ID types to prevent over-connected identity graphs and maintain data quality.

**Key capabilities**

  * Define directional limits (for example, each email connects to at most 1 `user_id`)
  * Prevent identity explosion from shared identifiers
  * Maintain audit trail of violations
  * Support incremental runs with consistent behavior
  * Optimize performance through controlled graph size


See [ID Graph Cardinality Rules](<https://www.rudderstack.com/docs/archive/profiles/0.24/dev-docs/advanced-id-stitcher-features/id-graph-cardinality-rules/>) for more details.

## How these features work together

Both features integrate seamlessly with your Profiles pipeline:

  * **Input filters** reduce data volume before graph processing.
  * **Cardinality rules** enforce connection limits during graph building.
  * **Inclusion/exclusion rules** provide final control over specific nodes and edges.


This layered approach ensures you have comprehensive control over your identity graph while maintaining optimal performance and data quality.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.24/dev-docs/optimizations/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.24/dev-docs/advanced-id-stitcher-features/id-graph-rules/>)