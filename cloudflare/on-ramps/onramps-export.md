# Export as Terraform

`POST /accounts/{account_id}/magic/cloud/onramps/{onramp_id}/export`

Export an On-ramp to terraform ready file(s) (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **onramp_id** (string, required) [path]: 

## Response

### 201

Exported file.

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

### 409

Conflict.

_Empty object_

### 500

Internal Server Error.

_Empty object_
