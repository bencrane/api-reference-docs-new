# Create Prefix Delegation

`POST /accounts/{account_id}/addressing/prefixes/{prefix_id}/delegations`

Create a new account delegation for a given IP prefix.

## Parameters

- **prefix_id** (string, required) [path]: 
- **account_id** (string, required) [path]: 

## Request Body

- **cidr** (string, required): IP Prefix in Classless Inter-Domain Routing format.
- **delegated_account_id** (string, required): Account identifier for the account to which prefix is being delegated.

## Response

### 200

Create Prefix Delegation response

- **result** (object, optional): 

### 4XX

Create Prefix Delegation response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
