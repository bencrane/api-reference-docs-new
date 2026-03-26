# Get Cloud Integration Setup Config

`GET /accounts/{account_id}/magic/cloud/providers/{provider_id}/initial_setup`

Get initial configuration to complete Cloud Integration setup (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **provider_id** (string, required) [path]: 

## Response

### 200

OK.

_Empty object_

### 400

Bad Request.

_Empty object_

### 401

Invalid Credentials.

_Empty object_

### 403

Forbidden.

_Empty object_

### 404

Not Found.

_Empty object_

### 500

Internal Server Error.

_Empty object_
