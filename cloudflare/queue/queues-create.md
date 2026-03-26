# Create Queue

`POST /accounts/{account_id}/queues`

Create a new queue

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **queue_name** (string, required): 

## Response

### 200

Created Queue

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
