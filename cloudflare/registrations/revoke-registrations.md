# Revoke registrations

`POST /accounts/{account_id}/devices/registrations/revoke`

Revokes a list of WARP registrations.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (array, required) [query]: A list of registration IDs to revoke.

## Response

### 200

Revoke registrations response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): V4 public API Pagination/Cursor info.
- **success** (boolean): Whether the API call was successful.
