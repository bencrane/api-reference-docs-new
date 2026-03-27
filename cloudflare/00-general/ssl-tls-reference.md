# Cloudflare SSL/TLS API Reference

**Complete API reference for SSL/TLS certificate management — custom certificates, Origin CA, certificate packs, Universal SSL, Keyless SSL, per-hostname TLS settings, and authenticated origin pulls**

---

## Table of Contents

1. [SSL Architecture Overview](#1-ssl-architecture-overview)
2. [Custom SSL Certificates](#2-custom-ssl-certificates)
3. [Origin CA Certificates](#3-origin-ca-certificates)
4. [Advanced Certificate Packs](#4-advanced-certificate-packs)
5. [Universal SSL](#5-universal-ssl)
6. [Total TLS](#6-total-tls)
7. [SSL Verification](#7-ssl-verification)
8. [Per-Hostname TLS Settings](#8-per-hostname-tls-settings)
9. [Keyless SSL](#9-keyless-ssl)
10. [Per-Hostname Authenticated Origin Pull](#10-per-hostname-authenticated-origin-pull)

---

## 1. SSL Architecture Overview

Cloudflare terminates TLS at its edge. The SSL/TLS architecture has two segments:

```
Client ←→ Cloudflare Edge (edge certificate) ←→ Your Origin (origin certificate)
```

### Certificate Types

| Type | What It Does | When to Use |
|------|-------------|-------------|
| **Universal SSL** | Free auto-provisioned certificate for all proxied hostnames on a zone | Default — works automatically |
| **Advanced Certificate Pack** | Ordered certificate with CA choice, validity, and hostname control | When you need specific CAs or extended validity |
| **Custom SSL** | Upload your own certificate + private key | BYO certs from external CAs |
| **Origin CA** | Cloudflare-issued certificate for origin server ↔ Cloudflare edge encryption | Securing the origin-to-edge segment |
| **Custom Hostname SSL** | Auto-provisioned for custom hostnames (SSL for SaaS) | Multi-tenant custom domains (see custom-hostnames-reference.md) |
| **Total TLS** | Auto-orders hostname-specific certificates for all proxied records | When Universal SSL's coverage isn't sufficient |
| **Keyless SSL** | TLS termination without exposing private keys to Cloudflare | High-security enterprise requirement |

### SSL Mode (Edge → Origin)

Configure via zone settings (`PATCH /zones/{zone_id}/settings/ssl`):

| Mode | Behavior |
|------|----------|
| `off` | No HTTPS at all |
| `flexible` | HTTPS client→edge, HTTP edge→origin (not secure) |
| `full` | HTTPS both segments, but doesn't validate origin cert |
| `strict` | HTTPS both segments, validates origin cert against trusted CAs |

**Recommendation:** Always use `strict` with an Origin CA certificate on your origin server.

---

## 2. Custom SSL Certificates

Upload your own certificates (from any CA) to Cloudflare.

### Upload Custom Certificate

```
POST /zones/{zone_id}/custom_certificates
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `certificate` | string | **Yes** | PEM-encoded certificate (including intermediates) |
| `private_key` | string | **Yes** | PEM-encoded private key |
| `bundle_method` | string | No | `"ubiquitous"` (max compatibility), `"optimal"` (shortest chain), `"force"` (as-is) |
| `type` | string | No | `"legacy_custom"` (supports non-SNI clients) or `"sni_custom"` (SNI only, default) |
| `deploy` | string | No | `"staging"` or `"production"` (default) |
| `geo_restrictions` | object | No | Restrict key to US, EU, or highest-security data centers |
| `policy` | string | No | Country-based key restriction (e.g., `"country: US"`, `"region: EU"`) |
| `custom_csr_id` | string | No | Link to a Custom CSR |

**Python SDK:**
```python
cert = client.custom_certificates.create(
    zone_id="my-zone-id",
    certificate=open("cert.pem").read(),
    private_key=open("key.pem").read(),
    bundle_method="optimal",
    type="sni_custom",
)
```

### List Custom Certificates

```
GET /zones/{zone_id}/custom_certificates
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | number | Page number |
| `per_page` | number | Results per page |
| `match` | string | Filter mode |
| `status` | string | Filter by status |

### Get Certificate Details

```
GET /zones/{zone_id}/custom_certificates/{custom_certificate_id}
```

### Edit Certificate

```
PATCH /zones/{zone_id}/custom_certificates/{custom_certificate_id}
```

Upload a new certificate/key pair. **Note:** PATCHing an `sni_custom` certificate creates a new resource ID and deletes the previous one.

| Field | Type | Description |
|-------|------|-------------|
| `certificate` | string | Updated PEM certificate |
| `private_key` | string | Updated PEM private key |
| `bundle_method` | string | Bundle method |
| `deploy` | string | `"staging"` or `"production"` |
| `geo_restrictions` | object | Geo restriction config |
| `policy` | string | Country/region policy |

### Delete Certificate

```
DELETE /zones/{zone_id}/custom_certificates/{custom_certificate_id}
```

### Prioritize Certificates

```
PUT /zones/{zone_id}/custom_certificates/prioritize
```

Set the order of `legacy_custom` certificates. Higher priority breaks ties.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `certificates` | array | **Yes** | Array of `{ "id": "cert-id", "priority": 1 }` |

---

## 3. Origin CA Certificates

Cloudflare-issued certificates for securing the connection between your origin server and Cloudflare's edge. Free, valid up to 15 years.

### Create Origin Certificate

```
POST /certificates
```

> **Note:** This endpoint uses the base URL without `/client/v4`. Authentication uses an API token or Origin CA Key.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `csr` | string | **Yes** | PEM-encoded Certificate Signing Request (newline-encoded) |
| `hostnames` | array | **Yes** | FQDNs or wildcards (e.g., `["example.com", "*.example.com"]`). Must belong to zones on your account. |
| `request_type` | string | **Yes** | `"origin-rsa"`, `"origin-ecc"`, or `"keyless-certificate"` |
| `requested_validity` | number | No | Days: `7`, `30`, `90`, `365`, `730`, `1095`, `5475` (15 years, default) |

**Hostname rules:**
- Wildcards: Only `*.domain.com` format (single level)
- No double wildcards (`*.*.domain.com`)
- No interior wildcards (`foo.*.domain.com`)
- Unicode hostnames auto-converted to Punycode

**Python SDK:**
```python
origin_cert = client.origin_ca_certificates.create(
    csr=open("origin.csr").read(),
    hostnames=["example.com", "*.example.com"],
    request_type="origin-rsa",
    requested_validity=5475,
)
print(origin_cert.certificate)  # PEM cert to install on origin
```

### List Origin Certificates

```
GET /certificates
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `zone_id` | string | query | **Required** — filter by zone |
| `page` | number | query | Page number |
| `per_page` | number | query | Results per page |
| `limit` | integer | query | Max results |
| `offset` | integer | query | Skip N results |

### Get Origin Certificate

```
GET /certificates/{certificate_id}
```

### Revoke Origin Certificate

```
DELETE /certificates/{certificate_id}
```

---

## 4. Advanced Certificate Packs

Order certificates from specific CAs with custom validity and hostname coverage.

### Order Advanced Certificate Pack

```
POST /zones/{zone_id}/ssl/certificate_packs/order
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `certificate_authority` | string | **Yes** | `"google"`, `"lets_encrypt"`, or `"ssl_com"` |
| `hosts` | array | **Yes** | Hostnames for the certificate. Must include the zone apex. Max 50 hosts. |
| `type` | string | **Yes** | `"advanced"` |
| `validation_method` | string | **Yes** | `"txt"`, `"http"`, or `"email"` |
| `validity_days` | integer | **Yes** | `14`, `30`, `90`, or `365` |
| `cloudflare_branding` | boolean | No | Add Cloudflare branding subdomain as Common Name |

**Python SDK:**
```python
pack = client.certificate_packs.create(
    zone_id="my-zone-id",
    certificate_authority="lets_encrypt",
    hosts=["example.com", "*.example.com"],
    type="advanced",
    validation_method="txt",
    validity_days=90,
)
```

### List Certificate Packs

```
GET /zones/{zone_id}/ssl/certificate_packs
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | number | Page number |
| `per_page` | number | Results per page |
| `status` | string | Filter by status |
| `deploy` | string | Filter by deploy environment |

### Get Certificate Pack

```
GET /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}
```

### Restart Validation / Add Branding

```
PATCH /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}
```

| Field | Type | Description |
|-------|------|-------------|
| `cloudflare_branding` | boolean | Add/remove Cloudflare branding |

Also restarts validation for packs in `validation_timed_out` status.

### Delete Certificate Pack

```
DELETE /zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}
```

### Get Certificate Pack Quotas

```
GET /zones/{zone_id}/ssl/certificate_packs/quota
```

---

## 5. Universal SSL

Universal SSL provides free, auto-provisioned certificates for all proxied hostnames on a zone.

### Get Universal SSL Settings

```
GET /zones/{zone_id}/ssl/universal/settings
```

### Edit Universal SSL Settings

```
PATCH /zones/{zone_id}/ssl/universal/settings
```

| Field | Type | Description |
|-------|------|-------------|
| `enabled` | boolean | Enable/disable Universal SSL. **Disabling removes all Universal SSL certificates and prevents new ones from being issued.** If no custom/advanced certificates exist, the zone will be inaccessible over HTTPS. |

> **Warning:** Disabling Universal SSL while HSTS, Always Use HTTPS, or HTTP→HTTPS redirects are enabled will make your site inaccessible.

---

## 6. Total TLS

Total TLS automatically orders hostname-specific certificates for every proxied A, AAAA, or CNAME record in your zone.

### Get Total TLS Settings

```
GET /zones/{zone_id}/acm/total_tls
```

### Enable/Disable Total TLS

```
POST /zones/{zone_id}/acm/total_tls
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `enabled` | boolean | **Yes** | Enable or disable Total TLS |
| `certificate_authority` | string | No | CA for certificates: `"google"`, `"lets_encrypt"`, or `"ssl_com"` |

---

## 7. SSL Verification

Check and manage SSL certificate validation status.

### Get SSL Verification Details

```
GET /zones/{zone_id}/ssl/verification
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `retry` | string | If present, triggers a validation retry |

Returns an array of verification records with validation status for each certificate pack.

### Edit Validation Method

```
PATCH /zones/{zone_id}/ssl/verification/{certificate_pack_id}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `validation_method` | string | **Yes** | `"http"`, `"cname"`, `"txt"`, or `"email"` |

Triggers an immediate validation check using the specified method.

### SSL/TLS Recommendation (Deprecated)

```
GET /zones/{zone_id}/ssl/recommendation
```

Returns Cloudflare's recommended SSL mode for the zone.

---

## 8. Per-Hostname TLS Settings

Override TLS settings for specific hostnames within a zone. Useful for applying different minimum TLS versions or cipher suites to different tenants.

### List Settings for a Zone

```
GET /zones/{zone_id}/hostnames/settings/{setting_id}
```

### Get Setting for a Hostname

```
GET /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}
```

### Set Setting for a Hostname

```
PUT /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}
```

| Setting ID | Value Type | Example | Description |
|-----------|-----------|---------|-------------|
| `ciphers` | array of strings | `["ECDHE-RSA-AES128-GCM-SHA256"]` | Allowed cipher suites (BoringSSL format) |
| `min_tls_version` | string | `"1.2"` | Minimum TLS version: `"1.0"`, `"1.1"`, `"1.2"`, `"1.3"` |
| `http2` | string | `"on"` | HTTP/2: `"on"` or `"off"` |

### Delete Setting for a Hostname

```
DELETE /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}
```

Reverts to zone-level defaults.

---

## 9. Keyless SSL

Keyless SSL allows TLS termination without sending private keys to Cloudflare. The private key stays on your infrastructure; Cloudflare contacts your keyless server for cryptographic operations.

### Create Keyless SSL Configuration

```
POST /zones/{zone_id}/keyless_certificates
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `certificate` | string | **Yes** | PEM-encoded certificate |
| `host` | string | **Yes** | Keyless SSL server hostname |
| `port` | number | **Yes** | Keyless SSL server port |
| `name` | string | No | Friendly name |
| `bundle_method` | string | No | `"ubiquitous"`, `"optimal"`, `"force"` |
| `tunnel` | object | No | Config for using Keyless SSL through a Cloudflare Tunnel |

### List Keyless SSL Configurations

```
GET /zones/{zone_id}/keyless_certificates
```

### Get Keyless SSL Configuration

```
GET /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}
```

### Edit Keyless SSL Configuration

```
PATCH /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}
```

| Field | Type | Description |
|-------|------|-------------|
| `enabled` | boolean | Enable/disable the keyless server |
| `host` | string | Update server hostname |
| `port` | number | Update server port |
| `name` | string | Update friendly name |
| `tunnel` | object | Tunnel configuration |

### Delete Keyless SSL Configuration

```
DELETE /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}
```

---

## 10. Per-Hostname Authenticated Origin Pull

Authenticated Origin Pulls use client certificates to verify that requests to your origin are from Cloudflare. Per-hostname configuration allows different certificates for different hostnames.

### Upload Hostname Client Certificate

```
POST /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `certificate` | string | **Yes** | PEM-encoded client certificate |
| `private_key` | string | **Yes** | PEM-encoded private key |

Maximum 10 hostname certificates per zone.

### List Hostname Client Certificates

```
GET /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates
```

### Get Hostname Client Certificate

```
GET /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}
```

### Delete Hostname Client Certificate

```
DELETE /zones/{zone_id}/origin_tls_client_auth/hostnames/certificates/{certificate_id}
```

> **Important:** Before deleting, you must first invalidate the association by sending a PUT with `enabled` set to `null`.

### Enable/Disable for Hostnames

```
PUT /zones/{zone_id}/origin_tls_client_auth/hostnames
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `config` | array | **Yes** | Array of `{ "hostname": "example.com", "cert_id": "cert-id", "enabled": true }` |

Maximum 100 associations per certificate. Set `enabled` to `null` to invalidate.

### Get Hostname Status

```
GET /zones/{zone_id}/origin_tls_client_auth/hostnames/{hostname}
```

### List Hostname Associations

```
GET /zones/{zone_id}/origin_tls_client_auth/hostnames
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `page` | number | Page number |
| `per_page` | number | Results per page |
| `status` | string | Filter by status |
