# Get Domain

`GET /accounts/{account_id}/workers/domains/{domain_id}`

Gets information about a domain.

## Parameters

- **account_id** (string, required) [path]: 
- **domain_id** (string, required) [path]: 

## Response

### 200

Get domain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Get domain failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
