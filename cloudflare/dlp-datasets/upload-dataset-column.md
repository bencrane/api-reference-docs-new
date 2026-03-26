# Upload a new version of a multi-column dataset

`POST /accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}/entries/{entry_id}`

This is used for multi-column EDMv2 datasets. The EDMv2 format can only be
created in the Cloudflare dashboard.

## Parameters

- **account_id** (string, required) [path]: 
- **dataset_id** (string, required) [path]: 
- **version** (integer, required) [path]: 
- **entry_id** (string, required) [path]: 


## Response

### 200

Dataset column uploaded successfully.

- **result** (object, optional): 

### 4XX

Failed to upload dataset column.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
