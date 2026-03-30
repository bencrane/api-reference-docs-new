> Sources:
> - https://trigger.dev/docs/logging
> - https://trigger.dev/docs/observability/dashboards
> - https://trigger.dev/docs/observability/query

# Logging, Tracing & Metrics

## Logging, tracing & metrics

How to use the built-in logging, tracing, and metrics system.

<img alt="The run log" />

The run log shows you exactly what happened in every run of your tasks. It is comprised of logs, traces and spans.

## Logs

You can use `console.log()`, `console.error()`, etc as normal and they will be shown in your run log. This is the standard function so you can use it as you would in any other JavaScript or TypeScript code. Logs from any functions/packages will also be shown.

### logger

We recommend that you use our `logger` object which creates structured logs. Structured logs will make it easier for you to search the logs to quickly find runs.

```ts /trigger/logging.ts theme={"theme":"css-variables"}
import { task, logger } from "@trigger.dev/sdk";

export const loggingExample = task({
  id: "logging-example",
  run: async (payload: { data: Record<string, string> }) => {
    //the first parameter is the message, the second parameter must be a key-value object (Record<string, unknown>)
    logger.debug("Debug message", payload.data);
    logger.log("Log message", payload.data);
    logger.info("Info message", payload.data);
    logger.warn("You've been warned", payload.data);
    logger.error("Error message", payload.data);
  },
});
```

## Tracing and spans

Tracing is a way to follow the flow of your code. It's very useful for debugging and understanding how your code is working, especially with long-running or complex tasks.

Trigger.dev uses OpenTelemetry tracing under the hood. With automatic tracing for many things like task triggering, task attempts, HTTP requests, and more.

| Name          | Description                      |
| :------------ | :------------------------------- |
| Task triggers | Task triggers                    |
| Task attempts | Task attempts                    |
| HTTP requests | HTTP requests made by your code. |

### Adding instrumentations

<img alt="The run log" />

