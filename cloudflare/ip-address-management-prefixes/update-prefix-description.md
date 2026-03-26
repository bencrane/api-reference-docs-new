# Update Prefix Description

`PATCH /accounts/{account_id}/addressing/prefixes/{prefix_id}`

Modify the description for a prefix owned by the account.

## Parameters

- **prefix_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, required): Description of the prefix.

## Response

### 200

Update Prefix Description response

- **result** (object, optional): 

### 4XX

Update Prefix Description response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
