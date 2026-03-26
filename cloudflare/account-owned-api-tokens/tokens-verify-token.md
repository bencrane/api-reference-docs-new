# Verify Token

`GET /accounts/{account_id}/tokens/verify`

Test whether a token works.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Verify Token response

- **result** (object, optional): 

### 4XX

Verify Token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
