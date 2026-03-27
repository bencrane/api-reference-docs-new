# Cloudflare Pages API Reference

**Complete API reference for Cloudflare Pages — programmatic static site deployment, direct asset upload, custom domains, and deployment management**

This is the most critical section for a multi-tenant landing page platform. Pages provides the hosting layer: create a project, upload pre-built HTML/CSS/JS directly (no git required), attach custom domains, and manage deployments — all via API.

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Projects](#2-projects)
3. [Deployments (Direct Upload)](#3-deployments-direct-upload)
4. [Custom Domains](#4-custom-domains)
5. [Build Cache](#5-build-cache)
6. [Deployment Configuration](#6-deployment-configuration)
7. [SDK Examples — End-to-End](#7-sdk-examples--end-to-end)

---

## 1. Architecture Overview

Cloudflare Pages is a JAMstack platform that serves static assets from Cloudflare's edge network. For programmatic use:

- **No git required** — the Direct Upload API lets you push pre-built assets as a deployment
- **Instant global deployment** — assets are distributed to 300+ edge locations
- **Automatic SSL** — every deployment gets HTTPS automatically
- **Preview deployments** — non-production branches get unique preview URLs
- **Pages Functions** — optional server-side logic via `_worker.js` (runs as a Worker)

### Key Concepts

| Concept | Description |
|---------|-------------|
| **Project** | A named container for deployments. Has a `production_branch`, build config, and deployment configs. |
| **Deployment** | A point-in-time snapshot of assets. Each deployment gets a unique URL. The latest production deployment is served at the project's domain. |
| **Direct Upload** | Upload pre-built assets directly via API (multipart form), bypassing git and the build system entirely. |
| **Custom Domain** | A domain (e.g., `landing.tenant.com`) pointed at a Pages project. SSL is auto-provisioned. |
| **Production Branch** | The branch name whose deployments are served at the primary domain. Other branch names create preview deployments. |

### URL Structure

- **Production:** `https://{project-name}.pages.dev`
- **Preview:** `https://{commit-hash}.{project-name}.pages.dev`
- **Custom domain:** `https://your-custom-domain.com` (after DNS setup)

---

## 2. Projects

### Create Project

```
POST /accounts/{account_id}/pages/projects
```

Creates a new Pages project. For programmatic deployment (no git), you still need to create the project first, then deploy to it.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | **Yes** | Project name. Becomes the `{project-name}.pages.dev` subdomain. Must be unique within the account. |
| `production_branch` | string | **Yes** | Branch name for production deployments (e.g., `"main"`). Deployments with this branch name serve at the primary domain. |
| `build_config` | object | No | Build configuration (irrelevant for direct upload). |
| `deployment_configs` | object | No | Environment-specific configs for preview and production (env vars, bindings, compatibility settings). |
| `source` | object | No | Git source control config (skip for direct upload). |

**`build_config` schema** (optional, for git-connected projects):

| Field | Type | Description |
|-------|------|-------------|
| `build_command` | string | Shell command to run (e.g., `npm run build`) |
| `destination_dir` | string | Output directory (e.g., `dist`, `build`, `out`) |
| `root_dir` | string | Working directory for the build |
| `build_caching` | boolean | Enable build dependency caching |

**`deployment_configs` schema** (each of `preview` and `production` supports):

| Field | Type | Description |
|-------|------|-------------|
| `env_vars` | object | Environment variables: `{ "KEY": { "value": "val" } }`. Set value to `null` to delete. |
| `kv_namespaces` | object | KV namespace bindings: `{ "BINDING_NAME": { "namespace_id": "..." } }` |
| `d1_databases` | object | D1 database bindings |
| `r2_buckets` | object | R2 bucket bindings |
| `durable_object_namespaces` | object | Durable Object bindings |
| `services` | object | Service bindings |
| `queue_producers` | object | Queue producer bindings |
| `ai_bindings` | object | Workers AI bindings |
| `vectorize_bindings` | object | Vectorize bindings |
| `hyperdrive_bindings` | object | Hyperdrive bindings |
| `compatibility_date` | string | Workers compatibility date |
| `compatibility_flags` | array | Workers compatibility flags |
| `placement` | object | Smart placement config: `{ "mode": "smart" }` |

**Python SDK:**
```python
project = client.pages.projects.create(
    account_id="my-account-id",
    name="tenant-landing-pages",
    production_branch="main",
    deployment_configs={
        "production": {
            "env_vars": {
                "API_URL": {"value": "https://api.myplatform.com"}
            }
        }
    }
)
print(project.name)       # "tenant-landing-pages"
print(project.subdomain)  # "tenant-landing-pages.pages.dev"
```

**TypeScript SDK:**
```typescript
const project = await client.pages.projects.create({
  account_id: 'my-account-id',
  name: 'tenant-landing-pages',
  production_branch: 'main',
});
```

### List Projects

```
GET /accounts/{account_id}/pages/projects
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `account_id` | string | path | **Required** |
| `page` | integer | query | Page number |
| `per_page` | integer | query | Results per page |

### Get Project

```
GET /accounts/{account_id}/pages/projects/{project_name}
```

Returns full project details including latest deployment, domains, and configuration.

### Update Project

```
PATCH /accounts/{account_id}/pages/projects/{project_name}
```

Modify project settings. **To delete an environment variable, set its key to `null` in `env_vars`.**

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Rename the project |
| `production_branch` | string | Change the production branch |
| `build_config` | object | Update build settings |
| `deployment_configs` | object | Update env vars, bindings, etc. |

### Delete Project

```
DELETE /accounts/{account_id}/pages/projects/{project_name}
```

Permanently deletes the project, all deployments, and removes custom domains. **This is irreversible.**

---

## 3. Deployments (Direct Upload)

This is the core workflow for programmatic landing page deployment. You upload pre-built assets directly — no git, no build step on Cloudflare's side.

### Create Deployment (Direct Upload)

```
POST /accounts/{account_id}/pages/projects/{project_name}/deployments
```

**Content-Type:** `multipart/form-data`

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `manifest` | string | No | JSON string mapping file paths to content hashes |
| `branch` | string | No | Branch name. If it matches `production_branch`, this becomes a production deployment. Otherwise it's a preview. |
| `commit_hash` | string | No | Git commit hash (metadata only) |
| `commit_message` | string | No | Commit message (metadata only) |
| `commit_dirty` | string | No | `"true"` or `"false"` |
| `_headers` | file | No | Custom headers file (Cloudflare Pages `_headers` format) |
| `_redirects` | file | No | Redirects file (Cloudflare Pages `_redirects` format) |
| `_routes.json` | file | No | Routes configuration |
| `_worker.js` | file | No | Pages Functions Worker script |
| `_worker.bundle` | file | No | Bundled Pages Functions |

> **Gap:** The scraped API docs don't fully document the direct upload multipart format. The SDK source reveals that you upload files as individual multipart parts with their file paths as the part names. The `manifest` field maps these paths to content hashes for deduplication. For the exact upload protocol, refer to the SDK implementations or use Wrangler CLI's `pages deploy` command which handles this transparently.

**Python SDK — Direct Upload:**
```python
deployment = client.pages.projects.deployments.create(
    project_name="tenant-landing-pages",
    account_id="my-account-id",
    branch="main",                        # Production deployment
    commit_message="Deploy tenant-123 landing page",
)
```

**TypeScript SDK — Direct Upload:**
```typescript
const deployment = await client.pages.projects.deployments.create(
  'tenant-landing-pages',
  {
    account_id: 'my-account-id',
    branch: 'main',
    commit_message: 'Deploy tenant-123 landing page',
  }
);
```

**Using Wrangler CLI (alternative — simpler for direct upload):**
```bash
# Deploy a directory of pre-built assets
npx wrangler pages deploy ./dist --project-name=tenant-landing-pages

# With branch for preview deployment
npx wrangler pages deploy ./dist --project-name=tenant-landing-pages --branch=preview-tenant-123
```

### List Deployments

```
GET /accounts/{account_id}/pages/projects/{project_name}/deployments
```

| Parameter | Type | Location | Description |
|-----------|------|----------|-------------|
| `env` | string | query | Filter by environment: `"production"` or `"preview"` |
| `page` | integer | query | Page number |
| `per_page` | integer | query | Results per page |

### Get Deployment Info

```
GET /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}
```

### Get Deployment Logs

```
GET /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/history/logs
```

Returns build and deployment logs — useful for debugging failed deployments.

### Retry Deployment

```
POST /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/retry
```

Re-runs a failed deployment.

### Rollback Deployment

```
POST /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}/rollback
```

Rolls back production to a previous successful deployment. **Only works for production deployments.**

### Delete Deployment

```
DELETE /accounts/{account_id}/pages/projects/{project_name}/deployments/{deployment_id}
```

---

## 4. Custom Domains

Attach custom domains to a Pages project. Cloudflare automatically provisions SSL certificates.

### Add Domain

```
POST /accounts/{account_id}/pages/projects/{project_name}/domains
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | **Yes** | The domain name (e.g., `landing.tenant.com` or `www.tenant-domain.com`) |

**Prerequisites:**
- The domain (or its parent zone) must be on Cloudflare (added as a zone in the same account)
- A CNAME record pointing the domain to `{project-name}.pages.dev` must exist (or will be created)

**Python SDK:**
```python
domain = client.pages.projects.domains.create(
    project_name="tenant-landing-pages",
    account_id="my-account-id",
    name="landing.tenant-domain.com"
)
print(domain.status)  # "initializing" → "pending" → "active"
```

**TypeScript SDK:**
```typescript
const domain = await client.pages.projects.domains.create(
  'tenant-landing-pages',
  { account_id: 'my-account-id', name: 'landing.tenant-domain.com' }
);
```

### List Domains

```
GET /accounts/{account_id}/pages/projects/{project_name}/domains
```

### Get Domain

```
GET /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}
```

Returns domain status including SSL provisioning state.

### Retry Domain Validation

```
PATCH /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}
```

Triggers a new validation check. Use when DNS has been updated and you need to re-verify.

### Delete Domain

```
DELETE /accounts/{account_id}/pages/projects/{project_name}/domains/{domain_name}
```

---

## 5. Build Cache

### Purge Build Cache

```
POST /accounts/{account_id}/pages/projects/{project_name}/purge_build_cache
```

Clears all cached build artifacts. Relevant for git-connected projects; not typically needed for direct upload workflows.

---

## 6. Deployment Configuration

### Environment Variables

Set via `deployment_configs` on the project. Separate configs for `preview` and `production`:

```python
client.pages.projects.edit(
    project_name="tenant-landing-pages",
    account_id="my-account-id",
    deployment_configs={
        "production": {
            "env_vars": {
                "TENANT_ID": {"value": "tenant-123"},
                "API_KEY": {"value": "secret-key"},
                "REMOVED_VAR": None  # Setting to None deletes it
            }
        }
    }
)
```

### Bindings

Pages Functions (`_worker.js`) can access Cloudflare services via bindings:

| Binding Type | Config Key | Example |
|-------------|-----------|---------|
| KV Namespace | `kv_namespaces` | `{ "CACHE": { "namespace_id": "abc123" } }` |
| R2 Bucket | `r2_buckets` | `{ "ASSETS": { "name": "tenant-assets" } }` |
| D1 Database | `d1_databases` | `{ "DB": { "id": "abc123" } }` |
| Durable Object | `durable_object_namespaces` | `{ "COUNTER": { "namespace_id": "abc123" } }` |
| Service | `services` | `{ "API": { "service": "my-worker", "environment": "production" } }` |
| Queue | `queue_producers` | `{ "QUEUE": { "name": "my-queue" } }` |
| AI | `ai_bindings` | `{ "AI": {} }` |

### `_headers` File Format

Controls HTTP response headers for specific paths:

```
/assets/*
  Cache-Control: public, max-age=31536000, immutable

/*
  X-Frame-Options: DENY
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
```

### `_redirects` File Format

Define URL redirects:

```
/old-page  /new-page  301
/blog/*    https://blog.example.com/:splat  302
```

---

## 7. SDK Examples — End-to-End

### Complete Tenant Landing Page Deployment (Python)

```python
from cloudflare import Cloudflare

client = Cloudflare()
ACCOUNT_ID = "your-account-id"

# 1. Create project (one-time per tenant or shared)
project = client.pages.projects.create(
    account_id=ACCOUNT_ID,
    name="tenant-123-landing",
    production_branch="main",
)

# 2. Deploy pre-built assets (using Wrangler CLI is easier for file upload)
#    Via API, use the multipart deployment endpoint
deployment = client.pages.projects.deployments.create(
    project_name="tenant-123-landing",
    account_id=ACCOUNT_ID,
    branch="main",
    commit_message="Initial landing page deploy",
)

# 3. Add custom domain
#    First, create CNAME record (see dns-reference.md)
client.dns.records.create(
    zone_id="tenant-zone-id",
    name="www",
    type="CNAME",
    content="tenant-123-landing.pages.dev",
    proxied=True,
    ttl=1,  # automatic
)

#    Then attach the domain to the project
domain = client.pages.projects.domains.create(
    project_name="tenant-123-landing",
    account_id=ACCOUNT_ID,
    name="www.tenant-domain.com",
)

# 4. Check domain status
domain_info = client.pages.projects.domains.get(
    project_name="tenant-123-landing",
    domain_name="www.tenant-domain.com",
    account_id=ACCOUNT_ID,
)
print(f"Domain status: {domain_info.status}")

# 5. Deploy an update
new_deployment = client.pages.projects.deployments.create(
    project_name="tenant-123-landing",
    account_id=ACCOUNT_ID,
    branch="main",
    commit_message="Update hero section copy",
)

# 6. Rollback if needed
client.pages.projects.deployments.rollback(
    deployment_id=deployment.id,  # Roll back to original
    project_name="tenant-123-landing",
    account_id=ACCOUNT_ID,
)
```

### Multi-Tenant Pattern: Shared Project with Branch Deploys

Instead of one project per tenant, you can use a single project with branch-based preview deployments:

```python
# Each tenant gets a preview URL: {branch}.{project}.pages.dev
deployment = client.pages.projects.deployments.create(
    project_name="landing-pages",
    account_id=ACCOUNT_ID,
    branch="tenant-456",  # Creates preview deployment
    commit_message="Deploy tenant-456 landing page",
)
# Preview URL: tenant-456.landing-pages.pages.dev
```

> **Gap:** The direct upload API's exact multipart file upload protocol (how individual asset files map to form parts) is not fully documented in the scraped API reference. The SDKs and Wrangler CLI abstract this, but for raw HTTP implementation, you may need to reference the Wrangler source code (`pages-action` repo or `workers-sdk` repo) for the upload protocol details.
