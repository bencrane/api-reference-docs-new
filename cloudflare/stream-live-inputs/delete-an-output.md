# Delete an output

`DELETE /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}`

Deletes an output and removes it from the associated live input.

## Parameters

- **output_identifier** (string, required) [path]: 
- **live_input_identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete an output response.

### 4XX

Delete an output response failure.
