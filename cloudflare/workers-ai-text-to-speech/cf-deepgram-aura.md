# Open Websocket connection with @cf/deepgram/aura model.

`GET /accounts/{account_id}/ai/run/@cf/deepgram/aura`

Opens a WebSocket connection to stream inference results from the @cf/deepgram/aura model.

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
