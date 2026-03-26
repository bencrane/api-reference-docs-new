# Create new target

`POST /accounts/{account_id}/infrastructure/targets`



## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **hostname** (string, required): A non-unique field that refers to a target. Case insensitive, maximum
length of 255 characters, supports the use of special characters dash
and period, does not support spaces, and must start and end with an
alphanumeric character.
- **ip** (object, required): The IPv4/IPv6 address that identifies where to reach a target

## Response

### 200

Successfully created the target

- **result** (object, optional): 

### 4XX

Failed to create the target

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
