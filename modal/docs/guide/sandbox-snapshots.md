# Snapshots
Sandboxes support snapshotting, allowing you to save your Sandbox’s state
and restore it later. This is useful for: Reducing startup latency
- Creating custom environments for your Sandboxes to run in
- Backing up your Sandbox’s state for debugging
- Running large-scale experiments with the same initial state
- Branching your Sandbox’s state to test different code changes independently

Modal currently supports three different kinds of Sandbox snapshots:
- [Filesystem Snapshots](#filesystem-snapshots)
- [Directory Snapshots (Beta)](#directory-snapshots-beta)
- [Memory Snapshots (Alpha)](#memory-snapshots-alpha)

## Filesystem Snapshots

Filesystem Snapshots are copies of the Sandbox’s filesystem at a given point in time.
These Snapshots are [Images](https://modal.com/docs/reference/modal.Image) and can be used to create
new Sandboxes.

To create a Filesystem Snapshot, you can use the [Sandbox.snapshot_filesystem()](https://modal.com/docs/reference/modal.Sandbox#snapshot_filesystem) method:

Filesystem Snapshots are optimized for performance: they are calculated as the difference
from your base image, so only modified files are stored. Restoring a Filesystem Snapshot
utilizes the same infrastructure we use to get fast cold starts for your Sandboxes.

Filesystem Snapshots will generally persist indefinitely.

## Directory Snapshots (Beta)

Directory Snapshots allow you to snapshot a specific directory within a running Sandbox. The resulting snapshot is an Image that can then be mounted into another already-running Sandbox (typically at a later time), which can be useful for:
- Updating system dependencies separately from application code**: Base dependencies can be updated by starting a new Sandbox from an updated base Image, and then mounting in previously snapshotted application code.
- **Using warm pools in combination with snapshots**: For use cases that benefit from a [warm pool](https://modal.com/docs/examples/sandbox_pool) of Sandboxes to reduce start-up latency, the first initialization can now happen in the warm pool without losing the ability to restore application-specific code at a later point in time.
- **Speeding up resumptions of previous sessions**: Files in mounted Images are prioritized when containers load files, so mounting a directory can speed up Sandbox resumptions vs. starting from a full file system image.

### Usage

Use `snapshot_directory` to snapshot a directory and `mount_image` to mount a previous directory snapshot at a directory path.

### Persistence

Directory snapshots are currently persisted for 30 days after they were last created or used. If you try to use an expired snapshot, Modal will raise a `NotFoundError`, letting you handle the case gracefully.

## Memory Snapshots (Alpha)

Alpha This feature is currently in Alpha and has a number of known [limitations](#limitations). See [feature maturity](https://modal.com/docs/guide/feature-maturity) for more details.

Sandbox memory snapshots are copies of a Sandbox’s entire state, both in memory and on the filesystem. These Snapshots can be restored later to create a new Sandbox, which is an exact clone of the original Sandbox.

To snapshot a Sandbox, create it with `_experimental_enable_snapshot` set to `True`, and use the `_experimental_snapshot` method, which returns a `SandboxSnapshot` object:

Create a new Sandbox from the returned SandboxSnapshot with `Sandbox._experimental_from_snapshot`:

The new Sandbox will be a duplicate of your original Sandbox. All running processes will still be running, in the same state as when they were snapshotted, and any changes made to the filesystem will be visible.

You can retrieve the ID of any Sandbox Snapshot with `snapshot.object_id` . To restore from a snapshot by ID, first rehydrate the Snapshot with `SandboxSnapshot.from_id` and then restore from it:

Note that these methods are *experimental*, and we may change them in the future.

### Re-snapshotting

Modal supports creating a new snapshot from a restored Sandbox snapshot. To maintain the snapshot’s expiration window, the new snapshot inherits the expiration of its parent.

Continuing from the example code above, we demonstrate re-snapshotting:

### Limitations
- Sandbox Memory Snapshots will expire 7 days after creation. For longer persisting snapshots, try [Filesystem Snapshots](https://modal.com/docs/guide/sandbox-snapshots).
- Open TCP connections will be closed automatically when a Snapshot is taken, and will need to be reopened when the Snapshot is restored.
- Snapshotting a sandbox will currently cause it to terminate. We intend to remove this limitation soon.
- Sandboxes created with `_experimental_enable_snapshot=True` or restored from Snapshots cannot run with GPUs.
- It is not possible to snapshot a sandbox while a `Sandbox.exec` command is still running. Furthermore, any background processes launched by a call to `Sandbox.exec` will not be properly restored after a snapshot.
- Sandbox memory snapshots can only be restored on the same exact instance type that the original Sandbox was run on. Given Modal’s diverse fleet of capacity, this can sometimes lead to scheduling delays, especially when memory snapshots are combined with narrow region pinning.

## Persisting Sandbox State

To persist state across Sandbox sessions, you need to:
- **Trigger the snapshot.** Snapshots are triggered from outside the Sandbox, typically just before termination. A common pattern is to run an exec process inside the Sandbox and wait for it to exit. Once it does, the controller takes a snapshot and terminates the Sandbox.
- **Store the snapshot ID.** The `object_id` string must be persisted so you can restore from it later. This is typically keyed by a session or user ID, and can be stored in your database, an external key-value store, or a [Modal Dict](https://modal.com/docs/guide/dicts).

The following example shows this pattern. This code would typically run in a Modal Function or your own backend, orchestrating the Sandbox:
