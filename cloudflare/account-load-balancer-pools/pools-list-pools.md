# List Pools

`GET /accounts/{account_id}/load_balancers/pools`

List configured pools.

## Parameters

- **account_id** (string, required) [path]: 
- **monitor** (string, optional) [query]: 

## Response

### 200

List Pools response.

- **result** (array, optional): 

### 4XX

List Pools response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
