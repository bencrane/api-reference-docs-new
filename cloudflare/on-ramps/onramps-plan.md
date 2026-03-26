# Plan On-ramp

`POST /accounts/{account_id}/magic/cloud/onramps/{onramp_id}/plan`

Plan an On-ramp (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **onramp_id** (string, required) [path]: 

## Response

### 202

Accepted.

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

### 409

Conflict.

_Empty object_

### 500

Internal Server Error.

_Empty object_
