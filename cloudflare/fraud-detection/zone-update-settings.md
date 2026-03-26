# Update Fraud Detection Settings

`PUT /zones/{zone_id}/fraud_detection/settings`

Update Fraud Detection settings for a zone.

Notes on `username_expressions` behavior:
- If omitted or set to null, expressions are not modified.
- If provided as an empty array `[]`, all expressions will be cleared.


## Parameters

- **zone_id** (string, required) [path]: 

## Request Body

- **user_profiles** (string, optional): Whether Fraud User Profiles is enabled for the zone. Values: `enabled`, `disabled`
- **username_expressions** (array, optional): List of expressions to detect usernames in write HTTP requests.

- Maximum of 10 expressions.
- Omit or set to null to leave unchanged on update.
- Provide an empty array `[]` to clear all expressions on update.
- Invalid expressions will result in a 10400 Bad Request with details in the `messages` array.


## Response

### 200

Updated Fraud Detection settings response

- **result** (object, optional): 

### 4XX

Update Fraud Detection settings failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
