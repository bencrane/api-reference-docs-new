# Create On-ramp

`POST /accounts/{account_id}/magic/cloud/onramps`

Create a new On-ramp (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **forwarded** (string, optional) [header]: 

## Request Body

- **adopted_hub_id** (string, optional): 
- **attached_hubs** (array, optional): 
- **attached_vpcs** (array, optional): 
- **cloud_asn** (integer, optional): Sets the cloud-side ASN. If unset or zero, the cloud's default ASN takes effect.
- **cloud_type** (string, required):  Values: `AWS`, `AZURE`, `GOOGLE`
- **description** (string, optional): 
- **dynamic_routing** (boolean, required): Enables BGP routing. When enabling this feature, set both install_routes_in_cloud and install_routes_in_magic_wan to false.
- **hub_provider_id** (string, optional): 
- **install_routes_in_cloud** (boolean, required): 
- **install_routes_in_magic_wan** (boolean, required): 
- **manage_hub_to_hub_attachments** (boolean, optional): 
- **manage_vpc_to_hub_attachments** (boolean, optional): 
- **name** (string, required): 
- **region** (string, optional): 
- **type** (string, required):  Values: `OnrampTypeSingle`, `OnrampTypeHub`
- **vpc** (string, optional): 

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
