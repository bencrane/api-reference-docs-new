# List Logpush jobs for a dataset

`GET /zones/{zone_id}/logpush/datasets/{dataset_id}/jobs`

Lists Logpush jobs for a zone for a dataset.

## Parameters

- **dataset_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Response

### 200

List Logpush jobs for a dataset response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List Logpush jobs for a dataset response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
