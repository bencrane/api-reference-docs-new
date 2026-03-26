# Uploads a new version for a document fingerprint.

`PUT /accounts/{account_id}/dlp/document_fingerprints/{document_fingerprint_id}`

Uploads a new document to create or update a fingerprint. The document structure is analyzed to enable detection of similar documents.

## Parameters

- **account_id** (string, required) [path]: 
- **document_fingerprint_id** (string, required) [path]: 


## Response

### 200

File uploaded successfully.

- **result** (object, optional): 

### 4XX

Failed to upload file.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
