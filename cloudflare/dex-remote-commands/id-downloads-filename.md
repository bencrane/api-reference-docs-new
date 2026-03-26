# Download command output file

`GET /accounts/{account_id}/dex/commands/{command_id}/downloads/{filename}`

Downloads artifacts for an executed command. Bulk downloads are not supported

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path
- **command_id** (string, required) [path]: Unique identifier for command
- **filename** (string, required) [path]: The name of the file to be downloaded, including the `.zip` extension

## Response

### 200

Get command artifacts response

### 4XX

Get downloaded commands failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
