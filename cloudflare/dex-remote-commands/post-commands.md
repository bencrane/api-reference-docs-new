# Create account commands

`POST /accounts/{account_id}/dex/commands`

Initiate commands for up to 10 devices per account

## Parameters

- **account_id** (string, required) [path]: unique identifier linked to an account in the API request path

## Request Body

- **commands** (array, required): List of device-level commands to execute

## Response

### 200

Create commands response

- **result** (object, optional): 

### 4XX

Create commands failure response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
