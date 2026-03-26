# Preview Rego Query

`POST /accounts/{account_id}/magic/cloud/resources/policy-preview`

Preview Rego query result against the latest resource catalog (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **policy** (string, required): 

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

### 422

Unprocessable Entity.

_Empty object_

### 500

Internal Server Error.

_Empty object_
