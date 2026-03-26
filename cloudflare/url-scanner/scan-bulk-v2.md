# Bulk create URL Scans

`POST /accounts/{account_id}/urlscanner/v2/bulk`

Submit URLs to scan. Check limits at https://developers.cloudflare.com/security-center/investigate/scan-limits/ and take into account scans submitted in bulk have lower priority and may take longer to finish.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

Array of object

## Response

### 200

Scan bulk request accepted successfully.

Type: array

### 400

Invalid input.

- **errors** (array): 
- **message** (string): 
- **status** (integer): Status code.

### 429

Scan request denied: rate limited.

- **description** (string): 
- **errors** (array): 
- **message** (string): 
- **status** (number):
