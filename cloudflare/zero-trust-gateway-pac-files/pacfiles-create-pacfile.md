# Create a PAC file

`POST /accounts/{account_id}/gateway/pacfiles`

Create a new Zero Trust Gateway PAC file.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **contents** (string, required): Actual contents of the PAC file
- **description** (string, optional): Detailed description of the PAC file.
- **name** (string, required): Name of the PAC file.
- **slug** (string, optional): URL-friendly version of the PAC file name. If not provided, it will be auto-generated

## Response

### 200

Returns a created PAC file response.

_Empty object_

### 4XX

Returns a created PAC file response failure.

_Empty object_
