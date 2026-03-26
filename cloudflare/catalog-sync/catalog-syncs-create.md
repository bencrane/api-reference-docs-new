# Create Catalog Sync

`POST /accounts/{account_id}/magic/cloud/catalog-syncs`

Create a new Catalog Sync (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **forwarded** (string, optional) [header]: 

## Request Body

- **description** (string, optional): 
- **destination_type** (string, required):  Values: `NONE`, `ZERO_TRUST_LIST`
- **name** (string, required): 
- **policy** (string, optional): 
- **update_mode** (string, required):  Values: `AUTO`, `MANUAL`

## Response

### 201

Created.

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

### 409

Conflict.

_Empty object_

### 422

Unprocessable Entity.

_Empty object_

### 500

Internal Server Error.

_Empty object_
