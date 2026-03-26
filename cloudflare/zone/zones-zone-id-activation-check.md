# Rerun the Activation Check

`PUT /zones/{zone_id}/activation_check`

Triggeres a new activation check for a PENDING Zone. This can be
triggered every 5 min for paygo/ent customers, every hour for FREE
Zones.

## Parameters

- **zone_id** (string, required) [path]: Zone ID

## Response

### 200

Successful Response

- **result** (object, optional): 

### 4XX

Client Error

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
