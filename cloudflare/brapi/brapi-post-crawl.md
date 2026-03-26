# Crawl websites.

`POST /accounts/{account_id}/browser-rendering/crawl`

Starts a crawl job for the provided URL and its children. Check available options like `gotoOptions` and `waitFor*` to control page load behaviour.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **cacheTTL** (number, optional) [query]: Cache TTL default is 5s. Set to 0 to disable.

## Request Body

_Empty object_

## Response

### 200

Returns the ID for the started crawl job.

- **errors** (array): 
- **result** (string): Crawl job ID.
- **success** (boolean): Response status.

### 400

The request contains errors or didn't properly encode content.

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
