# Upload an image

`POST /accounts/{account_id}/images/v1`

Upload an image with up to 10 Megabytes using a single HTTP POST (multipart/form-data) request.
An image can be uploaded by sending an image file or passing an accessible to an API url.


## Parameters

- **account_id** (string, required) [path]: 


## Response

### 200

Upload an image response

- **result** (object, optional): 

### 4XX

Upload an image response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
