# Get Domain History

`GET /accounts/{account_id}/intel/domain-history`

Gets historical security threat and content categories currently and previously assigned to a domain.

## Parameters

- **account_id** (string, required) [path]: 
- **domain** (string, optional) [query]: 

## Response

### 200

Get Domain History response.

_Empty object_

### 4XX

Get Domain History response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
