# List Logpush jobs for a dataset

`GET /accounts/{account_id}/logpush/datasets/{dataset_id}/jobs`

Lists Logpush jobs for an account for a dataset.

## Parameters

- **dataset_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

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
