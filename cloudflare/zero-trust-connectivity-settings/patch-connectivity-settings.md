# Updates the Zero Trust Connectivity Settings

`PATCH /accounts/{account_id}/zerotrust/connectivity_settings`

Updates the Zero Trust Connectivity Settings for the given account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **icmp_proxy_enabled** (boolean, optional): A flag to enable the ICMP proxy for the account network.
- **offramp_warp_enabled** (boolean, optional): A flag to enable WARP to WARP traffic.

## Response

### 200

Update Zero Trust Connectivity Settings response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): 
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Update Zero Trust Connectivity Settings response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
