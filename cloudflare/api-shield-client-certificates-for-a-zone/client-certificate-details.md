# Client Certificate Details

`GET /zones/{zone_id}/client_certificates/{client_certificate_id}`

Get Details for a single mTLS API Shield Client Certificate

## Parameters

- **zone_id** (string, required) [path]: 
- **client_certificate_id** (string, required) [path]: 

## Response

### 200

Client Certificate Details Response

- **result** (object, optional): 

### 4XX

Client Certificate Details Response Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
