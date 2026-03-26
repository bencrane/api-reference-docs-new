# Delete On-ramp

`DELETE /accounts/{account_id}/magic/cloud/onramps/{onramp_id}`

Delete an On-ramp (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **onramp_id** (string, required) [path]: 
- **destroy** (boolean, optional) [query]: 
- **force** (boolean, optional) [query]: 

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

### 409

Conflict.

_Empty object_

### 500

Internal Server Error.

_Empty object_
