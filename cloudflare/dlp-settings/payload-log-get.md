# Get payload log settings

`GET /accounts/{account_id}/dlp/payload_log`

Gets the current payload logging configuration for DLP, showing whether matched content is being logged.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Payload log settings.

- **result** (object, optional): 

### 4XX

Failed to get payload log settings.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
