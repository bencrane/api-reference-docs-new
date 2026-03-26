# Edit TURN key details

`PUT /accounts/{account_id}/calls/turn_keys/{key_id}`

Edit details for a single TURN key.

## Parameters

- **key_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): A short description of a TURN key, not shown to end users.

## Response

### 200

Edit TURN key details response

- **result** (object, optional): 

### 4XX

Edit TURN key details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
