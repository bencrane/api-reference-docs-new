# Revert an Events Durable Object to a point in time

`POST /accounts/{account_id}/cloudforce-one/events/{dataset_id}/revert-do`



## Parameters

- **account_id** (string, required) [path]: Account ID.
- **dataset_id** (string, required) [path]: Dataset UUID.

## Request Body

- **minutesAgo** (number, required): 

## Response

### 200

Revert scheduled for the specified Durable Object.

- **properties** (object): 
- **required** (array): 
- **type** (string): 

### 400

Bad Request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
