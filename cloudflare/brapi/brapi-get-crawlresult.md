# Get crawl result.

`GET /accounts/{account_id}/browser-rendering/crawl/{job_id}`

Returns the result of a crawl job.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **job_id** (string, required) [path]: Crawl job ID.
- **cacheTTL** (number, optional) [query]: Cache TTL default is 5s. Set to 0 to disable.
- **status** (string, optional) [query]: Filter by URL status.
- **cursor** (number, optional) [query]: Cursor for pagination.
- **limit** (number, optional) [query]: Limit for pagination.

## Response

### 200

Returns the result of a crawl job.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): Response status.

### 400

The request contains errors or didn't properly encode content.

- **errors** (array): 
- **success** (boolean): Response status.

### 500

Internal server error.

- **errors** (array): 
- **success** (boolean): Response status.
