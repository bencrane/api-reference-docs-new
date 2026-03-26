# Update Account

`PUT /accounts/{account_id}`

Update an existing account.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **created_on** (string, optional): Timestamp for the creation of the account
- **id** (string, optional): Identifier
- **managed_by** (object, optional): Parent container details
- **name** (string, optional): Account name
- **settings** (object, optional): Account settings
- **type** (enum, optional):  Values: `standard`, `enterprise`

## Response

### 200

Update Account response

- **result** (object, optional): 

### 4XX

Update Account response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
