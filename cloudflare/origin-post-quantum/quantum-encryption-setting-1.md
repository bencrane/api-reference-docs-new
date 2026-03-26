# Change Origin Post-Quantum Encryption setting

`PUT /zones/{zone_id}/cache/origin_post_quantum_encryption`

Instructs Cloudflare to use Post-Quantum (PQ) key agreement algorithms when connecting to your origin. Preferred instructs Cloudflare to opportunistically send a Post-Quantum keyshare in the first message to the origin (for fastest connections when the origin supports and prefers PQ), supported means that PQ algorithms are advertised but only used when requested by the origin, and off means that PQ algorithms are not advertised.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **value** (string, required): Value of the Origin Post Quantum Encryption Setting. Values: `preferred`, `supported`, `off`

## Response

### 200

Change Origin Post-Quantum Encryption setting response.

_Empty object_

### 4XX

Change Origin Post-Quantum Encryption setting response failure.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
