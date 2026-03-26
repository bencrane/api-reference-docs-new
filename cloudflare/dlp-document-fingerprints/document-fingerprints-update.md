# Update the attributes of a single document fingerprint.

`POST /accounts/{account_id}/dlp/document_fingerprints/{document_fingerprint_id}`

Updates metadata for an existing document fingerprint, such as its name or description.

## Parameters

- **account_id** (string, required) [path]: 
- **document_fingerprint_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): 
- **match_percent** (integer, optional): 
- **name** (string, optional): 

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
