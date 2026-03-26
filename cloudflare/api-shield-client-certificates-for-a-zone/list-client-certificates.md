# List Client Certificates

`GET /zones/{zone_id}/client_certificates`

List all of your Zone's API Shield mTLS Client Certificates by Status and/or using Pagination

## Parameters

- **zone_id** (string, required) [path]: 
- **status** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **limit** (integer, optional) [query]: 
- **offset** (integer, optional) [query]: 

## Response

### 200

List Client Certificates Response

- **result** (array, optional): 

### 4XX

List Client Certificates Response Failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
