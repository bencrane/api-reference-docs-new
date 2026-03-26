# Edit app details

`PUT /accounts/{account_id}/calls/apps/{app_id}`

Edit details for a single app.

## Parameters

- **app_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **name** (string, optional): A short description of Calls app, not shown to end users.

## Response

### 200

Edit app details response

- **result** (object, optional): 

### 4XX

Edit app details response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
