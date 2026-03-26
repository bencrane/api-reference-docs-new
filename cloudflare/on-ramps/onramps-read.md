# Read On-ramp

`GET /accounts/{account_id}/magic/cloud/onramps/{onramp_id}`

Read an On-ramp (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **onramp_id** (string, required) [path]: 
- **status** (boolean, optional) [query]: 
- **vpcs** (boolean, optional) [query]: 
- **post_apply_resources** (boolean, optional) [query]: 
- **planned_resources** (boolean, optional) [query]: 

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
