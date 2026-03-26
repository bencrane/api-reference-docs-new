# Get your Zero Trust organization DoH settings

`GET /accounts/{account_id}/access/organizations/doh`

Returns the DoH settings for your Zero Trust organization.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get your Zero Trust organization DoH settings response

- **result** (object, optional): 

### 4XX

Get your Zero Trust organization DoH settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
