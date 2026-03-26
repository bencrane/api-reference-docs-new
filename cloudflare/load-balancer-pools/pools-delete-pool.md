# Delete Pool

`DELETE /user/load_balancers/pools/{pool_id}`

Delete a configured pool.

## Parameters

- **pool_id** (string, required) [path]: 


## Response

### 200

Delete Pool response.

- **result** (object, optional): 

### 4XX

Delete Pool response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
