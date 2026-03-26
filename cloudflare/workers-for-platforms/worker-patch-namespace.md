# Patch dispatch namespace

`PATCH /accounts/{account_id}/workers/dispatch/namespaces/{dispatch_namespace}`

Patch a Workers for Platforms namespace. Omitted fields are left unchanged.

## Parameters

- **account_id** (string, required) [path]: 
- **dispatch_namespace** (string, required) [path]: 

## Request Body

- **name** (string, optional): The name of the dispatch namespace.
- **trusted_workers** (boolean, optional): Whether the Workers in the namespace are executed in a "trusted" manner. When a Worker is trusted, it has access to the shared caches for the zone in the Cache API, and has access to the `request.cf` object on incoming Requests. When a Worker is untrusted, caches are not shared across the zone, and `request.cf` is undefined. By default, Workers in a namespace are "untrusted".

## Response

### 200

Patch a Workers for Platforms namespace.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Failure to patch Workers for Platforms namespace.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
