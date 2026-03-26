# Detach Domain

`DELETE /accounts/{account_id}/workers/domains/{domain_id}`

Detaches a domain from a Worker. Both the Worker and all of its previews are no longer routable using this domain.

## Parameters

- **account_id** (string, required) [path]: 
- **domain_id** (string, required) [path]: 

## Response

### 200

Detach domain response.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Detach domain failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
