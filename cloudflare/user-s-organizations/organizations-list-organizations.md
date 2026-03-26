# List Organizations

`GET /user/organizations`

> **Deprecated**

Lists organizations the user is associated with.

## Parameters

- **name** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **match** (string, optional) [query]: 
- **status** (string, optional) [query]: 

## Response

### 200

List Organizations response

- **result** (array, optional): 

### 4XX

List Organizations response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
