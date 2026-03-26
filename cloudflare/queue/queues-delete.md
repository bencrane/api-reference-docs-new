# Delete Queue

`DELETE /accounts/{account_id}/queues/{queue_id}`

Deletes a queue

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Successful delete

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
