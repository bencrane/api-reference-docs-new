# Create an IPsec tunnel

`POST /accounts/{account_id}/magic/ipsec_tunnels`

Creates a new IPsec tunnel associated with an account. Use `?validate_only=true` as an optional query parameter to only run validation without persisting changes.

## Parameters

- **account_id** (string, required) [path]: 
- **x-magic-new-hc-target** (boolean, optional) [header]: If true, the health check target in the request and response bodies will be presented using the new object format. Defaults to false.

## Request Body

- **automatic_return_routing** (boolean, optional): True if automatic stateful return routing should be enabled for a tunnel, false otherwise.
- **bgp** (object, optional): 
- **cloudflare_endpoint** (string, optional): The IP address assigned to the Cloudflare side of the IPsec tunnel.
- **custom_remote_identities** (object, optional): 
- **customer_endpoint** (string, optional): The IP address assigned to the customer side of the IPsec tunnel. Not required, but must be set for proactive traceroutes to work.
- **description** (string, optional): An optional description forthe IPsec tunnel.
- **health_check** (object, optional): 
- **interface_address** (string, optional): A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side of the tunnel. Select the subnet from the following private IP space: 10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
- **interface_address6** (string, optional): A 127 bit IPV6 prefix from within the virtual_subnet6 prefix space with the address being the first IP of the subnet and not same as the address of virtual_subnet6. Eg if virtual_subnet6 is 2606:54c1:7:0:a9fe:12d2::/127 , interface_address6 could be 2606:54c1:7:0:a9fe:12d2:1:200/127
- **name** (string, optional): The name of the IPsec tunnel. The name cannot share a name with other tunnels.
- **psk** (string, optional): A randomly generated or provided string for use in the IPsec tunnel.
- **replay_protection** (boolean, optional): If `true`, then IPsec replay protection will be supported in the Cloudflare-to-customer direction.

## Response

### 200

Create IPsec tunnels response

- **result** (object, optional): 

### 4XX

Create IPsec tunnels response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
