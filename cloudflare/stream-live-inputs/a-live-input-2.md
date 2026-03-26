# Retrieve a live input

`GET /accounts/{account_id}/stream/live_inputs/{live_input_identifier}`

Retrieves details of an existing live input.

## Parameters

- **live_input_identifier** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Retrieve a live input response.

- **result** (object, optional): Details about a live input.

### 4XX

Retrieve a live input response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
