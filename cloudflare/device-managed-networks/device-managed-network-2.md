# Update a device managed network

`PUT /accounts/{account_id}/devices/networks/{network_id}`

Updates a configured device managed network.

## Parameters

- **network_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **config** (object, optional): The configuration object containing information for the WARP client to detect the managed network.
- **name** (string, optional): The name of the device managed network. This name must be unique.
- **type** (string, optional): The type of device managed network. Values: `tls`

## Response

### 200

Update a device managed network response.

- **result** (object, optional): 

### 4XX

Update a device managed network response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
