# Fetch a specific dataset

`GET /accounts/{account_id}/dlp/datasets/{dataset_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **dataset_id** (string, required) [path]: 

## Response

### 200

Dataset read successfully.

- **result** (object, optional): 

### 4XX

Dataset read failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
