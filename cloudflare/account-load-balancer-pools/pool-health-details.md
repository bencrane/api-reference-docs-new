# Pool Health Details

`GET /accounts/{account_id}/load_balancers/pools/{pool_id}/health`

Fetch the latest pool health status for a single pool.

## Parameters

- **pool_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Pool Health Details response.

- **result** (object, optional): A list of regions from which to run health checks. Null means every Cloudflare data center.

### 4XX

Pool Health Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
