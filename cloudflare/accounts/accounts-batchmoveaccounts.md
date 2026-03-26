# Batch move accounts

`POST /accounts/move`

Batch move a collection of accounts to a specific organization. ⚠️ Not implemented.

## Request Body

- **account_ids** (array, required): Move these accounts to the destination organization.
- **destination_organization_id** (string, required): Move accounts to this organization ID.

## Response

### 200

The request has succeeded.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 4XX

An unexpected error response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean):
