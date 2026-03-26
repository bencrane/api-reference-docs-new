# Create filters

`POST /zones/{zone_id}/filters`

> **Deprecated**

Creates one or more filters.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Create filters response

_Empty object_

### 4XX

Create filters response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
