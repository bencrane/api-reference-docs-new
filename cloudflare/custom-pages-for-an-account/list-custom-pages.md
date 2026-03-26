# List custom pages

`GET /accounts/{account_identifier}/custom_pages`

Fetches all the custom pages at the account level.

## Parameters

- **account_identifier** (string, required) [path]: 

## Response

### 200

List custom pages response

- **result** (array, optional): 

### 4XX

List custom pages response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
