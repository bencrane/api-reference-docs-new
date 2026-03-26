# Delete a live input

`DELETE /accounts/{account_id}/stream/live_inputs/{live_input_identifier}`

Prevents a live input from being streamed to and makes the live input inaccessible to any future API calls.

## Parameters

- **live_input_identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete a live input response.

### 4XX

Delete a live input response failure.
