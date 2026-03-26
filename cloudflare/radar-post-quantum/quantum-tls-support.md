# Check Post-Quantum TLS support

`GET /radar/post_quantum/tls/support`

Tests whether a hostname or IP address supports Post-Quantum (PQ) TLS key exchange. Returns information about the negotiated key exchange algorithm and whether it uses PQ cryptography.

## Parameters

- **host** (string, required) [query]: Hostname or IP address to test for Post-Quantum TLS support, optionally with port (defaults to 443).

## Response

### 200

Successful response.

- **result** (object): 
- **success** (boolean): 

### 400

Bad request.

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
