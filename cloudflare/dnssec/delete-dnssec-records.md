# Delete DNSSEC records

`DELETE /zones/{zone_id}/dnssec`

Delete DNSSEC.

## Parameters

- **zone_id** (string, required) [path]: 


## Response

### 200

Delete DNSSEC records response.

- **result** (string, optional): 

### 4XX

Delete DNSSEC records response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
