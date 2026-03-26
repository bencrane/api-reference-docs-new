# Update BGP Prefix

`PATCH /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes/{bgp_prefix_id}`

Update the properties of a BGP Prefix, such as the on demand advertisement status (advertised or withdrawn).

## Parameters

- **account_id** (string, required) [path]: 
- **prefix_id** (string, required) [path]: 
- **bgp_prefix_id** (string, required) [path]: 

## Request Body

- **asn_prepend_count** (integer, optional): Number of times to prepend the Cloudflare ASN to the BGP AS-Path attribute
- **auto_advertise_withdraw** (boolean, optional): Determines if Cloudflare advertises a BYOIP BGP prefix even when there is no matching BGP prefix in the Magic routing table. When true, Cloudflare will automatically withdraw the BGP prefix when there are no matching BGP routes, and will resume advertising when there is at least one matching BGP route.
- **on_demand** (object, optional): 

## Response

### 200

Update BGP Prefix response

- **result** (object, optional): 

### 4XX

Update BGP Prefix response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
