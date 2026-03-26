# Purge Queue

`POST /accounts/{account_id}/queues/{queue_id}/purge`

Deletes all messages from the Queue.

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **delete_messages_permanently** (boolean, optional): Confimation that all messages will be deleted permanently.

## Response

### 200

Updated Queue

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
