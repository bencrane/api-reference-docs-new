# Retrieve video details

`GET /accounts/{account_id}/stream/{identifier}`

Fetches details for a single video.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Retrieve video details response.

- **result** (object, optional): 

### 4XX

Retrieve video details response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
