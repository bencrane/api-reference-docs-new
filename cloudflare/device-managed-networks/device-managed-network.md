# Create a device managed network

`POST /accounts/{account_id}/devices/networks`

Creates a new device managed network.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **config** (object, required): The configuration object containing information for the WARP client to detect the managed network.
- **name** (string, required): The name of the device managed network. This name must be unique.
- **type** (string, required): The type of device managed network. Values: `tls`

## Response

### 200

Create a device managed networks response.

- **result** (object, optional): 

### 4XX

Create a device managed networks response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
