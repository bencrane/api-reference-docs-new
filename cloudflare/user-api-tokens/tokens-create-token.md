# Create Token

`POST /user/tokens`

Create a new access token.

## Request Body

- **condition** (object, optional): 
- **expires_on** (string, optional): The expiration time on or after which the JWT MUST NOT be accepted for processing.
- **name** (string, required): Token name.
- **not_before** (string, optional): The time before which the token MUST NOT be accepted for processing.
- **policies** (array, required): List of access policies assigned to the token.

## Response

### 200

Create Token response

- **result** (object, optional): 

### 4XX

Create Token response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
