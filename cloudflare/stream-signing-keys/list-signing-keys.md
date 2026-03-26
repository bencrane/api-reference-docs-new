# List signing keys

`GET /accounts/{account_id}/stream/keys`

Lists the video ID and creation date and time when a signing key was created.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

List signing keys response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List signing keys response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
