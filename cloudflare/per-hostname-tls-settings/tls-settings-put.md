# Edit TLS setting for hostname

`PUT /zones/{zone_id}/hostnames/settings/{setting_id}/{hostname}`

Update the tls setting value for the hostname.

## Parameters

- **zone_id** (string, required) [path]: 
- **setting_id** (string, required) [path]: 
- **hostname** (string, required) [path]: 

## Request Body

- **value** (object, required): The TLS setting value. The type depends on the `setting_id` used in the request path:
- `ciphers`: an array of allowed cipher suite strings in BoringSSL format (e.g., `["ECDHE-RSA-AES128-GCM-SHA256", "AES128-GCM-SHA256"]`)
- `min_tls_version`: a string indicating the minimum TLS version — one of `"1.0"`, `"1.1"`, `"1.2"`, or `"1.3"` (e.g., `"1.2"`)
- `http2`: a string indicating whether HTTP/2 is enabled — `"on"` or `"off"` (e.g., `"on"`)

## Response

### 200

Edit TLS setting for hostname response

- **result** (object, optional): 

### 4XX

Edit TLS setting for hostname response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
