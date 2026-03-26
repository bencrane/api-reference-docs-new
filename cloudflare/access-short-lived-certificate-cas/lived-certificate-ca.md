# Delete a short-lived certificate CA

`DELETE /accounts/{account_id}/access/apps/{app_id}/ca`

Deletes a short-lived certificate CA.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 202

Delete a short-lived certificate CA response

_Empty object_

### 4XX

Delete a short-lived certificate CA response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
