# Get Zaraz configuration

`GET /zones/{zone_id}/settings/zaraz/config`

Gets latest Zaraz configuration for a zone. It can be preview or published configuration, whichever was the last updated. Secret variables values will not be included.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Zaraz configuration response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Get Zaraz configuration response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
