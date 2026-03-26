# Prepare to upload a new version of a dataset

`POST /accounts/{account_id}/dlp/datasets/{dataset_id}/upload`

Creates a new version of a DLP dataset, allowing you to stage changes before activation. Used for single-column EDM and custom word lists.

## Parameters

- **account_id** (string, required) [path]: 
- **dataset_id** (string, required) [path]: 

## Response

### 200

Dataset version created successfully.

- **result** (object, optional): 

### 4XX

Dataset version creation failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
