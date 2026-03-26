# Delete a PAC file

`DELETE /accounts/{account_id}/gateway/pacfiles/{pacfile_id}`

Delete a configured Zero Trust Gateway PAC file.

## Parameters

- **pacfile_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Returns a deleted PAC file response.

_Empty object_

### 4XX

Returns a deleted PAC file response failure.

_Empty object_
