# Get indicator feeds owned by this account

`GET /accounts/{account_id}/intel/indicator-feeds`

Retrieves details for all accessible custom threat indicator feeds.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get indicator feeds response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

Get indicator feeds response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
