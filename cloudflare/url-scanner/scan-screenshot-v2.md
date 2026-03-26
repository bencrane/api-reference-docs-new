# Get screenshot

`GET /accounts/{account_id}/urlscanner/v2/screenshots/{scan_id}.png`

Get scan's screenshot by resolution (desktop/mobile/tablet).

## Parameters

- **scan_id** (string, required) [path]: Scan UUID.
- **account_id** (string, required) [path]: Account ID.
- **resolution** (string, optional) [query]: Target device type.

## Response

### 200

Returns the scan's requested screenshot.

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
