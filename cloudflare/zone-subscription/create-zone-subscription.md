# Create Zone Subscription

`POST /zones/{zone_id}/subscription`

Create a zone subscription, either plan or add-ons.

## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **app** (object, optional): 
- **component_values** (array, optional): The list of add-ons subscribed to.
- **currency** (string, optional): The monetary unit in which pricing information is displayed.
- **current_period_end** (string, optional): The end of the current period and also when the next billing is due.
- **current_period_start** (string, optional): When the current billing period started. May match initial_period_start if this is the first period.
- **frequency** (string, optional): How often the subscription is renewed automatically. Values: `weekly`, `monthly`, `quarterly`, `yearly`
- **id** (string, optional): Subscription identifier tag.
- **price** (number, optional): The price of the subscription that will be billed, in US dollars.
- **rate_plan** (object, optional): The rate plan applied to the subscription.
- **state** (string, optional): The state that the subscription is in. Values: `Trial`, `Provisioned`, `Paid`, `AwaitingPayment`, `Cancelled`, `Failed`, `Expired`
- **zone** (object, optional): A simple zone object. May have null properties if not a zone subscription.

## Response

### 200

Create Zone Subscription response

- **result** (object, optional): 

### 4XX

Create Zone Subscription response failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful Values: `false`
