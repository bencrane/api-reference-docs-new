# List all outputs associated with a specified live input

`GET /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs`

Retrieves all outputs associated with a specified live input.

## Parameters

- **live_input_identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

List all outputs associated with a specified live input response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (array, optional): 

### 4XX

List all outputs associated with a specified live input response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
