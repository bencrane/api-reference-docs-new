# List available Page Rules settings

`GET /zones/{zone_id}/pagerules/settings`

> **Deprecated**

Returns a list of settings (and their details) that Page Rules can apply to matching requests.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List available Page Rules settings response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): Settings available for the zone.

### 4XX

List available Page Rules settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
