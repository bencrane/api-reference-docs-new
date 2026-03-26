# View webhooks

`GET /accounts/{account_id}/stream/webhook`

Retrieves a list of webhooks.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

View webhooks response.

- **result** (object, optional): 

### 4XX

View webhooks response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
