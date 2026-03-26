# Get Queue

`GET /accounts/{account_id}/queues/{queue_id}`

Get details about a specific queue.

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Details of the requested Queue

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
