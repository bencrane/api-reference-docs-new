# Get a custom asset

`GET /accounts/{account_identifier}/custom_pages/assets/{asset_name}`

Fetches the details of a custom asset.

## Parameters

- **asset_name** (string, required) [path]: 
- **account_identifier** (string, required) [path]: 

## Response

### 200

Get a custom asset response

- **result** (object, optional): 

### 4XX

Get a custom asset response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
