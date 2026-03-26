# Update an mTLS certificate's hostname settings

`PUT /accounts/{account_id}/access/certificates/settings`

Updates an mTLS certificate's hostname settings.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **settings** (array, required): 

## Response

### 202

Update an mTLS certificates hostname settings response

_Empty object_

### 4XX

Update an mTLS certificates hostname settings failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
