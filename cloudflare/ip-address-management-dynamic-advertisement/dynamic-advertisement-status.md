# Update Prefix Dynamic Advertisement Status

`PATCH /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/status`

> **Deprecated**

Advertise or withdraw the BGP route for a prefix.

**Deprecated:** Prefer the BGP Prefixes endpoints, which additionally allow for advertising and withdrawing 
subnets of an IP prefix.


## Parameters

- **prefix_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **advertised** (boolean, required): Advertisement status of the prefix. If `true`, the BGP route for the prefix is advertised to the Internet. If 
`false`, the BGP route is withdrawn.


## Response

### 200

Update Prefix Dynamic Advertisement Status response

- **result** (object, optional): 

### 4XX

Update Prefix Dynamic Advertisement Status response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
