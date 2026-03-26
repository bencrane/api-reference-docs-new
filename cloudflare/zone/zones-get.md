# List Zones

`GET /zones`

Lists, searches, sorts, and filters your zones. Listing zones across more than 500 accounts
is currently not allowed.


## Parameters

- **name** (string, optional) [query]: 
- **status** (string, optional) [query]: 
- **account.id** (string, optional) [query]: 
- **account.name** (string, optional) [query]: 
- **page** (number, optional) [query]: 
- **per_page** (number, optional) [query]: 
- **order** (string, optional) [query]: 
- **direction** (string, optional) [query]: 
- **match** (string, optional) [query]: 

## Response

### 200

List Zones response.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful.
- **result_info** (object, optional): 
- **result** (array, optional): 

### 4XX

List Zones response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
