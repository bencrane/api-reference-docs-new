# Create a New Request Message

`POST /accounts/{account_id}/cloudforce-one/requests/{request_id}/message/new`



## Parameters

- **account_id** (string, required) [path]: 
- **request_id** (string, required) [path]: 

## Request Body

- **content** (string, optional): Content of message.

## Response

### 200

Create request message response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create request message response failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
