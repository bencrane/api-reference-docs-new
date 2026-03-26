# Update email scanner rule

`PUT /accounts/{account_id}/dlp/email/rules/{rule_id}`



## Parameters

- **account_id** (string, required) [path]: 
- **rule_id** (string, required) [path]: 

## Request Body

- **action** (object, required): 
- **conditions** (array, required): Triggered if all conditions match.
- **description** (string, optional): 
- **enabled** (boolean, required): 
- **name** (string, required): 

## Response

### 200

Update Email Scanner Rule response.

- **result** (object, optional): 

### 4XX

Update Email Scanner Rule failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
