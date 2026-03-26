# Create Keyless SSL Configuration

`POST /zones/{zone_id}/keyless_certificates`

Creates a Keyless SSL configuration that allows SSL/TLS termination without exposing private keys to Cloudflare. Keys remain on your infrastructure.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **bundle_method** (string, optional): A ubiquitous bundle has the highest probability of being verified everywhere, even by clients using outdated or unusual trust stores. An optimal bundle uses the shortest chain and newest intermediates. And the force bundle verifies the chain, but does not otherwise modify it. Values: `ubiquitous`, `optimal`, `force`
- **certificate** (string, required): The zone's SSL certificate or SSL certificate and intermediate(s).
- **host** (string, required): The keyless SSL name.
- **name** (string, optional): The keyless SSL name.
- **port** (number, required): The keyless SSL port used to communicate between Cloudflare and the client's Keyless SSL server.
- **tunnel** (object, optional): Configuration for using Keyless SSL through a Cloudflare Tunnel

## Response

### 200

Create Keyless SSL Configuration response

- **result** (object, optional): 

### 4XX

Create Keyless SSL Configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
