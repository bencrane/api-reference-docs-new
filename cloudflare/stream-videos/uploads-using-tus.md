# Initiate video uploads using TUS

`POST /accounts/{account_id}/stream`

Initiates a video upload using the TUS protocol. On success, the server responds with a status code 201 (created) and includes a `location` header to indicate where the content should be uploaded. Refer to https://tus.io for protocol details.

## Parameters

- **Tus-Resumable** (string, required) [header]: 
- **Upload-Creator** (string, optional) [header]: 
- **Upload-Length** (string, required) [header]: 
- **Upload-Metadata** (string, optional) [header]: 
- **account_id** (string, required) [path]: 
- **direct_user** (string, optional) [query]: 


## Response

### 200

Initiate video uploads using TUS response.

### 4XX

Initiate video uploads using TUS response failure.
