# Push Message Batch

`POST /accounts/{account_id}/queues/{queue_id}/messages/batch`

Push a batch of message to a Queue

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **delay_seconds** (number, optional): The number of seconds to wait for attempting to deliver this batch to consumers
- **messages** (array, optional): 

## Response

### 200

Successful batch ingestion

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
