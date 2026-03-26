# Update NetFlow Configuration

`PATCH /accounts/{account_id}/magic/sites/{site_id}/netflow_config`

Updates NetFlow configuration for a site.

## Parameters

- **account_id** (string, required) [path]: 
- **site_id** (string, required) [path]: 

## Request Body

- **active_timeout** (integer, optional): Timeout in seconds for active flows.
- **collector_ip** (string, optional): IPv4 address of the NetFlow collector.
- **collector_port** (integer, optional): UDP port of the NetFlow collector.
- **inactive_timeout** (integer, optional): Timeout in seconds for inactive flows.
- **sampling_rate** (integer, optional): Sampling rate for NetFlow records (1 = every packet).

## Response

### 200

Update NetFlow Configuration response

- **result** (object, optional): NetFlow configuration for a site.

### 4XX

Update NetFlow Configuration response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
