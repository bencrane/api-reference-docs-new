# Update Token

`PUT /user/tokens/{token_id}`

Update an existing token.

## Parameters

- **token_id** (string, required) [path]: 

## Request Body

- **condition** (object, optional): 
- **expires_on** (string, optional): The expiration time on or after which the JWT MUST NOT be accepted for processing.
- **id** (string, optional): Token identifier tag.
- **issued_on** (string, optional): The time on which the token was created.
- **last_used_on** (string, optional): Last time the token was used.
- **modified_on** (string, optional): Last time the token was modified.
- **name** (string, optional): Token name.
- **not_before** (string, optional): The time before which the token MUST NOT be accepted for processing.
- **policies** (array, optional): List of access policies assigned to the token.
- **status** (string, optional): Status of the token. Values: `active`, `disabled`, `expired`

## Response

### 200

Update Token response

- **result** (object, optional): 

### 4XX

Update Token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
