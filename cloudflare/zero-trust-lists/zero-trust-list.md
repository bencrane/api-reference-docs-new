# Create Zero Trust list

`POST /accounts/{account_id}/gateway/lists`

Creates a new Zero Trust list.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): Provide the list description.
- **items** (array, optional): Add items to the list.
- **name** (string, required): Specify the list name.
- **type** (string, required): Specify the list type. Values: `SERIAL`, `URL`, `DOMAIN`, `EMAIL`, `IP`, `CATEGORY`, `LOCATION`, `DEVICE`

## Response

### 200

Create Zero Trust list response.

_Empty object_

### 4XX

Create Zero Trust list response failure.

_Empty object_
