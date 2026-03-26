# Create an Access group

`POST /accounts/{account_id}/access/groups`

Creates a new Access group.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **exclude** (array, optional): Rules evaluated with a NOT logical operator. To match a policy, a user cannot meet any of the Exclude rules.
- **include** (array, required): Rules evaluated with an OR logical operator. A user needs to meet only one of the Include rules.
- **is_default** (boolean, optional): Whether this is the default group
- **name** (string, required): The name of the Access group.
- **require** (array, optional): Rules evaluated with an AND logical operator. To match a policy, a user must meet all of the Require rules.

## Response

### 201

Create an Access group response

_Empty object_

### 4XX

Create an Access group response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
