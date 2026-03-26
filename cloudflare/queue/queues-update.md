# Update Queue

`PUT /accounts/{account_id}/queues/{queue_id}`

Updates a Queue. Note that this endpoint does not support partial updates. If successful, the Queue's configuration is overwritten with the supplied configuration.

## Parameters

- **queue_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **consumers** (array, optional): 
- **consumers_total_count** (number, optional): 
- **created_on** (string, optional): 
- **modified_on** (string, optional): 
- **producers** (array, optional): 
- **producers_total_count** (number, optional): 
- **queue_id** (string, optional): 
- **queue_name** (string, optional): 
- **settings** (object, optional): 

## Response

### 200

Updated Queue

_Empty object_

### 4XX

Failure response

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
