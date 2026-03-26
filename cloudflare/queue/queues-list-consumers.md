# List Queue Consumers

`GET /accounts/{account_id}/queues/{queue_id}/consumers`

Returns the consumers for a Queue

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

All consumers attached to this Queue

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
