# Create new indicator feed

`POST /accounts/{account_id}/intel/indicator-feeds`

Creates a new custom threat indicator feed for sharing threat intelligence data.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **description** (string, optional): The description of the example test
- **name** (string, optional): The name of the indicator feed

## Response

### 200

Create indicator feed response

- **result** (object, optional): 

### 4XX

Get indicator feeds failure response

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
