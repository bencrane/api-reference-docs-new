# Update a Request Message

`PUT /accounts/{account_id}/cloudforce-one/requests/{request_id}/message/{message_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 
- **message_id** (integer, required) [path]: 

## Request Body

- **content** (string, optional): Content of message.

## Response

### 200

Update request message response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Update request message response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
