# Get information about an interconnect object

`GET /accounts/{account_id}/cni/interconnects/{icon}`



## Parameters

- **icon** (string, required) [path]: Interconnect name to retrieve information about
- **account_id** (string, required) [path]: 

## Response

### 200

Information about the specified interconnect

Type: object

### 400

Bad request

### 404

Interconnect not found

### 500

Internal server error
