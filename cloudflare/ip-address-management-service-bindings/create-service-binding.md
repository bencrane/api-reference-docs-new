# Create Service Binding

`POST /accounts/{account_id}/addressing/prefixes/{prefix_id}/bindings`

Creates a new Service Binding, routing traffic to IPs within the given CIDR to a service running on Cloudflare's network.
**NOTE:** The first Service Binding created for an IP Prefix must exactly match the IP Prefix's CIDR. Subsequent Service Bindings may be created with a more-specific CIDR. Refer to the  [Service Bindings Documentation](https://developers.cloudflare.com/byoip/service-bindings/) for compatibility details.


## Parameters

- **account_id** (string, required) [path]: 
- **prefix_id** (string, required) [path]: 

## Request Body

- **cidr** (string, required): IP Prefix in Classless Inter-Domain Routing format.
- **service_id** (string, required): Identifier of a Service on the Cloudflare network. Available services and their IDs may be found in the
**List Services** endpoint.


## Response

### 201

The created Service Binding

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create Service Binding response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
