# List fields

`GET /zones/{zone_id}/logs/received/fields`

Lists all fields available. The response is json object with key-value pairs, where keys are field names, and values are descriptions.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

List fields response

- **key** (string): 

### 4XX

List fields response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
