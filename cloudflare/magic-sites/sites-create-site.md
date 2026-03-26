# Create a new Site

`POST /accounts/{account_id}/magic/sites`

Creates a new Site

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **connector_id** (string, optional): Magic Connector identifier tag.
- **description** (string, optional): 
- **ha_mode** (boolean, optional): Site high availability mode. If set to true, the site can have two connectors and runs in high availability mode.
- **location** (object, optional): Location of site in latitude and longitude.
- **name** (string, required): The name of the site.
- **secondary_connector_id** (string, optional): Magic Connector identifier tag. Used when high availability mode is on.

## Response

### 200

Create Site response

- **result** (object, optional): 

### 4XX

Create Site response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
