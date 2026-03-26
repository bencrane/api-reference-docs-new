# List Monitors

`GET /user/load_balancers/monitors`

List configured monitors for a user.

## Response

### 200

Successful list monitors response.

- **result** (array, optional): 

### 4XX

Failed list monitors response.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
