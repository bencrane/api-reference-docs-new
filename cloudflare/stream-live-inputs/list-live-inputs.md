# List live inputs

`GET /accounts/{account_id}/stream/live_inputs`

Lists the live inputs created for an account. To get the credentials needed to stream to a specific live input, request a single live input.

## Parameters

- **account_id** (string, required) [path]: 
- **include_counts** (string, optional) [query]: 

## Response

### 200

List live inputs response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

List live inputs response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
