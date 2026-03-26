# Delete a single document fingerprint.

`DELETE /accounts/{account_id}/dlp/document_fingerprints/{document_fingerprint_id}`

Removes a document fingerprint from DLP configuration. Documents matching this fingerprint will no longer be detected.

## Parameters

- **account_id** (string, required) [path]: 
- **document_fingerprint_id** (string, required) [path]: 

## Response

### 200

Document fingerprint delete was successful.

### 4XX

Document fingerprint delete failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
