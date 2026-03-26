# Get information about the specified slot

`GET /accounts/{account_id}/cni/slots/{slot}`



## Parameters

- **slot** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Response

### 200

Information about the specified slot

- **account** (string): Customer account tag
- **facility** (object): 
- **id** (string): Slot ID
- **occupied** (boolean): Whether the slot is occupied or not
- **site** (string): 
- **speed** (string): 

### 400

Bad request

### 404

Slot not found

### 500

Internal server error
