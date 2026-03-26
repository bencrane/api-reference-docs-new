# Get DLP Entry

`GET /accounts/{account_id}/dlp/entries/{entry_id}`

Fetches a DLP entry by ID.

## Parameters

- **account_id** (string, required) [path]: 
- **entry_id** (string, required) [path]: 

## Response

### 200

Get entry response.

- **result** (object, optional): 

### 4XX

Get entry failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
