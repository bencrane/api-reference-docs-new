# Get tunnel route by IP

`GET /accounts/{account_id}/teamnet/routes/ip/{ip}`

Fetches routes that contain the given IP address.

## Parameters

- **ip** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **virtual_network_id** (string, optional) [query]: 
- **default_virtual_network_fallback** (boolean, optional) [query]: When the virtual_network_id parameter is not provided the request filter will default search routes that are in the default virtual network for the account. If this parameter is set to false, the search will include routes that do not have a virtual network.

## Response

### 200

Get tunnel route by IP response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Get tunnel route by IP response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
