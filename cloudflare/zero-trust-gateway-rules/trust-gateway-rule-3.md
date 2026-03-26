# Reset the expiration of a Zero Trust Gateway Rule

`POST /accounts/{account_id}/gateway/rules/{rule_id}/reset_expiration`

Resets the expiration of a Zero Trust Gateway Rule if its duration elapsed and it has a default duration. The Zero Trust Gateway Rule must have values  for both `expiration.expires_at` and `expiration.duration`.

## Parameters

- **rule_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Reset the expiration of a Zero Trust Gateway rule response.

_Empty object_

### 4XX

Reset the expiration of a Zero Trust Gateway rule response failure.

_Empty object_
