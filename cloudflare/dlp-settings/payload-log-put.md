# Set payload log settings

`PUT /accounts/{account_id}/dlp/payload_log`

Enables or disables payload logging for DLP matches. When enabled, matched content is stored for review.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **masking_level** (object, optional): 
- **public_key** (string, optional): Base64-encoded public key for encrypting payload logs.

- Set to null or empty string to disable payload logging.
- Set to a non-empty base64 string to enable payload logging with the given key.

For customers with configurable payload masking feature rolled out:
- If the field is missing, the existing setting will be kept. Note that this is different from setting to null or empty string.

For all other customers:
- If the field is missing, the existing setting will be cleared.

## Response

### 200

Payload log settings.

- **result** (object, optional): 

### 4XX

Failed to set payload log settings.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
