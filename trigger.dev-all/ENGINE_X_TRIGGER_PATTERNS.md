# Engine-X Trigger.dev Setup Patterns

> Canonical setup guide for Trigger.dev across the engine-x multi-service architecture.
>
> **SDK version**: 4.4.3 | **Plan**: Pro | **Import**: `@trigger.dev/sdk` (never `@trigger.dev/sdk/v3`)

---

## Table of Contents

1. [Project Topology](#1-project-topology)
2. [Authentication and Secret Key Management](#2-authentication-and-secret-key-management)
3. [Task Organization](#3-task-organization)
4. [Queue Architecture](#4-queue-architecture)
5. [Retry and Error Strategy](#5-retry-and-error-strategy)
6. [M2M Cross-Service Triggering](#6-m2m-cross-service-triggering)
7. [Schedule Ownership](#7-schedule-ownership)
8. [Deployment Strategy](#8-deployment-strategy)
9. [Observability and Monitoring](#9-observability-and-monitoring)
10. [The `trigger.config.ts` Template](#10-the-triggerconfigts-template)

---

## 1. Project Topology

### Recommendation

**One Trigger.dev project per engine-x service.** Six projects total, one for each service.

| Trigger.dev Project | Service | Short Code |
| :--- | :--- | :--- |
| `engine-x-dex` | data-engine-x-api | `dex` |
| `engine-x-oex` | outbound-engine-x-api | `oex` |
| `engine-x-cex` | creative-engine-x-api | `cex` |
| `engine-x-pex` | paid-engine-x-api | `pex` |
| `engine-x-aex` | auth-engine-x-api | `aex` |
| `engine-x-chex` | chat-engine-x-api | `chex` |

Downstream products (License to Haul, Money Machine, StaffingEdge, PaidEdge, ColdEmail.com) **share the project of the service that owns their domain**. License to Haul tasks live in `engine-x-dex` (data ingestion) or `engine-x-oex` (outbound). PaidEdge tasks live in `engine-x-pex`.

### Rationale

- **Isolation**: Each service deploys independently. A bad deploy in `engine-x-cex` cannot break `engine-x-dex` tasks. Queues, schedules, and environment variables are fully independent per project.
- **Pro plan supports 10 projects per org** — six projects leaves headroom for future services or a shared tooling project.
- **Secret key scoping**: Each project gets its own `TRIGGER_SECRET_KEY` per environment, mapping cleanly to one Doppler project per service.
- **Observability**: Dashboard filters by project. One project per service means each team sees only their tasks.

A monorepo-style single project was considered but rejected: it couples deploy cycles, makes queue naming collision possible, and creates a noisy dashboard. A per-product split was rejected because products share task code with their parent service and would exhaust the 10-project limit.

### Decision Table

| Approach | When to Use | Tradeoffs |
| :--- | :--- | :--- |
| **One project per service** (recommended) | Default for all engine-x services | Clean isolation; requires M2M keys for cross-service triggering |
| Single shared project | Tiny team, < 3 services, tasks heavily interleaved | Simpler key management; couples deploys, noisy dashboard |
| One project per downstream product | Products have completely independent task sets | Exhausts project limit fast; duplicates shared task code |

---

## 2. Authentication and Secret Key Management

### Recommendation

Each service stores its own Trigger.dev secret key in its Doppler project, per environment. Cross-service triggering uses the target service's secret key, also stored in the calling service's Doppler.

### Key Types

| Key Type | Format | Purpose | Where Stored |
| :--- | :--- | :--- | :--- |
| **Secret Key** | `tr_dev_*`, `tr_stg_*`, `tr_prod_*`, `tr_preview_*` | Trigger and manage tasks in a specific project + environment | Service's own Doppler project |
| **Personal Access Token (PAT)** | `tr_pat_*` | CI/CD deployments (user-scoped, cross-project) | GitHub Actions secrets (sourced from Doppler) |

### Doppler Variable Naming

Each service's Doppler project stores:

```
# Own project keys (one per environment)
TRIGGER_SECRET_KEY=tr_prod_...          # Production
TRIGGER_SECRET_KEY_DEV=tr_dev_...       # Development (if needed locally)
TRIGGER_SECRET_KEY_STG=tr_stg_...       # Staging
TRIGGER_SECRET_KEY_PREVIEW=tr_preview_... # Preview branches

# CI/CD deployment token
TRIGGER_ACCESS_TOKEN=tr_pat_...

# Cross-service keys (only in services that trigger remote tasks)
DEX_TRIGGER_SECRET_KEY=tr_prod_...      # data-engine-x's production key
OEX_TRIGGER_SECRET_KEY=tr_prod_...      # outbound-engine-x's production key
CEX_TRIGGER_SECRET_KEY=tr_prod_...      # creative-engine-x's production key
```

**Convention**: `{TARGET_SHORT_CODE}_TRIGGER_SECRET_KEY` — uppercase service code prefix, stored in the *calling* service's Doppler project. For example, if `outbound-engine-x` needs to trigger tasks in `data-engine-x`, then `DEX_TRIGGER_SECRET_KEY` lives in OEX's Doppler.

### Trigger.dev Auth vs. Better Auth

These are **completely independent systems**:

- **Better Auth** (at `api.authengine.dev`) handles user authentication for engine-x APIs using EdDSA JWTs. It is used by frontends and inter-service API calls.
- **Trigger.dev auth** uses project-scoped secret keys to authenticate task triggers and management API calls. It has no relationship to your user auth system.

A Trigger.dev task that calls another engine-x API endpoint should authenticate with that API using a service-to-service Better Auth token (or API key), not a Trigger.dev secret key. The Trigger.dev key is only for communicating with the Trigger.dev platform.

### Preview Branch Keys

Preview branches share a single `TRIGGER_SECRET_KEY` (prefixed `tr_preview_`) per project, differentiated by the `TRIGGER_PREVIEW_BRANCH` environment variable:

```bash
TRIGGER_SECRET_KEY="tr_preview_..."
TRIGGER_PREVIEW_BRANCH="feature-new-ingestion"
```

Store the preview secret key in Doppler's `dev` or `preview` config. The branch name is injected dynamically in CI from the git branch.

---

## 3. Task Organization

### Recommendation

Each service repo has a `/trigger` directory at the repository root, alongside the FastAPI app. The `trigger.config.ts` file lives at the repo root.

### Directory Layout

```
data-engine-x-api/
├── app/                        # FastAPI application (Python)
│   ├── main.py
│   ├── routers/
│   └── services/
├── trigger/                    # Trigger.dev tasks (TypeScript)
│   ├── ingestion/
│   │   ├── fmcsa.ts
│   │   └── sam-gov.ts
│   ├── enrichment/
│   │   ├── enigma.ts
│   │   └── prospeo.ts
│   ├── schedules/
│   │   └── daily-ingestion.ts
│   └── shared/
│       └── queues.ts           # Shared queue definitions
├── trigger.config.ts           # Trigger.dev configuration
├── package.json                # Node.js dependencies (Trigger.dev SDK)
├── tsconfig.json
├── Dockerfile                  # FastAPI container (separate from Trigger.dev)
└── pyproject.toml
```

The FastAPI app and Trigger.dev tasks coexist in the same repo but are deployed independently. The FastAPI app deploys to Railway as a Docker container. Trigger.dev tasks deploy via `trigger deploy` to Trigger.dev Cloud.

### Task ID Naming Convention

Prefix every task ID with the service short code, separated by a colon:

```
{service}:{domain}-{action}
```

Examples:

| Service | Task ID | Description |
| :--- | :--- | :--- |
| data-engine-x | `dex:ingest-fmcsa` | FMCSA data ingestion |
| data-engine-x | `dex:enrich-enigma` | Enigma enrichment pipeline |
| outbound-engine-x | `oex:send-sms` | Send SMS via Twilio |
| outbound-engine-x | `oex:voice-call` | Initiate voice AI call |
| creative-engine-x | `cex:render-video` | Remotion video render |
| creative-engine-x | `cex:generate-pdf` | PDF report generation |
| paid-engine-x | `pex:sync-meta-ads` | Meta Ads performance sync |
| paid-engine-x | `pex:generate-report` | Ad performance report |
| chat-engine-x | `chex:chat-completion` | AI chat orchestration |
| auth-engine-x | `aex:rotate-keys` | Key rotation maintenance |

The service prefix prevents ID collisions in dashboard search and makes cross-service triggering unambiguous — when `oex` triggers `dex:ingest-fmcsa`, the task ID is self-documenting.

### `schemaTask()` for Cross-Service Contracts

Use `schemaTask()` (with Zod validation) for **any task that is triggered cross-service**. This validates payloads before execution and produces clear errors on schema mismatch rather than silent failures:

```typescript
// trigger/enrichment/enigma.ts
import { schemaTask, logger } from "@trigger.dev/sdk";
import { z } from "zod";

export const enrichEnigma = schemaTask({
  id: "dex:enrich-enigma",
  schema: z.object({
    companyId: z.string(),
    dotNumber: z.string(),
    enrichmentType: z.enum(["full", "basic"]),
  }),
  run: async (payload) => {
    // payload is fully typed from the schema
    logger.info("Enriching via Enigma", { companyId: payload.companyId });
    const result = await enigmaClient.enrich(payload.dotNumber, payload.enrichmentType);
    return { companyId: payload.companyId, enriched: result };
  },
});
```

For tasks only triggered internally (within the same project), a regular `task()` with TypeScript types is sufficient.

### `dirs` Configuration

```typescript
// trigger.config.ts
export default defineConfig({
  project: "<project-ref>",
  dirs: ["./trigger"],
  // ...
});
```

Keep all task files under `./trigger`. Subdirectories within `./trigger` are automatically scanned. The `ignorePatterns` option excludes test files:

```typescript
ignorePatterns: ["**/*.test.ts", "**/*.spec.ts"],
```

### Triggering from Python (FastAPI)

The FastAPI backend triggers Trigger.dev tasks via the REST API. Use `httpx` or `requests`:

```python
# app/services/trigger.py
import httpx
import os

TRIGGER_SECRET_KEY = os.environ["TRIGGER_SECRET_KEY"]
TRIGGER_API_BASE = "https://api.trigger.dev/api/v1"

async def trigger_task(
    task_id: str,
    payload: dict,
    *,
    idempotency_key: str | None = None,
    tags: list[str] | None = None,
    ttl: str | None = None,
) -> dict:
    """Fire-and-forget trigger of a Trigger.dev task."""
    options = {}
    if idempotency_key:
        options["idempotencyKey"] = idempotency_key
    if tags:
        options["tags"] = tags
    if ttl:
        options["ttl"] = ttl

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{TRIGGER_API_BASE}/tasks/{task_id}/trigger",
            headers={
                "Authorization": f"Bearer {TRIGGER_SECRET_KEY}",
                "Content-Type": "application/json",
            },
            json={"payload": payload, "options": options},
        )
        response.raise_for_status()
        return response.json()
```

Usage in a FastAPI route:

```python
from app.services.trigger import trigger_task

@router.post("/ingest/fmcsa")
async def start_fmcsa_ingestion(request: IngestRequest):
    handle = await trigger_task(
        "dex:ingest-fmcsa",
        {"source": request.source, "date_range": request.date_range},
        idempotency_key=f"fmcsa-{request.date_range}",
        tags=[f"source:{request.source}"],
    )
    return {"run_id": handle["id"]}
```

---

## 4. Queue Architecture

### Recommendation

Use default per-task queues for most tasks. Define shared custom queues when multiple tasks hit the same rate-limited external API. Use concurrency keys for per-tenant isolation.

### Default Behavior

Every task automatically gets its own queue (named after the task ID) with **no concurrency limit**. This is fine for tasks that don't need throttling.

### When to Define Custom Queues

Define a shared custom queue when:
- Multiple tasks call the same rate-limited API (e.g., Enigma, Prospeo, Twilio)
- You need a global concurrency cap across related tasks
- You want to pause/resume a group of tasks together

### Queue Definitions per Service

```typescript
// trigger/shared/queues.ts (data-engine-x)
import { queue } from "@trigger.dev/sdk";

// External API rate limits
export const enigmaQueue = queue({
  name: "dex:api-enigma",
  concurrencyLimit: 10,       // Enigma API rate limit
});

export const prospeoQueue = queue({
  name: "dex:api-prospeo",
  concurrencyLimit: 5,        // Prospeo API rate limit
});

// Bulk ingestion (high throughput, bounded)
export const ingestionQueue = queue({
  name: "dex:ingestion",
  concurrencyLimit: 20,       // Parallel ingestion workers
});
```

```typescript
// trigger/shared/queues.ts (outbound-engine-x)
import { queue } from "@trigger.dev/sdk";

export const twilioSmsQueue = queue({
  name: "oex:api-twilio-sms",
  concurrencyLimit: 50,       // Twilio SMS rate limit
});

export const twilioVoiceQueue = queue({
  name: "oex:api-twilio-voice",
  concurrencyLimit: 10,       // Voice calls are expensive
});

export const vapiQueue = queue({
  name: "oex:api-vapi",
  concurrencyLimit: 5,        // Voice AI concurrent sessions
});
```

```typescript
// trigger/shared/queues.ts (creative-engine-x)
import { queue } from "@trigger.dev/sdk";

export const renderQueue = queue({
  name: "cex:render",
  concurrencyLimit: 3,        // CPU/memory intensive renders
});
```

```typescript
// trigger/shared/queues.ts (paid-engine-x)
import { queue } from "@trigger.dev/sdk";

export const metaAdsQueue = queue({
  name: "pex:api-meta-ads",
  concurrencyLimit: 10,
});

export const linkedinAdsQueue = queue({
  name: "pex:api-linkedin-ads",
  concurrencyLimit: 5,
});

export const hubspotQueue = queue({
  name: "pex:api-hubspot",
  concurrencyLimit: 10,
});
```

### Queue Naming Convention

```
{service}:{category}-{provider-or-domain}
```

Examples: `dex:api-enigma`, `oex:api-twilio-sms`, `cex:render`, `pex:api-meta-ads`

### Concurrency Keys for Per-Tenant Isolation

Use concurrency keys when different tenants or clients should not compete for queue slots:

```typescript
// outbound-engine-x: per-carrier SMS rate limiting
export const sendSms = task({
  id: "oex:send-sms",
  queue: twilioSmsQueue,
  run: async (payload: { carrierId: string; to: string; body: string }) => {
    await twilioClient.messages.create({ to: payload.to, body: payload.body });
  },
});

// Trigger with per-carrier concurrency key
await sendSms.trigger(
  { carrierId: "carrier_123", to: "+1555...", body: "Hello" },
  { concurrencyKey: `carrier_${payload.carrierId}` }
);
```

```typescript
// paid-engine-x: per-client ad account isolation
export const syncMetaAds = task({
  id: "pex:sync-meta-ads",
  queue: metaAdsQueue,
  run: async (payload: { clientId: string; adAccountId: string }) => {
    await metaApi.syncPerformance(payload.adAccountId);
  },
});

// Each client's sync runs independently
await syncMetaAds.trigger(
  { clientId: "client_456", adAccountId: "act_789" },
  { concurrencyKey: `client_${payload.clientId}` }
);
```

### Recommended Concurrency Limits by Task Type

| Task Category | Concurrency Limit | Rationale |
| :--- | :--- | :--- |
| **Data ingestion** (FMCSA, SAM.gov) | 10–20 | High throughput needed, but bound by source API and DB write capacity |
| **External API enrichment** (Enigma, Prospeo) | 5–10 | Rate-limited by provider; check provider docs for exact limits |
| **AI/LLM calls** (OpenAI, Anthropic) | 5–10 | Cost-controlled; higher limits for batch processing, lower for real-time |
| **Email sending** | 20–50 | Carrier rate limits; use concurrency keys per sender domain |
| **SMS sending** (Twilio) | 30–50 | Twilio rate limits per number; use concurrency keys per from-number |
| **Voice calls** (Vapi, Twilio) | 3–10 | Expensive per-minute; concurrent call capacity is limited |
| **Video/asset rendering** (Remotion) | 2–5 | CPU/memory bound; each render uses `large-1x` or higher |
| **PDF generation** | 5–10 | Moderate resource usage |
| **Report generation** | 3–5 | Often involves heavy DB queries + rendering |
| **CRM sync** (HubSpot, Salesforce) | 5–10 | API rate limits per account |

### Queue Depth Limits (Pro Plan)

| Environment | Max Queued Per Queue |
| :--- | :--- |
| Development | 5,000 |
| Staging / Production | 1,000,000 |

### Dynamic Concurrency Override

Use the Queue Management SDK to adjust limits at runtime during incidents or peak load:

```typescript
import { queues } from "@trigger.dev/sdk";

// Throttle Enigma during an outage
await queues.overrideConcurrencyLimit({ type: "custom", name: "dex:api-enigma" }, 1);

// Restore normal capacity
await queues.resetConcurrencyLimit({ type: "custom", name: "dex:api-enigma" });
```

---

## 5. Retry and Error Strategy

### Recommendation

Set conservative defaults in `trigger.config.ts`. Override per-task for specific error behavior. Use `catchError` for conditional retry logic, `AbortTaskRunError` for permanent failures, and `retry.fetch()` for HTTP calls.

### Config-Level Defaults

```typescript
// trigger.config.ts
retries: {
  enabledInDev: false,       // Don't retry in development
  default: {
    maxAttempts: 3,           // 1 initial + 2 retries
    minTimeoutInMs: 1000,     // 1 second minimum delay
    maxTimeoutInMs: 30_000,   // 30 second maximum delay
    factor: 2,                // Exponential backoff: 1s → 2s → 4s ...
    randomize: true,          // Jitter to avoid thundering herd
  },
},
```

### Per-Task Overrides

Tasks that call flaky external APIs should retry more aggressively:

```typescript
export const ingestFmcsa = task({
  id: "dex:ingest-fmcsa",
  retry: {
    maxAttempts: 5,           // More retries for government APIs
    factor: 2,
    minTimeoutInMs: 2000,
    maxTimeoutInMs: 60_000,
  },
  run: async (payload) => { /* ... */ },
});
```

Tasks with expensive side effects (sending email, charging payment) should retry less:

```typescript
export const sendSms = task({
  id: "oex:send-sms",
  retry: { maxAttempts: 2 },  // Limit retries to avoid duplicate sends
  run: async (payload) => { /* ... */ },
});
```

### `catchError` for Conditional Retry

Use `catchError` to inspect errors and decide whether to retry, skip, or retry at a specific time:

```typescript
export const callExternalApi = task({
  id: "dex:enrich-theirstack",
  retry: { maxAttempts: 5, factor: 2, minTimeoutInMs: 1000, maxTimeoutInMs: 60_000 },
  run: async (payload: { companyId: string }) => {
    const response = await fetch(`https://api.theirstack.com/v1/company/${payload.companyId}`);
    if (!response.ok) {
      const error = new Error(`TheirStack API ${response.status}`);
      (error as any).status = response.status;
      (error as any).retryAfter = response.headers.get("retry-after");
      throw error;
    }
    return await response.json();
  },
  catchError: async ({ error }) => {
    const status = (error as any)?.status;

    // 4xx client errors (except 429) — permanent failure, don't retry
    if (status >= 400 && status < 500 && status !== 429) {
      return { skipRetrying: true };
    }

    // 429 rate limited — retry after the specified delay
    if (status === 429) {
      const retryAfter = (error as any)?.retryAfter;
      if (retryAfter) {
        return { retryAt: new Date(Date.now() + parseInt(retryAfter) * 1000) };
      }
    }

    // 5xx or unknown — use default backoff
    return undefined;
  },
});
```

### `AbortTaskRunError` for Invalid Payloads

Throw `AbortTaskRunError` when the error is permanent and retrying will never succeed:

```typescript
import { task, AbortTaskRunError } from "@trigger.dev/sdk";

export const processCarrier = task({
  id: "dex:process-carrier",
  run: async (payload: { dotNumber: string }) => {
    if (!payload.dotNumber || !/^\d+$/.test(payload.dotNumber)) {
      throw new AbortTaskRunError("Invalid DOT number — will not retry");
    }
    // ... process
  },
});
```

### `retry.fetch()` for HTTP Calls

Use `retry.fetch()` for HTTP requests with status-based retry strategies:

```typescript
import { task, retry } from "@trigger.dev/sdk";

export const enrichProspeo = task({
  id: "dex:enrich-prospeo",
  queue: prospeoQueue,
  run: async (payload: { email: string }) => {
    const response = await retry.fetch(
      `https://api.prospeo.io/v1/enrich?email=${payload.email}`,
      {
        headers: { Authorization: `Bearer ${process.env.PROSPEO_API_KEY}` },
        retry: {
          byStatus: {
            "429": {
              strategy: "headers",
              limitHeader: "x-ratelimit-limit",
              remainingHeader: "x-ratelimit-remaining",
              resetHeader: "x-ratelimit-reset",
              resetFormat: "unix_timestamp_in_ms",
            },
            "500-599": {
              strategy: "backoff",
              maxAttempts: 3,
              factor: 2,
              minTimeoutInMs: 1000,
              maxTimeoutInMs: 30_000,
            },
          },
        },
      }
    );
    return await response.json();
  },
});
```

### `retry.onThrow()` for Scoped Retries

Use `retry.onThrow()` to retry a specific code block without restarting the entire task:

```typescript
import { task, retry, logger } from "@trigger.dev/sdk";

export const multiStepIngestion = task({
  id: "dex:multi-step-ingestion",
  run: async (payload: { sourceUrl: string }) => {
    // Step 1: Retry fetching up to 3 times (independent of task-level retry)
    const rawData = await retry.onThrow(
      async ({ attempt }) => {
        logger.info("Fetching source data", { attempt });
        const resp = await fetch(payload.sourceUrl);
        if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
        return await resp.json();
      },
      { maxAttempts: 3, factor: 2, minTimeoutInMs: 500 }
    );

    // Step 2: Transform (no retry needed — pure function)
    const transformed = transformRecords(rawData);

    // Step 3: Load with its own retry scope
    await retry.onThrow(
      async () => { await db.bulkUpsert(transformed); },
      { maxAttempts: 2, minTimeoutInMs: 1000 }
    );

    return { count: transformed.length };
  },
});
```

### OOM Handling

Tasks that process large datasets or render video should configure `retry.outOfMemory` to automatically retry on a larger machine:

```typescript
// creative-engine-x: video rendering
export const renderVideo = task({
  id: "cex:render-video",
  machine: "medium-2x",    // Start with 2 vCPU / 4 GB
  retry: {
    maxAttempts: 3,
    outOfMemory: {
      machine: "large-1x", // Retry on 4 vCPU / 8 GB if OOM
    },
  },
  run: async (payload: { templateId: string; data: Record<string, unknown> }) => {
    return await renderRemotionVideo(payload.templateId, payload.data);
  },
});

// data-engine-x: large dataset processing
export const processLargeDataset = task({
  id: "dex:process-large-dataset",
  machine: "medium-1x",    // Start with 1 vCPU / 2 GB
  retry: {
    maxAttempts: 3,
    outOfMemory: {
      machine: "large-2x", // Retry on 8 vCPU / 16 GB if OOM
    },
  },
  run: async (payload: { datasetId: string }) => {
    return await processDataset(payload.datasetId);
  },
});
```

### `onFailure` for Alerting

After all retries are exhausted, use `onFailure` to send alerts. Configure this globally in `trigger.config.ts` and override per-task when needed:

```typescript
// trigger.config.ts
onFailure: async ({ payload, error, ctx }) => {
  await sendSlackAlert({
    channel: "#engine-x-alerts",
    text: `Task failed: ${ctx.task.id} (run: ${ctx.run.id})`,
    error: error.message,
    environment: ctx.environment.type,
  });
},
```

### Machine Presets

| Preset | vCPU | Memory | Use For |
| :--- | :--- | :--- | :--- |
| `micro` | 0.25 | 0.25 GB | Lightweight webhook handlers, queue workers |
| `small-1x` | 0.5 | 0.5 GB | **Default.** Most API calls, data transforms |
| `small-2x` | 1 | 1 GB | Moderate processing, API orchestration |
| `medium-1x` | 1 | 2 GB | Data processing, image manipulation |
| `medium-2x` | 2 | 4 GB | AI inference, heavy computation |
| `large-1x` | 4 | 8 GB | Video processing, large model inference |
| `large-2x` | 8 | 16 GB | ML training, massive dataset processing |

**Recommendations by service:**

| Service | Default Machine | Tasks Needing Override |
| :--- | :--- | :--- |
| data-engine-x | `small-2x` | Large dataset processing → `large-1x` or `large-2x` |
| outbound-engine-x | `small-1x` | Voice AI processing → `medium-1x` |
| creative-engine-x | `medium-2x` | Video rendering → `large-1x`; PDF generation → `medium-1x` |
| paid-engine-x | `small-1x` | ClickHouse analytics → `medium-1x` |
| chat-engine-x | `medium-1x` | Long-context AI chat → `medium-2x` |
| auth-engine-x | `micro` | Key rotation, JWT operations — lightweight |

### Decision Table: Which Retry Technique

| Technique | Scope | Use When |
| :--- | :--- | :--- |
| Task-level `retry` | Entire task | Default backoff for transient failures |
| `catchError` | Per-attempt hook | Different errors need different handling (4xx skip, 429 rate-limit, 5xx retry) |
| `AbortTaskRunError` | Thrown in `run()` | Payload is invalid, business logic rejection — never retry |
| `retry.onThrow()` | Code block | Retry one step without restarting the whole task |
| `retry.fetch()` | HTTP request | Status-based retries with rate-limit header support |
| `retry.outOfMemory` | Task-level | Large data or rendering that may OOM |
| `onFailure` | After all retries | Alerting, cleanup, dead-letter logging |

---

## 6. M2M Cross-Service Triggering

### Recommendation

Use `tasks.trigger()` with the target service's secret key via `configure()`. Default to fire-and-forget (`trigger()`) — services are peer-level and should not block on each other. Use tags for cross-service correlation and TTL for staleness prevention.

### Pattern: Service A Triggers Task in Service B

```typescript
// outbound-engine-x triggers an enrichment task in data-engine-x
// File: trigger/cross-service/request-enrichment.ts
import { configure, tasks } from "@trigger.dev/sdk";

// Point the SDK at data-engine-x's project
configure({
  secretKey: process.env.DEX_TRIGGER_SECRET_KEY!,
});

// Type definition mirrors what dex:enrich-enigma expects
interface EnrichPayload {
  companyId: string;
  dotNumber: string;
  enrichmentType: "full" | "basic";
}

export async function requestEnrichment(companyId: string, dotNumber: string) {
  const handle = await tasks.trigger<{ payload: EnrichPayload }>(
    "dex:enrich-enigma",
    { companyId, dotNumber, enrichmentType: "full" },
    {
      tags: [`source:oex`, `company:${companyId}`],
      ttl: "2h",
      idempotencyKey: `enrich-${companyId}-${dotNumber}`,
    }
  );

  return handle; // { id: "run_..." }
}
```

### From Python (FastAPI)

Cross-service triggering from Python uses the REST API with the target service's secret key:

```python
# outbound-engine-x-api/app/services/trigger.py
import httpx
import os

async def trigger_dex_task(task_id: str, payload: dict, **options) -> dict:
    """Trigger a task in data-engine-x's Trigger.dev project."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"https://api.trigger.dev/api/v1/tasks/{task_id}/trigger",
            headers={
                "Authorization": f"Bearer {os.environ['DEX_TRIGGER_SECRET_KEY']}",
                "Content-Type": "application/json",
            },
            json={"payload": payload, "options": options},
        )
        response.raise_for_status()
        return response.json()
```

### Doppler Key Storage for M2M

| Calling Service | Doppler Variable | Target Service |
| :--- | :--- | :--- |
| outbound-engine-x | `DEX_TRIGGER_SECRET_KEY` | data-engine-x |
| outbound-engine-x | `CEX_TRIGGER_SECRET_KEY` | creative-engine-x |
| data-engine-x | `OEX_TRIGGER_SECRET_KEY` | outbound-engine-x |
| paid-engine-x | `DEX_TRIGGER_SECRET_KEY` | data-engine-x |
| paid-engine-x | `CEX_TRIGGER_SECRET_KEY` | creative-engine-x |

Only add cross-service keys to services that actually need them. Don't pre-populate all combinations.

### Idempotency Keys for Cross-Service Triggers

Always include an idempotency key for cross-service triggers to prevent duplicate work:

```typescript
await tasks.trigger<{ payload: RenderPayload }>(
  "cex:render-video",
  { templateId, data },
  {
    idempotencyKey: `render-${templateId}-${contentHash}`,
    idempotencyKeyTTL: "24h",
    tags: [`source:oex`, `template:${templateId}`],
    ttl: "1h",
  }
);
```

**Idempotency key convention**: `{action}-{primary-id}-{content-hash-or-version}`

### `trigger()` vs `triggerAndWait()`

| Method | Use When | Behavior |
| :--- | :--- | :--- |
| `trigger()` | **Default for cross-service.** Fire-and-forget. | Returns handle immediately; calling service continues. |
| `triggerAndWait()` | Only when the calling task *must* have the result to continue. | Blocks calling task (checkpointed — no slot consumed). Version-locks child to parent. |

**Rule**: Services are peer-level. Use `trigger()` for cross-service calls. If you need the result, have the target task write to a shared store (Supabase) and let the calling service poll or receive a webhook.

### Tags for Cross-Service Correlation

Apply consistent tags so runs can be traced across services in the dashboard:

```typescript
// Standard cross-service tags
tags: [
  `source:${callingService}`,          // e.g., "source:oex"
  `tenant:${tenantId}`,                // e.g., "tenant:acme-corp"
  `workflow:${workflowName}`,          // e.g., "workflow:lead-enrichment"
  `correlation:${correlationId}`,      // UUID linking related runs
]
```

Tags are limited to 10 per run, each under 128 characters.

### TTL Recommendations

| Scenario | TTL | Rationale |
| :--- | :--- | :--- |
| Real-time enrichment request | `30m` | Data becomes stale quickly |
| Report generation request | `2h` | User expects it within a work session |
| Background data sync | `6h` | Can tolerate delay |
| Campaign email trigger | `1h` | Email sequences are time-sensitive |
| Asset rendering | `4h` | Creative renders can take time but shouldn't queue forever |

---

## 7. Schedule Ownership

### Recommendation

The service that owns the data or domain owns the schedule. Use `schedules.task()` (declarative) for static schedules and `schedules.create()` (imperative) for dynamic per-tenant schedules.

### Principle

Schedules live in the same Trigger.dev project as the task they run. The domain owner decides when work happens:

- **data-engine-x** owns data ingestion and enrichment schedules
- **outbound-engine-x** owns campaign timing and communication schedules
- **paid-engine-x** owns ad performance sync schedules
- **creative-engine-x** owns asset cleanup schedules

### Declarative Schedules (`schedules.task()`)

Use for recurring work with a fixed cadence known at deploy time:

```typescript
// data-engine-x: trigger/schedules/daily-ingestion.ts
import { schedules, logger } from "@trigger.dev/sdk";

export const dailyFmcsaIngestion = schedules.task({
  id: "dex:schedule-fmcsa-daily",
  cron: {
    pattern: "0 3 * * *",           // 3:00 AM ET daily
    timezone: "America/New_York",
  },
  retry: { maxAttempts: 3 },
  run: async (payload) => {
    logger.info("Starting daily FMCSA ingestion", {
      scheduledFor: payload.timestamp.toISOString(),
      lastRun: payload.lastTimestamp?.toISOString(),
    });

    const since = payload.lastTimestamp ?? new Date(Date.now() - 86_400_000);
    const result = await ingestFmcsaData({ since });

    return { ingested: result.count };
  },
});
```

### Imperative Schedules (`schedules.create()`)

Use for per-tenant or user-configured schedules. **Always include `deduplicationKey`** to prevent duplicate schedules on redeploy or retry:

```typescript
// outbound-engine-x: trigger/schedules/campaign-drip.ts
import { schedules } from "@trigger.dev/sdk";

// Task definition (runs when the schedule fires)
export const campaignDrip = schedules.task({
  id: "oex:campaign-drip",
  run: async (payload) => {
    const campaignId = payload.externalId!; // Set when schedule was created
    await executeDripStep(campaignId);
  },
});

// Called from FastAPI when a user creates a campaign
export async function createCampaignSchedule(
  campaignId: string,
  cronPattern: string,
  timezone: string,
) {
  const schedule = await schedules.create({
    task: "oex:campaign-drip",
    cron: cronPattern,
    timezone,
    externalId: campaignId,
    deduplicationKey: `campaign-drip-${campaignId}`, // Required!
  });

  return schedule;
}

// Update schedule when user changes campaign timing
export async function updateCampaignSchedule(scheduleId: string, newCron: string) {
  await schedules.update(scheduleId, { cron: newCron });
}

// Delete schedule when campaign is archived
export async function deleteCampaignSchedule(scheduleId: string) {
  await schedules.del(scheduleId);
}
```

### Example Schedules by Service

**data-engine-x:**

| Schedule | Cron | Type | Description |
| :--- | :--- | :--- | :--- |
| `dex:schedule-fmcsa-daily` | `0 3 * * *` | Declarative | Daily FMCSA data ingestion |
| `dex:schedule-sam-gov-weekly` | `0 2 * * 1` | Declarative | Weekly SAM.gov refresh |
| `dex:schedule-enrichment-refresh` | `0 */4 * * *` | Declarative | Enrichment data refresh every 4 hours |
| `dex:schedule-materialized-views` | `0 0 * * *` | Declarative | Nightly materialized view refresh |

**outbound-engine-x:**

| Schedule | Cron | Type | Description |
| :--- | :--- | :--- | :--- |
| `oex:campaign-drip` | Varies | Imperative | Per-campaign drip sequences |
| `oex:schedule-voicemail-window` | `0 9 * * 1-5` | Declarative | Voicemail drop window (weekdays 9 AM) |
| `oex:schedule-sms-quiet-hours` | `0 21 * * *` | Declarative | Pause SMS sending for quiet hours |

**paid-engine-x:**

| Schedule | Cron | Type | Description |
| :--- | :--- | :--- | :--- |
| `pex:schedule-meta-ads-sync` | `*/30 * * * *` | Declarative | Meta Ads performance sync every 30 min |
| `pex:schedule-linkedin-ads-sync` | `0 */2 * * *` | Declarative | LinkedIn Ads sync every 2 hours |
| `pex:schedule-weekly-report` | `0 8 * * 1` | Declarative | Weekly performance report (Monday 8 AM) |
| Per-client report | Varies | Imperative | Client-configured reporting cadence |

**creative-engine-x:**

| Schedule | Cron | Type | Description |
| :--- | :--- | :--- | :--- |
| `cex:schedule-asset-cleanup` | `0 4 * * 0` | Declarative | Weekly cleanup of expired assets |
| `cex:schedule-template-refresh` | `0 6 * * *` | Declarative | Daily template cache refresh |

### Schedule Limits (Pro Plan)

- **1,000+ schedules per project** (additional bundles at $10/month per 1,000)
- Dynamic per-tenant schedules can scale to hundreds per service
- Use `deduplicationKey` on every imperative schedule to prevent duplicates

### Decision Table: Declarative vs Imperative

| Approach | When to Use | Example |
| :--- | :--- | :--- |
| `schedules.task()` (declarative) | Fixed cadence known at deploy time | Daily data ingestion, nightly cleanup |
| `schedules.create()` (imperative) | User-configured or per-tenant timing | Campaign drip sequences, client report schedules |

---

## 8. Deployment Strategy

### Recommendation

Each service deploys its own Trigger.dev tasks independently via GitHub Actions. Use preview branches for PR-based QA. Pin SDK versions. Use `--skip-promotion` + `promote` for coordinated releases.

### Independent Deploy per Service

Each service's repo has its own:
- `trigger.config.ts` with its project ref
- GitHub Actions workflow for Trigger.dev deployment
- `package.json` with pinned `@trigger.dev/sdk` and `trigger.dev` versions

Trigger.dev tasks deploy independently from the FastAPI app:
- **FastAPI**: Deploys to Railway via Docker
- **Trigger.dev tasks**: Deploy to Trigger.dev Cloud via `trigger deploy`

These can be deployed independently or coordinated with atomic deploys when a FastAPI change depends on a new task version.

### Environment Mapping

| Railway Environment | Trigger.dev Environment | Deploy Command |
| :--- | :--- | :--- |
| Development (local) | DEV | `npx trigger.dev@latest dev` |
| Staging | STAGING | `npx trigger.dev@latest deploy --env staging` |
| Production | PROD | `npx trigger.dev@latest deploy` |
| PR branches | PREVIEW | `npx trigger.dev@latest deploy --env preview` |

### GitHub Actions Workflows

**Production deployment** (on merge to `main`):

```yaml
# .github/workflows/deploy-trigger-prod.yml
name: Deploy Trigger.dev (prod)

on:
  push:
    branches: [main]
    paths:
      - 'trigger/**'
      - 'trigger.config.ts'
      - 'package.json'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20.x"
      - run: npm ci
      - name: Deploy Trigger.dev
        env:
          TRIGGER_ACCESS_TOKEN: ${{ secrets.TRIGGER_ACCESS_TOKEN }}
        run: npx trigger.dev@latest deploy
```

**Preview branch deployment** (on PR):

```yaml
# .github/workflows/deploy-trigger-preview.yml
name: Deploy Trigger.dev (preview)

on:
  pull_request:
    types: [opened, synchronize, reopened, closed]
    paths:
      - 'trigger/**'
      - 'trigger.config.ts'

jobs:
  deploy-preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "20.x"
      - run: npm ci
      - name: Deploy preview branch
        env:
          TRIGGER_ACCESS_TOKEN: ${{ secrets.TRIGGER_ACCESS_TOKEN }}
        run: npx trigger.dev@latest deploy --env preview
```

**Include `closed` in `pull_request.types`** — without it, preview branches won't be archived when PRs merge, and you'll hit the 20 active branch limit.

### PAT and Secret Management

1. Create a PAT at [cloud.trigger.dev/account/tokens](https://cloud.trigger.dev/account/tokens) (format: `tr_pat_*`)
2. Store in each service's Doppler project as `TRIGGER_ACCESS_TOKEN`
3. Inject into GitHub Actions via `${{ secrets.TRIGGER_ACCESS_TOKEN }}`

A single PAT works across all projects (it's user-scoped, not project-scoped). Use one PAT per CI system or per developer.

### Atomic Deploys (Coordinated Release)

When a FastAPI change depends on a new task version:

```bash
# Step 1: Deploy tasks without promoting
npx trigger.dev@latest deploy --skip-promotion
# Output: deploymentVersion=20250329.1

# Step 2: Deploy FastAPI to Railway with the version pinned
TRIGGER_VERSION=20250329.1 railway deploy

# Step 3: Promote the task version
npx trigger.dev@latest promote 20250329.1
```

### Version Pinning

Pin `trigger.dev` and `@trigger.dev/sdk` in `package.json`:

```json
{
  "devDependencies": {
    "trigger.dev": "4.4.3",
    "@trigger.dev/sdk": "4.4.3",
    "@trigger.dev/build": "4.4.3"
  },
  "scripts": {
    "trigger:dev": "trigger dev",
    "trigger:deploy": "trigger deploy",
    "trigger:deploy-staging": "trigger deploy --env staging"
  }
}
```

### Build Extensions per Service

| Service | Extensions Needed |
| :--- | :--- |
| **data-engine-x** | `syncEnvVars()` (from Doppler), possibly `pythonExtension()` if running Python scripts from tasks |
| **outbound-engine-x** | `syncEnvVars()` |
| **creative-engine-x** | `syncEnvVars()`, `ffmpeg()` for video processing, possibly `puppeteer()` for screenshot capture |
| **paid-engine-x** | `syncEnvVars()` |
| **chat-engine-x** | `syncEnvVars()` |
| **auth-engine-x** | `syncEnvVars()` |

### Doppler Env Var Sync

Use `syncEnvVars()` to pull secrets from Doppler at deploy time:

```typescript
// trigger.config.ts
import { defineConfig } from "@trigger.dev/sdk";
import { syncEnvVars } from "@trigger.dev/build/extensions/core";

export default defineConfig({
  project: "<project-ref>",
  dirs: ["./trigger"],
  build: {
    extensions: [
      syncEnvVars(async (ctx) => {
        // ctx.environment: "dev" | "staging" | "prod" | "preview"
        const dopplerConfig = ctx.environment === "prod" ? "prd" : ctx.environment;

        // Fetch secrets from Doppler CLI (available in CI)
        const { stdout } = await exec(
          `doppler secrets download --config ${dopplerConfig} --format json --no-file`
        );
        const secrets = JSON.parse(stdout);

        return Object.entries(secrets).map(([name, value]) => ({
          name,
          value: String(value),
        }));
      }),
    ],
  },
});
```

### Preview Branch Limits (Pro Plan)

- **20 active preview branches** per project (then $10/month per additional)
- Branches are auto-archived when PRs close (if `closed` type is in the workflow)
- Each preview branch has isolated versions, queues, schedules, and env vars

---

## 9. Observability and Monitoring

### Recommendation

Use a consistent tag strategy across all services. Use metadata for progress tracking on long-running tasks. Configure global `onFailure` for error alerting. Add OpenTelemetry instrumentations for AI calls.

### Tag Strategy

Apply these tags consistently on every trigger call:

| Tag | Format | Purpose |
| :--- | :--- | :--- |
| Service | `service:dex` | Identify which service triggered the run |
| Tenant | `tenant:{orgId}` | Filter runs by customer/org |
| Workflow | `workflow:{name}` | Group related runs (e.g., `workflow:lead-enrichment`) |
| Entity | `{entity}:{id}` | Link to domain object (e.g., `carrier:12345`, `campaign:abc`) |
| Source | `source:{service}` | For M2M: which service initiated the trigger |
| Correlation | `correlation:{uuid}` | Trace a workflow across multiple services |

**Limits**: Max 10 tags per run, each under 128 characters.

**Example trigger with tags:**

```typescript
await ingestFmcsa.trigger(
  { source: "fmcsa-api", dateRange: "2025-03-29" },
  {
    tags: [
      "service:dex",
      "workflow:fmcsa-ingestion",
      `date:2025-03-29`,
    ],
  }
);
```

### Metadata for Progress Tracking

Use `metadata.set()` for real-time progress visible in the dashboard:

```typescript
import { task, metadata, logger } from "@trigger.dev/sdk";

export const bulkIngestion = task({
  id: "dex:bulk-ingestion",
  run: async (payload: { records: unknown[]; source: string }) => {
    const total = payload.records.length;
    metadata.set("totalRecords", total);
    metadata.set("processedRecords", 0);
    metadata.set("status", "processing");

    for (let i = 0; i < total; i++) {
      await processRecord(payload.records[i]);

      // Update progress every 100 records
      if (i % 100 === 0) {
        metadata.set("processedRecords", i);
        metadata.set("progress", Math.round((i / total) * 100));
      }
    }

    metadata.set("processedRecords", total);
    metadata.set("progress", 100);
    metadata.set("status", "complete");

    return { processed: total };
  },
});
```

### Global `onFailure` Hook

Configure in `trigger.config.ts` for all-task error alerting:

```typescript
// trigger.config.ts
export default defineConfig({
  // ...
  onFailure: async ({ payload, error, ctx }) => {
    // Send to Slack
    await fetch(process.env.SLACK_WEBHOOK_URL!, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        text: [
          `*Task Failed*: \`${ctx.task.id}\``,
          `*Run*: ${ctx.run.id}`,
          `*Environment*: ${ctx.environment.type}`,
          `*Error*: ${error.message}`,
          `*Attempts*: ${ctx.attempt.number}`,
        ].join("\n"),
      }),
    });

    // Log structured error for downstream aggregation
    console.error(JSON.stringify({
      event: "task_failure",
      taskId: ctx.task.id,
      runId: ctx.run.id,
      environment: ctx.environment.type,
      error: error.message,
      attempts: ctx.attempt.number,
    }));
  },
});
```

### OpenTelemetry Instrumentations

Add instrumentations for key libraries used in tasks:

```typescript
// trigger.config.ts
import { PrismaInstrumentation } from "@prisma/instrumentation";

export default defineConfig({
  // ...
  telemetry: {
    instrumentations: [
      // Trace database queries (if using Prisma)
      new PrismaInstrumentation(),

      // Trace AI calls
      // new OpenAIInstrumentation(), // from @traceloop/instrumentation-openai
    ],
  },
});
```

**Recommended instrumentations by service:**

| Service | Instrumentations |
| :--- | :--- |
| data-engine-x | `@prisma/instrumentation` (DB queries), `@opentelemetry/instrumentation-http` |
| outbound-engine-x | `@opentelemetry/instrumentation-http` |
| creative-engine-x | `@opentelemetry/instrumentation-http` |
| paid-engine-x | `@opentelemetry/instrumentation-http` |
| chat-engine-x | `@traceloop/instrumentation-openai` (AI calls), `@opentelemetry/instrumentation-http` |

### Log Level Defaults

| Environment | Log Level | Rationale |
| :--- | :--- | :--- |
| DEV | `debug` | Full visibility during development |
| STAGING | `info` | Verbose enough for QA debugging |
| PROD | `warn` | Reduce noise; errors and warnings only |

Set in `trigger.config.ts`:

```typescript
logLevel: process.env.TRIGGER_LOG_LEVEL as any ?? "warn",
```

### Dashboard Filtering

With the tag strategy above, filter runs in the Trigger.dev dashboard by:
- **Service**: `service:dex` — see all data-engine-x runs
- **Tenant**: `tenant:acme-corp` — see all runs for a specific customer
- **Workflow**: `workflow:lead-enrichment` — trace a complete workflow
- **Correlation**: `correlation:{uuid}` — find all runs triggered by a single event

---

## 10. The `trigger.config.ts` Template

The complete, annotated template that any engine-x service can start from:

```typescript
// trigger.config.ts
import { defineConfig } from "@trigger.dev/sdk";
import { syncEnvVars } from "@trigger.dev/build/extensions/core";
// Uncomment as needed per service:
// import { ffmpeg } from "@trigger.dev/build/extensions/core";
// import { puppeteer } from "@trigger.dev/build/extensions/puppeteer";
// import { pythonExtension } from "@trigger.dev/build/extensions/python";
// import { PrismaInstrumentation } from "@prisma/instrumentation";

export default defineConfig({
  // ──────────────────────────────────────────────
  // PROJECT
  // ──────────────────────────────────────────────
  // Your project ref from the Trigger.dev dashboard.
  // Each engine-x service has its own project.
  project: "<project-ref>",

  // ──────────────────────────────────────────────
  // TASK DIRECTORIES
  // ──────────────────────────────────────────────
  // All task files live under ./trigger.
  // Subdirectories are scanned automatically.
  dirs: ["./trigger"],

  // ──────────────────────────────────────────────
  // RUNTIME
  // ──────────────────────────────────────────────
  // Options: "node" (21.7.3), "node-22" (22.16.0), "bun" (1.3.3, experimental)
  // Use "node" unless you need Node 22 features.
  runtime: "node",

  // ──────────────────────────────────────────────
  // LOGGING
  // ──────────────────────────────────────────────
  // Options: "debug", "info", "log", "warn", "error"
  // Override per environment via TRIGGER_LOG_LEVEL env var.
  logLevel: "warn",

  // ──────────────────────────────────────────────
  // DEFAULT MACHINE
  // ──────────────────────────────────────────────
  // Sets the default compute for all tasks in this project.
  // Override per-task with `machine: "large-1x"` on individual tasks.
  //
  // Presets:
  //   micro     = 0.25 vCPU / 0.25 GB
  //   small-1x  = 0.5  vCPU / 0.5  GB  (platform default)
  //   small-2x  = 1    vCPU / 1    GB
  //   medium-1x = 1    vCPU / 2    GB
  //   medium-2x = 2    vCPU / 4    GB
  //   large-1x  = 4    vCPU / 8    GB
  //   large-2x  = 8    vCPU / 16   GB
  defaultMachine: "small-1x",

  // ──────────────────────────────────────────────
  // MAX DURATION
  // ──────────────────────────────────────────────
  // Default wall-clock limit for all tasks (in seconds).
  // Override per-task with `maxDuration` on individual tasks.
  // Cloud-enforced maximum: 14 days.
  maxDuration: 300, // 5 minutes

  // ──────────────────────────────────────────────
  // RETRIES
  // ──────────────────────────────────────────────
  // Default retry config for all tasks.
  // Override per-task with `retry: { ... }` on individual tasks.
  retries: {
    enabledInDev: false, // Don't retry during local development
    default: {
      maxAttempts: 3,         // 1 initial attempt + 2 retries
      minTimeoutInMs: 1000,   // 1 second minimum backoff
      maxTimeoutInMs: 30_000, // 30 second maximum backoff
      factor: 2,              // Exponential: 1s → 2s → 4s
      randomize: true,        // Add jitter to prevent thundering herd
    },
  },

  // ──────────────────────────────────────────────
  // IGNORE PATTERNS
  // ──────────────────────────────────────────────
  // Exclude test files from task detection.
  ignorePatterns: ["**/*.test.ts", "**/*.spec.ts"],

  // ──────────────────────────────────────────────
  // BUILD
  // ──────────────────────────────────────────────
  build: {
    // Packages with native binaries that can't be bundled by esbuild.
    // Add any packages that cause "No loader is configured for .node files" errors.
    external: [],

    extensions: [
      // ── Doppler Env Var Sync ──
      // Pulls secrets from Doppler at deploy time.
      // Runs during `trigger deploy` only (not `trigger dev`).
      syncEnvVars(async (ctx) => {
        // ctx.environment: "dev" | "staging" | "prod" | "preview"
        // ctx.branch: string | undefined (preview branches only)
        //
        // Implement Doppler fetch here. Example:
        // const secrets = await fetchDopplerSecrets(ctx.environment);
        // return Object.entries(secrets).map(([name, value]) => ({ name, value }));
        return [];
      }),

      // ── Uncomment per service as needed ──
      // ffmpeg(),                    // creative-engine-x: video processing
      // puppeteer(),                 // creative-engine-x: screenshot capture
      // pythonExtension(),           // data-engine-x: Python script execution
    ],
  },

  // ──────────────────────────────────────────────
  // TELEMETRY (OpenTelemetry)
  // ──────────────────────────────────────────────
  telemetry: {
    instrumentations: [
      // Uncomment as needed:
      // new PrismaInstrumentation(),           // DB query tracing
      // new OpenAIInstrumentation(),           // AI call tracing
      // new HttpInstrumentation(),             // HTTP call tracing
    ],
  },

  // ──────────────────────────────────────────────
  // LIFECYCLE HOOKS
  // ──────────────────────────────────────────────

  // Runs when any task fails after all retries are exhausted.
  // Use for alerting (Slack, PagerDuty, etc.)
  onFailure: async ({ payload, error, ctx }) => {
    // Example: Send to Slack webhook
    if (process.env.SLACK_WEBHOOK_URL) {
      await fetch(process.env.SLACK_WEBHOOK_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          text: [
            `*Task Failed*: \`${ctx.task.id}\``,
            `*Run*: ${ctx.run.id}`,
            `*Environment*: ${ctx.environment.type}`,
            `*Error*: ${error.message}`,
          ].join("\n"),
        }),
      });
    }
  },

  // Uncomment if you need global init (runs before each task):
  // init: async ({ payload, ctx }) => {
  //   // Initialize shared resources (DB connections, etc.)
  // },

  // Uncomment if you need global success handler:
  // onSuccess: async ({ payload, output, ctx }) => {
  //   // Log success metrics
  // },
});
```

### Service-Specific Overrides

Copy the template above and apply these overrides per service:

**data-engine-x (`engine-x-dex`):**
```typescript
defaultMachine: "small-2x",    // Data processing needs more memory
maxDuration: 600,              // 10 min — ingestion can be slow
// build.extensions: add pythonExtension() if running Python
```

**outbound-engine-x (`engine-x-oex`):**
```typescript
defaultMachine: "small-1x",    // API calls are lightweight
maxDuration: 300,              // 5 min default
```

**creative-engine-x (`engine-x-cex`):**
```typescript
defaultMachine: "medium-2x",   // Rendering needs CPU + memory
maxDuration: 900,              // 15 min — video renders take time
// build.extensions: add ffmpeg(), possibly puppeteer()
```

**paid-engine-x (`engine-x-pex`):**
```typescript
defaultMachine: "small-1x",    // API syncs are lightweight
maxDuration: 300,              // 5 min default
```

**chat-engine-x (`engine-x-chex`):**
```typescript
defaultMachine: "medium-1x",   // AI chat needs moderate memory
maxDuration: 600,              // 10 min — long conversations
// telemetry.instrumentations: add OpenAI instrumentation
```

**auth-engine-x (`engine-x-aex`):**
```typescript
defaultMachine: "micro",       // Key rotation is lightweight
maxDuration: 120,              // 2 min — simple operations
```

---

## Quick Reference

### Pro Plan Limits

| Resource | Limit |
| :--- | :--- |
| Projects per org | 10 |
| Concurrent runs | 100+ (expandable) |
| Schedules per project | 1,000+ ($10/mo per additional 1,000) |
| Active preview branches | 20 per project ($10/mo per additional) |
| Queue depth (prod) | 1,000,000 per queue |
| Queue depth (dev) | 5,000 per queue |
| Batch trigger size | 1,000 items per call |
| Tags per run | 10 (each < 128 chars) |
| API rate limit | 1,500 req/min |
| Log retention | 30 days |
| Max run TTL (Cloud) | 14 days |

### Key Formats

| Item | Format | Example |
| :--- | :--- | :--- |
| Task ID | `{service}:{domain}-{action}` | `dex:ingest-fmcsa` |
| Queue name | `{service}:{category}-{provider}` | `oex:api-twilio-sms` |
| Doppler cross-service key | `{TARGET}_TRIGGER_SECRET_KEY` | `DEX_TRIGGER_SECRET_KEY` |
| Idempotency key | `{action}-{id}-{version}` | `enrich-company_123-v2` |
| Tag | `{namespace}:{value}` | `service:dex`, `tenant:acme` |
| TTL | Duration string or seconds | `"1h"`, `"30m"`, `3600` |
| Priority | Time offset in seconds | `3600` = dequeue before any unprioritized run from the last hour |
| Secret key prefix | Environment-scoped | `tr_dev_*`, `tr_stg_*`, `tr_prod_*`, `tr_preview_*` |
| PAT prefix | User-scoped | `tr_pat_*` |

### Import Checklist

```typescript
// Always import from @trigger.dev/sdk (never @trigger.dev/sdk/v3)
import {
  task,              // Define a task
  schemaTask,        // Define a task with Zod schema validation
  queue,             // Define a custom queue
  schedules,         // Declarative + imperative schedules
  configure,         // Configure SDK (secret key, etc.)
  tasks,             // Trigger tasks by ID string (M2M)
  runs,              // Query run status
  queues,            // Queue management API
  wait,              // Duration/date waits, waitpoint tokens
  retry,             // retry.fetch(), retry.onThrow()
  logger,            // Structured logging
  metadata,          // Run metadata KV store
  tags,              // Manage run tags
  batch,             // Batch operations
  AbortTaskRunError, // Throw to skip all retries
  defineConfig,      // trigger.config.ts
} from "@trigger.dev/sdk";

// Build extensions
import { syncEnvVars, ffmpeg, aptGet } from "@trigger.dev/build/extensions/core";
import { puppeteer } from "@trigger.dev/build/extensions/puppeteer";
import { pythonExtension } from "@trigger.dev/build/extensions/python";
```

### Cross-Reference to Canonical Docs

For deep dives on any topic, refer to the canonical reference docs in this repo:

| Topic | File |
| :--- | :--- |
| Architecture, SDK, auth, limits | `canonical-reference/TRIGGER_DEV_MASTER.md` |
| Task definition, lifecycle, triggering | `canonical-reference/TRIGGER_DEV_TASKS.md` |
| Queues, concurrency, slots | `canonical-reference/TRIGGER_DEV_QUEUES_CONCURRENCY.md` |
| Production patterns (fan-out, pipeline, M2M) | `canonical-reference/TRIGGER_DEV_PATTERNS.md` |
| When to use what | `canonical-reference/TRIGGER_DEV_DECISION_TREE.md` |
| Retry, catchError, OOM | `canonical-reference/TRIGGER_DEV_ERRORS_RETRIES.md` |
| Deployment, CI/CD, preview branches | `canonical-reference/TRIGGER_DEV_DEPLOYMENT.md` |
| Realtime streaming | `canonical-reference/TRIGGER_DEV_STREAMS.md` |
| Wait patterns, tokens | `canonical-reference/TRIGGER_DEV_WAITS_TOKENS.md` |
| Full config options | `llm-full-extraction/CONFIG.md` |
| Plan limits | `llm-full-extraction/LIMITS.md` |
| Machine presets | `llm-full-extraction/MACHINES.md` |
