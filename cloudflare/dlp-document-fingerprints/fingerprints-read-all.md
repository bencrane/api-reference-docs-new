# Retrieve data about all document fingerprints.

`GET /accounts/{account_id}/dlp/document_fingerprints`

Lists all document fingerprints configured for DLP scanning in the account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Document fingerprint read was successful.

- **result** (array, optional): 

### 4XX

Document fingerprint read failed.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
