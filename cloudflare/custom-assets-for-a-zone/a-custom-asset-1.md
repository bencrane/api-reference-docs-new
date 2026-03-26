# Delete a custom asset

`DELETE /zones/{zone_identifier}/custom_pages/assets/{asset_name}`

Deletes an existing custom asset.

## Parameters

- **asset_name** (string, required) [path]: 
- **zone_identifier** (string, required) [path]: 

## Response

### 204

Delete a custom asset response

### 4XX

Delete a custom asset response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
