# List images

`GET /accounts/{account_id}/images/v1`

> **Deprecated**

List up to 100 images with one request. Use the optional parameters below to get a specific range of images.

## Parameters

- **account_id** (string, required) [path]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **creator** (string, optional) [query]: 

## Response

### 200

List images response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

List images response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
