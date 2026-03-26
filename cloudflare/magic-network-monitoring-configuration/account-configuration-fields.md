# Update account configuration fields

`PATCH /accounts/{account_id}/mnm/config`

Update fields in an existing network monitoring configuration.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **default_sampling** (number, optional): Fallback sampling rate of flow messages being sent in packets per second. This should match the packet sampling rate configured on the router.
- **name** (string, optional): The account name.
- **router_ips** (array, optional): 
- **warp_devices** (array, optional): 

## Response

### 200

Update account configuration fields response

- **result** (object, optional): 

### 4XX

Update account configuration fields response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
