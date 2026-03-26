# Open Websocket connection with @cf/deepgram/aura-2-es model.

`GET /accounts/{account_id}/ai/run/@cf/deepgram/aura-2-es`

Opens a WebSocket connection to stream inference results from the @cf/deepgram/aura-2-es model.

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
