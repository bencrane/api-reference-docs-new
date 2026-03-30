# Validation Report — agent-3-findings vs llm-full-extraction

> **Date:** 2026-03-29
> **Scope:** Factual errors only. Stylistic, organizational, and missing-content differences are excluded per directive.

---

### [ERROR-001] TRIGGER_DEV_QUEUES_CONCURRENCY.md — Priority semantics incorrectly described as simple ranking

**agent-3-findings says:**

> Higher-priority runs are picked up before lower-priority ones when a concurrency slot becomes available.
>
> ```ts
> // Higher priority number = picked up sooner
> await myTask.trigger(
>   { orderId: "rush-123" },
>   { priority: 100 }
> );
> ```
>
> — `TRIGGER_DEV_QUEUES_CONCURRENCY.md`, lines 473–484

> Priority: "higher = picked up sooner, FIFO within same priority" (not "seconds offset")
>
> — `README.md`, line 38

> - When a concurrency slot opens, the highest-priority queued run in that queue is dequeued next.
> - Runs with the same priority are dequeued in FIFO order.
> - Priority does not preempt executing runs — it only affects the order of queued runs.
>
> — `TRIGGER_DEV_QUEUES_CONCURRENCY.md`, lines 495–497

**llm-full-extraction says:**

> The value for priority is a time offset in seconds that determines the order of dequeuing.
>
> If you specify a priority of `10` the run will dequeue before runs that were triggered with no priority 8 seconds ago, like in this example:
>
> ```ts
> // no priority = 0
> await myTask.trigger({ foo: "bar" });
>
> //... imagine 8s pass by
>
> // this run will start before the run above that was triggered 8s ago (with no priority)
> await myTask.trigger({ foo: "bar" }, { priority: 10 });
> ```
>
> If you passed a value of `3600` the run would dequeue before runs that were triggered an hour ago (with no priority).
>
> — `METADATA_TAGS.md`, lines 861–877

**Correction needed:**

The priority section in `TRIGGER_DEV_QUEUES_CONCURRENCY.md` (lines 468–497) must be rewritten to describe priority as **a time offset in seconds** that shifts a run's effective queue position, not a simple numeric ranking. The README.md "verified correction" on line 38 that says `(not "seconds offset")` is itself incorrect and should be reversed — the source confirms priority IS a seconds offset. The code example should use realistic offset values (e.g., `10`, `3600`) and explain the time-offset semantics with the queuing example from the source.

---

### [VERIFIED] Machine presets — all values match source

`agent-3-findings/TRIGGER_DEV_TASKS.md` lists: `micro` (0.25 vCPU / 0.25 GB), `small-1x` (0.5 / 0.5), `small-2x` (1 / 1), `medium-1x` (1 / 2), `medium-2x` (2 / 4), `large-1x` (4 / 8), `large-2x` (8 / 16), all with 10 GB disk. These match `llm-full-extraction/MACHINES.md` lines 37–45 exactly.

### [VERIFIED] Limits — concurrency, tags, payloads, schedules, queue depths all match source

Queue depth limits (Free: 500 dev / 10,000 prod; Hobby: 500 / 250,000; Pro: 5,000 / 1,000,000), tags (max 10 per run, each < 128 chars), and payload sizes all match `llm-full-extraction/LIMITS.md`.

### [VERIFIED] `catchError` vs `handleError` — naming and return shapes match source

Both sources agree `handleError` was renamed to `catchError`. Return shapes (`undefined`, `{ skipRetrying: true }`, `{ retryAt: Date }`) match `llm-full-extraction/ERRORS_RETRIES.md` lines 220–296.

### [VERIFIED] Trigger signatures — 3 positional args match source

`tasks.trigger(taskId, payload, options?)` matches `llm-full-extraction/TRIGGERING.md` lines 66–99.

### [VERIFIED] Import paths — `@trigger.dev/sdk` matches source

All imports use `@trigger.dev/sdk`. `defineConfig` imports from `@trigger.dev/sdk`. Matches source throughout.

### [VERIFIED] `triggerAndWait` return type — Result wrapper, `.ok`, `.unwrap()` match source

`.ok` check and `.unwrap()` shorthand both confirmed in `llm-full-extraction/raw/llms-full.txt` lines 191–192 and `GUIDES_AI_AGENTS.md` line 762.

### [VERIFIED] Version locking — method-to-locking table matches source

`trigger()` / `batchTrigger()` = not locked; `triggerAndWait()` / `batchTriggerAndWait()` = locked to parent version. Matches `llm-full-extraction/VERSIONING.md` lines 28–43.

### [VERIFIED] Queue slot semantics — EXECUTING consumes, WAITING does not, matches source

Both sources agree only actively executing runs consume concurrency slots. Waiting/checkpointed runs release their slot. Matches `llm-full-extraction/QUEUES_CONCURRENCY.md` line 16.

### [VERIFIED] Wait checkpointing — ~5 second threshold matches source

Both sources state waits longer than 5 seconds trigger checkpointing. Matches `llm-full-extraction/WAITS_TOKENS.md` line 18.

### [VERIFIED] Retry defaults — `maxAttempts: 3`, `factor: 2`, timeouts match source

Defaults (`maxAttempts: 3`, `minTimeoutInMs: 1000`, `maxTimeoutInMs: 10000`, `factor: 2`, `randomize: true`, `enabledInDev: false`) match `llm-full-extraction/raw/llms-full.txt` lines 1264–1274.

### [VERIFIED] Batch limits — 1,000 vs 500 at SDK 4.3.1 matches source

Both sources agree: 1,000 items per batch with SDK >= 4.3.1, 500 with older versions. Matches `llm-full-extraction/LIMITS.md` lines 106–108.

### [VERIFIED] OOM retry — `retry.outOfMemory` option shape matches source

`retry: { outOfMemory: { machine: "large-1x" } }` matches `llm-full-extraction/MACHINES.md` lines 939–947.

### [VERIFIED] Metadata API — `metadata.stream()` deprecation, `metadata.parent.set()` existence match source

`metadata.stream()` deprecated as of SDK 4.1.0, `metadata.parent.set()` confirmed, `metadata.flush()` confirmed. All match `llm-full-extraction/METADATA_TAGS.md` lines 272–277, 417–458, 386–391.

### [VERIFIED] Streams v2 — `streams.define()`, `streams.pipe()` match source

Both `streams.define()` signatures (generic type with object arg, and positional with schema) and `streams.pipe()` usage match `llm-full-extraction/STREAMS.md` lines 63–117 and `raw/llms-full.txt` line 7947.

---

## Summary

- **Total errors found:** 1
- **Critical (would cause build/runtime failure):** 0
- **Behavioral (would cause developers to misunderstand API semantics):** 1
- **All high-risk areas verified:**
  1. Machine presets
  2. Limits
  3. `catchError` vs `handleError`
  4. Trigger signatures
  5. Import paths
  6. `triggerAndWait` return type
  7. Version locking
  8. Queue slot semantics
  9. Wait checkpointing
  10. Retry defaults
  11. Batch limits
  12. OOM retry
  13. Metadata API
  14. Streams v2
