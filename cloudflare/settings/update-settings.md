# Update the current settings for the active account

`PUT /accounts/{account_id}/cni/settings`



## Parameters

- **account_id** (string, required) [path]: Account tag to update settings for

## Request Body

- **default_asn** (integer, optional): 

## Response

### 200

The active account settings values

- **default_asn** (integer): 

### 400

Bad request

### 404

Account not found

### 500

Internal server error
