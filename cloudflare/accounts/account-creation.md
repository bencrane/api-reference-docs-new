# Create an account

`POST /accounts`

Create an account (only available for tenant admins at this time)

## Request Body

- **name** (string, required): Account name
- **type** (enum, optional):  Values: `standard`, `enterprise`
- **unit** (object, optional): information related to the tenant unit, and optionally, an id of the unit to create the account on. see https://developers.cloudflare.com/tenant/how-to/manage-accounts/

## Response

### 200

Account Creation Success Response

- **result** (object, optional): 

### 4XX

Account Creation Failure Response

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
