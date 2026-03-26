# Batch DNS Records

`POST /zones/{zone_id}/dns_records/batch`

Send a Batch of DNS Record API calls to be executed together.

Notes:
- Although Cloudflare will execute the batched operations in a single database transaction, Cloudflare's distributed KV store must treat each record change as a single key-value pair. This means that the propagation of changes is not atomic. See [the documentation](https://developers.cloudflare.com/dns/manage-dns-records/how-to/batch-record-changes/ "Batch DNS records") for more information.
- The operations you specify within the /batch request body are always executed in the following order:

    - Deletes
    - Patches
    - Puts
    - Posts


## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **deletes** (array, optional): 
- **patches** (array, optional): 
- **posts** (array, optional): 
- **puts** (array, optional): 

## Response

### 200

Batch DNS Records response

_Empty object_

### 4XX

Batch DNS Records response failure

_Empty object_
