# Get json.

`POST /accounts/{account_id}/browser-rendering/json`

Gets json from a webpage from a provided URL or HTML. Pass `prompt` or `schema` in the body. Control page loading with `gotoOptions` and `waitFor*` options.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **cacheTTL** (number, optional) [query]: Cache TTL default is 5s. Set to 0 to disable.

## Request Body

_Empty object_

## Response

### 200

Returns the JSON based on a user prompt or JSON schema.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): Response status.

### 400

The request contains errors or didn't properly encode content.

- **errors** (array): 
- **success** (boolean): Response status.

### 422

Request failed due to site-related issues such as timeouts, SSL errors, or inaccessible content.

- **errors** (array): 
- **rawAiResponse** (string): Raw AI response will be returned, if it couldn't be parsed into valid JSON.
- **success** (boolean): Response status.

### 429

Request failed due to rate limiting. The Retry-After header indicates when the client should retry the request.

- **errors** (array): 
- **success** (boolean): Response status.

### 500

Internal server error.

- **errors** (array): 
- **success** (boolean): Response status.
