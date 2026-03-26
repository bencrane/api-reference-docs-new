# Get Links.

`POST /accounts/{account_id}/browser-rendering/links`

Get links from a web page.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **cacheTTL** (number, optional) [query]: Cache TTL default is 5s. Set to 0 to disable.

## Request Body

_Empty object_

## Response

### 200

Returns the links.

- **errors** (array): 
- **result** (array): 
- **success** (boolean): Response status.

### 400

The request contains errors or didn't properly encode content.

- **errors** (array): 
- **success** (boolean): Response status.

### 422

Request failed due to site-related issues such as timeouts, SSL errors, or inaccessible content.

- **errors** (array): 
- **success** (boolean): Response status.

### 429

Request failed due to rate limiting. The Retry-After header indicates when the client should retry the request.

- **errors** (array): 
- **success** (boolean): Response status.

### 500

Internal server error.

- **errors** (array): 
- **success** (boolean): Response status.
