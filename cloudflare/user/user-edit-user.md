# Edit User

`PATCH /user`

Edit part of your user details.

## Request Body

- **country** (string, optional): The country in which the user lives.
- **first_name** (string, optional): User's first name
- **last_name** (string, optional): User's last name
- **telephone** (string, optional): User's telephone number
- **zipcode** (string, optional): The zipcode or postal code where the user lives.

## Response

### 200

Edit User response

- **result** (object, optional): 

### 4XX

Edit User response failure

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
