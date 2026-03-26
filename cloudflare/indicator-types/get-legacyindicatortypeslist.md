# Lists all indicator types

`GET /accounts/{account_id}/cloudforce-one/events/indicatorTypes`

> **Deprecated**

This Method is deprecated. Please use /events/dataset/:dataset_id/indicatorTypes instead.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Response

### 200

Returns a list of indicator types.

- **items** (object): 
- **type** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
