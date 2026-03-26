# Delete multiple operations

`DELETE /zones/{zone_id}/api_gateway/operations`

Bulk removes multiple API operations from API Shield endpoint management in a single request. Efficient for cleaning up unused endpoints.

## Request Body

Array of object

## Response

### 200

Delete multiple operations response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete multiple operations response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
