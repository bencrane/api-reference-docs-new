# Delete a specified CNI object

`DELETE /accounts/{account_id}/cni/cnis/{cni}`



## Parameters

- **cni** (string, required) [path]: CNI ID to retrieve information about
- **account_id** (string, required) [path]: 

## Response

### 200

CNI has been successfully deleted

### 400

Bad request

### 404

CNI not found

### 500

Internal server error
