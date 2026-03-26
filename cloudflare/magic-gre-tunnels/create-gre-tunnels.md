# Create a GRE tunnel

`POST /accounts/{account_id}/magic/gre_tunnels`

Creates a new GRE tunnel. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

## Parameters

- **account_id** (string, required) [path]: 
- **x-magic-new-hc-target** (boolean, optional) [header]: If true, the health check target in the request and response bodies will be presented using the new object format. Defaults to false.

## Request Body

- **automatic_return_routing** (boolean, optional): True if automatic stateful return routing should be enabled for a tunnel, false otherwise.
- **bgp** (object, optional): 
- **cloudflare_gre_endpoint** (string, required): The IP address assigned to the Cloudflare side of the GRE tunnel.
- **customer_gre_endpoint** (string, required): The IP address assigned to the customer side of the GRE tunnel.
- **description** (string, optional): An optional description of the GRE tunnel.
- **health_check** (object, optional): 
- **interface_address** (string, required): A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side of the tunnel. Select the subnet from the following private IP space: 10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
- **interface_address6** (string, optional): A 127 bit IPV6 prefix from within the virtual_subnet6 prefix space with the address being the first IP of the subnet and not same as the address of virtual_subnet6. Eg if virtual_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 , interface_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127
- **mtu** (integer, optional): Maximum Transmission Unit (MTU) in bytes for the GRE tunnel. The minimum value is 576.
- **name** (string, required): The name of the tunnel. The name cannot contain spaces or special characters, must be 15 characters or less, and cannot share a name with another GRE tunnel.
- **ttl** (integer, optional): Time To Live (TTL) in number of hops of the GRE tunnel.

## Response

### 200

Create GRE tunnels response

- **result** (object, optional): 

### 4XX

Create GRE tunnels response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
