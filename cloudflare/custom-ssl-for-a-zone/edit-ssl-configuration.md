# Edit SSL Configuration

`PATCH /zones/{zone_id}/custom_certificates/{custom_certificate_id}`

Upload a new private key and/or PEM/CRT for the SSL certificate. Note: PATCHing a configuration for sni_custom certificates will result in a new resource id being returned, and the previous one being deleted.

## Parameters

- **custom_certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **bundle_method** (string, optional): A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. Values: `ubiquitous`, `optimal`, `force`
- **certificate** (string, optional): The zone's SSL certificate or certificate and the intermediate(s).
- **custom_csr_id** (string, optional): The identifier for the Custom CSR that was used.
- **deploy** (string, optional): The environment to deploy the certificate to, defaults to production Values: `staging`, `production`
- **geo_restrictions** (object, optional): Specify the region where your private key can be held locally for optimal TLS performance. HTTPS connections to any excluded data center will still be fully encrypted, but will incur some latency while Keyless SSL is used to complete the handshake with the nearest allowed data center. Options allow distribution to only to U.S. data centers, only to E.U. data centers, or only to highest security data centers. Default distribution is to all Cloudflare datacenters, for optimal performance.
- **policy** (string, optional): Specify the policy that determines the region where your private key will be held locally. HTTPS connections to any excluded data center will still be fully encrypted, but will incur some latency while Keyless SSL is used to complete the handshake with the nearest allowed data center. Any combination of countries, specified by their two letter country code (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements) can be chosen, such as 'country: IN', as well as 'region: EU' which refers to the EU region. If there are too few data centers satisfying the policy, it will be rejected.
Note: The API accepts this field as either "policy" or "policy_restrictions" in requests. Responses return this field as "policy_restrictions".
- **private_key** (string, optional): The zone's private key.

## Response

### 200

Edit SSL Configuration response

- **result** (object, optional): 

### 4XX

Edit SSL Configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
