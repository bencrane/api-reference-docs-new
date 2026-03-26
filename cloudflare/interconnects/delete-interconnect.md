# Delete an interconnect object

`DELETE /accounts/{account_id}/cni/interconnects/{icon}`



## Parameters

- **icon** (string, required) [path]: Interconnect name to retrieve information about
- **account_id** (string, required) [path]: 

## Response

### 200

Successfully deleted interconnect

### 400

Bad request

### 404

Interconnect not found

### 500

Internal server error
