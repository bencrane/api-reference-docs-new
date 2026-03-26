# Delete Custom Origin Trust Store

`DELETE /zones/{zone_id}/acm/custom_trust_store/{custom_origin_trust_store_id}`

Removes a CA certificate from the custom origin trust store. Origins using certificates signed by this CA will no longer be trusted.

## Parameters

- **custom_origin_trust_store_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

Delete Custom Origin Trust Store response

- **result** (object, optional): 

### 4XX

Delete Custom Origin Trust Store response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
