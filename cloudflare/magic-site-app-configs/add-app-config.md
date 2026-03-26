# Create a new App Config

`POST /accounts/{account_id}/magic/sites/{site_id}/app_configs`

Creates a new App Config for a site

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 201

Create Site App Config response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): Traffic decision configuration for an app.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Create Site App Config response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
