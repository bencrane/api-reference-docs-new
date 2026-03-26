# Retrieve TURN key details

`GET /accounts/{account_id}/calls/turn_keys/{key_id}`

Fetches details for a single TURN key.

## Parameters

- **key_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Retrieve TURN key details response

- **result** (object, optional): 

### 4XX

Retrieve TURN key details failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
