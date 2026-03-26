# List fields

`GET /zones/{zone_id}/logpush/datasets/{dataset_id}/fields`

Lists all fields available for a dataset. The response result is. an object with key-value pairs, where keys are field names, and values are descriptions.

## Parameters

- **dataset_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

List fields response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

List fields response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
