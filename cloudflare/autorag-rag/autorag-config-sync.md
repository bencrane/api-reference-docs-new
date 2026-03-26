# Sync

`PATCH /accounts/{account_id}/autorag/rags/{id}/sync`



## Parameters

- **id** (string, required) [path]: rag id
- **account_id** (string, required) [path]: 

## Response

### 200

Returns the autorag sync status

- **result** (object): 
- **success** (boolean): 

### 400

autorag_is_paused

- **errors** (array): 
- **success** (boolean): 

### 404

autorag_not_found

- **errors** (array): 
- **success** (boolean): 

### 429

sync_in_cooldown

- **errors** (array): 
- **success** (boolean): 

### 503

unable_to_connect_to_autorag

- **errors** (array): 
- **success** (boolean):
