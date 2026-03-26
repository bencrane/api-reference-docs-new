# Retrieve data about a specific document fingerprint.

`GET /accounts/{account_id}/dlp/document_fingerprints/{document_fingerprint_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **document_fingerprint_id** (string, required) [path]: 

## Response

### 200

Document fingerprint read was successful.

- **result** (object, optional): 

### 4XX

Document fingerprint read failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
