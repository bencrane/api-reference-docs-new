# Partially update DLP account-level settings.

`PATCH /accounts/{account_id}/dlp/settings`

Missing fields keep their existing values.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **ai_context_analysis** (boolean, optional): Whether AI context analysis is enabled at the account level.
- **ocr** (boolean, optional): Whether OCR is enabled at the account level.
- **payload_logging** (object, optional): 

## Response

### 200

DLP settings.

- **result** (object, optional): DLP account-level settings response.

### 4XX

Failed to update DLP settings.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
