# Open Websocket connection with @cf/pipecat-ai/smart-turn-v3 model.

`GET /accounts/{account_id}/ai/run/@cf/pipecat-ai/smart-turn-v3`

Opens a WebSocket connection to stream inference results from the @cf/pipecat-ai/smart-turn-v3 model.

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
