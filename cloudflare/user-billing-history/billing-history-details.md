# Billing History Details

`GET /user/billing/history`

> **Deprecated**

Accesses your billing history object.

## Parameters

- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **occurred_at** (string, optional) [query]: 
- **type** (string, optional) [query]: 
- **action** (string, optional) [query]: 

## Response

### 200

Billing History Details response

- **result** (array, optional): 

### 4XX

Billing History Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
