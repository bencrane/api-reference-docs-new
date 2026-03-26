# Delete registration

`DELETE /accounts/{account_id}/devices/registrations/{registration_id}`

Deletes a WARP registration.

## Parameters

- **registration_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Registration deleted response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
