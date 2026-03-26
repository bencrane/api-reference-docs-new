# Update Cron Triggers

`PUT /accounts/{account_id}/workers/scripts/{script_name}/schedules`

Updates Cron Triggers for a Worker.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Request Body

Array of object

## Response

### 200

Update Cron Triggers response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update Cron Triggers response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
