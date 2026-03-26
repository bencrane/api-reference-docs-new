# Create account configuration

`POST /accounts/{account_id}/mnm/config`

Create a new network monitoring configuration.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **default_sampling** (number, required): Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate configured on the router.
- **name** (string, required): The account name.
- **router_ips** (array, optional): 
- **warp_devices** (array, optional): 

## Response

### 200

Create account configuration response

- **result** (object, optional): 

### 4XX

Create account configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
