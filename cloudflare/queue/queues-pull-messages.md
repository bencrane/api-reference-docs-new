# Pull Queue Messages

`POST /accounts/{account_id}/queues/{queue_id}/messages/pull`

Pull a batch of messages from a Queue

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **batch_size** (number, optional): The maximum number of messages to include in a batch.
- **visibility_timeout_ms** (number, optional): The number of milliseconds that a message is exclusively leased. After the timeout, the message becomes available for another attempt.

## Response

### 200

A batch of messages in the Queue

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
