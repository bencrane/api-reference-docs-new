# Enable or Disable a Hostname for Client Authentication

`PUT /zones/{zone_id}/origin_tls_client_auth/hostnames`

Associate a hostname to a certificate and enable, disable or invalidate the association. If disabled, client certificate will not be sent to the hostname even if activated at the zone level. 100 maximum associations on a single certificate are allowed. Note: Use a null value for parameter *enabled* to invalidate the association.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **config** (array, required): 

## Response

### 200

Enable or Disable a Hostname for Client Authentication response

- **result** (array, optional): 

### 4XX

Enable or Disable a Hostname for Client Authentication response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
