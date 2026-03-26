# Get Smart Shield Settings

`GET /zones/{zone_id}/smart_shield`

Retrieve Smart Shield Settings.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Smart Shield Settings response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 500

Get Smart Shield Settings response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 502

Get Smart Shield Settings response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Patch Smart Shield Settings response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
