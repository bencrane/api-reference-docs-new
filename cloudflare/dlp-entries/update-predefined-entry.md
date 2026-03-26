# Update predefined entry

`PUT /accounts/{account_id}/dlp/entries/predefined/{entry_id}`

Updates a DLP entry.

## Parameters

- **account_id** (string, required) [path]: 
- **entry_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, required): 

## Response

### 200

Update predefined entry response.

- **result** (object, optional): 

### 4XX

Update entry failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
