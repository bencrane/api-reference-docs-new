# Analyze Certificate

`POST /zones/{zone_id}/ssl/analyze`

Returns the set of hostnames, the signature algorithm, and the expiration date of the certificate.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **bundle_method** (string, optional): A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. Values: `ubiquitous`, `optimal`, `force`
- **certificate** (string, optional): The zone's SSL certificate or certificate and the intermediate(s).

## Response

### 200

Analyze Certificate response

- **result** (object, optional): 

### 4XX

Analyze Certificate response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
