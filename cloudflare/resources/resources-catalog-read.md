# Read Resource

`GET /accounts/{account_id}/magic/cloud/resources/{resource_id}`

Read an resource from the Resource Catalog (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **resource_id** (string, required) [path]: 
- **v2** (boolean, optional) [query]: 

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
