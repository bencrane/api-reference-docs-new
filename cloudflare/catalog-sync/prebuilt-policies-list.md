# List Prebuilt Policies

`GET /accounts/{account_id}/magic/cloud/catalog-syncs/prebuilt-policies`

List prebuilt catalog sync policies (Closed Beta).

## Parameters

- **account_id** (string, required) [path]: 
- **destination_type** (string, optional) [query]: Specify type of destination, omit to return all.

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

### 500

Internal Server Error.

_Empty object_
