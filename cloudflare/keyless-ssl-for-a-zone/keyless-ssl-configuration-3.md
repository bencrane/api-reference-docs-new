# Edit Keyless SSL Configuration

`PATCH /zones/{zone_id}/keyless_certificates/{keyless_certificate_id}`

This will update attributes of a Keyless SSL. Consists of one or more of the following:  host,name,port.

## Parameters

- **keyless_certificate_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, optional): Whether or not the Keyless SSL is on or off.
- **host** (string, optional): The keyless SSL name.
- **name** (string, optional): The keyless SSL name.
- **port** (number, optional): The keyless SSL port used to communicate between Cloudflare and the client's Keyless SSL server.
- **tunnel** (object, optional): Configuration for using Keyless SSL through a Cloudflare Tunnel

## Response

### 200

Edit Keyless SSL Configuration response

- **result** (object, optional): 

### 4XX

Edit Keyless SSL Configuration response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
