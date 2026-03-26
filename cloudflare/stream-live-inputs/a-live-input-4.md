# Disable a live input

`POST /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/disable`

Prevents a live input from being streamed to and makes the live input inaccessible to any future API calls until enabled.

## Parameters

- **live_input_identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Disable a live input response.

- **result** (object, optional): Details about a live input.

### 4XX

Disable a live input response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
