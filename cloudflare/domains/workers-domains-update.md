# Attach Domain

`PUT /accounts/{account_id}/workers/domains`

Attaches a domain that routes traffic to a Worker.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **cert_id** (string, optional): ID of the TLS certificate issued for the domain.
- **environment** (string, optional): Worker environment associated with the domain.
- **hostname** (string, optional): Hostname of the domain. Can be either the zone apex or a subdomain of the zone. Requests to this hostname will be routed to the configured Worker.
- **id** (string, optional): Immutable ID of the domain.
- **service** (string, optional): Name of the Worker associated with the domain. Requests to the configured hostname will be routed to this Worker.
- **zone_id** (string, optional): ID of the zone containing the domain hostname.
- **zone_name** (string, optional): Name of the zone containing the domain hostname.

## Response

### 200

Attach domain response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Attach domain failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
