# Upload LOA Document

`POST /accounts/{account_id}/addressing/loa_documents`

Submit LOA document (pdf format) under the account.

## Parameters

- **account_id** (string, required) [path]: 


## Response

### 201

Upload LOA Document response

- **result** (object, optional): 

### 4XX

Upload LOA Document response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
