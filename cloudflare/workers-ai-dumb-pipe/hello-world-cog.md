# Open Websocket connection with @cf/test/hello-world-cog model.

`GET /accounts/{account_id}/ai/run/@cf/test/hello-world-cog`

Opens a WebSocket connection to stream inference results from the @cf/test/hello-world-cog model.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 101

Returns a websocket connection

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
