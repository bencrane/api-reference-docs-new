# Download LOA Document

`GET /accounts/{account_id}/addressing/loa_documents/{loa_document_id}/download`

Download specified LOA document under the account.

## Parameters

- **loa_document_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Download LOA Document response

### 4XX

Download LOA Document response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
