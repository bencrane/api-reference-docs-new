# Create Cloud Integration

`POST /accounts/{account_id}/magic/cloud/providers`

Create a new Cloud Integration (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **forwarded** (string, optional) [header]: 

## Request Body

- **cloud_type** (string, required):  Values: `AWS`, `AZURE`, `GOOGLE`, `CLOUDFLARE`
- **description** (string, optional): 
- **friendly_name** (string, required): 

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
