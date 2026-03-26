# Delete firewall rules

`DELETE /zones/{zone_id}/firewall/rules`

> **Deprecated**

Deletes existing firewall rules.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **id** (string, required): The unique identifier of the firewall rule.

## Response

### 200

Delete firewall rules response

- **result** (array, optional): 

### 4XX

Delete firewall rules response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
