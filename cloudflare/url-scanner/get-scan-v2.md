# Get URL scan

`GET /accounts/{account_id}/urlscanner/v2/result/{scan_id}`

Get URL scan by uuid

## Parameters

- **scan_id** (string, required) [path]: Scan UUID.
- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Scan has finished. It may or may not have been successful.

- **data** (object): 
- **lists** (object): 
- **meta** (object): 
- **page** (object): 
- **scanner** (object): 
- **stats** (object): 
- **task** (object): 
- **verdicts** (object): 

### 400

Invalid input.

- **errors** (array): 
- **message** (string): 
- **status** (integer): Status code.

### 404

Scan not found or in progress.

- **errors** (array): 
- **message** (string): Scan not found or in progress.
- **status** (integer): Status code.
- **task** (object):
