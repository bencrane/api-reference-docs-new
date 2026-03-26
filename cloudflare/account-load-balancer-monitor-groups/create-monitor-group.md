# Create Monitor Group

`POST /accounts/{account_id}/load_balancers/monitor_groups`

Create a new monitor group.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **created_at** (string, optional): The timestamp of when the monitor group was created
- **description** (string, required): A short description of the monitor group
- **id** (string, required): The ID of the Monitor Group to use for checking the health of origins within this pool.
- **members** (array, required): List of monitors in this group
- **updated_at** (string, optional): The timestamp of when the monitor group was last updated

## Response

### 200

Create Monitor Group response

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 412

Precondition Failed - Referenced monitor does not exist

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`

### 4XX

Create Monitor Group response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
