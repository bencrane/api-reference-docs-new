# Patch Cloud Integration

`PATCH /accounts/{account_id}/magic/cloud/providers/{provider_id}`

Update a Cloud Integration (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **provider_id** (string, required) [path]: 

## Request Body

- **aws_arn** (string, optional): 
- **azure_subscription_id** (string, optional): 
- **azure_tenant_id** (string, optional): 
- **description** (string, optional): 
- **friendly_name** (string, optional): 
- **gcp_project_id** (string, optional): 
- **gcp_service_account_email** (string, optional): 

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
