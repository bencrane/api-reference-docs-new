# List Regions

`GET /accounts/{account_id}/load_balancers/regions`

List all region mappings.

## Parameters

- **account_id** (string, required) [path]: 
- **subdivision_code** (string, optional) [query]: 
- **subdivision_code_a2** (string, optional) [query]: 
- **country_code_a2** (string, optional) [query]: 

## Response

### 200

List Regions response.

- **result** (object, optional): 

### 4XX

List Regions response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
