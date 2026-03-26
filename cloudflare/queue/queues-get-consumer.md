# Get Queue Consumer

`GET /accounts/{account_id}/queues/{queue_id}/consumers/{consumer_id}`

Fetches the consumer for a queue by consumer id

## Parameters

- **consumer_id** (string, required) [path]: 
- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Get Queue Consumer response.

_Empty object_

### 4XX

Get Queue Consumer response failure.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
