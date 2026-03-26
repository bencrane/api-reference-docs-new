# Update the Access key configuration

`PUT /accounts/{account_id}/access/keys`

Updates the Access key rotation settings for an account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **key_rotation_interval_days** (number, required): The number of days between key rotations.

## Response

### 200

Update the Access key configuration response

_Empty object_

### 4XX

Update the Access key configuration response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
