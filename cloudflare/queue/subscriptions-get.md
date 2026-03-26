# Get Event Subscription

`GET /accounts/{account_id}/event_subscriptions/subscriptions/{subscription_id}`

Get details about an existing event subscription

## Parameters

- **account_id** (string, required) [path]: 
- **subscription_id** (string, required) [path]: 

## Response

### 200

Details about an event subscription

_Empty object_

### 404

Event subscription does not exist

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
