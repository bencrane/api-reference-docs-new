# List Public Finetunes

`GET /accounts/{account_id}/ai/finetunes/public`

Lists publicly available fine-tuned models that can be used with Workers AI.

## Parameters

- **account_id** (string, required) [path]: 
- **limit** (number, optional) [query]: Pagination Limit
- **offset** (number, optional) [query]: Pagination Offset
- **orderBy** (string, optional) [query]: Order By Column Name

## Response

### 200

Returns all public finetunes

- **result** (array): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
