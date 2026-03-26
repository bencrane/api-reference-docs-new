# Create Client Certificate

`POST /zones/{zone_id}/client_certificates`

Create a new API Shield mTLS Client Certificate

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **csr** (string, required): The Certificate Signing Request (CSR). Must be newline-encoded.
- **validity_days** (integer, required): The number of days the Client Certificate will be valid after the issued_on date

## Response

### 200

Create Client Certificate Response

- **result** (object, optional): 

### 4XX

Create Client Certificate Response Failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
