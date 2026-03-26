# Create dispatch namespace

`POST /accounts/{account_id}/workers/dispatch/namespaces`

Create a new Workers for Platforms namespace.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): The name of the dispatch namespace.

## Response

### 200

Fetch a list of Workers for Platforms namespaces.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Failure to get list of Workers for Platforms namespaces.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
