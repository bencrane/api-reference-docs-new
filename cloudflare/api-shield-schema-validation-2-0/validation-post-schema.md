# Upload a schema to a zone

`POST /zones/{zone_id}/api_gateway/user_schemas`

> **Deprecated**




## Response

### 200

Upload a schema response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Upload a schema response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
- **upload_details** (object, optional):
