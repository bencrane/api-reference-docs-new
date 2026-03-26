# Update Peer

`PUT /accounts/{account_id}/secondary_dns/peers/{peer_id}`

Modify Peer.

## Parameters

- **peer_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **id** (string, required): 
- **ip** (string, optional): IPv4/IPv6 address of primary or secondary nameserver, depending on what zone this peer is linked to. For primary zones this IP defines the IP of the secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary zones this IP defines the IP of the primary nameserver Cloudflare will send AXFR/IXFR requests to.
- **ixfr_enable** (boolean, optional): Enable IXFR transfer protocol, default is AXFR. Only applicable to secondary zones.
- **name** (string, required): The name of the peer.
- **port** (number, optional): DNS port of primary or secondary nameserver, depending on what zone this peer is linked to.
- **tsig_id** (string, optional): TSIG authentication will be used for zone transfer if configured.

## Response

### 200

Update Peer response.

_Empty object_

### 4XX

Update Peer response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
