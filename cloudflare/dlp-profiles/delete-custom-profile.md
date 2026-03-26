# Delete custom profile

`DELETE /accounts/{account_id}/dlp/profiles/custom/{profile_id}`

Deletes a DLP custom profile.

## Parameters

- **account_id** (string, required) [path]: 
- **profile_id** (string, required) [path]: 

## Response

### 200

Delete custom profile response.

- **result** (object, optional): 

### 4XX

Delete custom profile failure response.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
