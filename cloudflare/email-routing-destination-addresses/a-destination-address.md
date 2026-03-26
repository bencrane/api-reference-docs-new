# Create a destination address

`POST /accounts/{account_id}/email/routing/addresses`

Create a destination address to forward your emails to. Destination addresses need to be verified before they can be used.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **email** (string, required): The contact email address of the user.

## Response

### 200

Create a destination address response

- **result** (object, optional):
