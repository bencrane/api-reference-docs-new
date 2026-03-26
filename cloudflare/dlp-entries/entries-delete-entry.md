# Delete custom entry

`DELETE /accounts/{account_id}/dlp/entries/{entry_id}`

Deletes a DLP custom entry.

## Parameters

- **account_id** (string, required) [path]: 
- **entry_id** (string, required) [path]: 

## Response

### 200

Delete custom entry response.

- **result** (object, optional): 

### 4XX

Delete custom entry failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
