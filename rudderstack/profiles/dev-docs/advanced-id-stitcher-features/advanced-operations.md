# Advanced ID Stitcher Operations

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Advanced ID Stitcher Operations

Learn about advanced operations available in the Profiles ID Stitcher, including the rebase incremental mode.

* * *

  * __2 minute read

  * 


This guide explains advanced operations available in the Profiles ID Stitcher, including the rebase incremental mode and how ID determinism ensures stable user identifiers across runs.

## The `rebase_incremental` flag

While the ID Stitcher typically runs in [Incremental Mode](<https://www.rudderstack.com/docs/profiles/concepts/incremental-features/>) (processing only the data that arrived since the start of the last run and merging it with previous run’s graph), you can use a powerful reset mechanism called `rebase_incremental`.

> ![info](/docs/images/info.svg)
> 
> This flag is currently only available in the CLI.

### How it works

When you set this flag to `true`, the pipeline changes behavior in three critical ways:

  * **Ignores history** : It does not load the previous mapping table (the graph state from the previous run).
  * **Full ingestion** : It removes the timestamp filters on the input tables, reading the **entire history** of edges from the beginning of time.
  * **Fresh calculation** : It rebuilds every cluster and recalculates every user ID from scratch using the current logic.


### Use cases

  * **Applying new rules retroactively** : If you update your blocklist (for example, adding a new spam IP), a standard incremental run only blocks future edges. A rebase applies this block to the entire history, splitting any clusters that were incorrectly merged by that IP in the past.
  * **Graph reset** : If the graph has become too “messy” (too many older, irrelevant edges), a rebase allows you to clean up the state based on current data retention policies.


## Why IDs are deterministic

A common concern with re-running a graph algorithm is that IDs might shuffle (for example, user `ABC` becomes user `XYZ`). The ID Stitcher logic prevents this.

**Logic used**

The user ID is not a random number — it is mathematically derived from the **anchor node** of the cluster.

  * **Anchor node** : The node with the earliest `occurred_at_col` timestamp in the cluster.
  * **Formula used** :


`ID = ID_GEN_OPERATOR(ANCHOR_NODE_VALUE + ANCHOR_NODE_TYPE)`

### Why IDs persist during incremental runs

The system carries forward the `rudder_main_id` from the previous run via the previous mapping table. New nodes simply adopt the existing ID of the cluster they join.

### Why IDs persist during rebase or fresh runs

Even if you delete the previous mapping table, the anchor node for a specific user (for example, the first cookie they used in 2021) effectively remains the same in the raw data.

  1. The algorithm re-groups the cluster.
  2. It identifies the node with the minimum timestamp (the same 2021 cookie).
  3. It hashes that value.


**Result** : The generated ID comes out identical to the previous run.

  


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/advanced-id-stitcher-features/id-graph-cardinality-rules/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/run-project/>)