# Get screenshot

`GET /accounts/{account_id}/urlscanner/scan/{scan_id}/screenshot`

> **Deprecated**

Get scan's screenshot by resolution (desktop/mobile/tablet).

## Parameters

- **scan_id** (string, required) [path]: Scan UUID.
- **account_id** (string, required) [path]: Account ID.
- **resolution** (string, optional) [query]: Target device type.

## Response

### 200

Returns the scan's requested screenshot.

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
