# Patch Magic WAN Address Space

`PATCH /accounts/{account_id}/magic/cloud/onramps/magic_wan_address_space`

Update the Magic WAN Address Space (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **prefixes** (array, required): 

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

### 422

Unprocessable Entity.

_Empty object_

### 500

Internal Server Error.

_Empty object_
