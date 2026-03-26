# Delete an Access application

`DELETE /accounts/{account_id}/access/apps/{app_id}`

Deletes an application from Access.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 202

Delete an Access application response

_Empty object_

### 4XX

Delete an Access application response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
