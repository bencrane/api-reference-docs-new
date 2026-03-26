# List On-ramps

`GET /accounts/{account_id}/magic/cloud/onramps`

List On-ramps (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **order_by** (string, optional) [query]: One of ["updated_at", "id", "cloud_type", "name"].
- **desc** (boolean, optional) [query]: 
- **status** (boolean, optional) [query]: 
- **vpcs** (boolean, optional) [query]: 

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

### 500

Internal Server Error.

_Empty object_
