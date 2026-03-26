# Update a custom asset

`PUT /zones/{zone_identifier}/custom_pages/assets/{asset_name}`

Updates the configuration of an existing custom asset.

## Parameters

- **asset_name** (string, required) [path]: 
- **zone_identifier** (string, required) [path]: 

## Request Body

- **description** (string, required): A short description of the custom asset.
- **url** (string, required): The URL where the asset content is fetched from.

## Response

### 200

Update a custom asset response

- **result** (object, optional): 

### 4XX

Update a custom asset response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
