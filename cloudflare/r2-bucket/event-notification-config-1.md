# Create Event Notification Rule

`PUT /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}`

Create event notification rule.

## Parameters

- **queue_id** (string, required) [path]: 
- **bucket_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Request Body

- **rules** (array, required): Array of rules to drive notifications.

## Response

### 200

Create Configuration response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Create Configuration failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
