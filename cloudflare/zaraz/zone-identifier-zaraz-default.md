# Get default Zaraz configuration

`GET /zones/{zone_id}/settings/zaraz/default`

Gets default Zaraz configuration for a zone.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Zaraz default configuration response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Get Zaraz default configuration response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
