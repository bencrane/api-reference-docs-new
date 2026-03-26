# Bulk create token validation rules

`POST /zones/{zone_id}/token_validation/rules/bulk`

Create zone token validation rules.

A request can create multiple Token Validation Rules.


## Request Body

Array of object

## Response

### 200

OK

- **result** (array, optional): 

### 4XX

Failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
