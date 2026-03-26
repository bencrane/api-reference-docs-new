# Create a tag

`POST /accounts/{account_id}/access/tags`

Create a tag

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): The name of the tag

## Response

### 201

Create a tag response

_Empty object_

### 4XX

Create a tag response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
