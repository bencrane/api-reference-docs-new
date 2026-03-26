# DeRef ReferenceBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# DeRef Reference Beta

Complete reference for this.DeRef() syntax and usage in incremental SQL models.

* * *

  * __4 minute read

  * 


This reference provides complete syntax and usage information for `this.DeRef()` in incremental SQL models.

## Overview

`this.DeRef()` references other models, creates dependency relationships, and enables incremental processing by referencing previous materializations.

## Parameter reference

Parameter| Type| Description  
---|---|---  
`dependency`| String| Specifies the dependency type:  


  * `"normal"`: Mandatory
  * `"optional"`: Use if exists
  * `"coercive"`: Prefer to create

  
**Default** : `"normal"`  
`pre_existing`| Boolean| When `true`, references a previous materialization of the model (typically the current model itself for incremental processing). Should be used with `dependency="optional"` and `checkpoint_name` to specify the baseline context.  
**Default** : `false`  
`prereqs`| Array| Prerequisites that must be met before referencing. Use `.Except()` for negative prerequisites  
  
**Default** : `[]`  
`baseline_name`| String| Baseline context name for incremental processing (must match `checkpoint_name`). Used when referencing delta models to specify which baseline checkpoint to use for delta computation.  
  
**Default** : `""`  
`checkpoint_name`| String| Checkpoint name for context management. When using `pre_existing=true`, this names the checkpoint context for referencing previous materializations.  
  
**Default** : `""`  
`time_grain_spec`| String| Time grain: `"hourly"`, `"daily"`, `"weekly"`, `"monthly"`, `"yearly"`  
  
**Default** : `""`  
`skip_dependency`| Boolean| Skip dependency registration  
**Default** : `false`  
`contract`| Contract object| Contract specification for model validation  
  
**Default** : `null`  
  
### Returned object methods

The object returned by `this.DeRef()` provides these methods:

Method| Description  
---|---  
`.IsEnabled()`| Returns `true` if the model is enabled and available. Returns `false` if `IsNil()` is `true` or if enablement status is not `enabled=true`. Prefer using `.IsEnabled()` in conditions to check if a model is available.  
`.IsNil()`| Returns `true` if the checkpoint itself wasn’t found. This is a structural check for missing checkpoints and is rarely used.  
`.Except()`| Creates a negative prerequisite. Use in `prereqs` to proceed only when the model does not exist.  
  
## Usage

This section explains some common usage patterns for `this.DeRef()`.

### Basic model reference
    
    
    {% with users = this.DeRef("inputs/users") %}
        SELECT * FROM {{ users }}
    {% endwith %}
    

### Optional dependency

Use `dependency="optional"` when the model may not exist. You can check if the model is enabled using `.IsEnabled()` method:
    
    
    {% with optional_model = this.DeRef("models/optional_feature", dependency="optional") %}
      {% if optional_model.IsEnabled() %}
        SELECT * FROM {{ optional_model }}
      {% else %}
        SELECT 'Feature not available' as status
      {% endif %}
    {% endwith %}
    

### Reference with contract
    
    
    {% set contract = BuildContract('{"is_event_stream": false, "with_columns":[{"name":"user_id"}]}') %}
    {% with events = this.DeRef("inputs/events", contract=contract) %}
        SELECT user_id, COUNT(*) as event_count
        FROM {{ events }}
        GROUP BY user_id
    {% endwith %}
    

### Incremental SQL model pattern

The standard pattern for incremental SQL models is shown:
    
    
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
    
    {% if lastThis %}
        -- Incremental mode: merge with baseline
        SELECT * FROM {{ lastThis }}
        UNION ALL
        SELECT * FROM {{ events_delta }}
    {% else %}
        -- Full refresh mode: process all data
        SELECT * FROM {{ events_full }}
    {% endif %}
    

**How it works**

  1. **lastThis** : References the previous materialization using `pre_existing=true`. Returns `nil` if no baseline exists.
  2. **events_delta** : Delta table (new data since baseline). Only enabled when `lastThis` exists (via `prereqs=[lastThis]`). Uses `baseline_name` to specify which baseline checkpoint to compare against.
  3. **events_full** : Full input table. Only enabled when `events_delta` does NOT exist (via `prereqs=[events_delta.Except()]`).
  4. **Conditional logic** : If `lastThis` exists, merge with delta; otherwise, process full data.


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Always declare all `this.DeRef()` calls together at the top of your template, not inside conditionals. Use `prereqs` to chain conditional evaluation instead.

### Prerequisites for conditional dependencies
    
    
    -- Ensure specific models exist before referencing
    {{ this.DeRef("models/target", prereqs=[model1, model2]) }}
    
    -- Negative prerequisite - only proceed if specified model does NOT exist
    {% set deltaInputVarTable = this.DeRef("inputs/events/incr_delta_tbl/var_table", dependency="optional") %}
    {{ this.DeRef("inputs/events/var_table", prereqs=[deltaInputVarTable.Except()]) }}
    

For `is_append_only` input models, Profiles automatically creates delta models at `/path/to/input/incr_delta_tbl`. Prerequisites determine the SQL generation strategy based on the availability of these incremental artifacts.

## See more

  * [Incremental SQL Models](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/incremental-sql-models/>): Overview of incremental SQL models
  * [Checkpoints and Baselines](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/checkpoints-and-baselines/>): Understand checkpoints and baselines
  * [How to Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>): Step-by-step guide to convert features to incremental


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/incremental-features/incremental-sql-models/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/incremental-features/make-features-incremental/>)