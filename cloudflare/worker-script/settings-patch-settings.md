# Patch Script Settings

`PATCH /accounts/{account_id}/workers/scripts/{script_name}/script-settings`

Patch script-level settings when using [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions). Including but not limited to Logpush and Tail Consumers.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Request Body

- **logpush** (boolean, optional): Whether Logpush is turned on for the Worker.
- **observability** (object, optional): 
- **tags** (object, optional): 
- **tail_consumers** (array, optional): List of Workers that will consume logs from the attached Worker.

## Response

### 200

Patch script settings.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Patch script settings failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
