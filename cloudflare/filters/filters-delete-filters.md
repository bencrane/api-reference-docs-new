# Delete filters

`DELETE /zones/{zone_id}/filters`

> **Deprecated**

Deletes one or more existing filters.

## Parameters

- **zone_id** (string, required) [path]: 
- **id** (array, required) [query]: 

## Response

### 200

Delete filters response

- **result** (array, optional): 

### 4XX

Delete filters response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
