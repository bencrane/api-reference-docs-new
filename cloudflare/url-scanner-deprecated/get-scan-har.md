# Get URL scan's HAR

`GET /accounts/{account_id}/urlscanner/scan/{scan_id}/har`

> **Deprecated**

Get a URL scan's HAR file. See HAR spec at http://www.softwareishard.com/blog/har-12-spec/.

## Parameters

- **scan_id** (string, required) [path]: Scan UUID.
- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Returns the scan's har.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether search request was successful or not

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
