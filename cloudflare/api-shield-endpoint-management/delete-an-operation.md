# Delete an operation

`DELETE /zones/{zone_id}/api_gateway/operations/{operation_id}`

Removes a single API operation from API Shield endpoint management. The operation will no longer be tracked or protected by API Shield rules.

## Response

### 200

Delete an operation response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete an operation response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
