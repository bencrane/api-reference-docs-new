# Update priority of firewall rules

`PATCH /zones/{zone_id}/firewall/rules`

> **Deprecated**

Updates the priority of existing firewall rules.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

_Unknown type_

## Response

### 200

Update priority of firewall rules response

- **result** (array, optional): 

### 4XX

Update priority of firewall rules response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
