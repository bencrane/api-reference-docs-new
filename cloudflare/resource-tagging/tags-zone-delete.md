# Delete tags from a zone-level resource

`DELETE /zones/{zone_id}/tags`

Removes all tags from a specific zone-level resource.

## Parameters

- **zone_id** (string, required) [path]: 
- **If-Match** (string, optional) [header]: ETag value for optimistic concurrency control. When provided, the server will
verify the current resource ETag matches before applying the write. Returns
412 Precondition Failed if the resource has been modified since the ETag was
obtained. Omit this header for unconditional writes.


## Request Body

One of: object, Variant 2

## Response

### 204

Tags successfully deleted (no content).

### 412

Precondition failed. The resource has been modified since the provided ETag was obtained.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 4XX

Delete tags response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.

### 5XX

Delete tags response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
