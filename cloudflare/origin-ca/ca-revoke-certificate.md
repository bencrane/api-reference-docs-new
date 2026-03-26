# Revoke Certificate

`DELETE /certificates/{certificate_id}`

Revoke an existing Origin CA certificate by its serial number. You can use an Origin CA Key as your User Service Key or an API token when calling this endpoint ([see above](#requests)).

## Parameters

- **certificate_id** (string, required) [path]: 


## Response

### 200

Revoke Certificate response

- **result** (object, optional): 

### 4XX

Revoke Certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
