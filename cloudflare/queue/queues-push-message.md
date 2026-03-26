# Push Message

`POST /accounts/{account_id}/queues/{queue_id}/messages`

Push a message to a Queue

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **delay_seconds** (number, optional): The number of seconds to wait for attempting to deliver this message to consumers

## Response

### 200

Successful message ingestion

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
