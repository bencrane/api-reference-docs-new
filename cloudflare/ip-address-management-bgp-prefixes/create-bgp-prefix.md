# Create BGP Prefix

`POST /accounts/{account_id}/addressing/prefixes/{prefix_id}/bgp/prefixes`

Create a BGP prefix, controlling the BGP advertisement status of a specific subnet. When created, BGP prefixes are initially withdrawn, and can be advertised with the Update BGP Prefix API.

## Parameters

- **account_id** (string, required) [path]: 
- **prefix_id** (string, required) [path]: 

## Request Body

- **cidr** (string, required): IP Prefix in Classless Inter-Domain Routing format.

## Response

### 200

Create BGP Prefix response

- **result** (object, optional): 

### 4XX

Create BGP Prefix response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
