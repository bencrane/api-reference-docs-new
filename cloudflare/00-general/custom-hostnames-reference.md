# Cloudflare Custom Hostnames API Reference (SSL for SaaS)

**Complete API reference for Custom Hostnames — multi-tenant custom domain mapping with automatic SSL provisioning**

Custom Hostnames (also called "SSL for SaaS" or "Cloudflare for SaaS") is the primary mechanism for mapping tenant-owned domains to your platform. Each custom hostname gets automatic SSL certificate provisioning and can be pointed at your origin, a Pages project, or a Worker.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Custom Hostnames CRUD](#2-custom-hostnames-crud)
3. [SSL Configuration](#3-ssl-configuration)
4. [Domain Control Validation (DCV)](#4-domain-control-validation-dcv)
5. [Fallback Origin](#5-fallback-origin)
6. [Certificate Bundles](#6-certificate-bundles)
7. [Multi-Tenant Integration Pattern](#7-multi-tenant-integration-pattern)

---

## 1. Architecture Overview

### How It Works

1. **Your zone** (e.g., `yourplatform.com`) has Custom Hostnames enabled
2. **Tenant creates** a CNAME from their domain (e.g., `www.tenant.com`) to your designated target (e.g., `tenants.yourplatform.com`)
3. **You create** a Custom Hostname via API for `www.tenant.com`
4. **Cloudflare** validates domain ownership (DCV) and provisions an SSL certificate
5. **Traffic** to `www.tenant.com` flows through Cloudflare → your origin (or Pages/Worker)

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Custom Hostname** | A tenant's domain registered to receive traffic through your Cloudflare zone |
| **Fallback Origin** | Default origin server for all custom hostnames without a specific `custom_origin_server` |
| **Custom Origin Server** | Per-hostname origin override (e.g., different Pages project or Worker per tenant) |
| **Custom Origin SNI** | SNI value sent during TLS handshake to the origin. Use `:request_host_header:` to pass the original hostname. |
| **DCV (Domain Control Validation)** | Proof that the custom hostname owner authorized SSL for their domain. Methods: HTTP, TXT, CNAME, Email. |
| **Custom Metadata** | Arbitrary key/value pairs stored per hostname — useful for tenant ID, plan tier, etc. |

### Hostname Status Lifecycle

```
pending → active
pending → pending_blocked → blocked
active → moved
active → pending_deletion → deleted
```

Full status values: `active`, `pending`, `active_redeploying`, `moved`, `pending_deletion`, `deleted`, `pending_blocked`, `pending_migration`, `pending_provisioned`, `test_pending`, `test_active`, `test_active_apex`, `test_blocked`, `test_failed`, `provisioned`, `blocked`

---

## 2. Custom Hostnames CRUD

### Create Custom Hostname

```
POST /zones/{zone_id}/custom_hostnames
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `hostname` | string | **Yes** | The tenant's custom domain (e.g., `www.tenant.com`) |
| `ssl` | object | No | SSL configuration (see SSL section below) |
| `custom_metadata` | object | No | Arbitrary key/value metadata. Per-hostname customer settings. |
| `custom_origin_server` | string | No | A valid hostname in your DNS zone to use as the origin for this custom hostname |
| `custom_origin_sni` | string | No | SNI sent to origin. Can be `:request_host_header:` to pass the request's Host header. |

**Python SDK:**
```python
hostname = client.custom_hostnames.create(
    zone_id="my-zone-id",
    hostname="www.tenant-domain.com",
    ssl={
        "method": "http",          # DCV method — recommended if CNAME already exists
        "type": "dv",
        "settings": {
            "min_tls_version": "1.2",
            "http2": "on",
        }
    },
    custom_metadata={
        "tenant_id": "tenant-123",
        "plan": "pro",
    },
    custom_origin_server="tenants.yourplatform.com",
)
print(hostname.id)              # Custom hostname ID
print(hostname.ssl.status)      # SSL provisioning status
```

**TypeScript SDK:**
```typescript
const hostname = await client.customHostnames.create({
  zone_id: 'my-zone-id',
  hostname: 'www.tenant-domain.com',
  ssl: {
    method: 'http',
    type: 'dv',
    settings: {
      min_tls_version: '1.2',
      http2: 'on',
    },
  },
  custom_metadata: {
    tenant_id: 'tenant-123',
    plan: 'pro',
  },
});
```

### List Custom Hostnames

```
GET /zones/{zone_id}/custom_hostnames
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `hostname` | string | query | Filter by hostname |
| `hostname.contain` | string | query | Hostname contains substring |
| `id` | string | query | Filter by custom hostname ID |
| `ssl_status` | string | query | Filter by SSL status |
| `hostname_status` | string | query | Filter by hostname status |
| `certificate_authority` | string | query | Filter by CA |
| `wildcard` | boolean | query | Filter wildcard hostnames |
| `custom_origin_server` | string | query | Filter by origin server |
| `ssl` | string | query | Filter by SSL type |
| `page` | number | query | Page number |
| `per_page` | number | query | Results per page |
| `order` | string | query | Sort field |
| `direction` | string | query | `"asc"` or `"desc"` |

**Find all hostnames for a tenant:**
```python
hostnames = client.custom_hostnames.list(
    zone_id="my-zone-id",
    hostname__contain="tenant-domain.com",
)
for h in hostnames:
    print(f"{h.hostname} — SSL: {h.ssl.status} — Status: {h.status}")
```

### Get Custom Hostname Details

```
GET /zones/{zone_id}/custom_hostnames/{custom_hostname_id}
```

Returns full details including SSL status, ownership verification records, and validation data.

### Edit Custom Hostname

```
PATCH /zones/{zone_id}/custom_hostnames/{custom_hostname_id}
```

| Field | Type | Description |
|-------|------|-------------|
| `ssl` | object | Update SSL configuration. Sending matching config triggers DCV re-check. Can change validation method (e.g., `http` → `email`). |
| `custom_metadata` | object | Update per-hostname metadata |
| `custom_origin_server` | string | Change the origin server |
| `custom_origin_sni` | string | Change the SNI for origin TLS handshake |

**Trigger DCV re-validation:**
```python
client.custom_hostnames.edit(
    custom_hostname_id="hostname-id",
    zone_id="my-zone-id",
    ssl={"method": "http", "type": "dv"},  # Sending matching config triggers re-check
)
```

### Delete Custom Hostname

```
DELETE /zones/{zone_id}/custom_hostnames/{custom_hostname_id}
```

**Permanently deletes the custom hostname and revokes all associated SSL certificates.** This cannot be undone.

---

## 3. SSL Configuration

### SSL Object Fields

When creating or editing a custom hostname, the `ssl` object controls certificate behavior:

| Field | Type | Description |
|-------|------|-------------|
| `method` | string | DCV method: `"http"`, `"txt"`, `"cname"`, `"email"` |
| `type` | string | Validation level: `"dv"` (domain validation — the standard) |
| `settings` | object | TLS settings (see below) |
| `bundle_method` | string | Certificate chain bundling: `"ubiquitous"`, `"optimal"`, `"force"` |
| `certificate_authority` | string | Issuing CA (when specified) |
| `custom_certificate` | string | BYO certificate PEM (for custom cert uploads) |
| `custom_key` | string | BYO private key PEM |
| `wildcard` | boolean | Request wildcard certificate coverage |

### SSL Settings

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| `min_tls_version` | string | `"1.0"`, `"1.1"`, `"1.2"`, `"1.3"` | Minimum TLS version |
| `http2` | string | `"on"`, `"off"` | HTTP/2 support |
| `tls_1_3` | string | `"on"`, `"off"` | Explicit TLS 1.3 toggle |
| `early_hints` | string | `"on"`, `"off"` | HTTP 103 Early Hints |
| `ciphers` | array | BoringSSL cipher strings | Allowed cipher suites |

### Certificate Bundle

You can bundle two certificates (one RSA + one ECDSA) for maximum compatibility. Use the `custom_cert_bundle` field during create or edit. Constraints:
- One certificate must be RSA, the other ECDSA
- Maximum two certificates per bundle

---

## 4. Domain Control Validation (DCV)

DCV proves the custom hostname owner authorized SSL provisioning. Choose based on your setup:

| Method | How It Works | When to Use |
|--------|-------------|-------------|
| `http` | Cloudflare places a file at `/.well-known/pki-validation/` on the hostname | **Recommended** — works automatically if the CNAME is already pointing to you |
| `txt` | Tenant adds a TXT record to their DNS | When the CNAME isn't set up yet |
| `cname` | Tenant adds a CNAME record for DCV | Alternative DNS validation |
| `email` | Verification email sent to domain WHOIS contacts + standard addresses | Last resort |

**HTTP validation is recommended** for programmatic use — if the tenant's CNAME is already pointing to your zone, validation happens automatically.

### Ownership Verification

The custom hostname response includes ownership verification data:

```json
{
  "ownership_verification": {
    "name": "_cf-custom-hostname.www.tenant.com",
    "type": "TXT",
    "value": "abc123..."
  },
  "ownership_verification_http": {
    "http_url": "http://www.tenant.com/.well-known/cf-custom-hostname-challenge/abc123",
    "http_body": "abc123..."
  }
}
```

Tenants must complete one of these verification methods for the hostname to become active.

---

## 5. Fallback Origin

The fallback origin is the default destination for all custom hostnames that don't have a specific `custom_origin_server` set.

### Set Fallback Origin

```
PUT /zones/{zone_id}/custom_hostnames/fallback_origin
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `origin` | string | **Yes** | Origin hostname (e.g., `fallback.yourplatform.com`) |

**Python SDK:**
```python
client.custom_hostnames.fallback_origin.update(
    zone_id="my-zone-id",
    origin="tenants.yourplatform.com",
)
```

### Get Fallback Origin

```
GET /zones/{zone_id}/custom_hostnames/fallback_origin
```

### Delete Fallback Origin

```
DELETE /zones/{zone_id}/custom_hostnames/fallback_origin
```

---

## 6. Certificate Bundles

For custom hostnames using BYO (Bring Your Own) certificates, you can manage individual certificates within a bundle.

### Replace Certificate in Bundle

```
PUT /zones/{zone_id}/custom_hostnames/{hostname_id}/certificate_pack/{pack_id}/certificates/{cert_id}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `custom_certificate` | string | **Yes** | PEM-encoded certificate |
| `custom_key` | string | **Yes** | PEM-encoded private key |

Constraints: RSA can only replace RSA, ECDSA can only replace ECDSA.

### Delete Certificate from Bundle

```
DELETE /zones/{zone_id}/custom_hostnames/{hostname_id}/certificate_pack/{pack_id}/certificates/{cert_id}
```

Cannot delete the last certificate in a pack.

---

## 7. Multi-Tenant Integration Pattern

### Onboarding a Tenant's Custom Domain

```python
from cloudflare import Cloudflare

client = Cloudflare()
ZONE_ID = "your-zone-id"

def onboard_tenant_domain(tenant_id: str, domain: str):
    """
    Complete flow for adding a tenant's custom domain.
    Assumes your zone already has a fallback origin configured.
    """

    # 1. Create the custom hostname with HTTP DCV
    hostname = client.custom_hostnames.create(
        zone_id=ZONE_ID,
        hostname=domain,
        ssl={
            "method": "http",
            "type": "dv",
            "settings": {
                "min_tls_version": "1.2",
                "http2": "on",
            }
        },
        custom_metadata={
            "tenant_id": tenant_id,
        },
    )

    # 2. Return verification instructions for the tenant
    return {
        "custom_hostname_id": hostname.id,
        "status": hostname.status,
        "ssl_status": hostname.ssl.status if hostname.ssl else "pending",
        "verification": {
            "cname_target": "tenants.yourplatform.com",
            "txt_record": hostname.ownership_verification,
            "http_verification": hostname.ownership_verification_http,
        },
        "instructions": (
            f"Point {domain} via CNAME to tenants.yourplatform.com. "
            "SSL will be provisioned automatically once the CNAME is active."
        ),
    }


def check_tenant_domain_status(custom_hostname_id: str):
    """Check if the tenant's domain is active and SSL is provisioned."""
    hostname = client.custom_hostnames.get(
        custom_hostname_id=custom_hostname_id,
        zone_id=ZONE_ID,
    )
    return {
        "hostname": hostname.hostname,
        "status": hostname.status,
        "ssl_status": hostname.ssl.status if hostname.ssl else None,
    }


def remove_tenant_domain(custom_hostname_id: str):
    """Remove a tenant's custom domain."""
    client.custom_hostnames.delete(
        custom_hostname_id=custom_hostname_id,
        zone_id=ZONE_ID,
    )
```

### Using Custom Origin Per Tenant

If different tenants need different origins (e.g., different Pages projects):

```python
hostname = client.custom_hostnames.create(
    zone_id=ZONE_ID,
    hostname="www.tenant.com",
    custom_origin_server="tenant-123-landing.pages.dev",
    ssl={"method": "http", "type": "dv"},
    custom_metadata={"tenant_id": "tenant-123"},
)
```

### Using Custom Origin SNI

To pass the original request hostname to the origin (useful when your origin needs to know which tenant domain was requested):

```python
hostname = client.custom_hostnames.create(
    zone_id=ZONE_ID,
    hostname="www.tenant.com",
    custom_origin_server="tenants.yourplatform.com",
    custom_origin_sni=":request_host_header:",  # Passes the actual hostname as SNI
    ssl={"method": "http", "type": "dv"},
)
```
