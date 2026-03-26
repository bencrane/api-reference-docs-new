# Generate the Letter of Authorization (LOA) for a given interconnect

`GET /accounts/{account_id}/cni/interconnects/{icon}/loa`



## Parameters

- **icon** (string, required) [path]: Interconnect name to retrieve information about
- **account_id** (string, required) [path]: 

## Response

### 200

Generated LOA in PDF format

### 400

Bad request

### 404

Interconnect not found

### 500

Internal server error
