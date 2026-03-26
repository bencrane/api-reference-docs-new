# Update an output

`PUT /accounts/{account_id}/stream/live_inputs/{live_input_identifier}/outputs/{output_identifier}`

Updates the state of an output.

## Parameters

- **output_identifier** (string, required) [path]: 
- **live_input_identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, required): When enabled, live video streamed to the associated live input will be sent to the output URL. When disabled, live video will not be sent to the output URL, even when streaming to the associated live input. Use this to control precisely when you start and stop simulcasting to specific destinations like YouTube and Twitch.

## Response

### 200

Update an output response.

- **result** (object, optional): 

### 4XX

Update an output response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
