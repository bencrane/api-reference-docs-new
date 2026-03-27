# Cloudflare Zones API Reference

**Complete API reference for zone lifecycle management — create, configure, purge cache, and manage zone settings**

A zone represents a domain on Cloudflare. Every DNS record, SSL certificate, Worker route, and security setting lives under a zone. For a multi-tenant platform, you'll either use a single shared zone (with custom hostnames for tenant domains) or create zones per tenant.

---

## Table of Contents

1. [Zone Lifecycle](#1-zone-lifecycle)
2. [Zone Settings](#2-zone-settings)
3. [Cache Purge](#3-cache-purge)
4. [Zone Holds](#4-zone-holds)
5. [Activation Check](#5-activation-check)

---

## 1. Zone Lifecycle

### Create Zone

```
POST /zones
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | **Yes** | Domain name (e.g., `example.com`). Max 253 chars total, 63 chars per label (per RFC 1035). |
| `account` | object | **Yes** | `{ "id": "account-id" }` — the account to create the zone in |
| `type` | string | No | Zone type (see below) |

**Zone types:**

| Type | Description |
|------|-------------|
| `full` | DNS hosted with Cloudflare (default). Change nameservers to Cloudflare's. |
| `partial` | CNAME setup — typically partner-hosted. Individual records proxied via CNAME. |
| `secondary` | Cloudflare as secondary DNS provider. |
| `internal` | Internal zone. Enterprise and explicitly enabled zones only. |

**Python SDK:**
```python
zone = client.zones.create(
    name="tenant-domain.com",
    account={"id": "my-account-id"},
    type="full",
)
print(zone.id)              # Zone ID (use for all subsequent zone operations)
print(zone.name_servers)    # Cloudflare nameservers to set at registrar
print(zone.status)          # "pending" until nameservers are updated
```

**TypeScript SDK:**
```typescript
const zone = await client.zones.create({
  name: 'tenant-domain.com',
  account: { id: 'my-account-id' },
  type: 'full',
});
```

### List Zones

```
GET /zones
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | string | Filter by domain name |
| `status` | string | Filter by status: `initializing`, `pending`, `active`, `moved` |
| `account.id` | string | Filter by account ID |
| `account.name` | string | Filter by account name |
| `page` | number | Page number |
| `per_page` | number | Results per page |
| `order` | string | Sort by: `name`, `status`, `account.id`, `account.name` |
| `direction` | string | `"asc"` or `"desc"` |
| `match` | string | `"all"` (AND) or `"any"` (OR) |

> **Limit:** Listing zones across more than 500 accounts is not allowed.

**Find a zone by domain:**
```python
zones = client.zones.list(name="tenant-domain.com")
for z in zones:
    print(f"{z.name}: {z.id} ({z.status})")
```

### Get Zone Details

```
GET /zones/{zone_id}
```

Returns full zone details including nameservers, status, plan, settings, and metadata.

**Response includes:**
- `id` — Zone ID
- `name` — Domain name
- `status` — Current status
- `name_servers` — Cloudflare's assigned nameservers
- `original_name_servers` — Original nameservers before switching
- `paused` — Whether the zone is paused (DNS-only mode)
- `type` — Zone type
- `plan` — Current plan (free, pro, business, enterprise)
- `account` — Account details
- `activated_on` — Activation timestamp
- `permissions` — Current user's permissions on this zone

### Edit Zone

```
PATCH /zones/{zone_id}
```

**Only one property can be changed at a time.**

| Field | Type | Description |
|-------|------|-------------|
| `paused` | boolean | Pause the zone (DNS-only, no security/performance features) |
| `plan` | object | **(Deprecated)** — use `/zones/{zone_id}/subscription` instead |
| `type` | string | Change zone type. Enterprise-only or explicitly enabled. |
| `vanity_name_servers` | array | Custom nameserver names (Business/Enterprise only) |

### Delete Zone

```
DELETE /zones/{zone_id}
```

**Permanently deletes the zone and all its records, settings, and certificates.** This is irreversible.

---

## 2. Zone Settings

### Get All Zone Settings (Deprecated)

```
GET /zones/{zone_id}/settings
```

Returns all settings as an array. Deprecated — use individual setting endpoints.

### Edit All Zone Settings (Deprecated)

```
PATCH /zones/{zone_id}/settings
```

Batch-update settings. Deprecated — use individual setting endpoints.

### Get Single Setting

```
GET /zones/{zone_id}/settings/{setting_id}
```

### Edit Single Setting

```
PATCH /zones/{zone_id}/settings/{setting_id}
```

### Key Settings for Multi-Tenant Hosting

| Setting ID | Values | Description |
|-----------|--------|-------------|
| `ssl` | `off`, `flexible`, `full`, `strict` | SSL mode |
| `always_use_https` | `on`, `off` | Redirect all HTTP to HTTPS |
| `automatic_https_rewrites` | `on`, `off` | Fix mixed content by rewriting HTTP URLs |
| `min_tls_version` | `1.0`, `1.1`, `1.2`, `1.3` | Minimum TLS version |
| `tls_1_3` | `on`, `off`, `zrt` | TLS 1.3 support |
| `http2` | `on`, `off` | HTTP/2 |
| `http3` | `on`, `off` | HTTP/3 (QUIC) |
| `0rtt` | `on`, `off` | 0-RTT (TLS early data) |
| `ipv6` | `on`, `off` | IPv6 compatibility |
| `websockets` | `on`, `off` | WebSocket support |
| `browser_cache_ttl` | integer | Browser cache TTL (seconds) |
| `always_online` | `on`, `off` | Serve stale content when origin is down |
| `development_mode` | `on`, `off` | Bypass cache for 3 hours (for debugging) |
| `security_level` | `off`, `essentially_off`, `low`, `medium`, `high`, `under_attack` | Security challenge threshold |
| `waf` | `on`, `off` | Web Application Firewall |
| `minify` | `{ "css": "on", "html": "on", "js": "on" }` | Asset minification |
| `brotli` | `on`, `off` | Brotli compression |
| `early_hints` | `on`, `off` | HTTP 103 Early Hints |
| `rocket_loader` | `on`, `off` | Async JS loading |
| `polish` | `off`, `lossless`, `lossy` | Image optimization |
| `mirage` | `on`, `off` | Image lazy loading for slow connections |
| `fonts` | `on`, `off` | Cloudflare Fonts (serve Google Fonts from your domain) |
| `speed_brain` | `on`, `off` | Speculative page prefetching |
| `origin_max_http_version` | `1`, `2` | Max HTTP version to origin |
| `origin_h2_max_streams` | integer | Max concurrent H2 streams to origin (default 100, Enterprise default 1) |

### Specific Setting Endpoints

Some settings have dedicated endpoints with richer schemas:

| Setting | GET Endpoint | PATCH Endpoint |
|---------|-------------|----------------|
| Aegis (dedicated egress IPs) | `GET /zones/{zone_id}/settings/aegis` | `PATCH /zones/{zone_id}/settings/aegis` |
| Fonts | `GET /zones/{zone_id}/settings/fonts` | `PATCH /zones/{zone_id}/settings/fonts` |
| Speed Brain | `GET /zones/{zone_id}/settings/speed_brain` | `PATCH /zones/{zone_id}/settings/speed_brain` |
| Origin Max HTTP Version | `GET /zones/{zone_id}/settings/origin_max_http_version` | `PATCH /zones/{zone_id}/settings/origin_max_http_version` |
| Origin H2 Max Streams | `GET /zones/{zone_id}/settings/origin_h2_max_streams` | `PATCH /zones/{zone_id}/settings/origin_h2_max_streams` |

---

## 3. Cache Purge

Purge cached content from Cloudflare's edge. Essential when updating tenant landing pages.

### Purge Cache

```
POST /zones/{zone_id}/purge_cache
```

Multiple purge strategies available (use exactly one):

#### Purge Everything

```json
{ "purge_everything": true }
```

Clears all cached content for the zone. Use sparingly — causes a cache stampede.

#### Purge by URL

```json
{
  "files": [
    "https://www.tenant.com/index.html",
    "https://www.tenant.com/styles.css"
  ]
}
```

For files with custom cache keys (device type, geo, language), include headers:

```json
{
  "files": [
    {
      "url": "https://www.tenant.com/image.jpg",
      "headers": {
        "CF-IPCountry": "US",
        "CF-Device-Type": "desktop",
        "Accept-Language": "en-US"
      }
    }
  ]
}
```

#### Purge by Cache Tag (Enterprise)

```json
{ "tags": ["tenant-123", "landing-page"] }
```

#### Purge by Host (Enterprise)

```json
{ "hosts": ["www.tenant.com", "landing.tenant.com"] }
```

#### Purge by Prefix (Enterprise)

```json
{ "prefixes": ["www.tenant.com/assets/", "www.tenant.com/images/"] }
```

**Python SDK:**
```python
# Purge specific URLs after deploying a tenant update
client.cache.purge(
    zone_id="my-zone-id",
    files=[
        "https://www.tenant.com/",
        "https://www.tenant.com/index.html",
    ]
)

# Purge everything (use sparingly)
client.cache.purge(
    zone_id="my-zone-id",
    purge_everything=True,
)
```

---

## 4. Zone Holds

Zone holds prevent the creation and activation of zones with a specific hostname. Useful for domain protection.

### Create Zone Hold

```
POST /zones/{zone_id}/hold
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `include_subdomains` | boolean | query | Also block subdomains and SSL for SaaS custom hostnames |

### Get Zone Hold

```
GET /zones/{zone_id}/hold
```

### Update Zone Hold

```
PATCH /zones/{zone_id}/hold
```

| Field | Type | Description |
|-------|------|-------------|
| `hold_after` | string | RFC 3339 timestamp — temporarily disable hold until this time. Past date = no effect. Empty string = current time. |
| `include_subdomains` | boolean | Extend to subdomains and SSL for SaaS custom hostnames |

### Delete Zone Hold

```
DELETE /zones/{zone_id}/hold
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `hold_after` | string | query | If provided, temporarily disable until this RFC 3339 time. Otherwise, disable indefinitely. |

---

## 5. Activation Check

### Trigger Activation Check

```
PUT /zones/{zone_id}/activation_check
```

Triggers a nameserver check for a `PENDING` zone. Rate limits:
- Paid plans: Every 5 minutes
- Free plans: Every hour
