# Delete a filter

`DELETE /zones/{zone_id}/filters/{filter_id}`

> **Deprecated**

Deletes an existing filter.

## Parameters

- **filter_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Delete a filter response

- **result** (object, optional): 

### 4XX

Delete a filter response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
