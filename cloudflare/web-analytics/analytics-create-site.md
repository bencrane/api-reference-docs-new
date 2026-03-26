# Create a Web Analytics site

`POST /accounts/{account_id}/rum/site_info`

Creates a new Web Analytics site.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **auto_install** (boolean, optional): If enabled, the JavaScript snippet is automatically injected for orange-clouded sites.
- **host** (string, optional): The hostname to use for gray-clouded sites.
- **zone_tag** (string, optional): The zone identifier.

## Response

### 200

Created Web Analytics site.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result** (object, optional): 

### 4XX

Failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
