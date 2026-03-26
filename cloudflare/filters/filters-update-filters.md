# Update filters

`PUT /zones/{zone_id}/filters`

> **Deprecated**

Updates one or more existing filters.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Update filters response

- **result** (array, optional): 

### 4XX

Update filters response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
