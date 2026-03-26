# Validate Prefix

`POST /accounts/{account_id}/addressing/prefixes/{prefix_id}/validate`

Triggers a new prefix validation. The checks are run asynchronously and include IRR, RPKI, and prefix ownership.

## Parameters

- **prefix_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 202

Validate Prefix response

- **result** (object, optional): 

### 4XX

Validate Prefix response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
