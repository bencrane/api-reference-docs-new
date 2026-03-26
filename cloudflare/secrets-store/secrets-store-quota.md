# View secret usage

`GET /accounts/{account_id}/secrets_store/quota`

Lists the number of secrets used in the account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Usage and quota

- **result** (object, optional): 

### 4XX

List store secrets response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
