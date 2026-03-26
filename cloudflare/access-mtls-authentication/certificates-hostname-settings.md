# List all mTLS hostname settings

`GET /accounts/{account_id}/access/certificates/settings`

List all mTLS hostname settings for this account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List mTLS hostname settings response

_Empty object_

### 4XX

List mTLS hostname settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
