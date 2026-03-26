# Export Resources

`GET /accounts/{account_id}/magic/cloud/resources/export`

Export resources in the Resource Catalog as a JSON file (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **provider_id** (string, optional) [query]: 
- **resource_type** (array, optional) [query]: 
- **resource_id** (array, optional) [query]: 
- **region** (string, optional) [query]: 
- **resource_group** (string, optional) [query]: 
- **search** (array, optional) [query]: 
- **order_by** (string, optional) [query]: One of ["id", "resource_type", "region"].
- **desc** (boolean, optional) [query]: 
- **v2** (boolean, optional) [query]: 

## Response

### 200

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

### 500

Internal Server Error.

_Empty object_
