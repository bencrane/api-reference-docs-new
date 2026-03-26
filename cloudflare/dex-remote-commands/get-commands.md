# List account commands

`GET /accounts/{account_id}/dex/commands`

Retrieves a paginated list of commands issued to devices under the specified account, optionally filtered by time range, device, or other parameters

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path
- **page** (number, required) [query]: Page number for pagination
- **per_page** (number, required) [query]: Number of results per page
- **from** (string, optional) [query]: Start time for the query in ISO (RFC3339 - ISO 8601) format
- **to** (string, optional) [query]: End time for the query in ISO (RFC3339 - ISO 8601) format
- **device_id** (string, optional) [query]: Unique identifier for a device
- **user_email** (string, optional) [query]: Email tied to the device
- **command_type** (string, optional) [query]: Optionally filter executed commands by command type
- **status** (string, optional) [query]: Optionally filter executed commands by status

## Response

### 200

Get commands response

- **result** (object, optional): 

### 4XX

Get commands failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
