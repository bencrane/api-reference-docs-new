# Respond to Invitation

`PATCH /user/invites/{invite_id}`

Responds to an invitation.

## Parameters

- **invite_id** (string, required) [path]: 

## Request Body

- **status** (enum, required): Status of your response to the invitation (rejected or accepted). Values: `accepted`, `rejected`

## Response

### 200

Respond to Invitation response

- **result** (object, optional): 

### 4XX

Respond to Invitation response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
