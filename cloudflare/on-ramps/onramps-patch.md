# Patch On-ramp

`PATCH /accounts/{account_id}/magic/cloud/onramps/{onramp_id}`

Update an On-ramp (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **onramp_id** (string, required) [path]: 

## Request Body

- **attached_hubs** (array, optional): 
- **attached_vpcs** (array, optional): 
- **description** (string, optional): 
- **install_routes_in_cloud** (boolean, optional): 
- **install_routes_in_magic_wan** (boolean, optional): 
- **manage_hub_to_hub_attachments** (boolean, optional): 
- **manage_vpc_to_hub_attachments** (boolean, optional): 
- **name** (string, optional): 
- **vpc** (string, optional): 

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
