# Unrevoke registrations

`POST /accounts/{account_id}/devices/registrations/unrevoke`

Unrevokes a list of WARP registrations.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (array, required) [query]: A list of registration IDs to unrevoke.

## Response

### 200

Unrevoke registrations response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): V4 public API Pagination/Cursor info.
- **success** (boolean): Whether the API call was successful.
