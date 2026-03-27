# Cloudflare DNS API Reference

**Complete API reference for DNS record management, zone DNS settings, DNSSEC, analytics, and DNS scanning**

DNS is the foundation of custom domain mapping for a multi-tenant platform. Every tenant custom domain requires a CNAME record pointing to your Pages project or Worker. This reference covers programmatic DNS record creation, batch operations, import/export, and zone-level DNS configuration.

---

## Table of Contents

1. [DNS Records for a Zone](#1-dns-records-for-a-zone)
2. [Batch Operations](#2-batch-operations)
3. [Import & Export](#3-import--export)
4. [DNS Scanning](#4-dns-scanning)
5. [DNS Settings](#5-dns-settings)
6. [DNSSEC](#6-dnssec)
7. [DNS Analytics](#7-dns-analytics)
8. [Account-Level DNS](#8-account-level-dns)

---

## 1. DNS Records for a Zone

### Create DNS Record

```
POST /zones/{zone_id}/dns_records
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | **Yes** | DNS record name (e.g., `example.com`, `www`, `tenant-123.example.com`). Automatically appended with zone name if not fully qualified. |
| `type` | string | **Yes** | Record type (see supported types below) |
| `content` | string | Conditional | Record value — required for simple types (A, AAAA, CNAME, TXT, NS, PTR) |
| `data` | object | Conditional | Structured data — required for complex types (SRV, CAA, HTTPS, LOC, etc.) |
| `ttl` | integer | **Yes** | Time to live in seconds. `1` = automatic. Range: 60–86400 for non-auto. |
| `proxied` | boolean | No | `true` = traffic passes through Cloudflare (orange cloud). `false` = DNS only (gray cloud). Default varies by type. |
| `priority` | integer | No | Required for MX and URI records |
| `comment` | string | No | Comment for the record (visible in dashboard) |
| `tags` | array | No | String tags for filtering |
| `settings` | object | No | `{ "ipv4_only": bool, "ipv6_only": bool }` |

**Supported record types (20):** A, AAAA, CAA, CERT, CNAME, DNSKEY, DS, HTTPS, LOC, MX, NAPTR, NS, OPENPGPKEY, PTR, SMIMEA, SRV, SSHFP, SVCB, TLSA, TXT, URI

**Important constraints:**
- A/AAAA records cannot coexist with CNAME records on the same name
- NS records cannot coexist with any other record type on the same name
- Domain names are always stored in Punycode (even if created with Unicode)

**Python SDK — Create CNAME for tenant:**
```python
record = client.dns.records.create(
    zone_id="my-zone-id",
    name="tenant-123",                          # becomes tenant-123.example.com
    type="CNAME",
    content="my-pages-project.pages.dev",       # Points to Pages project
    proxied=True,                               # Traffic through Cloudflare
    ttl=1,                                      # Automatic TTL
    comment="Tenant 123 landing page",
    tags=["tenant:123", "type:landing-page"],
)
print(record.id)  # DNS record ID for future updates
```

**TypeScript SDK:**
```typescript
const record = await client.dns.records.create({
  zone_id: 'my-zone-id',
  name: 'tenant-123',
  type: 'CNAME',
  content: 'my-pages-project.pages.dev',
  proxied: true,
  ttl: 1,
  comment: 'Tenant 123 landing page',
  tags: ['tenant:123', 'type:landing-page'],
});
```

### List DNS Records

```
GET /zones/{zone_id}/dns_records
```

Extensive filtering support:

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | string | Filter by record name |
| `name.exact` | string | Exact name match |
| `name.contains` | string | Name contains substring |
| `name.startswith` | string | Name starts with |
| `name.endswith` | string | Name ends with |
| `type` | string | Filter by record type (A, AAAA, CNAME, etc.) |
| `content` | string | Filter by content value |
| `content.exact` | string | Exact content match |
| `content.contains` | string | Content contains substring |
| `content.startswith` | string | Content starts with |
| `content.endswith` | string | Content ends with |
| `proxied` | string | Filter by proxy status |
| `comment` | string | Filter by comment substring |
| `comment.present` | string | Records with comments |
| `comment.absent` | string | Records without comments |
| `comment.exact` | string | Exact comment match |
| `comment.contains` | string | Comment contains |
| `comment.startswith` | string | Comment starts with |
| `comment.endswith` | string | Comment ends with |
| `tag` | string | Filter by tag |
| `tag.present` | string | Records with a specific tag key |
| `tag.absent` | string | Records without a specific tag key |
| `tag.exact` | string | Exact tag match |
| `tag.contains` | string | Tag contains |
| `tag.startswith` | string | Tag starts with |
| `tag.endswith` | string | Tag ends with |
| `tag_match` | string | Tag matching mode |
| `search` | string | Free-text search across name and content |
| `match` | string | Filter match mode: `"all"` (AND) or `"any"` (OR) |
| `page` | integer | Page number |
| `per_page` | integer | Results per page |
| `order` | string | Sort field |
| `direction` | string | `"asc"` or `"desc"` |

**Find all tenant CNAME records:**
```python
records = client.dns.records.list(
    zone_id="my-zone-id",
    type="CNAME",
    tag="type:landing-page",
)
for record in records:
    print(f"{record.name} → {record.content}")
```

### Get DNS Record

```
GET /zones/{zone_id}/dns_records/{dns_record_id}
```

### Update DNS Record (Full Replace)

```
PUT /zones/{zone_id}/dns_records/{dns_record_id}
```

Overwrites the entire record. All fields must be provided.

### Patch DNS Record (Partial Update)

```
PATCH /zones/{zone_id}/dns_records/{dns_record_id}
```

Updates only the provided fields. Same constraints as create (A/AAAA can't coexist with CNAME, etc.).

```python
# Update just the content (target) of a CNAME
client.dns.records.edit(
    dns_record_id="record-id",
    zone_id="my-zone-id",
    content="new-pages-project.pages.dev",
)
```

### Delete DNS Record

```
DELETE /zones/{zone_id}/dns_records/{dns_record_id}
```

Returns the deleted record's ID.

### Get DNS Record Usage

```
GET /zones/{zone_id}/dns_records/usage
```

Returns current record count and quota limit for the zone.

---

## 2. Batch Operations

### Batch DNS Records

```
POST /zones/{zone_id}/dns_records/batch
```

Execute multiple DNS operations in a single database transaction. **Operations execute in order: Deletes → Patches → Puts → Posts.**

> **Note:** While the batch is transactional at the database level, propagation to Cloudflare's distributed KV store is not atomic — individual records may propagate at slightly different times.

| Field | Type | Description |
|-------|------|-------------|
| `deletes` | array | Records to delete |
| `patches` | array | Records to partially update |
| `puts` | array | Records to fully replace |
| `posts` | array | Records to create |

**Python SDK — Batch create tenant records:**
```python
client.dns.records.batch(
    zone_id="my-zone-id",
    posts=[
        {
            "name": "tenant-100",
            "type": "CNAME",
            "content": "landing-pages.pages.dev",
            "proxied": True,
            "ttl": 1,
            "tags": ["tenant:100"],
        },
        {
            "name": "tenant-101",
            "type": "CNAME",
            "content": "landing-pages.pages.dev",
            "proxied": True,
            "ttl": 1,
            "tags": ["tenant:101"],
        },
    ]
)
```

---

## 3. Import & Export

### Export DNS Records

```
GET /zones/{zone_id}/dns_records/export
```

Returns DNS records in BIND config format (text).

### Import DNS Records

```
POST /zones/{zone_id}/dns_records/import
```

Upload a BIND config file to import records. Content-Type: `multipart/form-data`.

---

## 4. DNS Scanning

Cloudflare can scan for common DNS records on a domain — useful during initial zone setup.

### Trigger DNS Scan (Async)

```
POST /zones/{zone_id}/dns_records/scan/trigger
```

Starts an async background scan. Results are reviewed separately. **Does not auto-add records.**

### Review Scan Results

```
GET /zones/{zone_id}/dns_records/scan/review
```

Returns discovered records. These are temporary until accepted or rejected.

### Accept/Reject Scan Results

```
POST /zones/{zone_id}/dns_records/scan/review
```

| Field | Type | Description |
|-------|------|-------------|
| `accepts` | array | Record IDs to permanently add to the zone |
| `rejects` | array | Record IDs to permanently discard |

### Scan DNS Records (Deprecated)

```
POST /zones/{zone_id}/dns_records/scan
```

Legacy synchronous scan — use `scan/trigger` instead.

---

## 5. DNS Settings

### Zone-Level DNS Settings

```
GET /zones/{zone_id}/dns_settings
PATCH /zones/{zone_id}/dns_settings
```

### Account-Level DNS Settings

```
GET /accounts/{account_id}/dns_settings
PATCH /accounts/{account_id}/dns_settings
```

| Field | Type | Description |
|-------|------|-------------|
| `zone_defaults` | object | Default DNS settings for new zones |

---

## 6. DNSSEC

### Get DNSSEC Status

```
GET /zones/{zone_id}/dnssec
```

### Enable/Disable DNSSEC

```
PATCH /zones/{zone_id}/dnssec
```

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | `"active"` or `"disabled"` |
| `dnssec_multi_signer` | boolean | Enable multi-signer DNSSEC (multiple providers) |
| `dnssec_presigned` | boolean | Allow transfer of DNSSEC-signed zones from external providers |
| `dnssec_use_nsec3` | boolean | Use NSEC3 records with DNSSEC |

### Delete DNSSEC

```
DELETE /zones/{zone_id}/dnssec
```

---

## 7. DNS Analytics

### Analytics Table

```
GET /zones/{zone_id}/dns_analytics/report
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `metrics` | string | Comma-separated metrics |
| `dimensions` | string | Comma-separated dimensions |
| `since` | string | Start time (ISO 8601) |
| `until` | string | End time (ISO 8601) |
| `limit` | string | Max results |
| `sort` | string | Sort field |
| `filters` | string | Filter expression |

### Analytics by Time

```
GET /zones/{zone_id}/dns_analytics/report/bytime
```

Same parameters as above, plus:

| Parameter | Type | Description |
|-----------|------|-------------|
| `time_delta` | string | Time interval grouping |

---

## 8. Account-Level DNS

### Get Account DNS Record Usage

```
GET /accounts/{account_id}/dns_records/usage
```

Returns DNS record count and quota across all zones in the account.
