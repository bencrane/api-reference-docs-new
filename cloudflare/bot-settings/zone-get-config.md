# Get Zone Bot Management Config

`GET /zones/{zone_id}/bot_management`

Retrieve a zone's Bot Management Config

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Bot Management config response

- **result** (object, optional): 

### 4XX

Bot Management config response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
