# Roll Token

`PUT /user/tokens/{token_id}/value`

Roll the token secret.

## Parameters

- **token_id** (string, required) [path]: 

## Request Body

_Empty object_

## Response

### 200

Roll Token response

- **result** (string, optional): The token value.

### 4XX

Roll Token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
