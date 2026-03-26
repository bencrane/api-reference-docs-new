# Delete Membership

`DELETE /memberships/{membership_id}`

Remove the associated member from an account.

## Parameters

- **membership_id** (string, required) [path]: 


## Response

### 200

Delete Membership response

- **result** (object, optional): 

### 4XX

Delete Membership response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
