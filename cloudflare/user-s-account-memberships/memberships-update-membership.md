# Update Membership

`PUT /memberships/{membership_id}`

Accept or reject this account invitation.

## Parameters

- **membership_id** (string, required) [path]: 

## Request Body

- **status** (enum, required): Whether to accept or reject this account invitation. Values: `accepted`, `rejected`

## Response

### 200

Update Membership response

- **result** (object, optional): 

### 4XX

Update Membership response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
