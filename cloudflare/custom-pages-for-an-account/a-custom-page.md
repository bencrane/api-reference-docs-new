# Get a custom page

`GET /accounts/{account_identifier}/custom_pages/{identifier}`

Fetches the details of a custom page.

## Parameters

- **identifier** (string, required) [path]: 
- **account_identifier** (string, required) [path]: 

## Response

### 200

Get a custom page response

- **result** (object, optional): 

### 4XX

Get a custom page response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
