# Create an independent livestream

`POST /accounts/{account_id}/realtime/kit/{app_id}/livestreams`

Creates a livestream for the given App ID and returns ingest server, stream key, and playback URL. You can pass custom input to the ingest server and stream key, and freely distribute the content using the playback URL on any player that supports HLS/LHLS.

## Request Body

- **name** (string, optional): Name of the livestream

## Response

### 201

Successful response

- **data** (object): 
- **success** (boolean):
