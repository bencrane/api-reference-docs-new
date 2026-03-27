# Cloudflare Tier 2 Services API Reference

**Key endpoints and schemas for R2, KV, Cache, Turnstile, Rulesets, Load Balancers, and Images**

These services complement the core hosting stack. R2 and KV provide storage at the edge, Turnstile protects forms from bots, Rulesets control URL rewrites and redirects, and Images handles image optimization.

---

## Table of Contents

1. [R2 Object Storage](#1-r2-object-storage)
2. [Workers KV](#2-workers-kv)
3. [Cache Settings](#3-cache-settings)
4. [Turnstile (Bot Protection)](#4-turnstile-bot-protection)
5. [Rulesets (URL Rewrites, Redirects, Transform Rules)](#5-rulesets)
6. [Load Balancers](#6-load-balancers)
7. [Cloudflare Images](#7-cloudflare-images)

---

## 1. R2 Object Storage

R2 is S3-compatible object storage with zero egress fees. Useful for storing landing page assets (images, PDFs, generated files), tenant uploads, or build artifacts.

### Bucket Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST /accounts/{account_id}/r2/buckets` | POST | Create bucket |
| `GET /accounts/{account_id}/r2/buckets` | GET | List buckets |
| `GET /accounts/{account_id}/r2/buckets/{bucket_name}` | GET | Get bucket details |
| `PATCH /accounts/{account_id}/r2/buckets/{bucket_name}` | PATCH | Update bucket properties |
| `DELETE /accounts/{account_id}/r2/buckets/{bucket_name}` | DELETE | Delete bucket |

**Create Bucket:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | **Yes** | Bucket name |
| `locationHint` | string | No | Preferred region: `apac`, `eeur`, `enam`, `weur`, `wnam`, `oc` |
| `storageClass` | string | No | `"Standard"` or `"InfrequentAccess"` |

All R2 endpoints accept an optional `cf-r2-jurisdiction` header for data residency.

**Python SDK:**
```python
bucket = client.r2.buckets.create(
    account_id="my-account-id",
    name="tenant-assets",
    location_hint="enam",
)
```

### Custom Domains for R2

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST .../buckets/{name}/domains/custom` | POST | Add custom domain |
| `GET .../buckets/{name}/domains/custom` | GET | List custom domains |
| `GET .../buckets/{name}/domains/custom/{domain}` | GET | Get domain config |
| `PUT .../buckets/{name}/domains/custom/{domain}` | PUT | Edit domain config |
| `DELETE .../buckets/{name}/domains/custom/{domain}` | DELETE | Remove custom domain |

### R2 Public Access (r2.dev)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET .../buckets/{name}/domains/managed` | GET | Get r2.dev access status |
| `PUT .../buckets/{name}/domains/managed` | PUT | Enable/disable r2.dev access |

### CORS, Lifecycle, Lock

| Feature | GET | PUT/SET | DELETE |
|---------|-----|---------|--------|
| CORS Policy | `GET .../cors` | `PUT .../cors` | `DELETE .../cors` |
| Lifecycle Rules | `GET .../lifecycle` | `PUT .../lifecycle` | — |
| Lock Rules | `GET .../lock` | `PUT .../lock` | — |

### Temporary Access Credentials

```
POST /accounts/{account_id}/r2/temp-access-credentials
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `bucket` | string | **Yes** | Bucket name |
| `parentAccessKeyId` | string | **Yes** | Parent API token key ID |
| `permission` | string | **Yes** | `"admin-read-write"`, `"admin-read-only"`, `"object-read-write"`, `"object-read-only"` |
| `ttlSeconds` | integer | **Yes** | Credential lifetime |
| `objects` | array | No | Restrict to specific objects |
| `prefixes` | array | No | Restrict to specific prefixes |

### Sippy (Incremental Migration from S3/GCS)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET .../buckets/{name}/sippy` | GET | Get Sippy config |
| `PUT .../buckets/{name}/sippy` | PUT | Configure Sippy |
| `DELETE .../buckets/{name}/sippy` | DELETE | Disable Sippy |

### Event Notifications

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET .../event_notifications/r2/{bucket}/configuration` | GET | List all notification rules |
| `PUT .../event_notifications/r2/{bucket}/configuration/queues/{queue_id}` | PUT | Create notification rule |
| `GET .../event_notifications/r2/{bucket}/configuration/queues/{queue_id}` | GET | Get notification rule |
| `DELETE .../event_notifications/r2/{bucket}/configuration/queues/{queue_id}` | DELETE | Delete notification rule |

### Account Metrics

```
GET /accounts/{account_id}/r2/metrics
```

Returns storage and object count metrics across all buckets.

---

## 2. Workers KV

KV is a globally distributed key-value store. Use it for tenant configuration, edge-side routing tables, feature flags, or cached content.

### Namespace Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST /accounts/{account_id}/storage/kv/namespaces` | POST | Create namespace (body: `{ "title": "my-ns" }`) |
| `GET /accounts/{account_id}/storage/kv/namespaces` | GET | List namespaces |
| `GET .../namespaces/{namespace_id}` | GET | Get namespace |
| `PUT .../namespaces/{namespace_id}` | PUT | Rename namespace (body: `{ "title": "new-name" }`) |
| `DELETE .../namespaces/{namespace_id}` | DELETE | Delete namespace |

### Key-Value Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `PUT .../namespaces/{ns_id}/values/{key}` | PUT | Write a value (body = value, optional metadata via multipart) |
| `GET .../namespaces/{ns_id}/values/{key}` | GET | Read a value |
| `DELETE .../namespaces/{ns_id}/values/{key}` | DELETE | Delete a value |
| `GET .../namespaces/{ns_id}/metadata/{key}` | GET | Get metadata for a key |
| `GET .../namespaces/{ns_id}/keys` | GET | List keys (with optional `prefix`, `cursor`, `limit`) |

**Write with expiration:**

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `expiration` | integer | query | Unix timestamp when the key expires |
| `expiration_ttl` | integer | query | Seconds until the key expires (min 60) |

### Bulk Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `PUT .../namespaces/{ns_id}/bulk` | PUT | Write up to 10,000 key-value pairs (max 100MB total) |
| `POST .../namespaces/{ns_id}/bulk/delete` | POST | Delete up to 10,000 keys |
| `POST .../namespaces/{ns_id}/bulk/get` | POST | Read up to 100 keys at once |

**Bulk write format:**
```json
[
  { "key": "tenant-123:config", "value": "{\"theme\":\"blue\"}", "expiration_ttl": 86400 },
  { "key": "tenant-456:config", "value": "{\"theme\":\"red\"}" }
]
```

**Python SDK:**
```python
# Create namespace
ns = client.kv.namespaces.create(
    account_id="my-account-id",
    title="tenant-configs",
)

# Write a value
client.kv.namespaces.values.update(
    namespace_id=ns.id,
    key_name="tenant-123",
    account_id="my-account-id",
    value='{"theme": "blue", "logo": "https://r2.example.com/logos/123.png"}',
)

# Read a value
value = client.kv.namespaces.values.get(
    namespace_id=ns.id,
    key_name="tenant-123",
    account_id="my-account-id",
)
```

---

## 3. Cache Settings

### Zone Cache Settings

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET /zones/{zone_id}/cache/cache_reserve` | GET | Get Cache Reserve status |
| `PATCH /zones/{zone_id}/cache/cache_reserve` | PATCH | Enable/disable Cache Reserve (`"on"` / `"off"`) |
| `GET /zones/{zone_id}/cache/cache_reserve_clear` | GET | Get Cache Reserve clear status |
| `POST /zones/{zone_id}/cache/cache_reserve_clear` | POST | Start Cache Reserve clear (must disable first) |
| `GET /zones/{zone_id}/cache/regional_tiered_cache` | GET | Get Regional Tiered Cache status |
| `PATCH /zones/{zone_id}/cache/regional_tiered_cache` | PATCH | Enable/disable Regional Tiered Cache |
| `GET /zones/{zone_id}/cache/variants` | GET | Get image cache variants |
| `PATCH /zones/{zone_id}/cache/variants` | PATCH | Set image cache variants |
| `DELETE /zones/{zone_id}/cache/variants` | DELETE | Delete image cache variants |

**Cache Reserve** stores all cacheable content in persistent R2 storage, extending cache lifetimes. Requires a subscription.

**Regional Tiered Cache** routes requests through a regional hub before hitting the upper tier, improving cache hit rates.

**Variants** enable caching different image formats (WebP, AVIF) based on the `Accept` header, for file types like JPEG, PNG, GIF, BMP, TIFF.

---

## 4. Turnstile (Bot Protection)

Turnstile is Cloudflare's CAPTCHA alternative for protecting forms. Provides a site key for the frontend widget and a secret key for backend verification.

### Create Widget

```
POST /accounts/{account_id}/challenges/widgets
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | **Yes** | Widget name |
| `domains` | array | **Yes** | Domains where the widget is allowed |
| `mode` | string | **Yes** | `"managed"` (visible if needed), `"non-interactive"` (invisible challenge), `"invisible"` (fully invisible) |
| `bot_fight_mode` | boolean | No | Enable bot fight mode |
| `clearance_level` | string | No | `"no_clearance"`, `"jschallenge"`, `"managed"`, `"interactive"` |
| `region` | string | No | `"world"` or `"china"` |
| `offlabel` | boolean | No | Allow usage outside listed domains |
| `ephemeral_id` | boolean | No | Ephemeral identification |

**Python SDK:**
```python
widget = client.challenges.widgets.create(
    account_id="my-account-id",
    name="Landing Page Form Protection",
    domains=["www.tenant.com", "landing.yourplatform.com"],
    mode="managed",
)
print(widget.sitekey)   # Use in frontend widget
# Secret key is returned only on creation — store it securely
```

### Other Widget Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET /accounts/{account_id}/challenges/widgets` | GET | List widgets |
| `GET .../widgets/{sitekey}` | GET | Get widget details |
| `PUT .../widgets/{sitekey}` | PUT | Update widget config |
| `DELETE .../widgets/{sitekey}` | DELETE | Delete widget |
| `POST .../widgets/{sitekey}/rotate_secret` | POST | Rotate secret key (optional 2-hour grace period) |

---

## 5. Rulesets

Rulesets control URL redirects, rewrites, header transforms, rate limiting, and WAF behavior. Available at both zone and account levels.

### Key Phases for Multi-Tenant Hosting

| Phase | Purpose |
|-------|---------|
| `http_request_dynamic_redirect` | URL redirects (e.g., redirect old tenant URLs) |
| `http_request_transform` | URL rewrites and request header modifications |
| `http_response_headers_transform` | Response header modifications |
| `http_request_late_transform` | Late-stage request modifications |
| `http_request_redirect` | Static redirects |
| `http_request_cache_settings` | Per-request cache settings |
| `http_request_firewall_custom` | Custom WAF rules |
| `http_ratelimit` | Rate limiting |
| `http_config_settings` | Configuration overrides |

### Zone-Level Ruleset Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET /zones/{zone_id}/rulesets` | GET | List all zone rulesets |
| `POST /zones/{zone_id}/rulesets` | POST | Create zone ruleset |
| `GET /zones/{zone_id}/rulesets/{id}` | GET | Get ruleset |
| `PUT /zones/{zone_id}/rulesets/{id}` | PUT | Update ruleset (creates new version) |
| `DELETE /zones/{zone_id}/rulesets/{id}` | DELETE | Delete ruleset |
| `POST /zones/{zone_id}/rulesets/{id}/rules` | POST | Add rule to ruleset |
| `PATCH /zones/{zone_id}/rulesets/{id}/rules/{rule_id}` | PATCH | Update a rule |
| `DELETE /zones/{zone_id}/rulesets/{id}/rules/{rule_id}` | DELETE | Delete a rule |

### Entry Point Rulesets (Phase-Level)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET /zones/{zone_id}/rulesets/phases/{phase}/entrypoint` | GET | Get entry point for phase |
| `PUT /zones/{zone_id}/rulesets/phases/{phase}/entrypoint` | PUT | Update entry point |

### Versioning

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET .../rulesets/{id}/versions` | GET | List versions |
| `GET .../rulesets/{id}/versions/{version}` | GET | Get specific version |
| `DELETE .../rulesets/{id}/versions/{version}` | DELETE | Delete version |

Account-level rulesets follow the same pattern under `/accounts/{account_id}/rulesets`.

---

## 6. Load Balancers

Distribute traffic across multiple origins with health checking, geographic routing, and failover.

### Load Balancer Operations (Zone-Level)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST /zones/{zone_id}/load_balancers` | POST | Create load balancer |
| `GET /zones/{zone_id}/load_balancers` | GET | List load balancers |
| `GET .../load_balancers/{id}` | GET | Get details |
| `PUT .../load_balancers/{id}` | PUT | Update (full replace) |
| `PATCH .../load_balancers/{id}` | PATCH | Update (partial) |
| `DELETE .../load_balancers/{id}` | DELETE | Delete |

**Create Load Balancer — Key Fields:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | **Yes** | DNS name for the LB (e.g., `lb.example.com`) |
| `default_pools` | array | **Yes** | Pool IDs for default traffic |
| `fallback_pool` | string | **Yes** | Pool ID for when all default pools are unhealthy |
| `proxied` | boolean | No | Whether to proxy through Cloudflare |
| `steering_policy` | string | No | `"off"`, `"geo"`, `"random"`, `"dynamic_latency"`, `"proximity"`, `"least_outstanding_requests"`, `"least_connections"` |
| `session_affinity` | string | No | `"none"`, `"cookie"`, `"ip_cookie"`, `"header"` |
| `ttl` | integer | No | DNS TTL (when not proxied) |
| `country_pools` | object | No | Country→pool mapping |
| `region_pools` | object | No | Region→pool mapping |
| `pop_pools` | object | No | POP→pool mapping |
| `rules` | array | No | Custom routing rules |

### Pool Operations (User-Level)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST /user/load_balancers/pools` | POST | Create pool |
| `GET /user/load_balancers/pools` | GET | List pools |
| `GET .../pools/{id}` | GET | Get pool |
| `PUT .../pools/{id}` | PUT | Update pool |
| `PATCH .../pools/{id}` | PATCH | Partial update |
| `DELETE .../pools/{id}` | DELETE | Delete pool |
| `GET .../pools/{id}/health` | GET | Get health status |
| `GET .../pools/{id}/references` | GET | List resources using this pool |

### Monitor Operations (User-Level)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `POST /user/load_balancers/monitors` | POST | Create health monitor |
| `GET /user/load_balancers/monitors` | GET | List monitors |
| `GET .../monitors/{id}` | GET | Get monitor |
| `PUT .../monitors/{id}` | PUT | Update monitor |
| `PATCH .../monitors/{id}` | PATCH | Partial update |
| `DELETE .../monitors/{id}` | DELETE | Delete monitor |

**Monitor types:** `http`, `https`, `tcp`, `udp_icmp`, `icmp_ping`, `smtp`

---

## 7. Cloudflare Images

Image hosting, optimization, and transformation service.

### Upload Image

```
POST /accounts/{account_id}/images/v1
```

Upload via multipart form (file or URL). Max 10MB per image.

### Direct Upload URL (For Client-Side Upload)

```
POST /accounts/{account_id}/images/v2/direct_upload
```

Creates an authenticated upload URL for client-side uploads without exposing API keys. Returns a draft record until the image is actually uploaded.

### Image Operations

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET /accounts/{account_id}/images/v2` | GET | List images (v2 — cursor-paginated, up to 10,000, metadata filtering) |
| `GET .../images/v1/{id}` | GET | Get image details |
| `GET .../images/v1/{id}/blob` | GET | Download base image |
| `PATCH .../images/v1/{id}` | PATCH | Update access control and metadata |
| `DELETE .../images/v1/{id}` | DELETE | Delete image (purges from cache) |
| `GET .../images/v1/stats` | GET | Usage statistics (count vs quota) |

**List Images v2 — Metadata Filtering:**

Filter images by custom metadata using `meta.<field>[<operator>]=<value>`:
- Operators: `eq`, `eq:string`, `eq:number`, `eq:boolean`, `in`, `in:string`, `in:number`
- Max 5 filters per request
- Max 5 levels of nesting

**Python SDK:**
```python
# Upload image
image = client.images.v1.create(
    account_id="my-account-id",
    file=open("hero.jpg", "rb"),
    metadata={"tenant_id": "tenant-123", "type": "hero"},
)

# Get direct upload URL for client-side upload
upload = client.images.v2.direct_uploads.create(
    account_id="my-account-id",
)
print(upload.upload_url)  # Give this to the client
print(upload.id)          # Image ID (draft until uploaded)
```
