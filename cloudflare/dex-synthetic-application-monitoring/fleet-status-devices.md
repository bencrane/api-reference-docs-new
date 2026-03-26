# List fleet status devices

`GET /accounts/{account_id}/dex/fleet-status/devices`

List details for devices using WARP

## Parameters

- **account_id** (string, required) [path]: Unique identifier for account
- **to** (string, required) [query]: Time range end in ISO format
- **from** (string, required) [query]: Time range beginning in ISO format
- **page** (string, required) [query]: Page number
- **per_page** (string, required) [query]: Number of results per page
- **sort_by** (string, optional) [query]: Dimension to sort results by
- **colo** (string, optional) [query]: Cloudflare colo
- **device_id** (string, optional) [query]: Device-specific ID, given as UUID v4
- **mode** (string, optional) [query]: The mode under which the WARP client is run
- **status** (string, optional) [query]: Network status
- **platform** (string, optional) [query]: Operating system
- **version** (string, optional) [query]: WARP client version
- **source** (string, optional) [query]: Source:
  * `hourly` - device details aggregated hourly, up to 7 days prior
  * `last_seen` - device details, up to 60 minutes prior
  * `raw` - device details, up to 7 days prior


## Response

### 200

List devices response

- **result** (array, optional): 

### 4XX

List devices response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
