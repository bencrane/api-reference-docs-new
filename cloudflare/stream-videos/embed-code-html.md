# Retrieve embed Code HTML

`GET /accounts/{account_id}/stream/{identifier}/embed`

Fetches an HTML code snippet to embed a video in a web page delivered through Cloudflare. On success, returns an HTML fragment for use on web pages to display a video. On failure, returns a JSON response body.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Retreieve embed Code HTML response.

Type: string

### 4XX

Retreieve embed Code HTML response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