You can [add instrumentations](/config/config-file#instrumentations). The Prisma one above will automatically trace all Prisma queries.

### Add custom traces

If you want to add custom traces to your code, you can use the `logger.trace` function. It will create a new OTEL trace and you can set attributes on it.

```ts theme={"theme":"css-variables"}
import { logger, task } from "@trigger.dev/sdk";

export const customTrace = task({
  id: "custom-trace",
  run: async (payload) => {
    //you can wrap code in a trace, and set attributes
    const user = await logger.trace("fetch-user", async (span) => {
      span.setAttribute("user.id", "1");

      //...do stuff

      //you can return a value
      return {
        id: "1",
        name: "John Doe",
        fetchedAt: new Date(),
      };
    });

    const usersName = user.name;
  },
});
```

## Metrics

Trigger.dev collects system and runtime metrics automatically for deployed tasks, and provides an API for recording custom metrics using OpenTelemetry.

You can view metrics in the [Dashboards](/observability/dashboards), query them with [TRQL](/observability/query), and export them to external services via [telemetry exporters](/config/config-file#telemetry-exporters).

### Custom metrics API

Import `otel` from `@trigger.dev/sdk` and use the standard OpenTelemetry Metrics API to create custom instruments.

Create instruments **at module level** (outside the task `run` function) so they are reused across runs:

```ts /trigger/metrics.ts theme={"theme":"css-variables"}
import { task, logger, otel } from "@trigger.dev/sdk";

// Create a meter — instruments are created once at module level
const meter = otel.metrics.getMeter("my-app");

const itemsProcessed = meter.createCounter("items.processed", {
  description: "Total number of items processed",
  unit: "items",
});

const itemDuration = meter.createHistogram("item.duration", {
  description: "Time spent processing each item",
  unit: "ms",
});

const queueDepth = meter.createUpDownCounter("queue.depth", {
  description: "Current queue depth",
  unit: "items",
});

export const processQueue = task({
  id: "process-queue",
  run: async (payload: { items: string[] }) => {
    queueDepth.add(payload.items.length);

    for (const item of payload.items) {
      const start = performance.now();

      // ... process item ...

      const elapsed = performance.now() - start;

      itemsProcessed.add(1, { "item.type": "order" });
      itemDuration.record(elapsed, { "item.type": "order" });
      queueDepth.add(-1);
    }

    logger.info("Queue processed", { count: payload.items.length });
  },
});
```

#### Available instrument types

| Instrument    | Method                        | Use case                                                         |
| :------------ | :---------------------------- | :--------------------------------------------------------------- |
| Counter       | `meter.createCounter()`       | Monotonically increasing values (items processed, requests sent) |
| Histogram     | `meter.createHistogram()`     | Distributions of values (durations, sizes)                       |
| UpDownCounter | `meter.createUpDownCounter()` | Values that go up and down (queue depth, active connections)     |

All instruments accept optional attributes when recording values. Attributes let you break down metrics by dimension (e.g., by item type, status, or region).

### Automatic system and runtime metrics

Trigger.dev automatically collects the following metrics for deployed tasks. No configuration is needed. Requires SDK version **4.4.1 or later**.

| Metric name                     | Type    | Unit    | Description                  |
| :------------------------------ | :------ | :------ | :--------------------------- |
| `process.cpu.utilization`       | gauge   | ratio   | Process CPU usage (0-1)      |
| `process.cpu.time`              | counter | seconds | CPU time consumed            |
| `process.memory.usage`          | gauge   | bytes   | Process memory usage         |
| `nodejs.event_loop.utilization` | gauge   | ratio   | Event loop utilization (0-1) |
| `nodejs.event_loop.delay.p95`   | gauge   | seconds | Event loop delay p95         |
| `nodejs.event_loop.delay.max`   | gauge   | seconds | Event loop delay max         |
| `nodejs.heap.used`              | gauge   | bytes   | V8 heap used                 |
| `nodejs.heap.total`             | gauge   | bytes   | V8 heap total                |

<Note>
  In dev mode (`trigger dev`), only `process.*` and custom metrics are available.
</Note>

### Context attributes

All metrics (both automatic and custom) are tagged with run context so you can filter and group them:

* `run_id` — the run that produced the metric
* `task_identifier` — the task slug
* `attempt_number` — the attempt number
* `machine_name` — the machine preset (e.g., `small-1x`)
* `worker_version` — the deployed worker version
* `environment_type` — `PRODUCTION`, `STAGING`, `DEVELOPMENT`, or `PREVIEW`

### Querying metrics

Use [TRQL](/observability/query) to query metrics data. For example, to see average CPU utilization over time:

```sql theme={"theme":"css-variables"}
SELECT
  timeBucket(),
  avg(value) AS avg_cpu
FROM metrics
WHERE metric_name = 'process.cpu.utilization'
GROUP BY timeBucket
ORDER BY timeBucket
LIMIT 1000
```

See the [Query page](/observability/query#metrics-table-columns) for the full `metrics` table schema.

### Exporting metrics

You can send metrics to external observability services (Axiom, Honeycomb, Datadog, etc.) by configuring [telemetry exporters](/config/config-file#telemetry-exporters) in your `trigger.config.ts`.

---

## Dashboards

Create custom dashboards with real-time metrics powered by TRQL queries.

## Overview

In the Trigger.dev dashboard we have built-in dashboards and you can create your own.

Dashboards are powered by [TRQL queries](/observability/query) with widgets that can be displayed as charts, tables, or single values. They automatically refresh to show the latest data.

### Available metrics data

Trigger.dev automatically collects process metrics (CPU, memory) and Node.js runtime metrics (event loop, heap) for all deployed tasks -- no configuration needed. Requires SDK version **4.4.1 or later**. You can also create custom metrics using the `otel.metrics` API from the SDK.

All of this data is available in the `metrics` table for use in dashboard widgets. See [Logging, tracing & metrics](/logging#metrics) for the full list of automatic metrics and how to create custom ones, or the [Query page](/observability/query#metrics-table-columns) for the `metrics` table schema.

<img alt="The built-in Metrics dashboard" />

### Visualization types

* **Line chart** - Show trends over time
* **Bar chart** - Compare values across categories
* **Area chart** - Display cumulative trends
* **Table** - Show detailed data in rows
* **Single value** - Display a single metric (count, sum, average, etc.)

You can also add Titles to your dashboard.

## Filtering and time ranges

All widgets on a dashboard use the time range filter applied to the dashboard.

You can also filter the data by:

* Scope: Environment, Project, Organization
* Tasks
* Queues

## Creating custom dashboards

1. In the sidebar click the + icon next to "Dashboards".
2. Name your custom dashboard.
3. From the top-right you can "Add chart" or "Add title".
4. For charts you write [TRQL queries](/observability/query) and choose a visualization type.
5. You can resize and reposition widgets on your dashboards.

## Performance considerations

### Optimize queries for metrics

1. **Use time bucketing** - `timeBucket()` automatically groups by appropriate intervals
2. **Limit result size** - Add `LIMIT` clauses, especially for table widgets
3. **Use approximate functions** - `uniq()` instead of `uniqExact()` for faster approximate counts

## Exporting metric data

Export data from any metric widget:

1. Click the widget menu (three dots)
2. Select "Copy JSON" or "Copy CSV"

## Best practices

1. **Start simple** - Begin with basic metrics and iterate based on insights
2. **Use meaningful names** - Give widgets clear, descriptive titles
3. **Group related metrics** - Organize dashboards by theme (performance, costs, errors)
4. **Test queries first** - Use the Query page to develop and test before adding to dashboards

## Troubleshooting

### Widget shows "No data"

* Check that your query returns results in the Query page
* Verify time filters include the period with data
* Ensure task/queue filters match existing runs

### Widget is slow to load

* Add time range filters to your query
* Use `LIMIT` clauses
* Simplify aggregations
* Check query execution time in Query page

### Chart displays incorrectly

* Verify column names match visualization config
* Check data types (numbers for charts, dates for time series)
* Ensure `timeBucket()` is used for time-series charts
* Review that series columns exist in query results

## Limits

Dashboards are powered by Query so have [the same limits](/observability/query#limits) as Query.

There is a separate concurrency limits for metric widgets.

| Limit                     | Details        |
| :------------------------ | :------------- |
| Concurrent widget queries | 30 per project |

See [Limits](/limits) for details.

---

## Query

Query allows you to write custom queries against your data using TRQL (Trigger.dev Query Language), a SQL-style language based on ClickHouse SQL. You can query your data through the dashboard, SDK, or REST API.

### Available tables

* `runs`: contains all task run data including status, timing, costs, and task output. Run metadata (key-value set in your task) is not available on the Query page.
* `metrics`: contains metrics data for your runs including CPU, memory, and your custom metrics

### `metrics` table columns

| Column             | Type     | Description                                         |
| :----------------- | :------- | :-------------------------------------------------- |
| `metric_name`      | string   | Metric identifier (e.g., `process.cpu.utilization`) |
| `metric_type`      | string   | `gauge`, `sum`, or `histogram`                      |
| `value`            | number   | The observed value                                  |
| `bucket_start`     | datetime | 10-second aggregation bucket start time             |
| `run_id`           | string   | Associated run ID                                   |
| `task_identifier`  | string   | Task slug                                           |
| `attempt_number`   | number   | Attempt number                                      |
| `machine_id`       | string   | Machine that produced the metric                    |
| `machine_name`     | string   | Machine preset (e.g., `small-1x`)                   |
| `worker_version`   | string   | Worker version                                      |
| `environment_type` | string   | `PRODUCTION`, `STAGING`, `DEVELOPMENT`, `PREVIEW`   |
| `attributes`       | json     | Raw JSON attributes for custom data                 |

See [Logging, tracing & metrics](/logging#automatic-system-and-runtime-metrics) for the full list of automatically collected metrics and how to create custom metrics. You can visualize this data on [Dashboards](/observability/dashboards).

### `prettyFormat()`

Use `prettyFormat()` to format metric values for display:

```sql theme={"theme":"css-variables"}
SELECT
  timeBucket(),
  prettyFormat(avg(value), 'bytes') AS avg_memory
FROM metrics
WHERE metric_name = 'process.memory.usage'
GROUP BY timeBucket
ORDER BY timeBucket
LIMIT 1000
```

Available format types: `bytes`, `percent`, `duration`, `durationSeconds`, `quantity`, `costInDollars`.

## Using the Query dashboard

Navigate to the Query page to write and execute queries. The dashboard provides:

* **AI-powered query generation** - Describe what you want in natural language
* **Syntax highlighting** - SQL syntax highlighting for better readability
* **Query history** - Access your previous queries
* **Interactive help** - Built-in documentation for TRQL syntax and functions
* **Export options** - Download results as JSON or CSV

<img alt="The Query dashboard" />

## Querying from the SDK

Use `query.execute()` to run TRQL queries programmatically from your backend code:

```typescript theme={"theme":"css-variables"}
import { query } from "@trigger.dev/sdk";

// Basic query with defaults (environment scope, json format)
const result = await query.execute("SELECT run_id, status FROM runs LIMIT 10");
console.log(result.results); // Array<Record<string, any>>
```

### Type-safe queries

Use the `QueryTable` type for nice inferred types in your query results:

```typescript theme={"theme":"css-variables"}
import { query, type QueryTable } from "@trigger.dev/sdk";

// Type-safe query using QueryTable with specific columns
const typedResult = await query.execute<QueryTable<"runs", "run_id" | "status" | "triggered_at">>(
  "SELECT run_id, status, triggered_at FROM runs LIMIT 10"
);

typedResult.results.forEach((row) => {
  console.log(row.run_id, row.status); // Fully typed!
});
```

### Query options

```typescript theme={"theme":"css-variables"}
import { query } from "@trigger.dev/sdk";

const result = await query.execute("SELECT COUNT(*) as count FROM runs", {
  // Scope: "environment" (default), "project", or "organization"
  scope: "project",
  // Time period using shorthand (e.g., "7d", "30d", "1h")
  period: "7d",
  // Or use explicit time range
  // from: new Date("2024-01-01"),
  // to: new Date("2024-01-31"),

  // Response format: "json" (default) or "csv"
  format: "json",
});
```

### CSV export

Export query results as CSV by setting `format: "csv"`:

```typescript theme={"theme":"css-variables"}
const csvResult = await query.execute("SELECT run_id, status, triggered_at FROM runs", {
  format: "csv",
  period: "7d",
});

const lines = csvResult.results.split("\n");
console.log(lines[0]); // CSV header row
```

## Querying from the REST API

Execute queries via HTTP POST to `/api/v1/query`:

```sh theme={"theme":"css-variables"}
curl -X POST https://api.trigger.dev/api/v1/query \
  -H "Authorization: Bearer YOUR_SECRET_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "SELECT run_id, status FROM runs LIMIT 10",
    "scope": "environment",
    "period": "7d",
    "format": "json"
  }'
```

See the [API reference](/management/query/execute) for full details.

## TRQL syntax guide

### Basic queries

Select columns from a table:

```sql theme={"theme":"css-variables"}
SELECT run_id, task_identifier, status
FROM runs
LIMIT 10
```

Alias columns with `AS`:

```sql theme={"theme":"css-variables"}
SELECT task_identifier AS task, count() AS total
FROM runs
GROUP BY task
```

### Using \*

Note that when you use `SELECT *` we don't return all the columns, we only return the core columns. This is for performance reasons (the underlying ClickHouse database is columnar and selecting lots of columns isn't efficient).

You should specify the columns you want to return.

### Filtering with WHERE

Use comparison operators:

```sql theme={"theme":"css-variables"}
SELECT run_id, task_identifier FROM runs
WHERE status = 'Failed'
```

Available operators:

```sql theme={"theme":"css-variables"}
-- Comparison operators
WHERE status = 'Failed'           -- Equal
WHERE status != 'Completed'       -- Not equal
WHERE attempt_count > 3           -- Greater than
WHERE attempt_count >= 3          -- Greater than or equal
WHERE attempt_count < 5           -- Less than
WHERE attempt_count <= 5          -- Less than or equal

-- IN for multiple values
WHERE status IN ('Failed', 'Crashed')

-- LIKE for pattern matching (% = wildcard)
WHERE task_identifier LIKE 'email%'

-- ILIKE for case-insensitive matching
WHERE task_identifier ILIKE '%send%'

-- BETWEEN for ranges
WHERE triggered_at BETWEEN '2024-01-01' AND '2024-01-31'

-- NULL checks
WHERE completed_at IS NOT NULL
WHERE completed_at IS NULL

-- Array column checks
WHERE has(tags, 'user_12345')
WHERE notEmpty(tags)
WHERE hasAny(tags, array('user_12345', 'user_67890'))
WHERE hasAll(tags, array('user_12345', 'user_67890'))
WHERE indexOf(tags, 'user_12345') > 0
WHERE arrayElement(tags, 1) = 'user_12345'
```

### Sorting and limiting

Sort results with `ORDER BY`:

```sql theme={"theme":"css-variables"}
SELECT run_id, compute_cost, triggered_at
FROM runs
ORDER BY compute_cost DESC, triggered_at ASC
LIMIT 50
```

### Grouping and aggregation

Use `GROUP BY` with aggregate functions:

```sql theme={"theme":"css-variables"}
SELECT
  task_identifier,
  avg(value) AS avg_memory
FROM metrics
WHERE metric_name = 'process.memory.usage'
GROUP BY task_identifier
ORDER BY avg_memory DESC
LIMIT 20
```

## Available functions

TRQL provides a rich set of functions for data analysis.

### Aggregate functions

* `count()` - Count rows
* `countIf(col, cond)` - Count rows matching condition
* `countDistinct(col)` - Count unique values
* `sum(col)` - Sum of values
* `sumIf(col, cond)` - Sum values matching condition
* `avg(col)` - Average of values
* `min(col)` - Minimum value
* `max(col)` - Maximum value
* `median(col)` - Median value (50th percentile)
* `quantile(p)(col)` - Value at percentile p (0-1)
* `stddevPop(col)` - Population standard deviation
* `stddevSamp(col)` - Sample standard deviation

Example:

```sql theme={"theme":"css-variables"}
SELECT
  task_identifier,
  count() AS total_runs,
  avg(usage_duration) AS avg_duration_ms,
  median(usage_duration) AS median_duration_ms,
  quantile(0.95)(usage_duration) AS p95_duration_ms
FROM runs
GROUP BY task_identifier
```

### Date/time functions

**Time bucketing:**

```sql theme={"theme":"css-variables"}
-- Auto-bucket by time period based on query's time range
SELECT timeBucket(), count() AS runs
FROM runs
GROUP BY timeBucket()
```

**Date extraction:**

```sql theme={"theme":"css-variables"}
SELECT
  toYear(triggered_at) AS year,
  toMonth(triggered_at) AS month,
  toDayOfWeek(triggered_at) AS day_of_week,
  toHour(triggered_at) AS hour
FROM runs
```

**Date truncation:**

```sql theme={"theme":"css-variables"}
SELECT
  toStartOfDay(triggered_at) AS day,
  count() AS runs_per_day
FROM runs
GROUP BY day
ORDER BY day DESC
```

**Date arithmetic:**

```sql theme={"theme":"css-variables"}
-- Add/subtract time
SELECT dateAdd('day', 7, triggered_at) AS week_later
FROM runs

-- Calculate differences
SELECT dateDiff('minute', executed_at, completed_at) AS duration_minutes
FROM runs
WHERE completed_at IS NOT NULL
```

Common date functions:

* `now()` - Current date and time
* `today()` - Current date
* `toDate(dt)` - Convert to date
* `toStartOfDay(dt)`, `toStartOfHour(dt)`, `toStartOfMonth(dt)` - Truncate to start of period
* `formatDateTime(dt, format)` - Format datetime as string

### String functions

```sql theme={"theme":"css-variables"}
SELECT
  lower(status) AS status_lower,
  upper(status) AS status_upper,
  concat(task_identifier, '-', status) AS combined,
  substring(run_id, 1, 8) AS short_id,
  length(task_identifier) AS name_length
FROM runs
```

Common string functions:

* `length(s)` - String length
* `lower(s)`, `upper(s)` - Case conversion
* `concat(s1, s2, ...)` - Concatenate strings
* `substring(s, offset, len)` - Extract substring
* `trim(s)` - Remove whitespace
* `replace(s, from, to)` - Replace occurrences
* `startsWith(s, prefix)`, `endsWith(s, suffix)` - Check prefixes/suffixes

### Conditional functions

```sql theme={"theme":"css-variables"}
SELECT
  run_id,
  if(status = 'Failed', 1, 0) AS is_failed,
  multiIf(
    status = 'Completed', 'ok',
    status = 'Failed', 'bad',
    'other'
  ) AS status_category,
  coalesce(completed_at, triggered_at) AS end_time
FROM runs
```

* `if(cond, then, else)` - Conditional expression
* `multiIf(c1, t1, c2, t2, ..., else)` - Multiple conditions (like CASE)
* `coalesce(a, b, ...)` - First non-null value

### Math functions

```sql theme={"theme":"css-variables"}
SELECT
  round(compute_cost, 4) AS cost_rounded,
  ceil(usage_duration / 1000) AS duration_seconds_up,
  floor(usage_duration / 1000) AS duration_seconds_down,
  abs(compute_cost) AS cost_abs
FROM runs
```

### Array functions

Useful for working with tags and other array columns:

```sql theme={"theme":"css-variables"}
SELECT
  run_id,
  tags,
  length(tags) AS tag_count,
  has(tags, 'user_12345') AS is_production,
  arrayJoin(tags) AS individual_tag  -- Expand array to rows
FROM runs
WHERE notEmpty(tags)
```

### JSON functions

The `output`, `error`, and `metrics.attributes` columns are already JSON, so use dot notation to read or filter on them. You don't need `JSONExtract*` for these (those are for string columns).

```sql theme={"theme":"css-variables"}
SELECT
  run_id,
  output.message AS output_message,
  output.count AS count,
  output.externalId AS external_id
FROM runs
WHERE task_identifier = 'my-task'
  AND output.externalId = 'something'
ORDER BY triggered_at DESC
LIMIT 100
```

## Query scopes

Control what data your query can access:

* **`environment`** (default) - Query runs in the current environment only
* **`project`** - Query runs across all environments in the project
* **`organization`** - Query runs across all projects in the organization

```typescript theme={"theme":"css-variables"}
// Query across all environments in a project
const result = await query.execute("SELECT environment, count() FROM runs GROUP BY environment", {
  scope: "project",
});
```

## Time ranges

We recommend avoiding adding `triggered_at` in the actual TRQL query. The dashboard, API, and SDK have a time filter that is applied automatically and is easier to work with. It means the queries can be executed with multiple periods easily.

### Using period shorthand

```typescript theme={"theme":"css-variables"}
await query.execute("SELECT count() FROM runs", {
  period: "4d", // Last 4 days
});

// Supported periods: "1h", "6h", "12h", "1d", "7d", "30d", "90d", etc.
```

### Using explicit dates

```typescript theme={"theme":"css-variables"}
await query.execute("SELECT count() FROM runs", {
  from: new Date("2024-01-01"),
  to: new Date("2024-01-31"),
});

// Or use Unix timestamps
await query.execute("SELECT count() FROM runs", {
  from: Date.now() - 7 * 24 * 60 * 60 * 1000, // 7 days ago
  to: Date.now(),
});
```

## Example queries

### Failed runs (in the last 24 hours)

```sql theme={"theme":"css-variables"}
SELECT
  task_identifier,
  run_id,
  error,
  triggered_at
FROM runs
WHERE status = 'Failed'
ORDER BY triggered_at DESC
```

With the time filter set to 24h.

### Task success rate by day

```sql theme={"theme":"css-variables"}
SELECT
  toDate(triggered_at) AS day,
  task_identifier,
  countIf(status = 'Completed') AS completed,
  countIf(status = 'Failed') AS failed,
  round(completed / (completed + failed) * 100, 2) AS success_rate_pct
FROM runs
WHERE status IN ('Completed', 'Failed')
GROUP BY day, task_identifier
ORDER BY day DESC, task_identifier
```

### Top 10 most expensive runs

```sql theme={"theme":"css-variables"}
SELECT
  run_id,
  task_identifier,
  compute_cost,
  usage_duration,
  triggered_at
FROM runs
WHERE compute_cost > 0
ORDER BY compute_cost DESC
LIMIT 10
```

### Average compute duration over time

```sql theme={"theme":"css-variables"}
SELECT
  timeBucket() AS time,
  task_identifier,
  avg(usage_duration) AS avg_duration_ms,
  count() AS run_count
FROM runs
WHERE usage_duration IS NOT NULL
GROUP BY time, task_identifier
ORDER BY time ASC
```

### Runs by queue and machine

```sql theme={"theme":"css-variables"}
SELECT
  queue,
  machine,
  count() AS run_count,
  countIf(status = 'Completed') AS completed,
  countIf(status = 'Failed') AS failed
FROM runs
GROUP BY queue, machine
ORDER BY queue, machine
```

### CPU utilization over time

Track process CPU utilization bucketed over time.

```sql theme={"theme":"css-variables"}
SELECT
  timeBucket(),
  avg(value) AS avg_cpu
FROM metrics
WHERE metric_name = 'process.cpu.utilization'
GROUP BY timeBucket
ORDER BY timeBucket
LIMIT 1000
```

### Memory usage by task (past 7d)

Average process memory usage per task identifier over the last 7 days.

```sql theme={"theme":"css-variables"}
SELECT
  task_identifier,
  avg(value) AS avg_memory
FROM metrics
WHERE metric_name = 'process.memory.usage'
GROUP BY task_identifier
ORDER BY avg_memory DESC
LIMIT 20
```

### Available metric names

List all distinct metric names collected in your environment.

```sql theme={"theme":"css-variables"}
SELECT
  metric_name,
  count() AS sample_count
FROM metrics
GROUP BY metric_name
ORDER BY sample_count DESC
LIMIT 100
```

## Best practices

1. **Use the built-in time filtering** - The dashboard, API, and SDK have a time filter that is applied automatically and is easier to work with. It means the queries can be executed with multiple periods easily.
2. **Use LIMIT** - Add a `LIMIT` clause to reduce the rows returned if you don't need everything.
3. **Use appropriate aggregations** - For large datasets, use `uniq()` instead of `uniqExact()` for approximate but faster counts

## Limits

We have several limits to prevent abuse and ensure performance:

* **Concurrency limit**: We limit the number of concurrent queries per organization.
* **Row limit**: We limit the number of rows returned to 10k.
* **Time restrictions**: We limit the time period you can query.
* **Time/Memory limit**: We limit the memory a query can use and the time it can run for. As well as other limits like AST complexity.

See [Limits](/limits) for current quota details.

---
