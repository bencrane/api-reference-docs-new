# Add Account Custom Nameserver

`POST /accounts/{account_id}/custom_ns`



## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **ns_name** (string, required): The FQDN of the name server.
- **ns_set** (number, optional): The number of the set that this name server belongs to.

## Response

### 200

Add Account Custom Nameserver response

_Empty object_

### 4XX

Add Account Custom Nameserver response failure

_Empty object_
