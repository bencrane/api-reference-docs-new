# Delete a device posture rule

`DELETE /accounts/{account_id}/devices/posture/{rule_id}`

Deletes a device posture rule.

## Parameters

- **rule_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 


## Response

### 200

Delete a device posture rule response.

- **result** (object, optional): 

### 4XX

Delete a device posture rule response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
