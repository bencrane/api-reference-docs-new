# Create a Queue Consumer

`POST /accounts/{account_id}/queues/{queue_id}/consumers`

Creates a new consumer for a Queue

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Create Queue Consumer response.

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
