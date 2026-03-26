# Delete targets

`POST /accounts/{account_id}/infrastructure/targets/batch_delete`

Removes one or more targets.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **target_ids** (array, required): List of target IDs to bulk delete

## Response

### 200

Successfully deleted the targets

### 4XX

Failed to delete the targets

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
