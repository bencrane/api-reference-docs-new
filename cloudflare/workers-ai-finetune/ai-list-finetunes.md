# List Finetunes

`GET /accounts/{account_id}/ai/finetunes`

Lists all fine-tuning jobs created by the account, including status and metrics.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Returns all finetunes

- **result** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
