# Get Domain Details

`GET /accounts/{account_id}/intel/domain`

Gets security details and statistics about a domain.

## Parameters

- **account_id** (string, required) [path]: 
- **domain** (string, optional) [query]: 

## Response

### 200

Get Domain Details response.

_Empty object_

### 4XX

Get Domain Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful.
