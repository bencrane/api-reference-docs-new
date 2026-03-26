# Checkpoints and BaselinesBeta

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Checkpoints and Baselines Beta

Learn about checkpoints and baselines and how they enable incremental feature computation.

* * *

  * __3 minute read

  * 


This guide explains checkpoints and baselines and how they enable incremental feature computation.

## Overview

Checkpoints represent point-in-time snapshots of all Profiles inputs and their computed outputs. Each checkpoint is identified by a sequence number and references a specific time boundary. When running incrementally, Profiles builds models using:

  * **Stored computation** from a baseline checkpoint (a previous successful run)
  * **New warehouse data** that arrived after the baseline checkpoint’s timestamp


The baseline checkpoint provides the reference point for identifying what data has changed and what computations can be reused.

## What are checkpoints?

A **checkpoint** is a conceptual snapshot of all Profiles inputs data that landed before a specific timestamp, along with all computed outputs generated from that data. Profiles uses checkpoints to:

  * Reference a specific point-in-time state of your warehouse data
  * Identify new data that has arrived since the last checkpoint
  * Enable incremental computation by reusing previous results


Each checkpoint is identified by a unique sequence number (seqno). Every model output table is associated with a checkpoint and follows the naming pattern `Material_<modelname>_<modelhash>_<checkpoint_seqno>`.

### Current checkpoint

The **current checkpoint** is the checkpoint being produced during the current run.

### Baseline checkpoint

The **baseline checkpoint** is a previous checkpoint used as a reference point for incremental computation. In incremental runs, each model selects a named baseline to use. Once a baseline corresponding to a particular (checkpoint seqno, baseline name) pair is chosen, it remains fixed for that and all subsequent runs.

When Profiles runs incrementally, it:

  1. Selects a baseline checkpoint for each incrementally-run model
  2. Loads computed values from the baseline checkpoint’s model output tables
  3. Identifies new data that has arrived since the baseline
  4. Merges baseline values with new calculations
  5. Produces the current checkpoint


## How checkpoints work

This section explains how checkpoints and baselines work in Profiles.

### Checkpoint creation

Profiles automatically creates checkpoints after each successful run:

  1. **Checkpoint assignment** : A new sequence number (seqno) is assigned to represent this checkpoint
  2. **During run** : Profiles computes feature values from your warehouse data up to the checkpoint’s end timestamp
  3. **After computation** : Model output tables are materialized with names containing the checkpoint seqno (e.g., `Material_user_features_a1b2c3_42`)
  4. **Checkpoint registration** : The checkpoint seqno, along with its time boundaries and baseline references, is recorded in the registry
  5. **Next run** : The checkpoint becomes available as a baseline for subsequent incremental runs


### Baseline selection

When running incrementally, each model independently:

  1. Identifies available baselines (previous checkpoints with matching time boundaries)
  2. Selects an appropriate checkpoint as the baseline for the named baseline context
  3. Once selected, the baseline (checkpoint seqno, baseline name) pair remains fixed and is never changed
  4. Delta models and incremental models then compute changes since the baseline
  5. New calculations are merged with baseline values to produce the current checkpoint output


## Incremental vs full refresh

This section explains the difference between incremental and full refresh modes in Profiles.

### Incremental mode

When a baseline checkpoint is available, each incremental model:

  * References the baseline checkpoint’s model output table (e.g., `Material_user_features_a1b2c3_38` for baseline seqno 38)
  * Processes only new warehouse data that has arrived since the baseline checkpoint’s end timestamp
  * Merges baseline values with new calculations using your merge logic
  * Produces updated feature values in a new output table for the current checkpoint (e.g., `Material_user_features_a1b2c3_42` for current seqno 42)


### Full refresh mode

When no baseline checkpoint is available, Profiles:

  * Processes all data from scratch
  * Computes all feature values from the beginning
  * Creates a new checkpoint for future incremental runs


> ![info](/docs/images/info.svg)
> 
> The first run of an incremental feature always performs a full refresh to establish the baseline checkpoint. Subsequent runs use incremental computation.

## See more

  * [How to Use Checkpoints](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/use-checkpoints/>): Implementation guide for referencing checkpoints
  * [Incremental Features Overview](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/>)
  * [Make Features Incremental](<https://www.rudderstack.com/docs/profiles/dev-docs/incremental-features/make-features-incremental/>)


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/concepts/incremental-features/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/concepts/incremental-features/incremental-sql-models/>)