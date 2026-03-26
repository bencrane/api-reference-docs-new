# Delete signing keys

`DELETE /accounts/{account_id}/stream/keys/{identifier}`

Deletes signing keys and revokes all signed URLs generated with the key.

## Parameters

- **identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete signing keys response.

- **result** (string, optional): 

### 4XX

Delete signing keys response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
