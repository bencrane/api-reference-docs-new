# Rotate Zero Trust SSH account seed

`POST /accounts/{account_id}/gateway/audit_ssh_settings/rotate_seed`

Rotate the SSH account seed that generates the host key identity when connecting through the Cloudflare SSH Proxy.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Rotate Zero Trust SSH account seed response.

_Empty object_

### 4XX

Rotate Zero Trust SSH account seed response failure.

_Empty object_
