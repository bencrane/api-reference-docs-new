# Delete Queue Consumer

`DELETE /accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}`

Deletes the consumer for a queue.

## Parameters

- **consumer_id** (string, required) [path]: 
- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Successful consumer delete

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
