# Get Subdomain

`GET /accounts/{account_id}/workers/subdomain`

Returns a Workers subdomain for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get Subdomain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get Subdomain response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
