# Create a custom asset

`POST /accounts/{account_identifier}/custom_pages/assets`

Creates a new custom asset at the account level.

## Parameters

- **account_identifier** (string, required) [path]: 

## Request Body

- **description** (string, required): A short description of the custom asset.
- **name** (string, required): The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_).
- **url** (string, required): The URL where the asset content is fetched from.

## Response

### 200

Create custom asset response

- **result** (object, optional): 

### 4XX

Create custom asset response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
