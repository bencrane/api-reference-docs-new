# Get URL scan's HAR

`GET /accounts/{account_id}/urlscanner/v2/har/{scan_id}`

Get a URL scan's HAR file. See HAR spec at http://www.softwareishard.com/blog/har-12-spec/.

## Parameters

- **scan_id** (string, required) [path]: Scan UUID.
- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Returns the scan's har.

- **log** (object): 

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
