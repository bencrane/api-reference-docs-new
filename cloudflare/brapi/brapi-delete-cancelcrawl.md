# Cancel a crawl job.

`DELETE /accounts/{account_id}/browser-rendering/crawl/{job_id}`

Cancels an ongoing crawl job by setting its status to cancelled and stopping all queued URLs.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **job_id** (string, required) [path]: The ID of the crawl job to cancel.

## Response

### 200

Crawl job cancelled successfully.

- **errors** (array): 
- **result** (object): 
- **success** (boolean): Response status.

### 400

Job is already in final status and cannot be cancelled.

- **errors** (array): 
- **success** (boolean): Response status.

### 404

Crawl job not found.

- **errors** (array): 
- **success** (boolean): Response status.

### 500

Internal server error.

- **errors** (array): 
- **success** (boolean): Response status.
