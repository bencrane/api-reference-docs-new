# Get URL scan's DOM

`GET /accounts/{account_id}/urlscanner/v2/dom/{scan_id}`

Returns a plain text response, with the scan's DOM content as rendered by Chrome.

## Parameters

- **scan_id** (string, required) [path]: Scan UUID.
- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Returns a plain text response, with the scan's DOM content as rendered by Chrome.

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
