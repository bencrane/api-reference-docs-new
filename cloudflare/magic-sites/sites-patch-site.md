# Patch Site

`PATCH /accounts/{account_id}/magic/sites/{site_id}`

Patch a specific Site.

## Parameters

- **site_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **connector_id** (string, optional): Magic Connector identifier tag.
- **description** (string, optional): 
- **location** (object, optional): Location of site in latitude and longitude.
- **name** (string, optional): The name of the site.
- **secondary_connector_id** (string, optional): Magic Connector identifier tag. Used when high availability mode is on.

## Response

### 200

Patch Site response

- **result** (object, optional): 

### 4XX

Patch Site response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
