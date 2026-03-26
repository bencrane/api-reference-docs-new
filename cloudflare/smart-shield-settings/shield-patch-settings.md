# Patch Smart Shield Settings

`PATCH /zones/{zone_id}/smart_shield`

Set Smart Shield Settings.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **cache_reserve** (object, optional): 
- **regional_tiered_cache** (object, optional): 
- **smart_routing** (object, optional): 
- **smart_tiered_cache** (object, optional): 

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

Smart Shield Settings response failure.

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
