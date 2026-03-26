# Create Event Subscription

`POST /accounts/{account_id}/event_subscriptions/subscriptions`

Create a new event subscription for a queue

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **destination** (object, optional): Destination configuration for the subscription
- **enabled** (boolean, optional): Whether the subscription is active
- **events** (array, optional): List of event types this subscription handles
- **name** (string, optional): Name of the subscription
- **source** (object, optional): Source configuration for the subscription

## Response

### 200

Successfully created event subscription

_Empty object_

### 400

Invalid request body or validation errors

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.

### 404

Queue does not exist or resource not found on source

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.

### 405

Multiple subscriptions on same resource not supported

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Indicates if the API call was successful or not.
