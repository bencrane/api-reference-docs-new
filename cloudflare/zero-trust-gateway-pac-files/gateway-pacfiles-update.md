# Update a Zero Trust Gateway PAC file

`PUT /accounts/{account_id}/gateway/pacfiles/{pacfile_id}`

Update a configured Zero Trust Gateway PAC file.

## Parameters

- **pacfile_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **contents** (string, required): Actual contents of the PAC file
- **description** (string, required): Detailed description of the PAC file.
- **name** (string, required): Name of the PAC file.

## Response

### 200

Update a Zero Trust Gateway PAC file response.

_Empty object_

### 4XX

Update a Zero Trust Gateway PAC file response failure.

_Empty object_
