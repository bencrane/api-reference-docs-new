# List Domains

`GET /accounts/{account_id}/workers/domains`

Lists all domains for an account.

## Parameters

- **account_id** (string, required) [path]: 
- **zone_id** (string, optional) [query]: 
- **zone_name** (string, optional) [query]: 
- **service** (string, optional) [query]: 
- **hostname** (string, optional) [query]: 
- **environment** (string, optional) [query]: 

## Response

### 200

List domains response.

- **result** (array, optional): 

### 4XX

List domains failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
