# Billing Profile Details

`GET /accounts/{account_id}/billing/profile`

> **Deprecated**

Gets the current billing profile for the account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Billing Profile Details response

- **result** (object, optional): 

### 4XX

Billing Profile Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
