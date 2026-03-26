# Get a custom page

`GET /accounts/{account_id}/access/custom_pages/{custom_page_id}`

Fetches a custom page and also returns its HTML.

## Parameters

- **custom_page_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get a custom page response

_Empty object_

### 4XX

Get a custom page response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
