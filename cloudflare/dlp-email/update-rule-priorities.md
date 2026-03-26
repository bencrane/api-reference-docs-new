# Update email scanner rule priorities

`PATCH /accounts/{account_id}/dlp/email/rules`

Reorders DLP email scanning rules by updating their priority values. Higher priority rules are evaluated first.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **new_priorities** (object, required): 

## Response

### 200

Update Email Scanner Rule priorities response.

- **result** (object, optional): 

### 4XX

Update Email Scanner Rule priorities failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
