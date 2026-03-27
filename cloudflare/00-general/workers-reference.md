# Cloudflare Workers API Reference

**Complete API reference for Cloudflare Workers — edge compute for form handling, redirects, A/B testing, and dynamic content at the edge**

Workers run JavaScript/TypeScript/Python at Cloudflare's edge (300+ locations). For a multi-tenant platform, Workers handle request routing, form processing, header injection, analytics, A/B testing, and any server-side logic that runs before the static landing page is served.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Worker Scripts](#2-worker-scripts)
3. [Script Upload & Deployment](#3-script-upload--deployment)
4. [Routes](#4-routes)
5. [Custom Domains](#5-custom-domains)
6. [Secrets](#6-secrets)
7. [Cron Triggers (Scheduled)](#7-cron-triggers-scheduled)
8. [Versions & Gradual Rollouts](#8-versions--gradual-rollouts)
9. [Workers for Platforms](#9-workers-for-platforms)
10. [Account Settings & Subdomain](#10-account-settings--subdomain)
11. [Tail Logs](#11-tail-logs)
12. [Smart Placement](#12-smart-placement)

---

## 1. Architecture Overview

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Script** | A JavaScript/TypeScript/Python program that runs on Cloudflare's edge. Identified by `script_name`. |
| **Route** | A URL pattern (e.g., `example.com/api/*`) that maps incoming requests to a Worker script. Zone-scoped. |
| **Custom Domain** | A hostname attached directly to a Worker (alternative to routes). Account-scoped. |
| **Binding** | A connection between a Worker and a Cloudflare service (KV, R2, D1, Durable Objects, etc.). |
| **Module Syntax** | Modern Worker format using ES modules (`export default { fetch() {} }`). Recommended. |
| **Service Worker Syntax** | Legacy format using `addEventListener('fetch', ...)`. Still supported. |
| **Version** | An immutable snapshot of a Worker's code and config. Deployments reference versions. |
| **Deployment** | Configures which version(s) serve traffic, including percentage-based gradual rollouts. |

### Workers vs Pages Functions

| Aspect | Workers | Pages Functions |
|--------|---------|-----------------|
| Deployment | Standalone script upload | Part of a Pages deployment (`_worker.js`) |
| Routing | Route patterns or custom domains | Automatic file-based routing |
| Use case | General-purpose edge compute | Server-side logic for a Pages site |
| Management | Full API control | Deployed with Pages assets |

For a multi-tenant platform, you'll likely use both: Pages for static hosting, Workers for shared edge logic (routing, form handling, analytics).

---

## 2. Worker Scripts

### List Workers

```
GET /accounts/{account_id}/workers/scripts
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `account_id` | string | path | **Required** |
| `tags` | string | query | Filter by tags. Format: `tag1:value1,tag2:value2` |

### Search Workers

```
GET /accounts/{account_id}/workers/scripts-search
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `name` | string | query | Filter by script name |
| `id` | string | query | Filter by script ID |
| `order_by` | string | query | Sort field |
| `page` | integer | query | Page number |
| `per_page` | integer | query | Results per page |

### Get Worker (Download Script)

```
GET /accounts/{account_id}/workers/scripts/{script_name}
```

Returns the raw script content as multipart form data.

### Get Script Content Only

```
GET /accounts/{account_id}/workers/scripts/{script_name}/content/v2
```

Returns only the script content without metadata.

### Get Script Settings

```
GET /accounts/{account_id}/workers/scripts/{script_name}/settings
```

Returns metadata and configuration including bindings, usage model, and compatibility settings.

### Delete Worker

```
DELETE /accounts/{account_id}/workers/scripts/{script_name}
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `force` | boolean | query | If `true`, bypasses checks for active bindings or Durable Objects |

---

## 3. Script Upload & Deployment

### Upload Worker Module (Primary Deploy Method)

```
PUT /accounts/{account_id}/workers/scripts/{script_name}
```

**Content-Type:** `multipart/form-data`

This is the primary method for deploying a Worker. The script and its metadata are uploaded as a multipart form.

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `account_id` | string | path | **Required** |
| `script_name` | string | path | **Required** — becomes the Worker's identifier |
| `bindings_inherit` | string | query | Set to `"strict"` to fail if inherited bindings can't be resolved |

**Metadata object** (sent as the `metadata` part):

| Field | Type | Description |
|-------|------|-------------|
| `main_module` | string | Entry point file name for module syntax (e.g., `"index.js"`) |
| `body_part` | string | Entry point for service worker syntax |
| `compatibility_date` | string | Target date for Workers runtime behavior (e.g., `"2024-01-01"`) |
| `compatibility_flags` | array | Feature flags (e.g., `["nodejs_compat"]`) |
| `bindings` | array | Service bindings (see Bindings table below) |
| `usage_model` | string | `"standard"`, `"bundled"`, or `"unbound"` |
| `logpush` | boolean | Enable Logpush for this Worker |
| `placement` | object | Smart Placement config: `{ "mode": "smart" }` |
| `migrations` | object | Durable Object migrations |
| `tags` | array | String tags for organization |
| `tail_consumers` | array | Workers that receive tail logs from this Worker |
| `observability` | object | `{ "enabled": true, "head_sampling_rate": 1.0 }` |
| `limits` | object | `{ "cpu_ms": 50 }` — CPU time limit |
| `assets` | object | Static asset config for Worker Sites |
| `keep_bindings` | array | Binding types to preserve from previous version |

### Binding Types

| Type | Key Fields | Description |
|------|-----------|-------------|
| `kv_namespace` | `namespace_id` | KV store access |
| `r2_bucket` | `bucket_name`, `jurisdiction?` | R2 object storage |
| `d1` | `id` | D1 SQLite database |
| `durable_object_namespace` | `class_name`, `script_name?`, `environment?` | Durable Objects |
| `service` | `service`, `environment?` | Service-to-service binding |
| `queue` | `queue_name` | Queue producer |
| `hyperdrive` | `id` | Database connection pooling |
| `vectorize` | `index_name` | Vector database |
| `ai` | — | Workers AI inference |
| `analytics_engine` | `dataset` | Analytics Engine |
| `browser` | — | Browser rendering |
| `secret_text` | `text` | Secret value (encrypted) |
| `plain_text` | `text` | Non-secret text value |
| `json` | — | JSON value |
| `dispatch_namespace` | `namespace`, `outbound?` | Workers for Platforms dispatch |
| `mtls_certificate` | `certificate_id` | mTLS client certificate |
| `send_email` | `destination_address?` | Email sending |
| `assets` | — | Static assets |
| `secret_key` | `algorithm`, `format`, `usages`, `key_base64?` | Cryptographic key |
| `pipelines` | `pipeline` | Pipelines binding |
| `workflow` | `class_name`, `script_name?` | Workflow binding |

**Python SDK — Upload Worker:**
```python
import io

worker_code = """
export default {
    async fetch(request, env, ctx) {
        const url = new URL(request.url);

        // Form submission handling
        if (request.method === 'POST' && url.pathname === '/submit') {
            const formData = await request.formData();
            // Process form...
            return new Response(JSON.stringify({ success: true }), {
                headers: { 'Content-Type': 'application/json' }
            });
        }

        // Pass through to origin
        return fetch(request);
    }
}
"""

result = client.workers.scripts.update(
    script_name="tenant-form-handler",
    account_id="my-account-id",
    metadata={
        "main_module": "index.js",
        "compatibility_date": "2024-01-01",
        "bindings": [
            {
                "type": "kv_namespace",
                "name": "TENANT_CONFIG",
                "namespace_id": "kv-namespace-id"
            }
        ]
    },
    files=[("index.js", io.BytesIO(worker_code.encode()), "application/javascript+module")]
)
```

**TypeScript SDK — Upload Worker:**
```typescript
const result = await client.workers.scripts.update('tenant-form-handler', {
  account_id: 'my-account-id',
  metadata: {
    main_module: 'index.js',
    compatibility_date: '2024-01-01',
    bindings: [
      {
        type: 'kv_namespace',
        name: 'TENANT_CONFIG',
        namespace_id: 'kv-namespace-id',
      },
    ],
  },
  // files: [new File([workerCode], 'index.js', { type: 'application/javascript+module' })]
});
```

### Put Script Content (Code Only)

```
PUT /accounts/{account_id}/workers/scripts/{script_name}/content
```

Updates only the script code without modifying configuration/metadata. Uses headers to specify entry points:

| Header | Description |
|--------|-------------|
| `CF-WORKER-BODY-PART` | Service worker syntax entry point |
| `CF-WORKER-MAIN-MODULE-PART` | Module syntax entry point |

### Patch Script Settings (Config Only)

```
PATCH /accounts/{account_id}/workers/scripts/{script_name}/settings
```

Updates only the metadata/configuration without re-uploading code. Useful for changing bindings or usage model.

---

## 4. Routes

Routes map URL patterns to Worker scripts. They are zone-scoped (attached to a specific domain).

### Create Route

```
POST /zones/{zone_id}/workers/routes
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `pattern` | string | **Yes** | URL pattern (e.g., `example.com/api/*`, `*.example.com/form`) |
| `script` | string | No | Worker script name. Omit to disable the route (requests pass through). |

**Pattern syntax:**
- `example.com/*` — matches all paths on the domain
- `example.com/api/*` — matches paths starting with `/api/`
- `*.example.com/*` — matches all subdomains
- `example.com/exact-path` — matches exactly one path

**Python SDK:**
```python
route = client.workers.routes.create(
    zone_id="my-zone-id",
    pattern="*.tenant-domain.com/submit*",
    script="tenant-form-handler"
)
```

### List Routes

```
GET /zones/{zone_id}/workers/routes
```

### Update Route

```
PUT /zones/{zone_id}/workers/routes/{route_id}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `pattern` | string | **Yes** | Updated URL pattern |
| `script` | string | No | Updated Worker script name |

### Delete Route

```
DELETE /zones/{zone_id}/workers/routes/{route_id}
```

### Get Route

```
GET /zones/{zone_id}/workers/routes/{route_id}
```

---

## 5. Custom Domains

An alternative to routes — attach a hostname directly to a Worker at the account level.

### Attach Custom Domain

```
PUT /accounts/{account_id}/workers/domains
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `hostname` | string | **Yes** | The domain (e.g., `api.example.com`) |
| `service` | string | **Yes** | Worker script name |
| `zone_id` | string | **Yes** | Zone ID the hostname belongs to |
| `environment` | string | No | Worker environment (default: production) |

### List Custom Domains

```
GET /accounts/{account_id}/workers/domains
```

Filterable by `hostname`, `service`, `zone_id`, `zone_name`, `environment`.

### Delete Custom Domain

```
DELETE /accounts/{account_id}/workers/domains/{domain_id}
```

### Get Custom Domain

```
GET /accounts/{account_id}/workers/domains/{domain_id}
```

---

## 6. Secrets

Worker secrets are encrypted values accessible via `env.SECRET_NAME` in the Worker code. They are never returned in API responses.

### Add/Update Secret

```
PUT /accounts/{account_id}/workers/scripts/{script_name}/secrets
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | **Yes** | Secret name (becomes the binding name) |
| `text` | string | **Yes** | Secret value |
| `type` | string | **Yes** | `"secret_text"` |

### List Secrets

```
GET /accounts/{account_id}/workers/scripts/{script_name}/secrets
```

Returns secret names and types only — values are never exposed.

### Get Secret

```
GET /accounts/{account_id}/workers/scripts/{script_name}/secrets/{secret_name}
```

Returns metadata only, not the secret value.

### Delete Secret

```
DELETE /accounts/{account_id}/workers/scripts/{script_name}/secrets/{secret_name}
```

---

## 7. Cron Triggers (Scheduled)

Run Workers on a schedule (e.g., daily cache warming, periodic cleanup).

### Get Cron Triggers

```
GET /accounts/{account_id}/workers/scripts/{script_name}/schedules
```

### Update Cron Triggers

```
PUT /accounts/{account_id}/workers/scripts/{script_name}/schedules
```

**Request body:** Array of schedule objects (cron expressions).

```python
client.workers.scripts.schedules.update(
    script_name="daily-cleanup",
    account_id="my-account-id",
    body=[
        {"cron": "0 0 * * *"},    # Every day at midnight
        {"cron": "*/15 * * * *"}  # Every 15 minutes
    ]
)
```

---

## 8. Versions & Gradual Rollouts

Workers support immutable versions and percentage-based traffic splitting for gradual rollouts.

### Upload Version (Without Deploying)

```
POST /accounts/{account_id}/workers/scripts/{script_name}/versions
```

Creates a new version without immediately serving traffic.

### List Versions

```
GET /accounts/{account_id}/workers/scripts/{script_name}/versions
```

First result is the latest version.

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `deployable` | boolean | query | Filter to deployable versions only |
| `page` | integer | query | Page number |
| `per_page` | integer | query | Results per page |

### Get Version Detail

```
GET /accounts/{account_id}/workers/scripts/{script_name}/versions/{version_id}
```

### Create Deployment (Traffic Split)

```
POST /accounts/{account_id}/workers/scripts/{script_name}/deployments
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `strategy` | string | **Yes** | `"percentage"` |
| `versions` | array | **Yes** | Version objects with `version_id` and `percentage` (must sum to 100) |
| `force` | boolean | No | Bypass rolling-back restrictions |
| `annotations` | object | No | Metadata (message, author_email) |

**Example — Canary deployment:**
```python
client.workers.scripts.deployments.create(
    script_name="tenant-form-handler",
    account_id="my-account-id",
    strategy="percentage",
    versions=[
        {"version_id": "old-version-id", "percentage": 90},
        {"version_id": "new-version-id", "percentage": 10},
    ]
)
```

### List Deployments

```
GET /accounts/{account_id}/workers/scripts/{script_name}/deployments
```

First result is the active deployment.

---

## 9. Workers for Platforms

Workers for Platforms allows you to run customer/tenant Worker scripts in isolated dispatch namespaces. This is the enterprise multi-tenant pattern for per-tenant edge logic.

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Dispatch Namespace** | An isolated container for tenant Worker scripts |
| **Dispatch Worker** | Your main Worker that receives requests and dispatches to tenant scripts |
| **User Worker** | A tenant's script running inside the namespace |

### Namespace Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST /accounts/{account_id}/workers/dispatch/namespaces` | POST | Create namespace |
| `GET /accounts/{account_id}/workers/dispatch/namespaces` | GET | List namespaces |
| `GET /accounts/{account_id}/workers/dispatch/namespaces/{namespace}` | GET | Get namespace |
| `PATCH /accounts/{account_id}/workers/dispatch/namespaces/{namespace}` | PATCH | Update namespace |
| `DELETE /accounts/{account_id}/workers/dispatch/namespaces/{namespace}` | DELETE | Delete namespace |

### Script Operations (within a namespace)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `PUT .../namespaces/{ns}/scripts/{name}` | PUT | Upload script to namespace |
| `GET .../namespaces/{ns}/scripts` | GET | List scripts in namespace |
| `GET .../namespaces/{ns}/scripts/{name}` | GET | Get script details |
| `DELETE .../namespaces/{ns}/scripts/{name}` | DELETE | Delete script |
| `DELETE .../namespaces/{ns}/scripts` | DELETE | Bulk delete (with tag filter) |
| `PUT .../namespaces/{ns}/scripts/{name}/content` | PUT | Update script content |
| `GET .../namespaces/{ns}/scripts/{name}/content` | GET | Get script content |
| `GET .../namespaces/{ns}/scripts/{name}/settings` | GET | Get script settings |
| `PATCH .../namespaces/{ns}/scripts/{name}/settings` | PATCH | Update script settings |
| `GET .../namespaces/{ns}/scripts/{name}/bindings` | GET | Get script bindings |
| `GET .../namespaces/{ns}/scripts/{name}/secrets` | GET | List secrets |
| `PUT .../namespaces/{ns}/scripts/{name}/secrets` | PUT | Add secret |
| `DELETE .../namespaces/{ns}/scripts/{name}/secrets/{secret}` | DELETE | Delete secret |
| `GET .../namespaces/{ns}/scripts/{name}/tags` | GET | Get tags |
| `PUT .../namespaces/{ns}/scripts/{name}/tags` | PUT | Set tags |
| `DELETE .../namespaces/{ns}/scripts/{name}/tags/{tag}` | DELETE | Delete tag |

### Bulk Delete with Tag Filter

```
DELETE /accounts/{account_id}/workers/dispatch/namespaces/{namespace}/scripts
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `tags` | string | query | Filter by tags |
| `limit` | integer | query | Max scripts to delete |

Returns: `{ "deleted": [...], "deleted_count": N, "has_more": bool }`

---

## 10. Account Settings & Subdomain

### Workers Subdomain

Every account gets a `*.workers.dev` subdomain. Workers can be served at `{script-name}.{subdomain}.workers.dev`.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `PUT /accounts/{account_id}/workers/subdomain` | PUT | Create subdomain (body: `{ "subdomain": "my-company" }`) |
| `GET /accounts/{account_id}/workers/subdomain` | GET | Get current subdomain |
| `DELETE /accounts/{account_id}/workers/subdomain` | DELETE | Delete subdomain |

### Per-Script Subdomain Toggle

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST /accounts/{account_id}/workers/scripts/{name}/subdomain` | POST | Enable/disable (body: `{ "enabled": true }`) |
| `GET /accounts/{account_id}/workers/scripts/{name}/subdomain` | GET | Get status |
| `DELETE /accounts/{account_id}/workers/scripts/{name}/subdomain` | DELETE | Disable |

### Account Settings

```
GET /accounts/{account_id}/workers/account-settings
PUT /accounts/{account_id}/workers/account-settings
```

| Field | Type | Description |
|-------|------|-------------|
| `default_usage_model` | string | Default for new Workers: `"standard"`, `"bundled"`, `"unbound"` |
| `green_compute` | boolean | Enable green compute (route to renewable energy data centers) |

---

## 11. Tail Logs

Real-time log streaming from a running Worker.

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST /accounts/{account_id}/workers/scripts/{name}/tails` | POST | Start tail (returns WebSocket URL) |
| `GET /accounts/{account_id}/workers/scripts/{name}/tails` | GET | List active tails |
| `DELETE /accounts/{account_id}/workers/scripts/{name}/tails/{id}` | DELETE | Stop tail |

---

## 12. Smart Placement

Smart Placement automatically runs your Worker close to your backend services (rather than close to the user) when that would reduce total latency.

### List Available Regions

```
GET /accounts/{account_id}/workers/placement/regions
```

Enable via the `placement` field in script metadata:

```json
{ "placement": { "mode": "smart" } }
```
