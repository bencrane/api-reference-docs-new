# Get Script Settings

`GET /accounts/{account_id}/workers/scripts/{script_name}/script-settings`

Get script-level settings when using [Worker Versions](https://developers.cloudflare.com/api/operations/worker-versions-list-versions). Includes Logpush and Tail Consumers.

## Parameters

- **account_id** (string, required) [path]: 
- **script_name** (string, required) [path]: 

## Response

### 200

Fetch script settings.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Fetch script settings failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
