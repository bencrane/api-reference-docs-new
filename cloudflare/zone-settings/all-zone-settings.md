# Get all zone settings

`GET /zones/{zone_id}/settings`

> **Deprecated**

Available settings for your user in relation to a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get all Zone settings response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful
- **result** (array, optional): 

### 4XX

Get all Zone settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
