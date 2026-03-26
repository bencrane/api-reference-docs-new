# Get a Web Analytics site

`GET /accounts/{account_id}/rum/site_info/{site_id}`

Retrieves a Web Analytics site.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Response

### 200

Web Analytics site.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
