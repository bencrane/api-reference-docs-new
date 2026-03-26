# Pool Details

`GET /user/load_balancers/pools/{pool_id}`

Fetch a single configured pool.

## Parameters

- **pool_id** (string, required) [path]: 

## Response

### 200

Pool Details response.

- **result** (object, optional): 

### 4XX

Pool Details response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
