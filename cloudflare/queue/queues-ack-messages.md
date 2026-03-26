# Acknowledge + Retry Queue Messages

`POST /accounts/{account_id}/queues/{queue_id}/messages/ack`

Acknowledge + Retry messages from a Queue

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **acks** (array, optional): 
- **retries** (array, optional): 

## Response

### 200

Details of ACKs and retries

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
