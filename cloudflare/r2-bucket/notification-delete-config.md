# Delete Event Notification Rules

`DELETE /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration/queues/{queue_id}`

Delete an event notification rule. **If no body is provided, all rules for specified queue will be deleted**.

## Parameters

- **queue_id** (string, required) [path]: 
- **bucket_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Request Body

- **ruleIds** (array, optional): Array of rule ids to delete.

## Response

### 200

Delete Configuration response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 4XX

Delete Configuration failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
