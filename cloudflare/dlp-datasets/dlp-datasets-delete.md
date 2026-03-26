# Delete a dataset

`DELETE /accounts/{account_id}/dlp/datasets/{dataset_id}`

This deletes all versions of the dataset.

## Parameters

- **account_id** (string, required) [path]: 
- **dataset_id** (string, required) [path]: 

## Response

### 200

Dataset deleted successfully.

### 4XX

Dataset delete failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
