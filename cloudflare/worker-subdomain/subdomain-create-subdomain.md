# Create Subdomain

`PUT /accounts/{account_id}/workers/subdomain`

Creates a Workers subdomain for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **subdomain** (string, required): 

## Response

### 200

Create Subdomain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create Subdomain response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
