# Sets the column information for a multi-column upload

`POST /accounts/{account_id}/dlp/datasets/{dataset_id}/versions/{version}`

This is used for multi-column EDMv2 datasets. The EDMv2 format can only be
created in the Cloudflare dashboard. The columns in the response appear in
the same order as in the request.

## Parameters

- **account_id** (string, required) [path]: 
- **dataset_id** (string, required) [path]: 
- **version** (integer, required) [path]: 

## Request Body

Array of object

## Response

### 200

Dataset columns created successfully.

- **result** (array, optional): 

### 4XX

Failed to create dataset columns.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
