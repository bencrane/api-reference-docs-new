# Update Zero Trust account configuration

`PUT /accounts/{account_id}/gateway/configuration`

Update the current Zero Trust account configuration.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **settings** (object, optional): Specify account settings.

## Response

### 200

Zero Trust account configuration response.

_Empty object_

### 4XX

Zero Trust account configuration response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`
