# Upload a new version of a dataset

`POST /accounts/{account_id}/dlp/datasets/{dataset_id}/upload/{version}`

This is used for single-column EDMv1 and Custom Word Lists. The EDM format
can only be created in the Cloudflare dashboard. For other clients, this
operation can only be used for non-secret Custom Word Lists. The body must
be a UTF-8 encoded, newline (NL or CRNL) separated list of words to be matched.

## Parameters

- **account_id** (string, required) [path]: 
- **dataset_id** (string, required) [path]: 
- **version** (integer, required) [path]: 


## Response

### 200

Dataset version uploaded successfully.

- **result** (object, optional): 

### 4XX

Dataset version upload failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
