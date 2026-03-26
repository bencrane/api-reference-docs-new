# Update Zero Trust SSH settings

`PUT /accounts/{account_id}/gateway/audit_ssh_settings`

Update Zero Trust Audit SSH and SSH with Access for Infrastructure settings for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **public_key** (string, required): Provide the Base64-encoded HPKE public key that encrypts SSH session logs. See https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/use-cases/ssh/ssh-infrastructure-access/#enable-ssh-command-logging.

## Response

### 200

Update Zero Trust SSH settings response.

_Empty object_

### 4XX

Update Zero Trust SSH settings response failure.

_Empty object_
