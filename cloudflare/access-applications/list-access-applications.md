# List Access applications

`GET /accounts/{account_id}/access/apps`

Lists all Access applications in an account.

## Parameters

- **account_id** (string, required) [path]: 
- **name** (string, optional) [query]: 
- **domain** (string, optional) [query]: 
- **aud** (string, optional) [query]: 
- **target_attributes** (string, optional) [query]: 
- **exact** (boolean, optional) [query]: 
- **search** (string, optional) [query]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List Access applications response

_Empty object_

### 4XX

List Access applications response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
