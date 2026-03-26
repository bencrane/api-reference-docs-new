# Delete Subdomain

`DELETE /accounts/{account_id}/workers/subdomain`

Deletes a Workers subdomain for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 204

Subdomain deleted successfully.

### 4XX

Delete Subdomain response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
