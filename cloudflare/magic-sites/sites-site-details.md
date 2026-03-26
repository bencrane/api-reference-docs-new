# Site Details

`GET /accounts/{account_id}/magic/sites/{site_id}`

Get a specific Site.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **x-magic-new-hc-target** (boolean, optional) [header]: If true, the health check target in the response body will be presented using the new object format. Defaults to false.

## Response

### 200

Site Details response

- **result** (object, optional): 

### 4XX

Site Details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
