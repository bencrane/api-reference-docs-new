# Bulk edit token validation rules

`PATCH /zones/{zone_id}/token_validation/rules/bulk`

Edit token validation rules.

A request can update multiple Token Validation Rules.

Rules can be re-ordered using the `position` field.

Returns all updated rules.


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
