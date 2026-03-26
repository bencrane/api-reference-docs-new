# Get a filter

`GET /zones/{zone_id}/filters/{filter_id}`

> **Deprecated**

Fetches the details of a filter.

## Parameters

- **filter_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Get a filter response

- **result** (object, optional): 

### 4XX

Get a filter response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
