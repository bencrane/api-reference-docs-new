# Get Zero Trust Connectivity Settings

`GET /accounts/{account_id}/zerotrust/connectivity_settings`

Gets the Zero Trust Connectivity Settings for the given account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Get Zero Trust Connectivity Settings response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get Zero Trust Connectivity Settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
