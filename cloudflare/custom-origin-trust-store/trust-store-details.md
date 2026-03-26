# Custom Origin Trust Store Details

`GET /zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}`

Retrieves details about a specific certificate in the custom origin trust store, including expiration and subject information.

## Parameters

- **custom_origin_trust_store_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Custom Origin Trust Store Details response

- **result** (object, optional): 

### 4XX

Custom Origin Trust Store Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
