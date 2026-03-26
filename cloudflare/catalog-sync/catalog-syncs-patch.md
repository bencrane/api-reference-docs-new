# Patch Catalog Sync

`PATCH /accounts/{account_id}/magic/cloud/catalog-syncs/{sync_id}`

Update a Catalog Sync (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **sync_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): 
- **name** (string, optional): 
- **policy** (string, optional): 
- **update_mode** (string, optional):  Values: `AUTO`, `MANUAL`

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

### 422

Unprocessable Entity.

_Empty object_

### 500

Internal Server Error.

_Empty object_
