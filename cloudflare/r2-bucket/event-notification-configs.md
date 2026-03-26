# List Event Notification Rules

`GET /accounts/{account_id}/event_notifications/r2/{bucket_name}/configuration`

List all event notification rules for a bucket.

## Parameters

- **bucket_name** (string, required) [path]: 
- **account_id** (string, required) [path]: 
- **cf-r2-jurisdiction** (string, optional) [header]: 

## Response

### 200

Read Configuration response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`

### 404

No Configuration Found response.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Read Configuration failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
