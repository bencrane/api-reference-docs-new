# Get a Page Shield connection

`GET /zones/{zone_id}/page_shield/connections/{connection_id}`

Fetches a connection detected by Page Shield by connection ID.

## Parameters

- **zone_id** (string, required) [path]: 
- **connection_id** (string, required) [path]: 

## Response

### 200

Get a Page Shield connection response

- **result** (object, optional): 

### 4XX

Get a Page Shield connection response failure

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
