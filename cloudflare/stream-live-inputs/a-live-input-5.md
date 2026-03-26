# Enable a live input

`POST /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/enable`

Allows a live input to be streamed to and makes the live input accessible to any future API calls.

## Parameters

- **live_input_identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Enable a live input response.

- **result** (object, optional): Details about a live input.

### 4XX

Enable a live input response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
