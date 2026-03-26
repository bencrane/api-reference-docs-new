# Creates a new document fingerprint.

`POST /accounts/{account_id}/dlp/document_fingerprints`

Creates a new document fingerprint for DLP scanning. Document fingerprints detect documents that are structurally similar to the uploaded sample.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): 
- **match_percent** (integer, required): 
- **name** (string, required): 

## Response

### 200

Document fingerprint created successfully.

- **result** (object, optional): 

### 4XX

Document fingerprint creation failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
