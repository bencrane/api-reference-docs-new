# Create firewall rules

`POST /zones/{zone_id}/firewall/rules`

> **Deprecated**

Create one or more firewall rules.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **action** (object, required): The action to perform when the threshold of matched traffic within the configured period is exceeded.
- **filter** (object, required): 

## Response

### 200

Create firewall rules response

- **result** (array, optional): 

### 4XX

Create firewall rules response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Defines whether the API call was successful. Values: `false`
