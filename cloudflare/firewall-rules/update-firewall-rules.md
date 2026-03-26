# Update firewall rules

`PUT /zones/{zone_id}/firewall/rules`

> **Deprecated**

Updates one or more existing firewall rules.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

_Unknown type_

## Response

### 200

Update firewall rules response

- **result** (array, optional): 

### 4XX

Update firewall rules response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
