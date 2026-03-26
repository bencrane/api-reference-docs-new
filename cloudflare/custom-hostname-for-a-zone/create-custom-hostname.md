# Create Custom Hostname

`POST /zones/{zone_id}/custom_hostnames`

Add a new custom hostname and request that an SSL certificate be issued for it. One of three validation methods—http, txt, email—should be used, with 'http' recommended if the CNAME is already in place (or will be soon). Specifying 'email' will send an email to the WHOIS contacts on file for the base domain plus hostmaster, postmaster, webmaster, admin, administrator. If http is used and the domain is not already pointing to the Managed CNAME host, the PATCH method must be used once it is (to complete validation).  Enable bundling of certificates using the custom_cert_bundle field. The bundling process requires the following condition One certificate in the bundle must use an RSA, and the other must use an ECDSA.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **custom_metadata** (object, optional): Unique key/value metadata for this hostname. These are per-hostname (customer) settings.
- **hostname** (string, required): The custom hostname that will point to your hostname via CNAME.
- **ssl** (object, optional): SSL properties used when creating the custom hostname.

## Response

### 200

Create Custom Hostname response

- **result** (object, optional): 

### 4XX

Create Custom Hostname response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
