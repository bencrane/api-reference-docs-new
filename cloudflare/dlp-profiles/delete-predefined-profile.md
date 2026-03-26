# Delete predefined profile

`DELETE /accounts/{account_id}/dlp/profiles/predefined/{profile_id}`

This is a no-op as predefined profiles can't be deleted but is needed for our generated terraform API.

## Parameters

- **account_id** (string, required) [path]: 
- **profile_id** (string, required) [path]: 

## Response

### 200

Delete predefined profile response.

- **result** (object, optional): 

### 4XX

Delete predefined profile failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
