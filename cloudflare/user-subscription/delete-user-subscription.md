# Delete User Subscription

`DELETE /user/subscriptions/{identifier}`

Deletes a user's subscription.

## Parameters

- **identifier** (string, required) [path]: 


## Response

### 200

Delete User Subscription response

- **subscription_id** (string): Subscription identifier tag.

### 4XX

Delete User Subscription response failure

- **subscription_id** (string, optional): Subscription identifier tag.
- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
