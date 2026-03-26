# Create Certificate

`POST /certificates`

Create an Origin CA certificate. You can use an Origin CA Key as your User Service Key or an API token when calling this endpoint ([see above](#requests)).

## Request Body

- **csr** (string, required): The Certificate Signing Request (CSR). Must be newline-encoded.
- **hostnames** (array, required): Array of hostnames or wildcard names bound to the certificate.
Hostnames must be fully qualified domain names (FQDNs) belonging to zones on your account (e.g., `example.com` or `sub.example.com`). Wildcards are supported only as a `*.` prefix for a single level (e.g., `*.example.com`). Double wildcards (`*.*.example.com`) and interior wildcards (`foo.*.example.com`) are not allowed. The wildcard suffix must be a multi-label domain (`*.example.com` is valid, but `*.com` is not). Unicode/IDN hostnames are accepted and automatically converted to punycode.
- **request_type** (string, required): Signature type desired on certificate ("origin-rsa" (rsa), "origin-ecc" (ecdsa), or "keyless-certificate" (for Keyless SSL servers). Values: `origin-rsa`, `origin-ecc`, `keyless-certificate`
- **requested_validity** (number, optional): The number of days for which the certificate should be valid. Values: `7`, `30`, `90`, `365`, `730`, `1095`, `5475`

## Response

### 200

Create Certificate response

- **result** (object, optional): 

### 4XX

Create Certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
