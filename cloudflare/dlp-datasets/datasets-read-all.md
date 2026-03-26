# Fetch all datasets

`GET /accounts/{account_id}/dlp/datasets`

Lists all DLP datasets configured for the account, including custom word lists and EDM datasets.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Datasets read successfully.

- **result** (array, optional): 

### 4XX

Datasets read failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
