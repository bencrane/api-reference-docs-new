# Create a new App

`POST /accounts/{account_id}/magic/apps`

Creates a new App for an account

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **hostnames** (array, optional): FQDNs to associate with traffic decisions.
- **ip_subnets** (array, optional): IPv4 CIDRs to associate with traffic decisions. (IPv6 CIDRs are currently unsupported)
- **name** (string, required): Display name for the app.
- **source_subnets** (array, optional): IPv4 CIDRs to associate with traffic decisions. (IPv6 CIDRs are currently unsupported)
- **type** (string, required): Category of the app.

## Response

### 201

Create Account App response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): Custom app defined for an account.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Create Account App response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
