# How to Use CheckpointsBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# How to Use Checkpoints Beta

Learn how to reference and use checkpoints in incremental features and SQL models.

* * *

  * __4 minute read

  * 


This guide explains how to reference and use checkpoints when building incremental features and SQL models.

## Overview

Checkpoints represent point-in-time snapshots of warehouse data and their computed outputs from previous runs, enabling incremental computation. How you reference checkpoints depends on whether you’re using incremental entity vars or incremental SQL models.

See [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>) for conceptual information.

## Usage with incremental entity vars

When using a `merge:` clause in an incremental entity var, Profiles uses the checkpoint implicitly. You don’t need to explicitly reference the checkpoint.

### Example
    
    
    - entity_var:
        name: total_purchases
        select: SUM({{orders.value}})
        merge: SUM({{rowset.total_purchases}})
        from: inputs/orders
    

### How it works

The `{{rowset.total_purchases}}` reference automatically pulls the value from the baseline checkpoint. Profiles:

  * Retrieves the previously computed value from the baseline checkpoint
  * Computes the delta (new rows since the baseline)
  * Merges them using the `merge` property


The `{{rowset.}}` syntax refers to the changed rowset from the baseline checkpoint, giving you access to previous checkpoint values during the merge operation.

## Usage with incremental SQL models

When building an incremental SQL model, you must reference the previous checkpoint **explicitly** using `this.DeRef()` with `pre_existing=true`.

#### Reference past version of current model

To reference the previous materialization of the current model:
    
    
    {%- set lastThis = this.DeRef(
          pre_existing=true,
          dependency="optional",
          checkpoint_name="baseline") -%}
    
    {# All DeRef before this line. Note that DeRef should not be put in conditionals. DeRef mark dependencies — use prereqs for conditional dependencies #}
    
    {% if lastThis.IsEnabled() %}
        -- Incremental mode: merge with baseline
        SELECT * FROM {{ lastThis }}
        UNION ALL
        SELECT * FROM {{ events_delta }}
    {% else %}
        -- Full refresh mode: process all data
        SELECT * FROM {{ this.DeRef("inputs/events") }}
    {% endif %}
    

#### Reference another model’s previous materialization

To reference another model’s previous materialization:
    
    
    {%- set previousModel = this.DeRef("models/previous_model", 
                                       pre_existing=true,
                                       dependency="optional") -%}
    

### Key points

  * Use `pre_existing=true` to reference previous materializations. This indicates that the referenced material will NOT be created in the current run. If it doesn’t exist, it will be disabled. In SQL templates, you can check if the material is enabled using `<material>.IsEnabled()`.
  * Use `dependency="optional"` to handle cases where no baseline exists
  * Always check if `<reference>.IsEnabled()` is true/false to support full refresh mode (when baseline doesn’t exist, `IsEnabled()` returns false)
  * Use `checkpoint_name` to specify which baseline to use (defaults to `"baseline"`)


See [DeRef Reference](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/deref-reference/>) for complete syntax and usage.

## Delta models

Profiles automatically creates delta models for append-only inputs at the path `/path/to/input/incr_delta_tbl`. These models contain only rows that arrived after the baseline checkpoint timestamp.

### Reference delta models

Reference delta models in your incremental SQL templates:
    
    
    {%- set lastThis = this.DeRef(
          pre_existing=true,
          dependency="optional",
          checkpoint_name="baseline") -%}
    
    {% set events_delta = this.DeRef("inputs/events/incr_delta_tbl",
                                      dependency="coercive",
                                      baseline_name="baseline",
                                      prereqs=[lastThis]) %}
    
    {% set events_full = this.DeRef("inputs/events",
                                     prereqs=[events_delta.Except()]) %}
    
    {# All DeRef before this line. Note that DeRef should not be put in conditionals. DeRef mark dependencies — use prereqs for conditional dependencies #}
    
    {% if lastThis.IsEnabled() %}
        -- Incremental mode: use delta
        SELECT * FROM {{ events_delta }}
    {% else %}
        -- Full refresh mode: use full input
        SELECT * FROM {{ events_full }}
    {% endif %}
    

### How delta models work

  * Delta models contain only rows that arrived after the baseline checkpoint timestamp
  * They’re automatically enabled when a baseline exists, disabled otherwise
  * Use `prereqs=[lastThis]` to ensure the delta model is created only when a baseline exists
  * Use `baseline_name` to specify which baseline to use for delta computation (must match `checkpoint_name`)


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Always declare all DeRefs together at the top of your template, not inside conditionals. Use `prereqs` to chain conditional evaluation instead.

## Checkpoint management

Profiles automatically creates checkpoints after each successful run. Each checkpoint is identified by a sequence number and associated with specific time boundaries. Model output tables reference their checkpoint through their materialized table names (e.g., `Material_<modelname>_<modelhash>_<checkpoint_seqno>`).

## Troubleshooting

Issue| Solution  
---|---  
No baseline checkpoint available| Profiles automatically performs a full refresh to create the baseline. Ensure regular runs to maintain baseline availability.  
Baseline checkpoint incompatible| When new entity vars are added or existing definitions change, Profiles automatically discovers the model hash change and runs a full refresh.  
Checkpoints are too old| Profiles can use older checkpoints, but performance may degrade. Maintain regular run schedules.  
Materials consume excessive storage| Profiles automatically cleans up old materials based on your model retention periods. Review retention settings to adjust cleanup behavior.  
`pre_existing=true` returns `nil`| This is expected on first run or when no baseline exists. Always handle this case with conditional logic for full refresh mode.  
Delta model not available| Ensure your input has `contract: is_append_only: true` configured. Delta models are only created for append-only inputs.  
  
## See more

  * [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>): Conceptual overview
  * [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)
  * [DeRef Reference](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/deref-reference/>)
  * [How to Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>)


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/incremental-features/migrate-project-to-incremental/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/optimizations/>)