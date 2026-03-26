# Delete predefined entry

`DELETE /accounts/{account_id}/dlp/entries/predefined/{entry_id}`

This is a no-op as predefined entires can't be deleted but is needed for our generated terraform API.

## Parameters

- **account_id** (string, required) [path]: 
- **entry_id** (string, required) [path]: 

## Response

### 200

Delete predefined entry response.

- **result** (object, optional): 

### 4XX

Delete entry failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
