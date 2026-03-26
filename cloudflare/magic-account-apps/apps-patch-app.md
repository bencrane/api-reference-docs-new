# Update an App

`PATCH /accounts/{account_id}/magic/apps/{account_app_id}`

Updates an Account App

## Parameters

- **account_id** (string, required) [path]: 
- **account_app_id** (string, required) [path]: 

## Request Body

- **hostnames** (array, optional): FQDNs to associate with traffic decisions.
- **ip_subnets** (array, optional): IPv4 CIDRs to associate with traffic decisions. (IPv6 CIDRs are currently unsupported)
- **name** (string, optional): Display name for the app.
- **source_subnets** (array, optional): IPv4 CIDRs to associate with traffic decisions. (IPv6 CIDRs are currently unsupported)
- **type** (string, optional): Category of the app.

## Response

### 200

Update App response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **result** (object, optional): Custom app defined for an account.
- **success** (boolean, optional): Whether the API call was successful Values: `true`

### 4XX

Update App response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful
