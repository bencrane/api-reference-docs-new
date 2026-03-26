# Delete registrations

`DELETE /accounts/{account_id}/devices/registrations`

Deletes a list of WARP registrations.

## Parameters

- **account_id** (string, required) [path]: 
- **id** (array, required) [query]: A list of registration IDs to delete.

## Response

### 200

Delete a list of registrations response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): V4 public API Pagination/Cursor info.
- **success** (boolean): Whether the API call was successful.
