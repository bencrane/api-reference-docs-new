# Watermark profile details

`GET /accounts/{account_id}/stream/watermarks/{identifier}`

Retrieves details for a single watermark profile.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Watermark profile details response.

- **result** (object, optional): 

### 4XX

Watermark profile details response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
