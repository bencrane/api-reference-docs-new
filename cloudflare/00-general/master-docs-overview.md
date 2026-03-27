# Cloudflare API Technical Reference

**Comprehensive technical documentation for the Cloudflare API — programmatic control of edge hosting, DNS, SSL, Workers, and custom domain management for multi-tenant B2B platforms**

Generated: 2026-03-26

This document covers the complete Cloudflare API surface relevant to hosting and serving web content programmatically. It is the canonical reference for engineers building a system that deploys generated landing pages per tenant, maps custom domains with automatic SSL, runs edge logic via Workers, and manages DNS — all through Cloudflare's API. Use the linked supplementary files for full endpoint tables and SDK examples for each domain area.

---

## Table of Contents

### Tier 1 — Deep Coverage (full parameter tables, SDK examples)
1. [Authentication & API Access](#1-authentication--api-access)
2. [Pages — Static Site Deployment](pages-reference.md) ← **Start here for landing page deployment**
3. [Workers — Edge Logic](workers-reference.md)
4. [DNS — Record & Zone Management](dns-reference.md)
5. [Custom Hostnames — Multi-Tenant Domain Mapping](custom-hostnames-reference.md)
6. [Zones — Zone Lifecycle](zones-reference.md)
7. [SSL/TLS — Certificate Management](ssl-tls-reference.md)

### Tier 2 — Moderate Coverage (key endpoints, schemas, behavior)
8. [R2, KV, Cache, Turnstile, Rulesets, Load Balancers, Images](tier2-reference.md)

### Tier 3 — Light Coverage (overview, when to use)
9. [Accounts & IAM](#9-accounts--iam)
10. [D1 (Database)](#10-d1-database)
11. [Queues](#11-queues)
12. [Durable Objects](#12-durable-objects)
13. [Stream (Video)](#13-stream-video)
14. [AI / AI Gateway / Vectorize](#14-ai--ai-gateway--vectorize)
15. [Email Routing](#15-email-routing)
16. [Zero Trust](#16-zero-trust)
17. [Other Services](#17-other-services)

---

## API Fundamentals

### Base URL

```
https://api.cloudflare.com/client/v4
```

All endpoints documented here are relative to this base.

### Standard Response Envelope

Every Cloudflare API response follows this structure:

```json
{
  "success": true,
  "errors": [],
  "messages": [],
  "result": { ... },
  "result_info": {
    "page": 1,
    "per_page": 20,
    "total_pages": 1,
    "count": 5,
    "total_count": 5
  }
}
```

- `success` — boolean, always present
- `errors` — array of `{ code, message }` objects (empty on success)
- `result` — the response payload (object, array, or string depending on endpoint)
- `result_info` — pagination metadata (present on list endpoints)

### Pagination

List endpoints support cursor or page-based pagination:

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | integer | Page number (1-indexed) |
| `per_page` | integer | Results per page (default varies, max usually 100) |
| `direction` | string | Sort direction: `asc` or `desc` |
| `order` | string | Field to sort by (endpoint-specific) |

The SDKs provide auto-paginating iterators that handle this transparently.

### Rate Limits

- **Global rate limit:** 1,200 requests per 5 minutes per user (API token or key)
- **Per-endpoint limits:** Some endpoints (e.g., cache purge, DNS batch) have tighter limits
- HTTP 429 responses include `Retry-After` header
- Both SDKs auto-retry on 429 with exponential backoff (2 retries by default)

### Error Codes

| HTTP Status | Meaning | Common Cause |
|-------------|---------|--------------|
| 400 | Bad Request | Invalid parameters, malformed JSON |
| 401 | Unauthorized | Missing or invalid authentication |
| 403 | Forbidden | Token lacks required permissions |
| 404 | Not Found | Resource doesn't exist or wrong zone/account ID |
| 409 | Conflict | Resource already exists (e.g., duplicate DNS record) |
| 429 | Rate Limited | Too many requests |
| 5xx | Server Error | Cloudflare internal issue (retry) |

---

## 1. Authentication & API Access

Cloudflare supports three authentication methods. **API tokens are strongly recommended** — they are scoped, rotatable, and auditable.

### Authentication Methods

| Method | Headers | Scope | Recommendation |
|--------|---------|-------|----------------|
| **API Token** | `Authorization: Bearer {token}` | Scoped to specific permissions, zones, accounts | **Preferred** |
| **API Key + Email** | `X-Auth-Key: {key}` + `X-Auth-Email: {email}` | Full account access (legacy) | Avoid for new integrations |
| **User Service Key** | `X-Auth-User-Service-Key: {key}` | Origin CA certificate operations only | Niche use only |

### API Token Management

API tokens are the recommended authentication method. They can be scoped to specific permissions and resources.

#### Create Token
```
POST /user/tokens
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Human-readable token name |
| `policies` | array | Yes | Permission policies (see below) |
| `not_before` | string | No | ISO 8601 — token not valid before this time |
| `expires_on` | string | No | ISO 8601 — token expires at this time |
| `condition` | object | No | IP restriction: `{ "request.ip": { "in": ["1.2.3.0/24"], "not_in": ["1.2.3.4"] } }` |

**Policy structure:**
```json
{
  "policies": [
    {
      "effect": "allow",
      "resources": {
        "com.cloudflare.api.account.zone.*": "*"
      },
      "permission_groups": [
        { "id": "c8fed203ed3043cba015a93ad1616f1f" }
      ]
    }
  ]
}
```

#### Other Token Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `GET /user/tokens` | GET | List all tokens |
| `GET /user/tokens/{token_id}` | GET | Get token details |
| `PUT /user/tokens/{token_id}` | PUT | Update token (name, policies, status, expiry) |
| `DELETE /user/tokens/{token_id}` | DELETE | Destroy token |
| `PUT /user/tokens/{token_id}/value` | PUT | Roll (rotate) the token secret |
| `GET /user/tokens/verify` | GET | Test if the current token works |
| `GET /user/tokens/permission_groups` | GET | List all available permission groups |

#### Account-Owned Tokens

For service accounts and CI/CD, use account-owned tokens (same CRUD pattern under `/accounts/{account_id}/tokens`). These are tied to the account, not a user.

### Key Permission Groups for Multi-Tenant Hosting

| Permission Group | What It Grants |
|-----------------|----------------|
| Zone — DNS — Edit | Create/modify/delete DNS records |
| Zone — SSL and Certificates — Edit | Manage custom SSL, certificate packs, custom hostnames |
| Zone — Workers Routes — Edit | Manage Worker routes |
| Account — Workers Scripts — Edit | Upload/delete Worker scripts |
| Account — Pages — Edit | Create/manage Pages projects and deployments |
| Account — Workers R2 Storage — Edit | Manage R2 buckets and objects |
| Account — Workers KV Storage — Edit | Manage KV namespaces and keys |
| Zone — Zone — Edit | Create/delete zones |
| Zone — Zone Settings — Edit | Modify zone settings |
| Zone — Cache Purge — Purge | Purge cached content |

### SDK Initialization

**Python:**
```python
from cloudflare import Cloudflare

# Reads CLOUDFLARE_API_TOKEN from env automatically
client = Cloudflare()

# Explicit token
client = Cloudflare(api_token="my-cloudflare-api-token")

# Legacy API key + email
client = Cloudflare(api_key="my-key", api_email="me@example.com")
```

**TypeScript:**
```typescript
import Cloudflare from 'cloudflare';

// Reads CLOUDFLARE_API_TOKEN from env automatically
const client = new Cloudflare();

// Explicit token
const client = new Cloudflare({ apiToken: 'my-cloudflare-api-token' });

// Legacy API key + email
const client = new Cloudflare({ apiKey: 'my-key', apiEmail: 'me@example.com' });
```

**Environment variables (both SDKs):**

| Variable | Maps to |
|----------|---------|
| `CLOUDFLARE_API_TOKEN` | API Token (preferred) |
| `CLOUDFLARE_API_KEY` | Global API Key |
| `CLOUDFLARE_EMAIL` | Email for API Key auth |
| `CLOUDFLARE_API_USER_SERVICE_KEY` | Origin CA service key |

### SDK Common Patterns

**Auto-pagination (both SDKs handle this):**
```python
# Python — iterates all pages automatically
for zone in client.zones.list():
    print(zone.name)
```
```typescript
// TypeScript — async iterator
for await (const zone of client.zones.list()) {
  console.log(zone.name);
}
```

**Error handling:**
```python
# Python
from cloudflare import BadRequestError, AuthenticationError, RateLimitError
try:
    result = client.zones.create(name="example.com", account={"id": "abc"})
except AuthenticationError:
    print("Invalid token")
except RateLimitError:
    print("Rate limited — retry later")
```
```typescript
// TypeScript
try {
  const result = await client.zones.create({ name: 'example.com', account: { id: 'abc' } });
} catch (err) {
  if (err instanceof Cloudflare.AuthenticationError) { /* 401 */ }
  if (err instanceof Cloudflare.RateLimitError) { /* 429 */ }
}
```

**Retries:** Both SDKs auto-retry 2 times with exponential backoff on 408, 409, 429, and 5xx errors.

---

## 9. Accounts & IAM

Cloudflare accounts are the top-level organizational unit. Every zone, Worker, Pages project, and storage bucket belongs to an account.

**Key endpoints:**
- `GET /accounts` — List accounts you have access to
- `GET /accounts/{account_id}` — Get account details
- `PUT /accounts/{account_id}` — Update account settings
- `POST /accounts/{account_id}/members` — Add a member (with roles or policies)
- `GET /accounts/{account_id}/members` — List members
- `PUT /accounts/{account_id}/members/{member_id}` — Update member roles
- `DELETE /accounts/{account_id}/members/{member_id}` — Remove member
- `GET /accounts/{account_id}/roles` — List available roles
- `GET /accounts/{account_id}/iam/permission_groups` — List permission groups

Account creation (`POST /accounts`) is restricted to tenant admins. Account deletion is permanent and destroys all child resources.

---

## 10. D1 (Database)

D1 is Cloudflare's serverless SQLite database, accessible from Workers. Useful for storing tenant configuration, form submissions, or landing page metadata at the edge.

**Key concepts:** Each D1 database is bound to Workers via bindings. Queries run at the edge with automatic read replication. Write operations go to a primary region.

**API endpoints:** Under `/accounts/{account_id}/d1/database` — create, list, query, delete databases. In practice, D1 is most commonly accessed from within Worker code via the binding, not the REST API.

---

## 11. Queues

Cloudflare Queues provide guaranteed message delivery between Workers. Useful for async processing — e.g., queuing form submissions from a landing page Worker for backend processing.

**Key concepts:** Producers send messages, consumers (Workers) process them. Supports batching, retries, and dead-letter queues. Managed under `/accounts/{account_id}/queues`.

---

## 12. Durable Objects

Durable Objects provide strongly consistent, stateful storage co-located with a Worker. Each object has a unique ID, persistent storage, and a single-threaded execution model.

**Use cases for multi-tenant:** Rate limiting per tenant, real-time form collaboration, session state. Managed via Worker bindings, not directly via REST API. The API surface is limited to namespace management under `/accounts/{account_id}/workers/durable_objects/namespaces`.

---

## 13. Stream (Video)

Cloudflare Stream is a video hosting and delivery platform. Upload videos, get HLS/DASH playback URLs, manage live inputs, add captions, and create clips.

**API surface:** Under `/accounts/{account_id}/stream` — upload, list, delete videos, manage live inputs, signing keys, watermarks, and webhooks. Unlikely to be relevant for landing page hosting unless video content is part of the tenant experience.

---

## 14. AI / AI Gateway / Vectorize

- **Workers AI** — Run inference models (text generation, image classification, embeddings, etc.) at the edge via Worker bindings. API under `/accounts/{account_id}/ai`.
- **AI Gateway** — Proxy and cache AI API calls (OpenAI, Anthropic, etc.) with rate limiting, logging, and fallbacks. Managed under `/accounts/{account_id}/ai-gateway`.
- **Vectorize** — Vector database for AI embeddings, used with Workers AI for RAG applications. Under `/accounts/{account_id}/vectorize`.

These are specialized AI services, not directly relevant to landing page hosting.

---

## 15. Email Routing

Cloudflare Email Routing lets you create email addresses on your domain and forward them to existing mailboxes. Managed under zone-level endpoints.

**Key endpoints:** `/zones/{zone_id}/email/routing/rules` (routing rules), `/accounts/{account_id}/email/routing/addresses` (destination addresses). Could be useful for creating per-tenant email forwarding (e.g., `contact@tenant-domain.com` → `support@your-platform.com`).

---

## 16. Zero Trust

Cloudflare Zero Trust (formerly Access) is a comprehensive security platform including:
- **Access** — Identity-aware proxy for applications
- **Gateway** — Secure web gateway with DNS/HTTP/network filtering
- **Tunnel** — Expose private services to the internet securely
- **WARP** — Client VPN and DNS

Extensive API surface under `/accounts/{account_id}/access/`, `/accounts/{account_id}/gateway/`, and `/accounts/{account_id}/cfd_tunnel/`. Relevant if you need to protect admin interfaces or internal services, but not directly related to public landing page serving.

---

## 17. Other Services

| Service | API Path | One-Liner |
|---------|----------|-----------|
| **Spectrum** | `/zones/{zone_id}/spectrum/apps` | TCP/UDP proxy for non-HTTP protocols |
| **Argo Smart Routing** | `/zones/{zone_id}/argo/smart_routing` | Optimized routing through Cloudflare's network |
| **Waiting Room** | `/zones/{zone_id}/waiting_rooms` | Queue visitors during traffic spikes |
| **Web Analytics** | `/accounts/{account_id}/rum/site_info` | Privacy-first analytics without client-side JS |
| **Page Shield** | `/zones/{zone_id}/page_shield` | Monitor and control third-party scripts |
| **Zaraz** | `/zones/{zone_id}/zaraz` | Server-side tag management |
| **Registrar** | `/accounts/{account_id}/registrar/domains` | Domain registration at cost |
| **Hyperdrive** | `/accounts/{account_id}/hyperdrive/configs` | Connection pooling for databases from Workers |
| **Cloudflare Tunnel** | `/accounts/{account_id}/cfd_tunnel` | Expose private origins without public IPs |
| **Magic Transit** | Various | DDoS protection for network infrastructure |
| **IP Address Management** | `/accounts/{account_id}/addressing/prefixes` | BYOIP management |
| **Logpush** | `/zones/{zone_id}/logpush/jobs` | Push request/event logs to storage |
| **Notifications** | `/accounts/{account_id}/alerting/v3/policies` | Alert on events (DDoS, certificate expiry, etc.) |
| **API Shield** | `/zones/{zone_id}/api_gateway` | API security, schema validation, rate limiting |

---

## Multi-Tenant Architecture Reference

For a B2B platform that deploys generated landing pages per tenant with custom domains, the recommended Cloudflare architecture is:

### Option A: Pages + Custom Hostnames (Recommended)

1. **One Pages project** per tenant (or shared project with branch-based deploys)
2. **Direct Upload API** — push pre-built HTML/CSS/JS assets without git
3. **Custom Hostnames (SSL for SaaS)** on your zone — map `tenant.example.com` or `www.tenant-domain.com` to your Pages project
4. **Workers** for edge logic — form handling, redirects, A/B testing, analytics injection
5. **DNS records** — programmatic CNAME creation for tenants using your domain
6. **R2** — asset storage for images, PDFs, or generated content

### Option B: Workers + Custom Hostnames

1. **Workers for Platforms** — deploy per-tenant Worker scripts in a dispatch namespace
2. **Custom Hostnames** — map tenant domains to your zone
3. **Worker routes** — route traffic to the correct tenant Worker
4. **KV** — store tenant config, page content, or routing rules
5. **R2** — store static assets served by Workers

### Key Integration Flow

```
Tenant onboards → Create DNS record (CNAME) → Create Custom Hostname →
Deploy Pages/Worker → Attach custom domain → SSL auto-provisioned
```

See the individual reference files linked above for complete endpoint documentation, parameter tables, and SDK examples for each step of this flow.
