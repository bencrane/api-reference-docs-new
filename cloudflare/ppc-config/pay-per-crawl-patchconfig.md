# Changes pay-per-crawl config for a zone

`PATCH /zones/{zone_id}/pay-per-crawl/configuration`

Changes the pay-per-crawl config for a zone.

## Parameters

- **zone_id** (string, required) [path]: zone id

## Request Body

- **bot_overrides** (object, optional): 
- **enabled** (boolean, optional): 
- **price_usd_microcents** (integer, optional): 

## Response

### 200

OK

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **result_info** (object): 
- **success** (boolean): 

### 400

Bad Request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
