# Address Map Details

`GET /accounts/{account_id}/addressing/address_maps/{address_map_id}`

Show a particular address map owned by the account.

## Parameters

- **address_map_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Address Map Details response

- **result** (object, optional): 

### 4XX

Address Map Details response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
