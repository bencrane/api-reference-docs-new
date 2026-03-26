# Activate a Zero Trust certificate

`POST /accounts/{account_id}/gateway/certificates/{certificate_id}/activate`

Bind a single Zero Trust certificate to the edge.

## Parameters

- **certificate_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 202

Activates Zero Trust certificate details response.

_Empty object_

### 4XX

Activates Zero Trust certificate details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`
