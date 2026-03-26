# Update device certificate provisioning status

`PATCH /zones/{zone_id}/devices/policy/certificates`

Enable Zero Trust Clients to provision a certificate, containing a x509 subject, and referenced by Access device posture policies when the client visits MTLS protected domains. This facilitates device posture without a WARP session.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **enabled** (boolean, required): The current status of the device policy certificate provisioning feature for WARP clients.

## Response

### 200

Update a zone to toggle permission for devices to provision certificates response.

- **result** (object, optional): 

### 4XX

Patch a zone to toggle permission for devices to provision certificates failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
