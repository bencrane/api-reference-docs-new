# Edit Custom Hostname

`PATCH /zones/{zone_id}/custom_hostnames/{custom_hostname_id}`

Modify SSL configuration for a custom hostname. When sent with SSL config that matches existing config, used to indicate that hostname should pass domain control validation (DCV). Can also be used to change validation type, e.g., from 'http' to 'email'. Bundle an existing certificate with another certificate by using the "custom_cert_bundle" field. The bundling process supports combining certificates as long as the following condition is met. One certificate must use the RSA algorithm, and the other must use the ECDSA algorithm.

## Parameters

- **custom_hostname_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **custom_metadata** (object, optional): Unique key/value metadata for this hostname. These are per-hostname (customer) settings.
- **custom_origin_server** (string, optional): a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME record.
- **custom_origin_sni** (string, optional): A hostname that will be sent to your custom origin server as SNI for TLS handshake. This can be a valid subdomain of the zone or custom origin server name or the string ':request_host_header:' which will cause the host header in the request to be used as SNI. Not configurable with default/fallback origin server.
- **ssl** (object, optional): SSL properties used when creating the custom hostname.

## Response

### 200

Edit Custom Hostname response

- **result** (object, optional): 

### 4XX

Edit Custom Hostname response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
