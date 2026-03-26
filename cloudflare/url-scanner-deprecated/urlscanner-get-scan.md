# Get URL scan

`GET /accounts/{account_id}/urlscanner/scan/{scan_id}`

> **Deprecated**

Get URL scan by uuid

## Parameters

- **scan_id** (string, required) [path]: Scan UUID.
- **account_id** (string, required) [path]: Account ID.
- **full** (boolean, optional) [query]: Whether to return full report (scan summary and network log).

## Response

### 200

Scan has finished. It may or may not have been successful.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether request was successful or not

### 202

Scan is in progress. Check current status in `result.scan.task.status`. Possible statuses: `Queued`,`InProgress`,`InPostProcessing`,`Finished`.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether request was successful or not

### 400

Invalid params.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether request was successful or not

### 404

Scan not found.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether request was successful or not
