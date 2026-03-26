# Get the Latest Scan Result

`GET /accounts/{account_id}/cloudforce-one/scans/results/{config_id}`



## Parameters

- **account_id** (string, required) [path]: Defines the Account ID.
- **config_id** (string, required) [path]: Defines the Config ID.

## Response

### 200

Returns Current Open Ports.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 4XX

Get the Latest Scan Result failure.

- **errors** (object, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional):
