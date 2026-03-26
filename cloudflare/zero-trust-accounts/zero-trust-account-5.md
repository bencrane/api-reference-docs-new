# Get logging settings for the Zero Trust account

`GET /accounts/{account_id}/gateway/logging`

Retrieve the current logging settings for the Zero Trust account.

## Parameters

- **account_id** (string, required) [path]: 

## Response

### 200

Logging settings retrieval response.

- **result** (object, optional): 

### 4XX

Logging settings retrieval response failure.

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Indicate whether the API call was successful. Values: `false`
