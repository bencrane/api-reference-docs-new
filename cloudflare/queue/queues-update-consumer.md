# Update Queue Consumer

`PUT /accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}`

Updates the consumer for a queue, or creates one if it does not exist.

## Parameters

- **consumer_id** (string, required) [path]: 
- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Update Queue Consumer response.

_Empty object_

### 4XX

Update Queue Consumer response failure.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
