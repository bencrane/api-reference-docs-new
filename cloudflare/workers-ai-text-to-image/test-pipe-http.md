# Open Websocket connection with @cf/sven/test-pipe-http model.

`GET /accounts/{account_id}/ai/run/@cf/sven/test-pipe-http`

Opens a WebSocket connection to stream inference results from the @cf/sven/test-pipe-http model.

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
