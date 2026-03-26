# Delete a custom page

`DELETE /accounts/{account_id}/access/custom_pages/{custom_page_id}`

Delete a custom page

## Parameters

- **custom_page_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 202

Delete a custom page response

_Empty object_

### 4XX

Delete a custom page response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
