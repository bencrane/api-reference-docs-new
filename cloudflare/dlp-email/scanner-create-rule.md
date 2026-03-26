# Create email scanner rule

`POST /accounts/{account_id}/dlp/email/rules`

Creates a new DLP email scanning rule that defines what content patterns to detect in email messages and what actions to take.

## Parameters

- **account_id** (string, required) [path]: 

## Request Body

- **action** (object, required): 
- **conditions** (array, required): Triggered if all conditions match.
- **description** (string, optional): 
- **enabled** (boolean, required): 
- **name** (string, required): 

## Response

### 200

New Email Scanner Rule response.

- **result** (object, optional): 

### 4XX

New Email Scanner Rule failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
