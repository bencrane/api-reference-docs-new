# Get Spectrum application configuration

`GET /zones/{zone_id}/spectrum/apps/{app_id}`

Gets the application configuration of a specific application inside a zone.

## Parameters

- **app_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get Spectrum application configuration response.

- **result** (object, optional): 

### 4XX

Get Spectrum application configuration response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
