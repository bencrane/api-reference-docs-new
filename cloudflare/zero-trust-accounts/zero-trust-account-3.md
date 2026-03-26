# Update device settings for a Zero Trust account

`PUT /accounts/{account_id}/devices/settings`

Updates the current device settings for a Zero Trust account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **disable_for_time** (number, optional): Sets the time limit, in seconds, that a user can use an override code to bypass WARP.
- **external_emergency_signal_enabled** (boolean, optional): Controls whether the external emergency disconnect feature is enabled.
- **external_emergency_signal_fingerprint** (string, optional): The SHA256 fingerprint (64 hexadecimal characters) of the HTTPS server certificate for the external_emergency_signal_url. If provided, the WARP client will use this value to verify the server's identity. The device will ignore any response if the server's certificate fingerprint does not exactly match this value.
- **external_emergency_signal_interval** (string, optional): The interval at which the WARP client fetches the emergency disconnect signal, formatted as a duration string (e.g., "5m", "2m30s", "1h"). Minimum 30 seconds.
- **external_emergency_signal_url** (string, optional): The HTTPS URL from which to fetch the emergency disconnect signal. Must use HTTPS and have an IPv4 or IPv6 address as the host.
- **gateway_proxy_enabled** (boolean, optional): Enable gateway proxy filtering on TCP.
- **gateway_udp_proxy_enabled** (boolean, optional): Enable gateway proxy filtering on UDP.
- **root_certificate_installation_enabled** (boolean, optional): Enable installation of cloudflare managed root certificate.
- **use_zt_virtual_ip** (boolean, optional): Enable using CGNAT virtual IPv4.

## Response

### 200

Update device settings for a Zero Trust account response.

_Empty object_

### 4XX

Update device settings for a Zero Trust account response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
