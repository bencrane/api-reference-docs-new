# List Access application policies

`GET /accounts/{account_id}/access/apps/{app_id}/policies`

Lists Access policies configured for an application. Returns both exclusively scoped and reusable policies used by the application.

## Parameters

- **app_id** (string, required) [path]: The application ID.
- **account_id** (string, required) [path]: 
- **page** (integer, optional) [query]: 
- **per_page** (integer, optional) [query]: 

## Response

### 200

List Access application policies response

_Empty object_

### 4XX

List Access application policies response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
