# List Memberships

`GET /memberships`

List memberships of accounts the user can access.

## Parameters

- **account.name** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **name** (string, optional) [query]: 
- **status** (string, optional) [query]: 

## Response

### 200

List Memberships response

Type: object

### 4XX

List Memberships response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
