# Open Websocket connection with @cf/deepgram/nova-3-ws model.

`GET /accounts/{account_id}/ai/run/@cf/deepgram/nova-3-ws`

Opens a WebSocket connection to stream inference results from the @cf/deepgram/nova-3-ws model.

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
