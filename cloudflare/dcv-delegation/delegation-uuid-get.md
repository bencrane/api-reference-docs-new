# Retrieve the DCV Delegation unique identifier.

`GET /zones/{zone_id}/dcv_delegation/uuid`

Retrieve the account and zone specific unique identifier used as part of the CNAME target for DCV Delegation.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Retrieve the DCV Delegation unique identifier response.

- **result** (object, optional): 

### 4XX

Retrieve the DCV Delegation unique identifier response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
