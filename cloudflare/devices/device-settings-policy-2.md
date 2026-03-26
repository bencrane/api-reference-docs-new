# Create a device settings profile

`POST /accounts/{account_id}/devices/policy`

Creates a device settings profile to be applied to certain devices matching the criteria.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **allow_mode_switch** (boolean, optional): Whether to allow the user to switch WARP between modes.
- **allow_updates** (boolean, optional): Whether to receive update notifications when a new version of the client is available.
- **allowed_to_leave** (boolean, optional): Whether to allow devices to leave the organization.
- **auto_connect** (number, optional): The amount of time in seconds to reconnect after having been disabled.
- **captive_portal** (number, optional): Turn on the captive portal after the specified amount of time.
- **description** (object, optional): 
- **disable_auto_fallback** (boolean, optional): If the `dns_server` field of a fallback domain is not present, the client will fall back to a best guess of the default/system DNS resolvers unless this policy option is set to `true`.
- **enabled** (boolean, optional): Whether the policy will be applied to matching devices.
- **exclude** (array, optional): List of routes excluded in the WARP client's tunnel. Both 'exclude' and 'include' cannot be set in the same request.
- **exclude_office_ips** (boolean, optional): Whether to add Microsoft IPs to Split Tunnel exclusions.
- **include** (array, optional): List of routes included in the WARP client's tunnel. Both 'exclude' and 'include' cannot be set in the same request.
- **lan_allow_minutes** (number, optional): The amount of time in minutes a user is allowed access to their LAN. A value of 0 will allow LAN access until the next WARP reconnection, such as a reboot or a laptop waking from sleep. Note that this field is omitted from the response if null or unset.
- **lan_allow_subnet_size** (number, optional): The size of the subnet for the local access network. Note that this field is omitted from the response if null or unset.
- **match** (string, required): The wirefilter expression to match devices. Available values: "identity.email", "identity.groups.id", "identity.groups.name", "identity.groups.email", "identity.service_token_uuid", "identity.saml_attributes", "network", "os.name", "os.version".
- **name** (string, required): The name of the device settings profile.
- **precedence** (number, required): The precedence of the policy. Lower values indicate higher precedence. Policies will be evaluated in ascending order of this field.
- **register_interface_ip_with_dns** (boolean, optional): Determines if the operating system will register WARP's local interface IP with your on-premises DNS server.
- **sccm_vpn_boundary_support** (boolean, optional): Determines whether the WARP client indicates to SCCM that it is inside a VPN boundary. (Windows only).
- **service_mode_v2** (object, optional): 
- **support_url** (string, optional): The URL to launch when the Send Feedback button is clicked.
- **switch_locked** (boolean, optional): Whether to allow the user to turn off the WARP switch and disconnect the client.
- **tunnel_protocol** (string, optional): Determines which tunnel protocol to use.

## Response

### 200

Create a device settings profile response.

- **result** (object, optional): 

### 4XX

Create a device settings profile response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
