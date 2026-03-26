# Patch Pools

`PATCH /accounts/{account_id}/load_balancers/pools`

Apply changes to a number of existing pools, overwriting the supplied properties. Pools are ordered by ascending `name`. Returns the list of affected pools. Supports the standard pagination query parameters, either `limit`/`offset` or `per_page`/`page`.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **notification_email** (string, optional): The email address to send health status notifications to. This field is now deprecated in favor of Cloudflare Notifications for Load Balancing, so only resetting this field with an empty string `""` is accepted. Values: ``

## Response

### 200

Patch Pools response.

- **result** (array, optional): 

### 4XX

Patch Pools response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
